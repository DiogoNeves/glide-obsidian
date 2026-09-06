#!/usr/bin/env python3
"""Read-only local Codex metadata hints; never a human-activity or review cursor.

Offsets are useful only while inventory_fingerprint is unchanged. Compare it
between pages; live files can otherwise shift positions. App message IDs and
durable coverage receipts remain the authoritative reviewed boundary.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat

MAX_HEADER_BYTES = 65536
KNOWN_EXTERNAL = {"cli", "vscode", "app-server", "appserver", "desktop", "codex desktop"}
INTERNAL = {"subagent", "guardian", "approval", "review"}


class HeaderGap(ValueError):
    pass


def timestamp(value: str | datetime) -> datetime:
    """Require an explicit timezone; do not guess the host's local timezone."""
    result = datetime.fromisoformat(value.replace("Z", "+00:00")) if isinstance(value, str) else value
    if not isinstance(result, datetime) or result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("Timestamp must include a timezone offset")
    return result.astimezone(timezone.utc)


def fingerprint(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def origin_class(source: object) -> str:
    if isinstance(source, dict):
        keys = {str(key).lower() for key in source}
        return "internal" if keys & INTERNAL else "unknown"
    if isinstance(source, str):
        normalized = source.lower().strip()
        tokens = set(normalized.replace("-", " ").replace("_", " ").split())
        if tokens & INTERNAL:
            return "internal"
        if normalized in KNOWN_EXTERNAL:
            return "noninternal"
    return "unknown"


def read_header(path: Path, expected: os.stat_result) -> dict:
    """Read exactly the first line, without buffered read-ahead into messages."""
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    fd = os.open(path, flags)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode):
            raise HeaderGap("nonregular-rejected")
        identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
        if identity(before) != identity(expected):
            raise HeaderGap("changed-during-scan")
        data = bytearray()
        while len(data) < MAX_HEADER_BYTES:
            char = os.read(fd, 1)
            if not char:
                raise HeaderGap("partial-header")
            data.extend(char)
            if char == b"\n":
                break
        else:
            raise HeaderGap("header-too-large")
        if identity(os.fstat(fd)) != identity(before):
            raise HeaderGap("changed-during-scan")
        try:
            item = json.loads(data)
        except (ValueError, UnicodeError) as exc:
            raise HeaderGap("invalid-header") from exc
        if not isinstance(item, dict) or item.get("type") != "session_meta":
            raise HeaderGap("missing-session-meta")
        meta = item.get("payload")
        if not isinstance(meta, dict) or not isinstance(meta.get("id"), str) or not meta["id"]:
            raise HeaderGap("invalid-session-meta")
        return meta
    finally:
        os.close(fd)


def load_titles(home: Path, gap) -> dict[str, str]:
    """The index is an optional title hint, never the discovery source."""
    path = home / "session_index.jsonl"
    titles = {}
    try:
        if path.is_symlink():
            gap("symlink-rejected", path)
            return {}
        if not path.exists():
            return {}
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, "rb") as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                gap("nonregular-index", path)
                return {}
            for number, line in enumerate(handle, 1):
                try:
                    row = json.loads(line)
                    if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                        raise ValueError("Invalid index row")
                    title = row.get("thread_name")
                    if isinstance(title, str):
                        titles[row["id"]] = title
                except (ValueError, UnicodeError):
                    gap("invalid-index-row", path, line=number)
    except OSError:
        gap("unreadable-index", path)
    return titles


