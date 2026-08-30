# Eval Loop

Purpose: help Glide improve from real use without telemetry, external storage, automated scoring, model judges, or private transcript storage by default.

## Core Loop

1. Use the system normally.
2. After useful runs, append one tiny row to `Agent HQ/Evals/Run Log.md`.
3. Tag the row with short facets.
4. Choose an eval decision: `keep`, `tune`, or `case`.
5. During drift or background review, cluster repeated facets in `Agent HQ/Evals/Signal Clusters.md`.
6. Promote only important failures, near-misses, repeated patterns, or unusually good behavior to `Agent HQ/Evals/Eval Cases.md`.
7. Use clusters and cases as evidence before changing skills, checklists, or operating instructions.

## Run Log Format

Use:

`Date | Run | Touch Type | Sources Used | Useful? | Facets | Eval Decision | Improve Next`

Keep rows short. Do not copy full private transcripts, raw connector dumps, or detailed traces unless the user explicitly asks.

## Facets

Use 1-4 short tags. Prefer stable tags over prose.

Common facets:

- `missed-deadline`
- `stale-memory`
- `too-broad-question`
- `good-timing`
- `approval-boundary`
- `connector-failure`
- `quiet-source-risk`
- `goal-forward`
- `maintenance-crowding`
- `memory-update`
- `source-provenance`
- `follow-through`

Add new facets only when they are likely to recur.

## Eval Decisions

- `keep`: the behavior should happen again.
- `tune`: mostly useful, but the run exposed an improvement.
- `case`: promote or update a reusable eval case.

Use `case` sparingly. Most rows should be `keep` or `tune`.

## Signal Clusters

Cluster only repeated or high-stakes signals. A good cluster says what pattern is recurring, which facets and rows support it, what should change, and whether the fix is covered by an eval case.

Do not treat clusters as automatic permission to change behavior. Behavior-changing fixes still need user approval.

## Boundaries

- Do not store transcripts, private connector dumps, or sensitive source data in eval files.
- Do not add telemetry, external storage, automated scoring, or model-judge infrastructure.
- Do not enable new automations from eval evidence alone.
- Treat clusters and cases as evidence for small, approval-aware improvements.
