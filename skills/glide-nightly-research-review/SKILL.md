---
name: glide-nightly-research-review
description: Run a quiet scheduled Glide research and memory maintenance pass, especially for 4am background review of open loops, open research, recent interactions, eval signals, area connections, stale working-memory candidates, and concise instruction improvements.
---

# Glide Nightly Research Review

## Load

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Checklists/Nightly Research Review.md`
- `Agent HQ/User Profile.md`
- `Agent HQ/Open Loops.md`
- `Agent HQ/Questions Queue.md`
- `Agent HQ/Research/Research Index.md`
- `Agent HQ/Follow-Through Ledger.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Contradiction Register.md`
- `Agent HQ/Decision Log.md`
- `Agent HQ/Evals/*.md`
- `Agent HQ/Evals/Nightly Research Audit.md`
- Relevant area files under `Agent HQ/Areas/`
- Recent user-agent exchanges when the harness can access them safely
- Configured read/fetch connectors when useful

## Process

1. Start with a short internal analysis and plan: what to inspect, what matters most, and which tracks can run in parallel.
2. Use parallel subagents when available. Give each subagent a narrow track: memory gaps, open-loop research, active research, area connections, eval/process improvement, stale working-memory candidates, or concise-instruction cleanup.
3. Integrate findings yourself. Do not paste subagent outputs wholesale.
4. Use `$glide-deep-research-subject` for source-heavy loops and `$glide-harness-drift-review` for process drift when useful.
5. Prefer broad reusable patterns over adding highly specific rules.
6. Update Agent HQ quietly when there is durable value.
7. Retire stale working-memory candidates only when unused for over a month and plainly low-value, duplicated, or superseded. Preserve useful context in long-term memory before removing it from active working files.
8. Keep a rolling 4-day audit of this schedule's changes in `Agent HQ/Evals/Nightly Research Audit.md`.
9. Ask for approval before behavior-changing instruction edits, destructive deletion, sensitive external actions, or changes requiring personal judgment.

## Output

- No user-facing report by default.
- Internal audit of changed files and why.
- Updated research, open loops, questions, area links, eval notes, or concise operating instructions when useful.
- Approval-needed items only when required.