def inventory(codex_home: str | Path, since: str | datetime, *, limit: int = 20,
              offset: int = 0, now: datetime | None = None) -> dict:
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError("limit must be an integer from 1 to 100")
    if type(offset) is not int or offset < 0:
        raise ValueError("offset must be a nonnegative integer")
    since = timestamp(since)
    snapshot = timestamp(now or datetime.now(timezone.utc))
    home = Path(os.path.abspath(Path(codex_home).expanduser()))
    sessions = home / "sessions"
    gaps, candidates = [], []
    inspected = headers = internal = 0

    def gap(reason, path, **details):
        try:
            relative = Path(path).relative_to(home).as_posix()
        except ValueError:
            relative = str(path)
        gaps.append({"reason": reason, "path": relative, **details})

    # Reject symlinked roots before reading the optional index or any headers.
    available = False
    try:
        root_link = next((p for p in (sessions, *sessions.parents) if p.is_symlink()), None)
        available = root_link is None and sessions.is_dir()
        if root_link:
            gap("symlink-rejected", root_link)
        elif not available:
            gap("sessions-unavailable", sessions)
    except OSError:
        gap("unreadable-root", sessions)
    titles = load_titles(home, gap) if available else {}
    since_ns, snapshot_ns = int(since.timestamp() * 1e9), int(snapshot.timestamp() * 1e9)

    if available:
        def walk_error(error):
            gap("unreadable-directory", error.filename or sessions)

        for directory, dirs, names in os.walk(sessions, followlinks=False, onerror=walk_error):
            for name in list(dirs):
                child = Path(directory) / name
                if child.is_symlink():
                    dirs.remove(name)
                    gap("symlink-rejected", child)
            dirs.sort()
            for name in sorted(names):
                if not name.startswith("rollout-") or not name.endswith(".jsonl"):
                    continue
                path = Path(directory) / name
                inspected += 1
                try:
                    info = path.lstat()
                    if stat.S_ISLNK(info.st_mode):
                        gap("symlink-rejected", path)
                        continue
                    if not stat.S_ISREG(info.st_mode):
                        gap("nonregular-rejected", path)
                        continue
                    if info.st_mtime_ns < since_ns:
                        continue
                    if info.st_mtime_ns > snapshot_ns:
                        gap("modified-after-snapshot", path)
                        continue
                    headers += 1
                    meta = read_header(path, info)
                except HeaderGap as exc:
                    gap(str(exc), path)
                    continue
                except OSError:
                    gap("unreadable-header-or-stat", path)
                    continue
                source = meta.get("source")
                classification = origin_class(source)
                if classification == "internal":
                    internal += 1
                    continue
                if classification == "unknown":
                    gap("unknown-origin", path)
                row = {
                    "id": meta["id"], "title": titles.get(meta["id"], ""),
                    "relative_path": path.relative_to(home).as_posix(),
                    "mtime": datetime.fromtimestamp(info.st_mtime, timezone.utc).isoformat(),
                    "mtime_ns": info.st_mtime_ns, "size": info.st_size,
                    "source": source, "origin_class": classification,
                    "cwd": meta.get("cwd") if isinstance(meta.get("cwd"), str) else "",
                }
                row["metadata_fingerprint"] = fingerprint(row)
                candidates.append(row)

    candidates.sort(key=lambda row: (-row["mtime_ns"], row["relative_path"]))
    gaps.sort(key=lambda item: (item["path"], item["reason"], item.get("line", 0)))
    page = candidates[offset:offset + limit]
    pending = max(0, len(candidates) - offset - len(page))
    scope = {
        "kind": "local-codex-rollout-metadata", "codex_home": str(home),
        "rollout_root": str(sessions), "since_inclusive": since.isoformat(),
        "includes": "All creation-date directories under sessions; first-line session_meta only",
        "excludes": "Archived-session storage, cloud chats, other hosts, message bodies and tool output",
    }
    return {
        "status": "partial-metadata-inventory" if gaps else "metadata-inventory",
        "source_scope": scope, "snapshot_time": snapshot.isoformat(),
        "inventory_fingerprint": fingerprint({"scope": scope, "candidates": candidates, "gaps": gaps}),
        "inspected_count": inspected, "headers_inspected_count": headers,
        "internal_excluded_count": internal, "candidate_count": len(candidates),
        "returned_count": len(page), "skipped_before_page_count": min(offset, len(candidates)),
        "pending_count": pending, "offset": offset,
        "next_offset": offset + len(page) if pending else None,
        "gap_count": len(gaps), "gaps": gaps[:100], "gaps_omitted_count": max(0, len(gaps) - 100),
        "sessions": page,
        "limitations": [
            "Mtime and index titles are discovery hints, not proof of human activity or completed message review.",
            "Compare inventory_fingerprint between offset pages; changed inventories can skip or repeat entries.",
            "Offsets are not durable cursors. App message IDs and durable coverage receipts own the reviewed boundary.",
            "Unknown origins need inspection before attribution. Gaps remain unresolved even when pending_count is zero.",
        ],
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", default=os.environ.get("CODEX_HOME", "~/.codex"))
    parser.add_argument("--since", required=True, help="Inclusive modification-time hint with timezone, ISO 8601")
    parser.add_argument("--limit", type=int, default=20, help="Candidates per metadata page, 1..100")
    parser.add_argument("--offset", type=int, default=0, help="Within-run offset; compare inventory fingerprints")
    args = parser.parse_args(argv)
    try:
        result = inventory(args.codex_home, args.since, limit=args.limit, offset=args.offset)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
