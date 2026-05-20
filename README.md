# Glide for Obsidian

Glide is a self-evolving personal coach and pilot for [Obsidian](https://obsidian.md/).

It gives an agent a simple home for your goals, areas, decisions, questions, research, and recurring check-ins. The point is not to create a bigger task system. **The point is to help you live with better defaults**: research areas you are not actively watching, gather context for the ones you care about, notice contradictions, and keep useful momentum without turning your life into admin.

Glide is plain Markdown: principles, memory, workflows, checklists, skills, and automation prompts that an agent can read and evolve with you. Codex, Claude Code, or another agent harness is the execution layer. Glide sets useful defaults; you choose how to run it, what tools it can access, and what data leaves your machine.

## Why Glide Exists

I built Glide because I want more attention for family, content, projects, and the ideas I keep coming back to.

For those areas, I want help managing context: old notes, rough thoughts, decisions, questions, and patterns I keep returning to. For the rest of adult life, like finances, admin, and maintenance, I want strong defaults and more autopilot, with clear approval boundaries.

That balance should be intentional, and it should change over time.

Glide grew out of [Storyloop](https://github.com/DiogoNeves/Storyloop), especially the thing I missed most afterwards: smart notes. It keeps that feeling: notes and workflows that reduce noise, increase signal, and become an evolvable interface for agents. I talked through the prototype in [this video](https://youtu.be/3Q95Rh8sRic).

It is especially useful for creators, solopreneurs, researchers, operators, and anyone who wants to manage their own context better while automating more of the rest.

## A Small Example

One way I use Glide is with messy Obsidian notes: notebook photos, quick fragments, and rough project thoughts.

I can ask, "add a writing entry for this idea," and it turns the raw note into a linked draft direction using my existing notes plus light validation.

I still capture messily. Glide adds memory and continuity around it.

## How It Works

- `Agent HQ/` as the agent-owned workspace inside your vault
- areas for durable parts of life or work
- goals, decisions, questions, ponders, contradictions, research, and reviews
- skills and checklists for repeatable ways of thinking
- a light daily loop
- drift review so the system can change without quietly becoming something else

Glide should feel less like software you manage and more like a coach that remembers, a pilot that watches the instruments, and a system you can keep changing in natural language.

## Notes Stay Yours

Glide keeps the agent's memory, working files, and operating structure in `Agent HQ/`. It can read the rest of your vault for context, but it should not mix its internal workings into your ordinary notes unless you explicitly ask.

## What Is Included

- `templates/Agent HQ/`: a generic installable Glide workspace.
- `templates/Agent HQ/User Profile.md`: concise high-level user context refreshed by `glide-update-user-profile`.
- `skills/`: portable Agent Skills prefixed with `glide-`, including profile updates, reviews, research, decisions, and daily check-ins.
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
