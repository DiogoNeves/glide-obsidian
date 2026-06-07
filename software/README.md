# Optional Software Access

Glide can connect to other software when the user chooses to give the harness access.

This is optional. Glide does not require app access, and app access depends on the harness, operating system permissions, connectors, and the app's own APIs or automation support.

## macOS Pattern

Many macOS apps can be accessed through the same general ladder:

1. Use an official connector, API, or MCP server when available.
2. Use export/import files when they are safer or easier to review.
3. Use AppleScript, JavaScript for Automation, Shortcuts, URL schemes, or app automation when the app supports them.
4. Use browser or computer control only when no better interface exists.

Start read-only. Ask before writing, sending, deleting, archiving, purchasing, posting, scheduling, or changing account data.

Default durable note updates to the Obsidian vault, not Apple Notes or another external note app, unless the user explicitly asks to write somewhere else.

macOS may require the user to approve Automation permissions for the harness or terminal app controlling another app. Do not bypass privacy prompts or blindly click security dialogs.

## Note Imports

Before importing notes from any external app or export, learn how the target vault works.

1. Inspect the vault instructions, templates, category/index notes, project notes, recent notes, and existing imported notes.
2. Sample enough notes to understand filenames, links, tags, source markers, attachments, categories, and what should stay out of the vault.
3. Create or update the app-specific import skill/checklist from that structure before the first real import.
4. Do a dry-run mapping for new or ambiguous import patterns and ask before writing.
5. Revalidate the mapping when the vault structure changes or imported notes start looking wrong.

Start metadata-first. Read note bodies only when needed to infer structure or decide whether a scoped import is appropriate.

## App Guides

- [Things](things.md)
- [Apple Notes](apple-notes.md)
- [Messages / iMessage](imessage.md)

## Adding Another App

Add a short guide for each app only when it has app-specific safety rules, semantics, or setup steps.

A good app guide should include:

- what the app is the source of truth for,
- safe read methods,
- approval-gated write methods,
- vault-structure learning before note imports,
- methods to avoid,
- likely permission prompts,
- what to report back to the user.
