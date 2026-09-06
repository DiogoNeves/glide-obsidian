Read this protocol when versioned memory has been explicitly enabled for this instance. Existing files keep their current authority until the recorded cutover. Installing this note alone does not migrate data, create schedules, or enable learned behavior.

## Three Responsibilities

| Responsibility | Durable material | Agent behavior |
| --- | --- | --- |
| Original writing and sources | Existing notes, clippings and permitted source files | Read and cite; preserve wording, filenames, formatting and ownership |
| Knowledge | Coherent concepts, claims, evidence and relationships | Extract selectively, qualify, connect and challenge |
| Operations | Accepted commitments, open loops, decisions, outcomes and procedures | Reconcile evidence and support follow-through |

A coherent page may contain several claims. Do not create a page for every fact, impose link quotas, or turn a passing idea into a commitment. A historical statement of what someone believed remains distinct from whether that belief was correct.

## Files Own Memory

The configured memory store contains immutable `Bundles/*.md` change records, submitted `Proposals/*.md`, current `Records/` pages, `Views/` and `Writer.md`. Successful bundles contain complete revised records and the authoritative metadata needed to rebuild them. Current pages and views can be recreated from the bundles. Do not edit a bundle or silently adopt an external edit to a current page.

SQLite, Python, local configuration, credentials, locks and caches stay outside the workspace or vault and outside its synchronization. SQLite indexes the files; it is not a second source of truth. Deleting a test index must not lose accepted content, history, provenance or review decisions. A meaningful claim must be recoverable from Markdown, not only from a SQL row.

Use the installed runtime through its configured local entrypoint. Never infer that a package or skill copied to another machine is installed there. The public installation and upgrade guides accompany the distribution; record the actual runtime/config paths privately during setup.

## Evidence And Time

Each record has a stable ID, revision, origin, review state and source references. Keep claim-level distinctions when one page mixes external assertions, historical records, stated views and agent inferences. Approval changes review status; it does not change an inference into authored text or an established fact.

Evidence needs the source identity, relevant passage or locator, source revision/hash when available, and applicable time. Retain a sufficient permitted excerpt or revision to explain an older conclusion after its source changes. Distinguish when an observation applied from when it was recorded. Multiple summaries of one source are not independent corroboration.

Use focused keyword queries. Each keyword lookup ranks managed record matches before source matches. Default search excludes `Agent HQ/Legacy Memory/` and `Glide HQ/Legacy Memory/`; retrieve that archived material deliberately with `kind="source"` and source inclusion enabled. Returned archive evidence is labeled `archived-ai-history` and `non-independent-history`: it records earlier AI context and is not fresh corroboration or current operating state.

Explain why a connection matters. Reuse the existing concept when appropriate; do not equate similarity with contradiction or supersession. New counterevidence can mark a conclusion contested without silently replacing an accepted conclusion.

## Write And Recovery Contract

Use `propose` and `apply`; do not directly edit generated records. Each proposal identifies its expected parent revision. Apply requires a stable idempotency key, and a stale proposal must be refreshed before applying. Report success only from the runtime's returned receipt and resulting revision.

There is one designated writer per instance. A local lock is not a cross-machine lock. Stop the old writer before transferring the role; do not automatically fail over when another machine appears offline. Read-only devices may receive synchronized files in any order. Treat a missing predecessor or incomplete bundle as pending synchronization, and a hash/chain violation as an integrity failure requiring investigation.

Publishing a bundle and its current pages is not an atomic multi-file sync operation. The runtime recovers committed bundles and rebuilds current pages/indexes. Actionable reviews must validate their expected revision. Source cursors advance only after the corresponding successful durable write; repeated intake must be harmless.

Keep processing instructions and metadata outside original writing. Source protection requires effective filesystem/tool restrictions; instructions alone are not an enforced boundary. Verify the actual execution permissions before describing sources as technically read-only.

## Successful Job Checkpoints

Scheduled workflows use the fixed IDs `daily`, `evening`, `dream` and `integrity`. Call `glide_job_inputs(job_id, batch_limit)` before processing; its bounded input list, `processed_through`, `checkpoint_id` and `checkpoint_revision` define this run. Reading history or a source receipt does not advance a checkpoint.

Only after that batch succeeds, call `glide_finish_job` with `job_id`, the returned `processed_through`, complete revised `records`, `expected_revisions`, an evidence-backed `summary`, `evidence` and a stable `idempotency_key`. The expected revisions must name each output record and the returned checkpoint ID/revision. Permitted job outputs and the checkpoint commit in one bundle; never submit an already applied record a second time. Knowledge requiring separate review follows the policy below; checkpoint the actual outcome, retaining unresolved proposals as pending. Preserve any pending batch and leave the checkpoint unchanged on failure. The checkpoint proves processing through a specific bundle, not that every source scan or external action succeeded.

