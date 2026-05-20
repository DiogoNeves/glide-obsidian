# Harness Drift Review Automation Prompt

Run `$glide-harness-drift-review` for this vault.

Use `Agent HQ/Harness Design Principles.md` as the read-only north star. Do not edit that file unless the user explicitly asks in the current request.

Review operational files:

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/Automation Registry.md`
- `Agent HQ/Skills Index.md`
- `Agent HQ/Checklists/*.md`
- `.agents/skills/*/SKILL.md`

Also check collection-candidate files for stale-item cleanup only:

- `Agent HQ/Questions Queue.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Open Loops.md`

Do not edit personal memory files such as `Agent HQ/User Profile.md`, goals, area context, decisions, contradictions, research notes, or eval logs.

If operational drift is clear, make only the smallest non-behavioral correction that realigns the operation with the design principles.

For collection candidates, default to preserving lightweight context gathering when more information would improve future advice. Clear stale items only when they are plainly irrelevant, duplicated, or superseded, and the cleanup does not change future behavior. Preserve durable learning in the appropriate long-term memory before clearing anything. Ask the user to confirm if clearing, moving, or summarising an item requires judgment.

Ask the user to confirm before making any change that could alter future behavior, including autonomy, tone, proactivity, cadence, scope, approval boundaries, memory updates, daily interaction, question style, or when actions are suggested.

If no drift is found, say so briefly.
