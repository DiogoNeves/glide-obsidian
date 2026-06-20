# Harness Drift Review

## Installable Prompt

Run `$glide-harness-drift-review` for this vault.

Use `Agent HQ/Harness Design Principles.md` as the read-only north star. Do not edit that file unless the user explicitly asks in the current request.

Review operational files:

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/Automation Registry.md`
- `Agent HQ/Skills Index.md`
- `Agent HQ/Checklists/*.md`
- installed `glide-*` skills

Read `Agent HQ/Evals/*.md` as evidence only. Recurring `Improve Next` notes and `Partial` outcomes can become candidates for small instruction updates.

Also check collection-candidate files for stale-item cleanup only:

- `Agent HQ/Questions Queue.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Open Loops.md`

If operational drift is clear, make only the smallest non-behavioral correction that realigns the operation with the design principles.

Ask the user to confirm before making any change that could alter future behavior, including autonomy, tone, proactivity, cadence, scope, approval boundaries, memory updates, daily interaction, question style, or when actions are suggested.

If no drift is found, say so briefly.

## Suggested Schedule

- Cadence: weekly or twice weekly
- Time: user-preferred evening time
- Workspace: the Obsidian vault where Glide is installed
- Output: short drift report, or small operational edits plus a summary

## Install Notes

- Confirm before enabling.
- Record the active schedule in `Agent HQ/Automation Registry.md`.
- If the harness cannot schedule recurring runs, keep this as a proposed manual automation.
