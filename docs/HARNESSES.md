# Harnesses

Glide is harness-agnostic. It defines behavior in Markdown, checklists, and portable skills. A harness executes that behavior.

## Codex

Suggested layout:

- root instructions: `AGENTS.md`
- skills: `.agents/skills/<skill-name>/SKILL.md`
- Glide workspace: `Agent HQ/`

Use the Codex adapter snippets in `adapters/codex/`.

Codex automations can run recurring prompts. Install automations only after the user confirms the schedule, prompt, model, and workspace.

Use `adapters/codex/AUTOMATIONS.md` for the Daily Glide Check-In and Harness Drift Review install flow.

## Claude Code

Suggested layout:

- root instructions: `CLAUDE.md`
- skills: `.claude/skills/<skill-name>/SKILL.md`
- Glide workspace: `Agent HQ/`

Use the Claude Code adapter snippets in `adapters/claude-code/`.

Claude Code can also package capabilities through extensions or plugins. Keep the Markdown template install simple first.

Use `adapters/claude-code/AUTOMATIONS.md` when a scheduler or recurring-run mechanism is available.

## Other Harnesses

Ask the user:

- Which root instruction file does the harness read?
- Where should `SKILL.md` folders live?
- Does it support recurring automations?
- Does it support subagents?
- What data leaves the local machine?

If a harness does not support skills, install only `Agent HQ/` and add the core process instructions to the harness root file.

Each adapter folder includes a root instruction snippet, an automation install note, and starter prompts for the Daily Glide Check-In and Harness Drift Review. Only install recurring runs when the harness supports them and the user confirms.

## Portability Rule

Keep Glide behavior in English files. Harness-specific code should be a thin adapter, not the source of truth.