With no changed inputs and no substantive outputs, stop quietly; `glide_finish_job` also returns `no-change` without appending a bundle. Processing new inputs that produce no semantic change may still commit their successful checkpoint. Daily selects current evidence and one useful touch; evening reconciles meaningful changes to accepted commitments; dream consolidates; integrity verifies and prepares human spot checks. Do not manufacture a finding to make a job appear productive.

## Coaching And Consolidation

Coach toward better decisions and observed outcomes. Retain a decision's desired outcome, assumptions, supporting evidence, counterevidence, uncertainty, review trigger, useful test and observed result. Distinguish a preference from the testable assumptions used to pursue it. Be motivating and candid; recommending a smaller test, a pause or stopping can be useful.

A dream pass processes changed evidence in a bounded, resumable batch, reuses knowledge, refreshes compact context, flags tensions and extracts supported procedural lessons. It does not delete sources, invent commitments, close loops without completion evidence, or overwrite goals. Keep the Now view short; completed events leave the foreground while remaining retrievable. Retain the ledger's evidence separately from the open loop's current next action.

Now is a bounded view of the last committed snapshot. An open/waiting operation becomes eligible when its `review_at` is at or before that snapshot's recorded time, alongside the existing commitment/deadline rules. Rebuilding on a later date does not change an old snapshot silently. Daily reconciliation still checks current time and due reviews in the underlying operations; the generated page is not a live clock.

## Controlled Improvement

Automatic activation is disabled until the user explicitly opts into this policy for the instance. Once enabled, at most one small learned overlay may activate per week after motivating evidence, a precise versioned change, relevant regression cases and held-out checks all support it. Preserve the previous version and revert demonstrated regressions. Unknown or failed checks do not justify activation. A rejected valid candidate is recorded and consumes that week's candidate budget; do not keep trying alternatives against the same held-out set. Reverting an active change remains possible even if the evaluation files become unavailable.

Runtime 0.1.0 can automatically activate only the typed `retrieval_aliases` and `context_priority` changes: retrieval vocabulary and ordering of existing eligible records in context views. Routing, presentation and procedural lessons may be proposed as workflow records for human review; this runtime does not automatically activate them. Use `glide_overlay_evaluate` to inspect a candidate, `glide_overlay_activate` for its independently checked activation, and `glide_overlay_rollback` for evidence-backed reversal. These are separate tested mutations; do not route an overlay through an ordinary proposal or count evaluation as activation. No overlay may change permissions, evidence-admission or completion rules, goals, retention, providers, schedules, external-action authority, its own acceptance tests or protected principles. Keep core instructions intact. Evaluation may use local deterministic checks and human review; model judgments are advisory, never sole approval evidence. No new external evaluation service is implied.

Each week, prepare two uncertain cases and one ordinary case for human spot checks; alternate ordinary accepted and skipped material over time. Assess citation support, missed evidence, appropriate challenge and review burden. Three samples are not a trust score.

## Display And Interaction

Use readable, valid, collision-safe filenames. The Obsidian adapter does not repeat the filename as an H1 inside generated notes. Do not normalize original titles.

Show a review's claim, supporting passage, counterevidence, proposed change and affected records. Distinguish preview selection from submission and confirmed application. Controls must submit a proposal ID and revision to an available conversation/tool bridge. If that bridge is unavailable, use a clear conversational decision; do not simulate a successful mutation.

## Knowledge review preference

Fresh instances use `knowledge_review: manual` and `review_ui: text`. On upgrade, omitted options preserve existing values **and absent keys**; choosing interactive presentation alone does not impose a knowledge policy. `glide_verify.review_settings.job_knowledge_policy` distinguishes `manual`, `automatic` and `legacy-authorized`. Explicit manual mode rejects knowledge records in job transactions: propose them for a conversational decision, apply the reviewed proposal separately, then checkpoint the actual completed work without submitting those records twice. Explicit automatic mode admits job knowledge only under the same AI/unreviewed, exact-evidence and `automatic_source_prefixes` restrictions as `glide_apply(..., knowledge_ingestion=true)`; separately authorized operational outputs remain independent. An absent knowledge policy preserves existing authorized job scope and does not opt into the automatic-ingestion pathway. These settings govern workflow and runtime admission, not authenticated proof of a human decision or permission for external actions.

Automatic knowledge retains AI authorship, unreviewed status and exact scoped Markdown evidence. That pathway cannot create commitments, delivery/completion state, due dates or superseding decisions. Operations retain their separately authorized procedure.

Prefer compact job change descriptors and page relevant historical inputs with `glide_job_input_page(job_id, bundle, cursor, limit)`. Registering an archive does not require reviewing or promoting every historical claim. Render text by default; interactive reviews use the same evidence and decisions with a verified follow-up bridge and text fallback. Question/adjust controls start conversation and do not apply changes.
