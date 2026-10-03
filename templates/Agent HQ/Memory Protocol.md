# Memory Protocol

The runtime contract governs explicitly authorized versioned-memory setup and use. Recorded cutover makes managed records authoritative for migrated state; it does not change original-note or unmigrated-file ownership. Do not enable or migrate implicitly. Read `Contracts/Memory Core.md` for the shared evidence, revision, writer, retrieval, checkpoint and improvement invariants. Its generated source belongs to the matching Glide runtime distribution.

Current managed records are authoritative for migrated state; legacy profile, goals, ledgers and area notes are historical or explicitly unmigrated evidence. Start with Now/Ongoing/Durable and relevant records, then retrieve exact evidence. Use bounded `glide_get` passages when useful; a truncated record is not a complete replacement payload. Escalate to full current revisions before editing.

## Review settings

Fresh installations default to `knowledge_review: manual` and `review_ui: text`. Upgrades preserve omitted values and absent keys. Read effective settings from `glide_verify.review_settings`; presentation and knowledge admission are independent.

Manual knowledge needs a reviewed proposal and separate application before checkpointing its outcome; do not submit that applied record twice. Explicit automatic mode admits only AI-authored, unreviewed knowledge supported by exact scoped Markdown evidence under `automatic_source_prefixes`. It cannot create commitments, delivery/completion, due dates or superseding decisions. Absent knowledge policy preserves previously authorized job scope (`legacy-authorized`), not permission for automatic ingestion or external action.

## Learned improvement

Automatic activation stays disabled until explicit instance opt-in. Only typed `retrieval_aliases` and `context_priority` overlays qualify; at most one candidate may activate per week under motivating evidence, precise versioning, regression/held-out checks and a retained rollback version. Failed/unknown checks do not authorize activation; a rejected valid candidate consumes the week's budget. No change may alter permissions, evidence admission, completion, goals, retention, providers, schedules, external-action authority or its own tests. Model judgments are advisory. For an eligible evaluation/activation/rollback, read `Reference/Memory Protocol Details.md` under Controlled Improvement; storage of a lesson never activates it.

## Obsidian and optional capabilities

Use collision-safe readable names, meaningful Obsidian links and no repeated filename H1 in generated pages. Preserve original titles. Now is the last committed snapshot, not a live clock; daily reconciliation checks current time and due reviews in underlying operations.

Load optional detail only when used:
- Conversation capture/recovery: `Checklists/Conversation Learning.md`, then `Conversation Recovery.md` for authorized history.
- Project-progress output: `glide-project-progress` after successful relevant intake. Approved category scope permits only new derived root-level notes, never existing-writing edits or another category.
- Recovery: `Checklists/Recovery.md` for setup, upgrades, transfer or relevant integrity checks.
- Collaborative documents: `Checklists/Input and Collaboration.md`.
- Installation/compatibility detail: `Reference/Memory Protocol Details.md`.

Configuration, executable/runtime paths, credentials, SQLite, locks and caches remain private and outside the synced vault. Installed tool availability and instance source permissions control usable capabilities; missing tools do not authorize an alternate unrestricted writer. Repository updates do not change saved jobs, sources, models or permissions.
