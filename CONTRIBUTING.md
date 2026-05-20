# Contributing To Glide for Obsidian

Glide is early and intentionally Markdown-first. Contributions are welcome when they make the system easier to install, safer to evolve, or more useful in real use.

## Good Contributions

- Better default area templates.
- Clearer checklists.
- New portable skills.
- Harness adapters for Codex, Claude Code, OpenCode, local agents, or other tools.
- Privacy and install safety improvements.
- Examples of daily check-ins that felt useful.
- Examples of behavior that created friction.

## Contribution Rules

- Do not include personal vault content, private names, emails, client data, financial details, medical details, or private project data.
- Use generic language: `the user`, `your vault`, `your goals`, `your areas`.
- Keep skills portable and concise.
- Put long process detail in checklists or docs rather than bloating `SKILL.md`.
- Prefer additive examples over changing core behavior.
- For behavior changes, explain which design principle the change supports.

## Skill Style

Each skill should:

- live in `skills/<skill-name>/SKILL.md`,
- use a `glide-` prefix,
- include short YAML frontmatter with `name` and `description`,
- load only the context it needs,
- keep final judgment and high-stakes approval in the main harness thread.

## Privacy Review

Before opening a pull request, scan for personal data:

- names and emails,
- absolute local paths,
- private company names,
- family or health details,
- app or account details,
- copied personal notes,
- model/provider credentials.

See [docs/PRIVACY.md](docs/PRIVACY.md).
