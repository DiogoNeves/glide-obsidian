# Validate the Obsidian edition

## Recorded local validation — 6 September 2026

Content build `df711b913f09` passed **139 runtime tests with no skips** on the tested macOS host, including the explicitly enabled Codex source-reader boundary check. Both fresh adapter installations passed the package/content-pin checks; the installed wheel rendered the review and imported its packaged helpers. The separate model-screen evaluator passed five synthetic tests without calling a model. These are local results, not a claim that hosted CI has run or every supported host is equivalent.

Recovery tests delete an independent disposable SQLite index and recover the same Markdown records, historical answers and review receipts. Paging regressions keep a large archive and long record bodies out of default job summaries while preserving exact revision references. The [eight-case model screen](https://github.com/DiogoNeves/glide/blob/main/examples/model-screen/README.md) is limited evidence for provisional model roles, not a ranking of coaching quality.


This distribution uses the shared runtime and [validation procedure](https://github.com/DiogoNeves/glide/blob/main/docs/VALIDATION.md). Use the matching local Glide checkout's `docs/VALIDATION.md` for an unpublished build. Run its suite and [setup walkthrough](SETUP.md) with `adapter=obsidian` and `store_path=Agent HQ/Memory`.

Verify that generated records have meaningful Obsidian links, valid filenames and no repeated opening title. Original writing must stay byte-identical. Delete only an independent copied store's SQLite index, rebuild, and compare current records, history, source evidence and review receipts. A copied-store check does not prove actual Obsidian Sync completeness or a second machine's configuration.

The [behavior cases](../examples/memory-evaluation-cases.json) are synthetic evaluation specifications, not model performance results. Structural validation and deterministic tests do not establish that coaching is useful. Evaluate dated beliefs, counterevidence, source independence and the distinction between ideas, commitments and completion; sample uncertain and ordinary/skipped cases with the owner weekly.

Interactive reviews must produce a real conversation/tool submission and runtime receipt. Text is the portable default and fallback. Desktop integration has exercised the round-trip, but mobile support and a particular host's configuration remain separate checks. Do not report a local UI selection as applied.

Record the actual current test totals and skips. An earlier 100-test run was 99 passed and one environment-dependent sandbox skip, not 100 passes. Release checks also cover the two distributions' shared content pin, package contents, skill links, clean setup and privacy; see the shared validation guide and [upgrade procedure](UPGRADING.md).

## Optional daily-note companion — 6 September 2026

Companion build `487aef401c97` passed **28 synthetic tests** locally. They cover category permission, preserved writing, late/duplicate activity, crash recovery, SQLite rebuild, edited-note provenance, host handover, bounded batches, MCP input constraints and installation/content pins. The unchanged shared build again passed all **139 tests with no skips**, including the local Codex boundary check. The new skill passed structural validation. A fresh process using the installed companion exposed the existing tools plus its three optional tools and correctly reported the category disabled before approval.

These are local checks, not a hosted CI result or evidence of a completed production daily-note run. [Daily-note setup and validation](DAILY-NOTES.md) documents the exact commands, limitations and first-output review.

## Conversation continuity — 6 September 2026

The metadata-only history inventory passed **14 synthetic tests** locally, covering resumed older tasks, missing/stale indexes, internal-origin filtering before pagination, header-only reads, symlinks, unreadable/partial inputs, changed files and paging drift. Run `python -B -m unittest discover -s tests -p test_conversation_inventory.py -v` from this checkout. The new skill passed structural validation. An independent agent reviewed six synthetic conversational scenarios and the procedure's corrections; this was a reading-based behavioral review, not an executed model benchmark or proof of future compliance.

The [six scenarios](../examples/conversation-learning-cases.json) distinguish explicit steering, temporary context, unaccepted suggestions, late corrections, duplicate retries and inferred overgeneralization. Evaluate later behavior as well as saved records. Live history access is partial by source and page; inventory counts are not reviewed-message counts. The unchanged shared runtime's results above were not rerun for these helper/instruction changes. See [setup, coverage and rollback](CONVERSATION-LEARNING.md).

A separate fresh read-only agent answered three questions from an installed private instance without an answer key, correctly preserving current operational state, unaccepted interests versus commitments, and scoped user guidance versus inactive candidates. Exact receipt replay also returned the existing revisions. These checks supplement the synthetic cases; private test data is not distributed, and later scheduled behavior remains a field check.

## Input and collaboration

The [synthetic input cases](../examples/input-surface-cases.json) exercise conversation delivery, optional shared vault notes, stale checkbox approval, backlog handling, mixed authorship, failed notifications, unavailable scoped writers and separate project-progress permissions. Use them for an independent behavioral review against the [canonical checklist](../templates/Agent%20HQ/Checklists/Input%20and%20Collaboration.md). They contain no answer key or execution claim.

Check that required input is answerable in conversation, internal links are optional, and a new collaborative note follows the vault's existing conventions without expanding write authority. Verify scoped edits preserve intervening human changes, a checked box follows revision validation and a real receipt, and unavailable file capability retains a conversation fallback. Record checks actually performed; document/skill validation alone does not establish later scheduled behavior.

A [recorded independent reasoning review](../examples/input-surface-review.md) evaluated the six generic cases and both Obsidian-specific cases, without an answer key. It identified a delivery-failure gap that was clarified and reviewed again. No document edits, notification delivery or runtime decisions were executed by this evaluation; later scheduled behavior remains a field check. Both changed skills and referenced routes passed structural checks. The pinned runtime and companion code are unchanged.

## Recovery configuration exports

The shared owner helper has eight synthetic tests for version preservation/idempotency, read-only inspection, pending backup status, changed/missing inputs, symlinks, traversal/duplicate names, credential/database tripwires and unexpected export files. Run `python3 -B -m unittest discover -s tests -p test_recovery_bundle.py -v` in the matching **glide** checkout. These checks do not prove backup service operation or restoration of a complete instance; follow [the recovery procedure](RECOVERY.md) in the actual harness.
