# Glide for Obsidian

Glide is a self-evolving personal coach and pilot for [Obsidian](https://obsidian.md/).

It gives an agent a simple home for your goals, areas, decisions, questions, research, and recurring check-ins. The point is not to create a bigger task system. **The point is to help you live with better defaults**: research areas you are not actively watching, gather context for the ones you care about, notice contradictions, and keep useful momentum without turning your life into admin.

Glide is plain Markdown: principles, memory, workflows, checklists, skills, and automation prompts that an agent can read and evolve with you. Codex, Claude Code, or another agent harness is the execution layer. Glide sets useful defaults; you choose how to run it, what tools it can access, and what data leaves your machine.

## Why Glide Exists

I want to be more present for family, content, projects, and the work and ideas that actually feel alive.

For those, Glide helps manage context: old notes, rough thoughts, projects, decisions, questions, and the patterns I keep circling back to.

For the other parts of adult life, like finances, admin, and maintenance, I want unusually good defaults with more autopilot and clear approval boundaries.

Glide lets you decide which areas need active context help and which should run more quietly in the background. That balance can change over time.

The idea grew out of [Storyloop](https://github.com/DiogoNeves/Storyloop), a creative journal for YouTube creators. Glide keeps the part that felt most useful: reducing noise and increasing signal from your own life, so your notes and workflows become an evolvable interface for agents.

It is especially useful for creators, solopreneurs, researchers, operators, and anyone who wants to manage their own context better while automating more of the rest.

## How It Works

- `Agent HQ/` as the agent-owned workspace inside your vault
- areas for durable parts of life or work
- goals, decisions, questions, ponders, contradictions, research, and reviews
- skills and checklists for repeatable ways of thinking
- a light daily loop
- drift review so the system can change without quietly becoming something else

Glide should feel less like software you manage and more like a coach that remembers, a pilot that watches the instruments, and a system you can keep changing in natural language.

## A Small Example

I use Obsidian for messy manual notes: notebook photos, quick fragments, and rough project thoughts.

Glide can turn a tiny request like "add a writing entry for this idea" into a linked note that draws on my own notes, thoughts, and light validation. It keeps the useful source context and gives the idea a clean first shape.

The important bit is that manual capture still works; the agent adds continuity around it.

## Notes Stay Yours

Glide keeps the agent's memory, working files, and operating structure in `Agent HQ/`. It can read the rest of your vault for context, but it should not mix its internal workings into your ordinary notes unless you explicitly ask.

## What Is Included

- `templates/Agent HQ/`: a generic installable Glide workspace.
- `skills/`: portable Agent Skills prefixed with `glide-`.
- `automations/`: installable starter prompts for daily check-ins and drift review.
- `adapters/`: Codex, Claude Code, and generic harness notes.
- `INSTALL.md`: an agent-readable installer flow.
- `docs/CONCEPT.md`: the short philosophy behind Glide.
- `examples/`: brief walkthroughs for common use cases.
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

Glide itself does not collect telemetry, run servers, transmit vault data, or store user data anywhere. It is Markdown structure and instructions installed in your vault.

Privacy depends on the harness and services you choose to connect. Review your model provider, sync, Git hosting, connectors, and automation policies before giving any tool access to sensitive content.

See [docs/PRIVACY.md](docs/PRIVACY.md).

## Contributing

Suggestions are welcome: better default areas, sharper checklists, new skills, harness adapters, privacy improvements, and examples of what made Glide useful or annoying in real use.

See [CONTRIBUTING.md](CONTRIBUTING.md).

This project grew from how I use [Codex](https://openai.com/index/introducing-the-codex-app/) and [Obsidian](https://obsidian.md/) daily, following a structure inspired by [How I use Obsidian](https://stephango.com/vault).
