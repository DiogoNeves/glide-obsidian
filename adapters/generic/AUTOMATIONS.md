# Generic Harness Automations

Use this file when installing Glide automations in another harness.

Ask first:

- Does the harness support recurring runs?
- What file or UI defines recurring runs?
- What working directory should the run use?
- What model/provider will process vault context?
- Where should output appear?

## Daily Glide Check-In

- Name: Daily Glide Check-In
- Suggested cadence: daily or weekdays at the user's preferred morning time
- Prompt source: `adapters/generic/DAILY_GLIDE_CHECK_IN.md`
- Skill or checklist: `glide-daily-check-in` or `Agent HQ/Checklists/Daily Glide Check-In.md`

## Harness Drift Review

- Name: Harness Drift Review
- Suggested cadence: weekly or twice weekly at the user's preferred evening time
- Prompt source: `adapters/generic/HARNESS_DRIFT_REVIEW.md`
- Skill or checklist: `glide-harness-drift-review` or `Agent HQ/Checklists/Harness Drift Review.md`

## Nightly Research Review

- Name: Nightly Research Review
- Suggested cadence: daily at 4am local time
- Prompt source: `adapters/generic/NIGHTLY_RESEARCH_REVIEW.md`
- Skill or checklist: `glide-nightly-research-review` or `Agent HQ/Checklists/Nightly Research Review.md`

## After Install

- Add or update entries in `Agent HQ/Automation Registry.md`.
- If recurring runs are not supported, leave these as proposed manual automations.
- Do not create duplicate recurring runs.
