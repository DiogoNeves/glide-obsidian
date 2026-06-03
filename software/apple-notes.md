# Apple Notes

Use when the user wants Glide to inspect or export Apple Notes data.

## Safety Contract

Treat Apple Notes as sensitive personal data.

Prefer the Notes.app AppleScript interface over direct database access. Start with metadata-only checks before reading note bodies.

Do not create, edit, rename, move, delete, lock, unlock, or archive notes unless the user explicitly asks for that exact action.

## Vault Structure First

Before importing Apple Notes into Obsidian, learn the vault's note structure.

Inspect the vault instructions, templates, recent root notes, project notes, category/index notes, existing imported notes, links, tags, source markers, and attachment conventions. Sample enough notes to infer how imported notes should be named, linked, tagged, sourced, deduplicated, and routed.

If the import behavior is not already encoded, create or update the Apple Notes import skill/checklist before writing imported notes. For a new or ambiguous import pattern, prepare a dry-run mapping and ask the user before creating files.

Revalidate this mapping when the vault structure changes or imported notes start looking wrong.

## Safe Read Path

Start with a tiny read-only probe:

```sh
osascript -e 'tell application "Notes" to count notes'
```

If that works, inspect account or folder metadata before note bodies.

Only read note bodies when the user asks for the specific scope. Export content to a temporary file outside the vault when possible, then summarize or import only what the user approves.

## macOS Permissions

The first AppleScript query may wait for a macOS Automation permission prompt. The user must approve the harness or terminal app controlling Notes.

Direct filesystem reads of Apple Notes storage may fail because of macOS privacy protections. Do not bypass those protections casually. If database access is ever needed, copy the store to a temporary location first and query only the copy in read-only mode.
