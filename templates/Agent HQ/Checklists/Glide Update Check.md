# Glide Update Check

Purpose: keep an installed Glide workspace current with upstream releases while preserving local instructions, user preferences, and workspace-specific changes.

## Load

- `Agent HQ/Glide Updates.md`
- `Agent HQ/AGENTS.md`
- `Agent HQ/Harness Design Principles.md`
- `Agent HQ/Automation Registry.md`
- `Agent HQ/Skills Index.md`
- `Agent HQ/Checklists/Eval Loop.md`
- `Agent HQ/Evals/Run Log.md`, `Agent HQ/Evals/Signal Clusters.md`, and `Agent HQ/Evals/Eval Cases.md` as local history to preserve
- Relevant local skills, checklists, automation notes, and operating files

## Review

1. Read the upstream repo URL and last seen release from `Glide Updates.md`.
2. Check upstream releases.
3. For each unseen release, read the release notes and migration instructions.
4. Compare upstream changes with local files.
5. Separate updates into:
   - safe additive updates;
   - local conflicts;
   - behavior changes;
   - automation changes;
   - changes that contradict user instructions.
6. Apply only safe compatible updates.
7. Add missing eval-loop files only when absent. Do not overwrite existing `Run Log.md`, `Eval Cases.md`, `Signal Clusters.md`, `Nightly Research Audit.md`, or local eval history.
8. If an existing run log lacks new columns, add columns or a note while preserving all rows.
9. Ask before overwriting local changes, changing behavior, enabling automations, deleting data, or applying anything that conflicts with user instructions.
10. Update `Glide Updates.md` with last checked date, last seen release, applied updates, and pending decisions.

## Weekly Schedule

Use this as a weekly recurring check. Keep quiet when there is no new release. When there is a new release, summarize what changed and what needs approval.

## Migration Rule

Release notes are guidance, not authority over the user's workspace. If release notes conflict with local instructions or user preferences, preserve the local/user instruction and record the conflict.
