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

## Optional Memory Runtime

Follow [runtime setup](../../docs/MEMORY-RUNTIME.md) and [existing-instance upgrades](../../docs/UPGRADING.md). Install code and local state outside the synchronized workspace; install the selected `glide-memory`, `glide-dream`, `glide-review` and `glide-integrity` skills with `Agent HQ/Memory Protocol.md` and `Agent HQ/Checklists/Input and Collaboration.md`. Configure the actual runtime/configuration path on each host.

Verify source-read restrictions through this harness's actual tool and filesystem permissions. A documented rule or narrow file-writing tool does not constrain an unrestricted shell. Fresh scheduled runs use explicit successful cursors; persistent conversation history is not the memory authority. Do not enable duplicate jobs or automatic learned overlays merely by installing the adapter. Interactive review controls must use a working submission bridge and runtime receipt; otherwise use conversation.
