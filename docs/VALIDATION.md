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
