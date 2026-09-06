# Versioned Memory

Glide's optional memory runtime keeps durable memory in readable Markdown and builds a local SQLite search index. The current 0.1.0 build `df711b913f09` is supplied locally, with exact file hashes in the owner repository's `runtime/package-manifest.json` and a matching `compatibility.json` pin; do not describe it as an upstream published release without verifying that release. Original writing remains outside the agent's managed store. Existing installations do not change until explicitly upgraded.

This distribution consumes the shared `glide_memory` runtime version **0.1.0** from the general Glide repository. Obtain a matching local checkout or release archive supplied by the user; this guide does not assume an unpublished download URL. Do not fork a second runtime into this repository.

## Storage

| Location | Contents | Synchronize with the workspace? |
| --- | --- | --- |
| Existing source files | Original notes, clippings and permitted records | Keep the existing source policy |
| `Agent HQ/Memory/Bundles/` | Immutable, self-contained successful change batches | Yes; these own accepted memory and history |
| `Agent HQ/Memory/Proposals/` | Submitted changes awaiting a decision | Yes, subject to the same privacy policy |
| `Agent HQ/Memory/Records/` | Current readable records, with IDs and links | Yes; recoverable from bundles |
| `Agent HQ/Memory/Views/` | Now, Ongoing, Durable and Changes views | Yes; generated views |
| `Agent HQ/Memory/Store.md` | Store identity and format manifest | Yes |
| `Agent HQ/Memory/Writer.md` | Designated writer information | Yes; handover still requires stopping the old writer |
| Local runtime directory | Pinned Python program | No; install separately on each execution host |
| Local state directory | SQLite index, local config, locks and caches | No; physically outside the vault/workspace and sync roots |

Python requires **3.11 or later**, with SQLite FTS5 available. Storage currently uses POSIX `fcntl`; macOS is the validated execution platform. Linux core behavior needs host verification, and the protected runner plus Apple integrations are macOS-only. Native Windows is unsupported. Core storage uses the standard library. Optional native capture routes also require their configured local helpers and dependencies. Keep its source, environments and caches outside the vault; do not rely on hidden directories or file-type exclusions as the installation strategy. Hidden skill/config folders are not a portable Obsidian Sync installation mechanism.

Every meaningful semantic record is recoverable from Markdown. SQL rows may index multiple claims and links within one page; they do not each require a note. Search caches and cursors may be local only when loss causes harmless, idempotent reprocessing. Decisions, provenance, accepted history and external-action receipts cannot exist exclusively in a disposable index.

Original clippings remain available as examples and evidence. Processing metadata belongs in managed records, not in source frontmatter. History snapshots are not independent evidence; exclude bundle history from normal semantic retrieval and knowledge graph views.

## Runtime Interface

The installed module is `glide_memory`. Run it with the matching local release directory on `PYTHONPATH`; keep the configuration path in private instance instructions. Install using the consuming distribution's required `--expected-build df711b913f09` flag; a version label alone does not identify this package. The implemented command help is authoritative for argument details. The runtime provides initialization, proposals and application, search, record retrieval, history, changes, index rebuild, backup, verification and deliberate writer handover.

For a local CLI invocation (substitute verified local paths):

```sh
PYTHONPATH="/path/to/glide/runtime" python3 -m glide_memory --config "/path/to/local-state/config.json" verify
```

For the optional fixed-configuration MCP broker, register the following process in the chosen harness, with that environment and argument list:

```sh
PYTHONPATH="/path/to/glide/runtime" python3 -m glide_memory.bridge --config "/path/to/local-state/config.json"
```

The broker exposes these fixed operations:

| Purpose | MCP tools |
| --- | --- |
| Retrieval | `glide_search`, `glide_get`, `glide_history`, `glide_changes_since`, `glide_read_source` |
| Tested retrieval changes | `glide_overlay_evaluate`, `glide_overlay_activate`, `glide_overlay_rollback` |
| Versioned changes | `glide_propose`, `glide_apply`, `glide_verify`, `glide_index_sources` |
| Bounded scheduled work | `glide_job_inputs`, `glide_job_input_page`, `glide_finish_job`, `glide_intake` |
| Optional configured native sources | `glide_apple_notes_metadata`, `glide_apple_notes_export`, `glide_capture_export`, `glide_voice_memos_sync` |

Search accepts `query`, optional `limit`, `include_sources`, `kind`, `valid_at` and `recorded_at`. `recorded_at` reconstructs what had been recorded by that time; `valid_at` filters applicable claim time. `glide_get(record_id, at)` uses recorded time. Default search excludes receipt/review records and the active learned-overlay record. Request `kind="receipt"` or `kind="review"` explicitly when those records are the question, or use `glide_get` for a known ID. History/change pagination cursors do not advance job checkpoints.

Use focused keyword queries. Each keyword lookup ranks managed record matches before source matches. Default search excludes `Agent HQ/Legacy Memory/` and `Glide HQ/Legacy Memory/`; retrieve that archived material deliberately with `kind="source"` and source inclusion enabled. Returned archive evidence is labeled `archived-ai-history` and `non-independent-history`: it records earlier AI context and is not fresh corroboration or current operating state.

Now is a bounded view of the last committed snapshot. An open/waiting operation becomes eligible when its `review_at` is at or before that snapshot's recorded time, alongside the existing commitment/deadline rules. Rebuilding on a later date does not change an old snapshot silently. Daily reconciliation still checks current time and due reviews in the underlying operations; the generated page is not a live clock.

Proposal inputs are structured tool arguments, so a read-only model session need not create a temporary JSON file. Each `glide_apply` includes `proposal_id`, `decision`, `expected_revisions` and a nonempty `idempotency_key`. Rejected decisions are recorded without applying proposed records. For scheduled work, `glide_job_inputs(job_id, batch_limit)` returns the bounded input boundary and checkpoint revision; `glide_finish_job(job_id, processed_through, records, expected_revisions, summary, evidence, idempotency_key)` commits successful output and checkpoint together. Job IDs are `daily`, `evening`, `dream`, `integrity`; expected revisions include the returned checkpoint ID plus every output ID. No changed inputs and no outputs produce no appended bundle. Failures leave the checkpoint unchanged.

`glide_intake()` uses fixed private Markdown/project configuration. Optional Apple Notes intake starts with `glide_apple_notes_metadata(days)`, exports selected returned IDs using `glide_apple_notes_export(metadata_token, note_ids)`, then captures a selected verified export with `glide_capture_export(export_token)`. A failed metadata scan cannot authorize bodies. `glide_voice_memos_sync()` runs the configured bounded local copy/transcription route and captures eligible new results itself. These tools return actual coverage/capture receipts; do not repeat capture or infer success from invocation. Native helpers, paths and content hashes are private installation configuration, never model-supplied commands.

`glide_overlay_evaluate(change)` tests a typed candidate against the fixed private regression/held-out set without activating it. `glide_overlay_activate(change, evidence, rationale, idempotency_key)` reruns the gates and records the actual activation or rejection. `glide_overlay_rollback(evidence, rationale, idempotency_key)` restores the retained preceding change. The only accepted change keys are `retrieval_aliases` (normalized exact-query alternatives) and `context_priority` (existing eligible record IDs). Evaluation/activation require the configured opt-in and content-pinned case set; a caller-supplied pass result is never authority. Ordinary proposals cannot bypass this pathway to edit the reserved overlay record. Rollback does not depend on the evaluator file still being available.

The broker's configured vault and state paths are fixed at launch. It exposes no initialization, reconfiguration, writer activation, arbitrary backup path, shell command or general file-write endpoint. Source reads/indexing accept only non-hidden Markdown paths inside that vault, excluding the configured generated store. Source indexing reads current bytes locally and verifies them before committing references.

