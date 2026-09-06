# Set up versioned memory in Obsidian

The [shared setup walkthrough](https://github.com/DiogoNeves/glide/blob/main/docs/SETUP.md) is maintained with the Python runtime in the Glide repository. Use the matching local checkout/archive and its `docs/SETUP.md` when testing an unpublished build; `main` is not a substitute for the pin in this distribution's `compatibility.json`.

Use these distribution values in that walkthrough:

```sh
export GLIDE_PACKAGE='/absolute/path/to/glide'
export GLIDE_DIST='/absolute/path/to/glide-obsidian'
export GLIDE_ADAPTER='obsidian'
export GLIDE_STORE='Agent HQ/Memory'
```

The guide covers prerequisites, a synthetic source → proposal → receipt, local writer activation, Codex MCP/read-only settings, per-device skills, intake, optional native sources and learned overlays, interactive/text review, recovery and schedule verification. The shared runtime contains the SQLite schema, all core Python, reusable native helper source and review template. There is no separate Obsidian database implementation or empty database to copy.

For the real vault, preserve its existing unique-note, clipping, reference and attachment conventions. Markdown intake reads files where they live; an additional inbox is optional. Keep Python, the SQLite index, dependencies and private configuration outside the vault and every synchronization root. Reading and linking the synced Markdown needs no runtime.

Install this edition's four memory skills with `templates/Agent HQ/Memory Protocol.md`, and merge its root instructions. Check skill discovery and local paths on every device; hidden folders do not constitute an Obsidian Sync installer. Generated notes use Obsidian links and valid filenames without repeated opening titles. Originals receive no processing tags, block IDs or rewrites.

Fresh preferences are manual knowledge review and text presentation. Automatic knowledge is an optional, explicitly scoped inbox workflow; output remains AI-authored and unreviewed. Interactive presentation is independent and falls back to conversation. Upgrading preserves omitted preferences and absent keys; review the [explicit and legacy policy distinctions](MEMORY-RUNTIME.md#setup-and-review-preferences). Use the [optional automation portfolio](../automations/portable-memory.md) after cutover.

Before activating this vault, use [existing-instance upgrades](UPGRADING.md), [compatibility](COMPATIBILITY.md) and [validation](VALIDATION.md). Review [SQLite/Git/sync choices](STORAGE-AND-GIT.md) when configuring transport or backups.

Optionally offer [daily unique project notes](DAILY-NOTES.md) after the core setup. Category permission, the Obsidian companion, per-device installation and an existing intake-job step are separate from knowledge-review preferences. Leave it disabled until the owner chooses the project scope.
