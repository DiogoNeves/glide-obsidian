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

## Optional Memory Runtime

Follow [runtime setup](../../docs/MEMORY-RUNTIME.md) and [existing-instance upgrades](../../docs/UPGRADING.md). Install code and local state outside the synchronized workspace; install the selected `glide-memory`, `glide-dream`, `glide-review` and `glide-integrity` skills with `Agent HQ/Memory Protocol.md`. Configure the actual runtime/configuration path on each host.

Verify source-read restrictions through this harness's actual tool and filesystem permissions. A documented rule or narrow file-writing tool does not constrain an unrestricted shell. Fresh scheduled runs use explicit successful cursors; persistent conversation history is not the memory authority. Do not enable duplicate jobs or automatic learned overlays merely by installing the adapter. Interactive review controls must use a working submission bridge and runtime receipt; otherwise use conversation.
