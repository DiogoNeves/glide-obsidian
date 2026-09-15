# Optional daily unique project notes

Enable this when you want project progress to appear among your ordinary Obsidian unique notes, with links back to Glide's retained evidence. It creates one new root-level note per active project and completed day. It does not edit your daily journal, append to existing notes, create project pages, or backfill the archive.

This is an **Obsidian-only companion** to the pinned shared memory runtime. Project progress is its first supported category. Other categories need their own reviewed source/output adapter; permission for project notes does not enable them.

## Decide once, then run within that scope

During setup, ask: “Would you like daily unique notes for project progress? Which projects should be included?” Show the proposed project scope, tags, timezone, start date and optional links before recording the answer. Default to disabled. Use today's date unless the owner explicitly chooses otherwise. Do not repeat the permission question every day; ask again for expanded scope or editing an existing note.

Project scope can be a list of exact project-index entries or `all`. **All includes future locally available projects admitted through that index.** Explain this before accepting it. Source intake still resolves local paths privately and verifies Git activity. Unavailable or incomplete projects are reported separately.

An existing project/category note can be linked, but neither is required. Keep the owner's unique-note conventions. The current output uses a filename such as `2026-09-05 1720 Garden progress.md`, with small properties and no repeated opening title:

```markdown
---
tags: [note, journal, progress]
origin: ai
glide_daily_note: daily-note:<stable id>
related: ["[[Agent HQ/Memory/Records/receipt/<activity record>]]"]
---

Recorded Git activity; release or deployment is not inferred.

- Improve seed labels · [commit](https://github.com/example/garden/commit/<sha>)
```

The initial implementation lists escaped commit subjects with exact commit links. It is a verifiable activity record, not an inferred account of shipped value. Follow linked memory for interpretation. Generated notes retain AI authorship and are identified by the companion's reader/search tools as derived views, not independent corroboration.

## Install outside the vault

First complete [memory setup](SETUP.md). This companion requires Python 3.11+, macOS/Linux, and shared build **`83c6ad3a80a8`**. Local instance state and the vault must be on the **same filesystem** for atomic creation of new notes. The runtime and state remain physically outside the vault and every sync root. This feature adds no database schema and changes no shared runtime files.

Use verified absolute local paths:

```sh
export GLIDE_DIST='/absolute/path/to/glide-obsidian'
export GLIDE_HOME='/absolute/path/to/local-glide'
export GLIDE_VAULT='/absolute/path/to/vault'
export GLIDE_RUNTIME='/absolute/path/to/local-glide/runtime/0.1.0-83c6ad3a80a8'
export GLIDE_CONFIG='/absolute/path/to/local-glide/instances/main/config.json'
python3 "$GLIDE_DIST/daily_notes/install.py" \
  --source "$GLIDE_DIST/daily_notes" --home "$GLIDE_HOME" \
  --vault "$GLIDE_VAULT" --runtime "$GLIDE_RUNTIME" \
  --expected-build 1a36a228f2b2
```

The installer verifies the companion's manifest and the installed shared runtime's actual content before copying anything. Record its result privately. Installation does not enable a category or change any scheduler. Do not force a mismatched package through installation.

In the existing fixed MCP server configuration, change the module from `glide_memory.bridge` to **`glide_obsidian.bridge`**. Keep the same interpreter, fixed `--config` argument, permissions and connector settings. Set `PYTHONPATH` to the installer's reported `pythonpath` (companion plus shared runtime). Keep `PYTHONDONTWRITEBYTECODE=1`. Reload the server and check that the existing tools remain available alongside `glide_project_notes_settings`, `glide_project_notes_preview` and `glide_project_notes_write`.

Install the concise `skills/glide-project-progress/SKILL.md` in the harness's discovered skill location on this device. Only Markdown skill instructions belong there; all Python stays in the local package directory. Merge local instructions without changing protected writing.

## Record the category permission

Trusted setup records the owner's exact decision as source evidence and saves a private JSON decision file outside the vault. Its two fields are:

