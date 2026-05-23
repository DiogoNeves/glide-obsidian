# Optional Software Access

Glide can connect to other software when the user chooses to give the harness access.

This is optional. Glide does not require app access, and app access depends on the harness, operating system permissions, connectors, and the app's own APIs or automation support.

## macOS Pattern

Many macOS apps can be accessed through the same general ladder:

1. Use an official connector, API, or MCP server when available.
2. Use export/import files when they are safer or easier to review.
3. Use AppleScript, Shortcuts, URL schemes, or app automation when the app supports them.
4. Use browser or computer control only when no better interface exists.

Start read-only. Ask before writing, sending, deleting, archiving, purchasing, posting, scheduling, or changing account data.

macOS may require the user to approve Automation permissions for the harness or terminal app controlling another app. Do not bypass privacy prompts or blindly click security dialogs.

## App Guides

- [Things](things.md)
- [Apple Notes](apple-notes.md)

## Adding Another App

Add a short guide for each app only when it has app-specific safety rules, semantics, or setup steps.

A good app guide should include:

- what the app is the source of truth for,
- safe read methods,
- approval-gated write methods,
- methods to avoid,
- likely permission prompts,
- what to report back to the user.
