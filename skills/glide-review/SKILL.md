---
name: glide-review
description: Prepare and apply a source-backed Glide memory review through verified proposal IDs and revision receipts.
---

Read `Agent HQ/Memory Protocol.md`, the proposal, its expected revision and the exact evidence passages. Show what would change, why, counterevidence or uncertainty, and the affected record links.

Use the configured `review_ui` preference: text by default, or an interactive review when available and useful. Show the same evidence and choices in the conversation if rendering or submission is unavailable. A control may submit a proposal ID and revision only through an available conversation/tool bridge; otherwise ask for the decision conversationally. Local selection is a preview, not a saved decision.

After the user's decision, use `glide_apply` with the proposal ID, decision, expected revisions and stable idempotency key within the existing action scope. A stale proposal needs refreshed evidence and review. Report application only after the returned receipt confirms the actual new revision. Rejecting a proposal must not apply it. Preserve AI origin even when the user approves its interpretation.

For a weekly spot check, select two uncertain cases and one ordinary case, alternating accepted and skipped ordinary material over time. Judge source support and missed information rather than matching expected wording or producing a numerical trust claim.
