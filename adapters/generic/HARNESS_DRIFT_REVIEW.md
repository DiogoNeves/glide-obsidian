# Harness Drift Review Prompt

Run the installed `glide-harness-drift-review` skill for this vault, or follow `Agent HQ/Checklists/Harness Drift Review.md` if the harness does not support skills.

Use `Agent HQ/Harness Design Principles.md` as the read-only north star. Do not edit that file unless the user explicitly asks in the current request.

Review operational files:

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/Automation Registry.md`
- `Agent HQ/Skills Index.md`
- `Agent HQ/Checklists/*.md`
- the configured Glide skill directory

Also check collection-candidate files for stale-item cleanup only:

- `Agent HQ/Questions Queue.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Open Loops.md`

If operational drift is clear, make only the smallest non-behavioral correction that realigns the operation with the design principles.

Ask the user to confirm before making any change that could alter future behavior, including autonomy, tone, proactivity, cadence, scope, approval boundaries, memory updates, daily interaction, question style, or when actions are suggested.

If no drift is found, say so briefly.
