# Codex Adapter

Use this adapter when Codex is the execution harness.

## Install Shape

- Start from the Obsidian vault root.
- Copy Glide workspace to `Agent HQ/`.
- Copy skills to `.agents/skills/`.
- Create or update root `AGENTS.md` with `ROOT_AGENTS_SECTION.md`.
- Offer automations only after explicit confirmation.

## Starter Automation Prompts

- `AUTOMATIONS.md`
- `DAILY_GLIDE_CHECK_IN.md`
- `HARNESS_DRIFT_REVIEW.md`

Codex automations should be specific, reviewable, and conservative. Prefer a short useful daily output over broad daily summaries.

## Optional Memory Runtime

Follow [complete runtime setup](../../docs/SETUP.md) and [existing-instance upgrades](../../docs/UPGRADING.md). Install code and local state outside the synchronized workspace; install the selected `glide-memory`, `glide-dream`, `glide-review` and `glide-integrity` skills with `Agent HQ/Memory Protocol.md`. Configure the actual runtime/configuration path on each host.

Verify source-read restrictions through this harness's actual tool and filesystem permissions. A documented rule or narrow file-writing tool does not constrain an unrestricted shell. Fresh scheduled runs use explicit successful cursors; persistent conversation history is not the memory authority. Do not enable duplicate jobs or automatic learned overlays merely by installing the adapter. Interactive review controls must use a working submission bridge and runtime receipt; otherwise use conversation.

Fresh installs use manual knowledge review and text presentation. Automatic knowledge processing and interactive UI are separate owner choices. Inspect `glide_verify` for effective review settings and preserve omitted choices on upgrades. Compact job inputs can be expanded with `glide_job_input_page` for relevant history.
