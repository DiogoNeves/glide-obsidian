# Install Glide for Obsidian

This file is written for an agent harness to execute, but it is also readable by a human.

## Human Summary

The installer should:

1. Start from the root folder of the target Obsidian vault.
2. Inspect the existing vault without changing anything.
3. Ask which harness is being used: Codex, Claude Code, OpenCode/other, or manual.
4. Ask which default areas to include.
5. Explain how Glide works and how to interact with it.
6. Copy the Glide structure and selected skills only after confirmation.
7. Create or update the correct root harness instruction file.
8. Mention optional software access guides.
9. Suggest light evolution practices.
10. Offer starter automations if the harness supports them, after explicit confirmation.

All install paths in this file are relative to the Obsidian vault root.

Glide sets useful defaults. Your harness decides where computation happens and what data is sent.

## Installer Contract

- Install Glide from the root folder of the target Obsidian vault, not from a subfolder.
- Treat `Agent HQ/`, `.agents/skills/`, `.claude/skills/`, `AGENTS.md`, and `CLAUDE.md` as vault-root paths.
- Do not change the target vault during inspection.
- Do not overwrite existing files without explicit confirmation.
- Do not merge into an existing `Agent HQ/` without explicit confirmation.
- Do not install automations without explicit confirmation.
- Do not promise privacy guarantees for third-party harnesses, models, connectors, Git hosts, sync providers, or automation services.

## Step 1: Inspect The Vault

Inspect only. Do not write files.

Confirm that the target directory is the Obsidian vault root. If the current working directory is a subfolder, stop and ask the user to run the installer from the vault root or provide the vault root path.

Check for:

- `Agent HQ/`
- `Agent HQ/Automations/`
- `.agents/skills/`
- `.claude/skills/`
- `AGENTS.md`
- `CLAUDE.md`
- other harness instruction files
- existing automation files or automation documentation
- how the vault is organized: root notes, daily/calendar notes, unique notes, project notes, category/index notes, attachments, templates, clippings, and any naming or linking conventions

Report what exists and what Glide would need to create or update.

Also summarize the vault's note style in one short paragraph. If the vault has clear conventions, adapt the root harness instruction section minimally so Glide respects them. For example: where project notes live, how calendar notes are used, how unique notes are named, where attachments belong, and whether ordinary notes should stay mostly in the vault root. Do not reorganize the vault or add broad rules unless the user confirms.

For any optional app workflow that imports notes into the vault, use this note-style summary as the starting point, then sample representative notes and create or update the app-specific import skill/checklist before the first real import.

If `Agent HQ/` already exists, stop and ask whether to:

- merge carefully,
- install Glide under another folder,
- skip the structure and install only skills,
- or cancel.

## Step 2: Ask Which Harness To Use

Ask the user which harness should run Glide.

Recommended mappings:

| Harness | Root instruction file | Skill directory |
| --- | --- | --- |
| Codex | `AGENTS.md` | `.agents/skills/` |
| Claude Code | `CLAUDE.md` | `.claude/skills/` |
| Other or manual | ask the user | ask the user |

For Codex, create `AGENTS.md` if missing or append/update a clearly marked Glide section.

For Claude Code, create `CLAUDE.md` if missing or append/update a clearly marked Glide section.

For other harnesses, ask which root instruction file and skill directory the harness uses.

## Step 3: Ask Which Areas To Include

Recommended default areas:

- Finance
- Health
- Family
- Home
- Career
- Business
- Friends & Community
- Travel

Ask whether to include all, none, or a custom subset.

Create areas using the `glide-create-area` skill behavior. Each area should include:

- `AGENTS.md`
- `Area.md`
- `Goals.md`
- `Context.md`
- `Reminders.md`
- `Sources.md`
- `Decisions.md`
- `Questions.md`
- `Reviews/README.md`
- `Checklists/README.md`
- `Research/README.md`

## Step 4: Explain Glide To The User

Before installing, explain:

