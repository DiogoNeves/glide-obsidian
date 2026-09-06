# Glide for Obsidian

Glide is a personal coach and memory layer for your Obsidian vault, run through Codex, Claude Code or another supported agent harness.

Keep capturing thoughts, unique notes and clippings in your existing style. Glide reads that material and adds connected knowledge and operational context under `Agent HQ/`. You can ask what changed, what remains open, or whether an old assumption still holds.

## Three parts

- **Your writing:** original notes and source material, preserved unchanged.
- **Knowledge:** useful concepts with supporting passages, dates, uncertainty and meaningful links.
- **Operations:** intentions, commitments, decisions and outcomes, kept distinct.

The optional memory runtime keeps records and revision history in **human-readable Markdown**, using Obsidian links and valid filenames without repeating the title inside each generated note. SQLite is a local, rebuildable search index. Python, the database and private configuration stay outside the synchronized vault; reading your notes needs none of them.

Reviews work in conversation. Text is the default; interactive reviews are optional and only report success after a real writer receipt. Optional automatic knowledge processing keeps its output marked as AI and unreviewed. It does not authorize external actions.

The recorded local validation passed **139 runtime tests**, including recovery after deleting a disposable SQLite index. [Validation details](docs/VALIDATION.md) explain the checks, model screen and remaining field observations.

## Get started

Open your vault in the agent harness and ask it to follow [INSTALL.md](INSTALL.md). Existing capture conventions stay in place.

- [Complete memory setup](docs/SETUP.md): the shared runtime and Obsidian-specific choices.
- [Upgrade an existing instance](docs/UPGRADING.md): inspection, migration, machine handover and rollback.
- [Validation](docs/VALIDATION.md): executable checks for provenance, recovery, stale writes and bounded learning, with their limits.
- [Storage and runtime contract](docs/MEMORY-RUNTIME.md).

Glide provides no hosted service or telemetry. Your harness, model provider, connectors and sync choices determine data exposure. See [privacy](docs/PRIVACY.md).

This edition preserves the file-and-link approach inspired by [How I use Obsidian](https://stephango.com/vault). [Contributions](CONTRIBUTING.md) are welcome.
