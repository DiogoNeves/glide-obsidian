# Glide for Obsidian

Glide is a portable operating layer for agent-assisted Obsidian vaults.

It gives an AI harness a clear way to help with goals, decisions, areas of life or work, recurring reviews, research, and lightweight daily check-ins without turning everything into one endless chat thread.

Glide is not a hosted service. It is a set of Markdown files, templates, checklists, and portable skills. Codex, Claude Code, OpenCode, local models, cloud models, connectors, Git, Obsidian Sync, and automations are the execution layer. Glide defines behavior; your harness decides where computation happens and what data is sent.

## Why Glide Exists

Modern agent tools are powerful, but they often lack a durable operating structure. Glide provides that structure:

- a calm `Agent HQ/` workspace inside your vault
- areas for ongoing domains like finance, health, family, career, business, home, friends, and travel
- goals, decisions, questions, contradictions, ponders, research, and reviews
- skills that teach an agent how to evolve the system over time
- daily check-ins that stay light instead of becoming homework
- drift review so the system keeps its original principles as it changes

The aim is not maximum autonomy. The aim is useful human agency: automate low-value coordination, preserve attention, and keep the user engaged with the decisions that actually matter.

## What Is Included

- `templates/Agent HQ/`: a generic installable Glide workspace.
- `skills/`: portable Agent Skills prefixed with `glide-`.
- `automations/`: installable starter prompts for daily check-ins and drift review.
- `adapters/`: Codex, Claude Code, and generic harness notes.
- `INSTALL.md`: an agent-readable installer flow.
- `docs/PRIVACY.md`: what Glide does and does not do with data.
- `docs/HARNESSES.md`: how Glide maps to common agent harnesses.

## Install

Read [INSTALL.md](INSTALL.md) or ask your agent harness to follow it.

The installer flow is intentionally conservative:

1. Inspect your vault without changing anything.
2. Ask which harness you use.
3. Ask which default areas to include.
4. Explain how Glide works.
5. Copy the structure and skills only after confirmation.
6. Create or update the correct root instruction file.
7. Offer starter automations only after explicit confirmation.

## Privacy

Glide itself does not collect telemetry, run servers, transmit vault data, or store user data anywhere. It is local Markdown structure and instructions.

Privacy depends on the harness and services you choose to connect. Review your model provider, harness, sync, Git hosting, connector, browser tool, and automation policies before giving any tool access to sensitive content.

See [docs/PRIVACY.md](docs/PRIVACY.md).

## Contributing

Suggestions are welcome: better default areas, sharper checklists, new skills, harness adapters, privacy improvements, and examples of what made Glide useful or annoying in real use.

See [CONTRIBUTING.md](CONTRIBUTING.md).
