# Generic Harness Adapter

Use this adapter when the harness is not Codex or Claude Code.

Start from the Obsidian vault root. All paths below are relative to that root.

Ask the user:

- Which root instruction file should Glide update?
- Where should `SKILL.md` folders live?
- Does the harness support recurring automations?
- Does the harness support subagents?
- What model/provider privacy policy applies?

If the harness does not support skills, install `Agent HQ/` and add the root instruction snippet to the harness's instruction file.

## Starter Automation Prompts

- `AUTOMATIONS.md`
- `DAILY_GLIDE_CHECK_IN.md`
- `HARNESS_DRIFT_REVIEW.md`

If recurring runs are not supported, install these as proposed manual automations in `Agent HQ/Automations/`.
