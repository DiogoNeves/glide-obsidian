# Privacy

Glide is Markdown structure, templates, skills, and instructions installed in your vault.

Glide does not:

- run servers,
- collect telemetry,
- transmit vault data,
- operate a hosted service.

Glide defines behavior. Your chosen harness decides where computation happens and what data is sent.

## What Actually Handles Your Data

Privacy depends on what you connect to Glide:

- agent harnesses such as Codex, Claude Code, OpenCode, or other tools,
- cloud model providers,
- local model runtimes,
- Obsidian Sync or other sync tools,
- Git hosting,
- email, calendar, browser, or app connectors,
- automation services,
- operating-system permissions.

Review those tools' privacy, retention, training, logging, connector, and automation policies before giving them access to sensitive content.

## Connectors And Automations

Plain vault-file access is different from connected tool access.

Connectors and automations may expose more data because they can read inboxes, calendars, browsers, files, tasks, or external apps depending on configuration. Install them deliberately and keep approval boundaries clear.

## Recommended Defaults

- Start with the smallest access that works.
- Add connectors only when they solve a real problem.
- Prefer read-only access first.
- Require approval before high-stakes or external actions.
- Keep `Harness Design Principles.md` protected.
- Review automation output before increasing autonomy.

## Repository Hygiene

This repository should never include personal vault content or private examples.

Before public release:

- scan the working tree for private content,
- rebuild git history if any personal metadata or content exists,
- use neutral author metadata,
- use neutral license attribution,
- verify all examples are generic.

## Optional Local Memory Runtime

When enabled, the runtime stores a searchable SQLite index and private configuration outside the workspace/vault. The index can contain source text and metadata; treat it as sensitive local data even though it is rebuildable. The Markdown bundle store includes history and retained evidence, so its sync and backup destinations receive that content too. The runtime itself does not grant connector access, choose a cloud model or enable a hosted service. Public repositories contain only synthetic fixtures and generic setup instructions.
