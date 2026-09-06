---
name: glide-project-progress
description: Create approved daily unique project-progress notes in Obsidian after successful project intake, preserving existing notes and linking retained Git evidence.
---

Use the optional Obsidian companion's `glide_project_notes_*` tools. Missing tools or a disabled category mean setup is needed; do not substitute unrestricted file writes. Setup asks which projects are included and records permission once. The canonical setup procedure is `docs/DAILY-NOTES.md` in the matching glide-obsidian release.

After successful relevant project intake, read `glide_project_notes_settings`. If enabled, use `glide_project_notes_write` for the previous completed local day. Use `glide_project_notes_preview` when the user wants to inspect an example first. Only pass a date for an explicitly requested catch-up. If `pending_projects` is nonzero, continue at most once, then report the remainder.

Return created-note links and actual receipts, distinguishing skipped cases and pending review. Keep unchanged scheduled runs quiet. Existing notes, incomplete intake, late activity and changed permission require the reported review, not an overwrite or automatic scope expansion.

The notes describe recorded Git activity, not inferred delivery or completion. Their linked memory retains original evidence; the daily note is not an independent corroborating source. A separate user-maintained project page is optional. Personal journaling and other note categories remain outside this permission.