- Glide lives in `Agent HQ/`.
- The user can talk naturally.
- The harness converts conversation into structure.
- `User Profile.md` keeps concise high-level context and is refreshed by `glide-update-user-profile` only when durable signal appears.
- Ponders do not automatically become goals.
- Durable answers should be captured as the conversation progresses.
- Glide memory and agent workings stay in `Agent HQ/`; ordinary vault notes are read for context but not edited unless the user explicitly asks.
- Daily check-ins should be light.
- Optional software access guides can help connect apps such as Things, Apple Notes, Apple Calendar, or Messages after the user approves the access method.
- High-stakes actions require approval.
- Glide itself does not collect data; the chosen harness controls execution and data exposure.

## Step 5: Install After Confirmation

After explicit confirmation:

1. Copy the base `templates/Agent HQ/` files and folders into the vault, excluding default area subfolders until area selection is applied.
2. Copy only the selected area folders from `templates/Agent HQ/Areas/`.
3. If no default areas are selected, copy `templates/Agent HQ/Areas/AGENTS.md` and leave the folder ready for future areas.
4. Copy selected `skills/glide-*` folders into the harness-specific skill directory.
5. Create or update the root harness instruction file with the appropriate adapter snippet.
6. Add only the minimal vault-convention guidance needed from inspection.
7. Leave existing unrelated instructions intact.
8. Record selected default areas and installed skills in `Agent HQ/Automation Registry.md` or another appropriate operations note.

Use these adapter snippets:

- Codex: `adapters/codex/ROOT_AGENTS_SECTION.md`
- Claude Code: `adapters/claude-code/ROOT_CLAUDE_SECTION.md`
- Generic: `adapters/generic/ROOT_INSTRUCTIONS_SECTION.md`

## Step 6: Offer Starter Automations

Offer three starter automations:

- Daily Glide Check-In
- Harness Drift Review
- Nightly Research Review

Confirm before creating any automation.

Prefer adding steps to an existing automation if one already exists.

The installable prompt sources are:

- `automations/daily-glide-check-in.md`
- `automations/harness-drift-review.md`
- `automations/nightly-research-review.md`

Use harness-specific versions when available:

- `adapters/codex/AUTOMATIONS.md`
- `adapters/codex/DAILY_GLIDE_CHECK_IN.md`
- `adapters/codex/HARNESS_DRIFT_REVIEW.md`
- `adapters/codex/NIGHTLY_RESEARCH_REVIEW.md`
- `adapters/claude-code/AUTOMATIONS.md`
- `adapters/claude-code/DAILY_GLIDE_CHECK_IN.md`
- `adapters/claude-code/HARNESS_DRIFT_REVIEW.md`
- `adapters/claude-code/NIGHTLY_RESEARCH_REVIEW.md`
- `adapters/generic/AUTOMATIONS.md`
- `adapters/generic/DAILY_GLIDE_CHECK_IN.md`
- `adapters/generic/HARNESS_DRIFT_REVIEW.md`
- `adapters/generic/NIGHTLY_RESEARCH_REVIEW.md`

For each automation:

1. Ask whether to install it now.
2. Ask for cadence, time, timezone, workspace, model, reasoning effort, and output destination when the harness needs those fields.
3. If an equivalent automation already exists, ask whether to update it instead of creating a duplicate.
4. Create the recurring run only after confirmation.
5. Update `Agent HQ/Automation Registry.md` and the matching note in `Agent HQ/Automations/`.

If the harness does not support automations, keep the notes in `Agent HQ/Automations/` as proposed manual automations.

## Step 7: Offer Optional Software Access

Mention that `software/` contains optional guides for connecting other apps. Do not enable app access by default.

If the user wants app access:

1. Ask which software they want to connect.
2. Prefer official connectors, APIs, MCP servers, exports, AppleScript, Shortcuts, or URL schemes before computer control.
3. Add only the relevant app guide or checklist.
4. Record approval boundaries before reading or writing app data.
5. For app-specific behavior, create a small skill and checklist instead of expanding the daily check-in.

Current starter guides:

- `software/things.md`
- `software/apple-notes.md`
- `software/apple-calendar.md`
- `software/imessage.md`

## Step 8: Help The User Evolve Glide

Suggest:

- create skills for repeatable tasks,
- keep automations few and high-signal,
- give feedback when the daily run is noisy or useful,
- add areas only when a real domain needs ongoing care,
- keep `Harness Design Principles.md` protected,
- periodically review drift before changing behavior.
