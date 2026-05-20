# Install Glide for Obsidian

This file is written for an agent harness to execute, but it is also readable by a human.

## Human Summary

The installer should:

1. Inspect the existing vault without changing anything.
2. Ask which harness is being used: Codex, Claude Code, OpenCode/other, or manual.
3. Ask which default areas to include.
4. Explain how Glide works and how to interact with it.
5. Copy the Glide structure and selected skills only after confirmation.
6. Create or update the correct root harness instruction file.
7. Suggest light evolution practices.
8. Offer to add the daily automation if the harness supports it, after explicit confirmation.

Glide sets useful defaults. Your harness decides where computation happens and what data is sent.

## Installer Contract

- Do not change the target vault during inspection.
- Do not overwrite existing files without explicit confirmation.
- Do not merge into an existing `Agent HQ/` without explicit confirmation.
- Do not install automations without explicit confirmation.
- Do not promise privacy guarantees for third-party harnesses, models, connectors, Git hosts, sync providers, or automation services.

## Step 1: Inspect The Vault

Inspect only. Do not write files.

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
- `User Profile.md` keeps concise high-level context and is refreshed only when durable signal appears.
- Ponders do not automatically become goals.
- Durable answers should be captured as the conversation progresses.
- Glide memory and agent workings stay in `Agent HQ/`; ordinary vault notes are read for context but not edited unless the user explicitly asks.
- Daily check-ins should be light.
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

Offer only two starter automations:

- Daily Glide Check-In
- Harness Drift Review

Confirm before creating either.

Prefer adding steps to an existing automation if one already exists.

The installable prompt sources are:

- `automations/daily-glide-check-in.md`
- `automations/harness-drift-review.md`

Use harness-specific versions when available:

- `adapters/codex/AUTOMATIONS.md`
- `adapters/codex/DAILY_GLIDE_CHECK_IN.md`
- `adapters/codex/HARNESS_DRIFT_REVIEW.md`
- `adapters/claude-code/AUTOMATIONS.md`
- `adapters/claude-code/DAILY_GLIDE_CHECK_IN.md`
- `adapters/claude-code/HARNESS_DRIFT_REVIEW.md`
- `adapters/generic/AUTOMATIONS.md`
- `adapters/generic/DAILY_GLIDE_CHECK_IN.md`
- `adapters/generic/HARNESS_DRIFT_REVIEW.md`

For each automation:

1. Ask whether to install it now.
2. Ask for cadence, time, timezone, workspace, model, reasoning effort, and output destination when the harness needs those fields.
3. If an equivalent automation already exists, ask whether to update it instead of creating a duplicate.
4. Create the recurring run only after confirmation.
5. Update `Agent HQ/Automation Registry.md` and the matching note in `Agent HQ/Automations/`.

If the harness does not support automations, keep the notes in `Agent HQ/Automations/` as proposed manual automations.

## Step 7: Help The User Evolve Glide

Suggest:

- create skills for repeatable tasks,
- keep automations few and high-signal,
- give feedback when the daily run is noisy or useful,
- add areas only when a real domain needs ongoing care,
- keep `Harness Design Principles.md` protected,
- periodically review drift before changing behavior.
