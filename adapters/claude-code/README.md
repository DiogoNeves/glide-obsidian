# Claude Code Adapter

Use this adapter when Claude Code is the execution harness.

## Install Shape

- Start from the Obsidian vault root.
- Copy Glide workspace to `Agent HQ/`.
- Copy skills to `.claude/skills/`.
- Create or update root `CLAUDE.md` with `ROOT_CLAUDE_SECTION.md`.
- If using Claude Code plugins later, keep this Markdown install as the source of truth.

Claude Code skills are regular folders containing `SKILL.md`. Keep Glide skills prefixed with `glide-`.

## Starter Automation Prompts

- `AUTOMATIONS.md`
- `DAILY_GLIDE_CHECK_IN.md`
- `HARNESS_DRIFT_REVIEW.md`

Install recurring runs only when the user has chosen a scheduler or Claude Code automation mechanism and confirmed the schedule.
