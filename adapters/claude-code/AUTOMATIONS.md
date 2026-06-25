# Claude Code Automations

Use this file when installing Glide automations with Claude Code or a scheduler that launches Claude Code.

## Daily Glide Check-In

- Name: Daily Glide Check-In
- Workspace: the user's Obsidian vault
- Suggested cadence: daily or weekdays at the user's preferred morning time
- Prompt source: `adapters/claude-code/DAILY_GLIDE_CHECK_IN.md`
- Skill: `glide-daily-check-in`

Ask the user which scheduler or recurring-run mechanism should call Claude Code. Confirm the schedule, working directory, model, and destination before enabling it.

## Harness Drift Review

- Name: Harness Drift Review
- Workspace: the user's Obsidian vault
- Suggested cadence: weekly or twice weekly at the user's preferred evening time
- Prompt source: `adapters/claude-code/HARNESS_DRIFT_REVIEW.md`
- Skill: `glide-harness-drift-review`

Ask the user which scheduler or recurring-run mechanism should call Claude Code. Confirm the schedule, working directory, model, and destination before enabling it.

## Nightly Research Review

- Name: Nightly Research Review
- Workspace: the user's Obsidian vault
- Suggested cadence: daily at 4am local time
- Prompt source: `adapters/claude-code/NIGHTLY_RESEARCH_REVIEW.md`
- Skill: `glide-nightly-research-review`

Ask the user which scheduler or recurring-run mechanism should call Claude Code. Confirm the schedule, working directory, model, and destination before enabling it.

## After Install

- Add or update entries in `Agent HQ/Automation Registry.md`.
- If native recurring automation is not available, leave these as proposed manual automations.
- Do not create duplicate recurring runs.
