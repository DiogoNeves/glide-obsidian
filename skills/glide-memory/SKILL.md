---
name: glide-memory
description: Retrieve or propose updates to an explicitly enabled Glide versioned memory store, with source evidence and revision checks.
---

Read `Agent HQ/Memory Protocol.md` and the private instance's configured runtime entrypoint. If versioned memory is not enabled, preserve the current storage workflow; do not migrate implicitly.

Translate questions into short concept/key-term queries; use Now/Ongoing for an action overview, and do not treat a failed full-sentence keyword search as evidence of absence.

Retrieve the relevant current records, their evidence and history before advising or changing memory. Use `glide_search`, `glide_get` and `glide_history`, then `glide_read_source` for referenced Markdown passages. For earlier knowledge use search `recorded_at` or get `at`; `valid_at` asks when a claim applied. Search excludes receipts and reviews by default; request `kind="receipt"` or `kind="review"` explicitly, or retrieve a known ID. Use focused keywords; managed matches lead each keyword lookup. Legacy Memory is excluded by default: request `kind="source"` deliberately for archived, non-independent history. A search hit alone is not verification.

For new material, read effective review settings from `glide_verify` and follow the protocol's manual or explicitly scoped automatic knowledge path. Presentation is independent; no UI is required for automatic intake. Separate original writing, durable knowledge and operational evidence. Reuse coherent records and meaningful links. Preserve claim origin, review status and applicable/recorded times. Keep ideas, accepted commitments and completion evidence distinct.

Submit a scoped `glide_propose` against the current revision, then use `glide_apply`. Scheduled job outputs instead use the protocol's `glide_job_inputs`/`glide_finish_job` transaction. Apply only within the instance's already authorized scope, using a stable idempotency key. Return the affected record links and actual receipt. Never write generated records or bundles through an alternate route, and never use memory intake as permission to act in an external system.
