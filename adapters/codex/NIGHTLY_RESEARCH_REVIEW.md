# Nightly Research Review Automation Prompt

If versioned memory is enabled and its cutover is recorded, read `Agent HQ/Memory Protocol.md` and use the [portable-memory procedure](../../automations/portable-memory.md) with job ID `dream`. Run the installed `glide-dream` skill over changed evidence. Use the managed store, compact job inputs and the protocol's review/checkpoint rules; preserve pending work and stay quiet when unchanged. Do not run the legacy file-writing instructions below in this mode. Source access and external actions retain their existing authority.

Otherwise, use the existing workflow below.

Run `$glide-nightly-research-review` for this vault.

Use the Glide skill and checklist as the source of truth. Suggested schedule: daily at 4am local time.

Start with internal analysis and planning. Then use parallel subagents when available for memory gaps, open-loop research, active research, eval/process improvement, area connections, concise representation, and stale working-memory candidates.

Keep output internal by default. Update Agent HQ and `Agent HQ/Evals/Nightly Research Audit.md` with a rolling 4-day audit. Ask for approval before behavior-changing edits, destructive deletion, sensitive external actions, or changes requiring personal judgment.
