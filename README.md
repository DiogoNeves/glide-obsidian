# Glide for Obsidian

Glide is a self-evolving personal coach and pilot for [Obsidian](https://obsidian.md/).

It gives an agent a simple home for your goals, areas, decisions, questions, research, and recurring check-ins. The point is not to create a bigger task system. The point is to help you live with better defaults: research areas you are not actively watching, gather context for the ones you care about, notice contradictions, and keep useful momentum without turning your life into admin.

Glide is plain Markdown: principles, memory, workflows, checklists, skills, and automation prompts that an agent can read and evolve with you. Codex, Claude Code, or another agent harness is the execution layer. Glide defines behavior; your harness decides where computation happens and what data is sent.

## Why Glide Exists

Most agent tools are powerful in the moment and forgetful over time. Glide gives them a durable shape:

- `Agent HQ/` as the agent-owned workspace inside your vault
- areas for durable parts of life or work
- goals, decisions, questions, ponders, contradictions, research, and reviews
- skills and checklists for repeatable ways of thinking
- a light daily loop
- drift review so the system can change without quietly becoming something else

Glide should feel less like software you manage and more like a coach that remembers, a pilot that watches the instruments, and a system you can keep changing in natural language.

## A Small Example

I use Obsidian for messy manual notes too: photos of notebook pages, quick fragments, and rough project thoughts. Glide can turn a tiny request like "add a writing entry for this idea" into a linked note that pulls from previous notes, keeps the useful source context, and gives the idea a first shape. The important bit is that manual capture still works; the agent adds continuity around it.

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

Privacy depends on the harness and services you choose to connect. Review your model provider, sync, Git hosting, connectors, and automation policies before giving any tool access to sensitive content.

See [docs/PRIVACY.md](docs/PRIVACY.md).

## Contributing

Suggestions are welcome: better default areas, sharper checklists, new skills, harness adapters, privacy improvements, and examples of what made Glide useful or annoying in real use.

See [CONTRIBUTING.md](CONTRIBUTING.md).

This project grew from how I use [Codex](https://openai.com/index/introducing-the-codex-app/) and [Obsidian](https://obsidian.md/) daily, following a structure inspired by [How I use Obsidian](https://stephango.com/vault).
