# Automations

Glide ships two starter automations:

- Daily Glide Check-In
- Harness Drift Review

These are installable prompts, not a background service. The selected harness decides whether recurring automations are supported and how they are scheduled.

## Install Contract

- Ask before installing either automation.
- Ask for cadence, timezone, workspace, and model when the harness requires them.
- Prefer adding Glide steps to an existing relevant automation if one already exists.
- Keep both automations easy to review.
- Record active and proposed automations in `Agent HQ/Automation Registry.md`.

## Suggested Defaults

| Automation | Suggested Cadence | Purpose |
| --- | --- | --- |
| Daily Glide Check-In | Daily or weekdays, user-preferred morning time | Refresh `User Profile.md` when durable signal appears, then provide one useful question, insight, small low-risk action, ponder follow-up, or open-loop nudge |
| Harness Drift Review | Weekly or twice weekly, user-preferred evening time | Keep operating files aligned with the protected design principles |

## Adapter Prompts

- Codex: `adapters/codex/DAILY_GLIDE_CHECK_IN.md` and `adapters/codex/HARNESS_DRIFT_REVIEW.md`
- Claude Code: `adapters/claude-code/DAILY_GLIDE_CHECK_IN.md` and `adapters/claude-code/HARNESS_DRIFT_REVIEW.md`
- Generic: `adapters/generic/DAILY_GLIDE_CHECK_IN.md` and `adapters/generic/HARNESS_DRIFT_REVIEW.md`

If the harness does not support recurring automations, copy the relevant prompt into `Agent HQ/Automations/` and keep it listed as proposed in `Agent HQ/Automation Registry.md`.
