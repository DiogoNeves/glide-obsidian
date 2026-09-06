from datetime import datetime, timezone
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stderr

SPEC = importlib.util.spec_from_file_location(
    "conversation_inventory", Path(__file__).resolve().parents[1] / "tools/conversation_inventory.py"
)
context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(context)

NOW = datetime(2026, 9, 6, 12, tzinfo=timezone.utc)
SINCE = "2026-09-05T00:00:00Z"
RECENT = datetime(2026, 9, 6, 10, tzinfo=timezone.utc).timestamp()


class ConversationInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name).resolve()
        (self.home / "sessions").mkdir()

    def rollout(self, name, source="vscode", *, day="2026/09/06", mtime=RECENT, raw=None):
        path = self.home / "sessions" / day / ("rollout-" + name + ".jsonl")
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = {"type": "session_meta", "payload": {"id": name, "source": source, "cwd": "/synthetic/project"}}
        data = raw if raw is not None else json.dumps(meta).encode() + b"\nPRIVATE BODY MUST NOT BE READ\xff\n"
        path.write_bytes(data)
        os.utime(path, (mtime, mtime))
        return path

    def scan(self, **kwargs):
        return context.inventory(self.home, SINCE, now=NOW, **kwargs)

    def test_old_resumed_file_is_found_without_index_and_old_unchanged_is_skipped(self):
        self.rollout("resumed", day="2025/01/01")
        self.rollout("unchanged", day="2025/01/01", mtime=RECENT - 10 * 86400)
        result = self.scan()
        self.assertEqual(["resumed"], [s["id"] for s in result["sessions"]])
        self.assertEqual("", result["sessions"][0]["title"])
        self.assertEqual(2, result["inspected_count"])
        self.assertEqual(1, result["headers_inspected_count"])

    def test_stale_index_only_supplies_title_and_missing_entry_does_not_hide_file(self):
        self.rollout("indexed", day="2026/02/01")
        self.rollout("missing", day="2026/03/01")
        (self.home / "session_index.jsonl").write_text(json.dumps({
            "id": "indexed", "thread_name": "A title hint", "updated_at": "2026-02-01T00:00:00Z"
        }) + "\n")
        result = {s["id"]: s for s in self.scan()["sessions"]}
        self.assertEqual({"indexed", "missing"}, set(result))
        self.assertEqual("A title hint", result["indexed"]["title"])

    def test_internal_origins_are_filtered_before_limit(self):
        for number, source in enumerate(({"subagent": {"thread_spawn": {}}}, "guardian", "approval-review", {"approval": {}})):
            self.rollout("internal-" + str(number), source, mtime=RECENT + number)
        self.rollout("useful", mtime=RECENT - 30)
        result = self.scan(limit=1)
        self.assertEqual(["useful"], [s["id"] for s in result["sessions"]])
        self.assertEqual(4, result["internal_excluded_count"])
        self.assertEqual(1, result["candidate_count"])
        self.assertEqual(0, result["pending_count"])

    def test_unknown_origin_is_returned_but_explicitly_unresolved(self):
        self.rollout("unknown", {"future-origin": "new"})
        result = self.scan()
        self.assertEqual("unknown", result["sessions"][0]["origin_class"])
        self.assertEqual("unknown-origin", result["gaps"][0]["reason"])
        self.assertEqual("partial-metadata-inventory", result["status"])

    def test_partial_header_is_a_gap_not_an_empty_success(self):
        self.rollout("partial", raw=b'{"type":"session_meta","payload":')
        result = self.scan()
        self.assertEqual(0, result["candidate_count"])
        self.assertEqual("partial-header", result["gaps"][0]["reason"])

    def test_missing_source_and_unreadable_header_are_gaps(self):
        self.rollout("unreadable")
        with patch.object(context, "read_header", side_effect=PermissionError):
            result = self.scan()
        self.assertEqual("unreadable-header-or-stat", result["gaps"][0]["reason"])
        result = context.inventory(self.home / "absent", SINCE, now=NOW)
        self.assertEqual("sessions-unavailable", result["gaps"][0]["reason"])
        self.assertEqual(0, result["returned_count"])

    def test_root_and_optional_index_stat_errors_are_reported(self):
        with patch.object(Path, "is_dir", side_effect=PermissionError):
            result = self.scan()
        self.assertEqual("unreadable-root", result["gaps"][0]["reason"])
        self.rollout("still-discoverable")
        with patch.object(Path, "exists", side_effect=PermissionError):
            result = self.scan()
        self.assertEqual("unreadable-index", result["gaps"][0]["reason"])
        self.assertEqual(1, result["returned_count"])

    def test_symlinked_file_directory_root_and_index_are_rejected(self):
        outside = self.home / "outside"; outside.mkdir()
        target = outside / "rollout-target.jsonl"
        target.write_text("This must never be opened.")
        (self.home / "sessions" / "rollout-linked.jsonl").symlink_to(target)
        (self.home / "sessions" / "linked-day").symlink_to(outside, target_is_directory=True)
        (self.home / "session_index.jsonl").symlink_to(target)
        with patch.object(context, "read_header", side_effect=AssertionError("Symlink read")):
            result = self.scan()
        self.assertEqual(3, result["gap_count"])
        self.assertTrue(all(g["reason"] == "symlink-rejected" for g in result["gaps"]))
        linked = self.home / "linked-home"; linked.symlink_to(self.home, target_is_directory=True)
        result = context.inventory(linked, SINCE, now=NOW)
        self.assertEqual("symlink-rejected", result["gaps"][0]["reason"])

    def test_header_read_stops_at_newline_and_source_is_unchanged(self):
        path = self.rollout("bounded")
        before = path.read_bytes()
        original_read = os.read
        count = 0

        def observe(fd, length):
            nonlocal count
            self.assertEqual(1, length)
            count += 1
            self.assertLessEqual(count, before.index(b"\n") + 1)
            return original_read(fd, length)

        with patch.object(context.os, "read", side_effect=observe):
            result = self.scan()
        self.assertEqual(1, result["candidate_count"])
        self.assertEqual(before.index(b"\n") + 1, count)
        self.assertEqual(before, path.read_bytes())

    def test_fingerprint_is_deterministic_and_changes_with_metadata(self):
        path = self.rollout("stable")
        first = self.scan()
        second = self.scan()
        self.assertEqual(first["inventory_fingerprint"], second["inventory_fingerprint"])
        self.assertEqual(first["sessions"][0]["metadata_fingerprint"], second["sessions"][0]["metadata_fingerprint"])
        self.assertEqual(context.fingerprint({"b": 1, "a": 2}), context.fingerprint({"a": 2, "b": 1}))
        os.utime(path, (RECENT + 1, RECENT + 1))
        self.assertNotEqual(first["inventory_fingerprint"], self.scan()["inventory_fingerprint"])

    def test_offset_pages_have_counts_and_detect_drift(self):
        for n in range(3):
            self.rollout(str(n), mtime=RECENT + n)
        first, second = self.scan(limit=1), self.scan(limit=1, offset=1)
        self.assertEqual(first["inventory_fingerprint"], second["inventory_fingerprint"])
        self.assertEqual((3, 1, 2, 1), (first["candidate_count"], first["returned_count"], first["pending_count"], first["next_offset"]))
        self.assertEqual(["1"], [s["id"] for s in second["sessions"]])
        self.rollout("new", mtime=RECENT + 20)
        self.assertNotEqual(first["inventory_fingerprint"], self.scan(limit=1, offset=1)["inventory_fingerprint"])

    def test_changed_during_header_read_is_not_published(self):
        path = self.rollout("racing")
        expected = path.stat()
        os.utime(path, (RECENT + 1, RECENT + 1))
        with self.assertRaisesRegex(context.HeaderGap, "changed-during-scan"):
            context.read_header(path, expected)

    def test_future_modification_and_malformed_index_remain_visible(self):
        self.rollout("future", mtime=NOW.timestamp() + 1)
        (self.home / "session_index.jsonl").write_bytes(b"{partial")
        reasons = {g["reason"] for g in self.scan()["gaps"]}
        self.assertEqual({"modified-after-snapshot", "invalid-index-row"}, reasons)

    def test_invalid_ranges_and_naive_timestamps_are_rejected(self):
        for value in (0, 101, -1, 1.5, True):
            with self.subTest(limit=value), self.assertRaises(ValueError):
                self.scan(limit=value)
        for value in (-1, 0.5, True):
            with self.subTest(offset=value), self.assertRaises(ValueError):
                self.scan(offset=value)
        for value in ("2026-09-05", "not-a-date", "2026-09-05T00:00:00"):
            with self.subTest(since=value), self.assertRaises(ValueError):
                context.inventory(self.home, value, now=NOW)
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            context.main(["--codex-home", str(self.home), "--since", SINCE, "--limit", "101"])
        self.assertEqual(2, raised.exception.code)


if __name__ == "__main__":
    unittest.main()
