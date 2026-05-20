# Codex Automations

Use this file when installing Glide automations in Codex.

## Daily Glide Check-In

- Name: Daily Glide Check-In
- Kind: recurring workspace automation
- Workspace: the user's Obsidian vault
- Suggested cadence: daily or weekdays at the user's preferred morning time
- Prompt source: `adapters/codex/DAILY_GLIDE_CHECK_IN.md`
- Skill: `glide-daily-check-in`

Ask the user to confirm the schedule, model, reasoning effort, workspace, and destination before creating it.

## Harness Drift Review

- Name: Harness Drift Review
- Kind: recurring workspace automation
- Workspace: the user's Obsidian vault
- Suggested cadence: weekly or twice weekly at the user's preferred evening time
- Prompt source: `adapters/codex/HARNESS_DRIFT_REVIEW.md`
- Skill: `glide-harness-drift-review`

Ask the user to confirm the schedule, model, reasoning effort, workspace, and destination before creating it.

## After Install

- Add or update entries in `Agent HQ/Automation Registry.md`.
- If an equivalent automation already exists, prefer updating it or adding a Glide step to it.
- Do not create duplicate recurring runs.
