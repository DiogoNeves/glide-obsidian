---
name: glide-integrity
description: Verify Glide memory recovery, provenance and writer consistency, and prepare bounded evaluation and improvement reviews.
---

Read `Agent HQ/Memory Protocol.md`, the current writer/configuration and relevant evaluation cases. Start with compact `glide_job_inputs(job_id="integrity")` descriptors, page relevant history through `glide_job_input_page`, and use `glide_verify` to distinguish missing sync predecessors, divergent current pages, and corrupt revision history. Do not repair authored sources or rewrite authoritative bundles.

For an upgrade or storage change, rebuild an independent test index from copied Markdown and verify history, provenance and current state. Exercise interruption/retry and stale-proposal behavior when the changed component warrants it. A successful schema check does not establish semantic accuracy.

Prepare two uncertain cases and one ordinary accepted/skipped case for the weekly human sample and evaluate eligible learned overlays against regression and held-out cases. Use observed behavior, not expected prose. The protocol's explicit opt-in, one-activation-per-week limit and protected rules apply; failed or missing checks block activation. Use `glide_overlay_evaluate`, the separately gated `glide_overlay_activate`, and `glide_overlay_rollback` as appropriate; evaluation alone does not apply a change. Keep any repair or rollback scoped to the diagnosed defect and return verifiable evidence.

Finish a successful bounded review through `glide_finish_job` under the protocol. Preserve unresolved failures as findings without claiming verification passed; a failed batch does not advance its checkpoint. Do not append an unchanged routine success.
