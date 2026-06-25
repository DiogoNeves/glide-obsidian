# Automations

Glide ships four starter automations:

- Daily Glide Check-In
- Harness Drift Review
- Nightly Research Review
- Weekly Glide Update Check

These are installable prompts, not a background service. The selected harness decides whether recurring automations are supported and how they are scheduled.

## Install Contract

- Ask before installing any automation.
- Ask for cadence, timezone, workspace, and model when the harness requires them.
- Prefer adding Glide steps to an existing relevant automation if one already exists.
- Keep automations easy to review.
- Record active and proposed automations in `Agent HQ/Automation Registry.md`.

## Suggested Defaults

| Automation | Suggested Cadence | Purpose |
| --- | --- | --- |
| Daily Glide Check-In | Daily or weekdays, user-preferred morning time | Call `glide-update-user-profile`, scan area reminders, then prefer one useful item; max three urgent or very important items |
| Harness Drift Review | Weekly or twice weekly, user-preferred evening time | Keep operating files aligned with the protected design principles |
| Nightly Research Review | Daily at 4am local time | Quietly deepen open research, connect areas, improve memory, and keep a rolling 4-day internal audit |
| Weekly Glide Update Check | Weekly, low-disruption time | Check upstream releases and migration notes without overwriting local instructions |

## Adapter Prompts

- Codex: `adapters/codex/DAILY_GLIDE_CHECK_IN.md`, `adapters/codex/HARNESS_DRIFT_REVIEW.md`, `adapters/codex/NIGHTLY_RESEARCH_REVIEW.md`, and `adapters/codex/WEEKLY_GLIDE_UPDATE_CHECK.md`
- Claude Code: `adapters/claude-code/DAILY_GLIDE_CHECK_IN.md`, `adapters/claude-code/HARNESS_DRIFT_REVIEW.md`, `adapters/claude-code/NIGHTLY_RESEARCH_REVIEW.md`, and `adapters/claude-code/WEEKLY_GLIDE_UPDATE_CHECK.md`
- Generic: `adapters/generic/DAILY_GLIDE_CHECK_IN.md`, `adapters/generic/HARNESS_DRIFT_REVIEW.md`, `adapters/generic/NIGHTLY_RESEARCH_REVIEW.md`, and `adapters/generic/WEEKLY_GLIDE_UPDATE_CHECK.md`

If the harness does not support recurring automations, copy the relevant prompt into `Agent HQ/Automations/` and keep it listed as proposed in `Agent HQ/Automation Registry.md`.
