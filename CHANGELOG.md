# Changelog

Notable changes to Glide for Obsidian.

## 2026-06-25

### Added Weekly Glide Update Checks

- Added `glide-check-for-updates`, `Agent HQ/Glide Updates.md`, a weekly update-check automation prompt, and harness adapter prompts.
- Added update-state and migration guidance so installed workspaces can track the last seen upstream release and preserve local instructions.

### Added Nightly Research Review

- Added `glide-nightly-research-review` for quiet 4am background research, memory, eval, and cross-area maintenance.
- Added installable automation prompts and adapter prompts for Codex, Claude Code, and generic harnesses.
- Added a rolling 4-day `Nightly Research Audit` template for internal change tracking.

## 2026-06-20

### Capped Daily Check-In Output

- Updated daily check-ins to prefer one item, allow up to three only when each is urgent or very important, and ask before continuing when more may matter.
- Added daily ranking and source-arbitration rules for competing signals.
- Added evals as read-only drift-review evidence.

## 2026-06-15

### Added Follow-Through And Calendar Guidance

- Added `Follow-Through Ledger.md` as a lightweight place for promises, waiting threads, and commitments that should not disappear.
- Updated daily check-ins and automation prompts to scan follow-through items alongside reminders, open loops, goals, questions, ponders, and app-action candidates.
- Added an Apple Calendar software guide with read-only macOS access patterns and approval-gated write boundaries.
- Added a general app interface checklist for connector, file, browser, and computer-use workflows.
- Updated harness drift review to trim verbose new instructions when clarity and behavior are preserved.
- Added purchase research and stronger weekly review guidance around commitments, task sources, and realistic planning.

## 2026-06-07

### Clarified Apple Notes Scripting Access

- Updated Apple Notes guidance from AppleScript-only wording to the broader Notes.app scripting interface.
- Added guidance to prefer JavaScript for Automation helpers with native Notes date filters for recurring metadata scans.
- Added a safety note to retry read-only metadata checks through the user-approved automation path when a managed sandbox cannot reach Notes.app.

## 2026-06-03

### Added Vault-Structure Learning Before Note Imports

- Added a general rule that note-import workflows should inspect the vault's existing structure before writing imported notes.
- Updated Apple Notes guidance to create or update the import skill/checklist from sampled vault conventions before the first real import.
- Added installer guidance so optional app-import workflows adapt to the user's vault instead of assuming a generic note shape.

## 2026-05-25

### Added Messages / iMessage Access Guide

- Added a Messages/iMessage software guide for macOS.
- Documented safe read paths, approval-gated sends, macOS permissions, and methods to avoid.
- Clarified that Messages access should start read-only, narrow, and should not import private transcripts into Obsidian by default.

## 2026-05-23

### Added Area Reminders

- Added `Reminders.md` templates to every default area.
- Updated area creation, area reviews, daily check-ins, and automation prompts to treat reminders as first-class area context.
- Added reminder rules so date-aware and trigger-aware items stay quiet until they are due, within lead time, newly relevant, or high-stakes enough to prepare.
- Updated the personal finance example to include finance reminders.

### Added Optional Software Access Guides

- Added `software/` with optional guides for connecting Glide to other apps.
- Added initial guides for Things and Apple Notes.
- Clarified that app access depends on the user's harness and permissions.
- Clarified that note updates default to the Obsidian vault unless the user explicitly asks to write somewhere else.

## 2026-05-21

### Clarified Installation From Vault Root

- Updated installation instructions to make the Obsidian vault root the expected starting point.
- Clarified that the installer should inspect the user's existing vault organization before making changes.

## 2026-05-20

### Added User Profile Refresh

- Added `Agent HQ/User Profile.md` as concise high-level user context.
- Added `glide-update-user-profile` as a standalone skill.
- Added `Agent HQ/Checklists/Update User Profile.md`.
- Updated daily check-ins, root harness snippets, drift review, and related skills to load and refresh the profile only when durable signal appears.

### Added Concept Docs And Examples

- Added `docs/CONCEPT.md` to explain Glide as a personal coach and pilot over long-term context.
- Added examples for turning messy manual notes into writing entries.
- Added an example for researching personal finance organization and proposing a monthly finance check.
- Updated daily check-in instructions to support multiple relevant checks while keeping the user-facing output short.

### Refined README Positioning

- Reworked the README around Glide as a self-evolving personal coach and pilot.
- Clarified the purpose: better defaults, less life admin, more attention for what matters.
- Added the Storyloop inspiration and smart-notes connection.
- Clarified that Glide's internal memory and working structure stay in `Agent HQ/` unless the user asks otherwise.

### Initial Public Template

- Created the first distributable Glide for Obsidian package.
- Added the installable `templates/Agent HQ/` workspace.
- Added default areas: Finance, Health, Family, Home, Career, Business, Friends & Community, and Travel.
- Added core skills for area creation, area review, life systems review, WOOP goals, decision packets, contradiction detection, deep research, daily check-ins, harness drift review, and skill updates.
- Added Codex, Claude Code, and generic harness adapters.
- Added starter automation prompts for daily check-ins and harness drift review.
- Added privacy, harness, release privacy checklist, installation, and contribution docs.