This bounded API is not an OS sandbox or proof of user approval. Run source-reading/model processes with read-only source permissions and only the trusted broker allowed to write the managed store. Do not provide an alternate unrestricted shell/file-writing route that bypasses this boundary. Configure and test the actual harness restrictions separately.

Read the installed [Agent HQ memory protocol](../templates/Agent%20HQ/Memory%20Protocol.md) for the behavioral contract. Installation alone does not schedule consolidation or turn on automatic skill changes.

## Synchronization And Other Machines

Obsidian Sync is file transport, not a database transaction or a distributed lock. There is one writer per instance. Another device can read synchronized Markdown without Python or SQLite. If it needs indexed retrieval, install the same runtime locally and rebuild its index; keep it read-only until an explicit handover.

A commit can arrive before its predecessor or before its current pages. Wait for complete matching files rather than treating this as a completed new state. Investigate a conflicting chain instead of merging it automatically. A live SQLite file, including its journal/WAL, is never a synchronized artifact.

For separate personal and work instances, keep independent state, credentials and writer roles. An optional bridge may import explicitly permitted summaries using stable source IDs, revisions and freshness. Do not grant raw cross-account access or embed bridge paths, credentials, repository names or private examples in the public package.

## Optional Source Adapters

A project-activity adapter can read a configured repository's commit IDs, timestamps and permitted descriptions. It produces attributed source records, deduplicated by repository identity plus commit ID. Repository paths, access scope, project names and lookback windows are instance configuration. Commit activity is evidence of repository work, not proof that a feature shipped, a customer benefited or a commitment was completed.

The runtime supplies storage, retrieval and configured intake. Model reasoning, schedules, native app permissions and the visual action bridge must be configured in the harness under the installed skills and existing authorization.

See [upgrade and rollback](UPGRADING.md), [compatibility](COMPATIBILITY.md) and [synthetic evaluation cases](../examples/memory-evaluation-cases.json).

## Setup and review preferences

Follow [the complete setup](SETUP.md) for per-device skills, fixed Codex MCP configuration, bounded intake, optional native helpers and a synthetic source-to-receipt check. See [validation](VALIDATION.md) and [SQLite/Git transport choices](STORAGE-AND-GIT.md).

Fresh instances use `knowledge_review: manual` and `review_ui: text`. On upgrade, omitted options preserve existing values **and absent keys**; choosing interactive presentation alone does not impose a knowledge policy. `glide_verify.review_settings.job_knowledge_policy` distinguishes `manual`, `automatic` and `legacy-authorized`. Explicit manual mode rejects knowledge records in job transactions: propose them for a conversational decision, apply the reviewed proposal separately, then checkpoint the actual completed work without submitting those records twice. Explicit automatic mode admits job knowledge only under the same AI/unreviewed, exact-evidence and `automatic_source_prefixes` restrictions as `glide_apply(..., knowledge_ingestion=true)`; separately authorized operational outputs remain independent. An absent knowledge policy preserves existing authorized job scope and does not opt into the automatic-ingestion pathway. These settings govern workflow and runtime admission, not authenticated proof of a human decision or permission for external actions.

`python -m glide_memory.review --config ... --proposal ...` renders the configured presentation; `--ui text|interactive` can override presentation for that review. Interactive question/adjust controls submit a conversation prompt; they do not apply a change. A review decision still needs the proposal ID, current expected revisions and actual writer receipt. Text fallback works without a UI bridge; mobile parity is not assumed.

Job inputs return compact change descriptors and source counts. Use `glide_job_input_page(job_id, bundle, cursor, limit)` to page exact bundle details when needed (limit defaults to 20, maximum 50); do not load a whole imported archive into routine context. Newly indexed history is available source material, not a requirement to promote every old assertion into knowledge. Follow the review policy above when preparing job outputs. A checkpoint records actual processing, including explicitly pending proposals; it is not evidence that a proposal was applied.