```json
{
  "policy": {
    "enabled": true,
    "timezone": "Europe/London",
    "start_date": "2026-09-06",
    "projects": ["projects/garden.md"],
    "titles": {"projects/garden.md": "Garden"},
    "project_notes": {},
    "tags": ["note", "journal", "progress"],
    "category_note": null
  },
  "approval": {
    "path": "Agent HQ/Source Captures/Conversations/Daily note decision.md",
    "sha256": "<actual SHA-256 of that Markdown source>",
    "quote": "<exact passage approving this category and scope>"
  }
}
```

Replace the synthetic values with the user's actual decision; do not invent an approval. `project_notes` maps index entries to existing vault-relative Markdown paths. `category_note` optionally names an existing category page. No processing metadata is added to those pages. With the verified companion/runtime `PYTHONPATH` active, run:

```sh
python3 -m glide_obsidian.configure --config "$GLIDE_CONFIG" \
  --decision '/absolute/path/to/private-decision.json'
```

This stores an approved Markdown permission record and matching local host configuration. Permission changes are deliberately absent from MCP tools and learned overlays. To disable, record the user's new decision through the same setup entrypoint with `enabled: false`. A mismatch between local configuration and the retained approval stops output instead of silently adopting new scope.

## Daily execution and review

Add `glide-project-progress` to the **existing source-intake job after successful project intake**, without changing the job's model, schedule or external-action authority. Pause any older job writing the same progress notes. A scheduled start is not a successful intake receipt. No second daily scheduler is needed.

The tool defaults to yesterday in the approved timezone. Dates before the start date are skipped; an explicit historical date must be completed, within the past seven days and inside the approved window. No activity means no empty note. A call writes at most 20 ready projects and returns `pending_projects`; continue at most once in the scheduled run, then report remaining work for the next run or explicit review. A crash is retryable after inspection. Do not loop indefinitely.

A preview changes no files. Writing first commits a publication plan with the complete note, evidence and permission revision to Markdown history. It then atomically creates a new file without replacement and commits a completion receipt. The daily note links to its activity record; the receipt links back to the daily note. SQLite is just the existing rebuildable index.

The response distinguishes written notes, previous writes and cases needing review. Return a real receipt before claiming success. Do not claim a local preview selection applied anything. Keep no-change scheduled runs quiet.

Existing matching progress notes are preserved and flagged rather than automatically treated as covering the evidence. Later-discovered commits for a written day remain in managed memory and need review before supplemental output. Changed, moved or deleted notes are not overwritten or recreated. Projects with partial intake are withheld. Conflicting paths or changed permissions stop publication.

## Upgrade, handover and rollback

Use [UPGRADING.md](UPGRADING.md) first. Back up the existing MCP configuration, local instance configuration and relevant jobs; preserve all retained bundles. Install the companion alongside the old runtime and validate with synthetic data before changing the execution host.

For a new machine, stop the old writer and its jobs, sync and verify Markdown history, install the same packages, and rebuild. The retained approval does not automatically enable writing on the new host: recreate its local settings from that verified decision during the explicit handover. Confirm the configured vault/state support same-filesystem atomic creation. Then activate only the selected writer.

To roll back, stop the optional output step and restore the previous MCP entrypoint/PYTHONPATH. Keep the permission, plans and receipts in history. Preserve generated notes, including any later human edits. Existing shared operations continue through the unchanged runtime. Never delete notes to make a rollback appear clean.

## Validation

From the distribution checkout, with the matching shared checkout available:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="daily_notes:/absolute/path/to/glide/runtime" \
  python3 -m unittest discover -s daily_notes/tests -v
```

The synthetic suite checks permission defaults, scope, date boundaries, evidence, optional project links, preservation of writing, legacy duplicates, late activity, incomplete intake, interrupted publication, SQLite rebuild, host handover, batch continuation, symlink/path behavior, fixed MCP arguments and installer pins. The shared runtime's existing suite runs separately in CI. Passing these checks does not establish that every real project's commit messages make a useful daily note; review the first few outputs and refine only from that evidence.
