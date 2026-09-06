# Optional versioned-memory automations

Use this portfolio only after this instance's versioned-memory cutover is recorded. Keep legacy prompts for instances that have not enabled it. These are installable procedures, not an installed scheduler. Inspect existing jobs first, reuse their useful scope, and pause superseded writers before enabling replacements.

Read `Agent HQ/Memory Protocol.md` for the canonical write, review-policy and checkpoint contract. Install its four memory skills on the execution host. Model choice, schedules, connectors and external-action permissions remain explicit instance decisions.

| Job | Runtime checkpoint ID | Procedure and dependency |
| --- | --- | --- |
| Source intake | Successful intake receipts | Run configured Markdown/project intake; optional native imports produce their own capture receipts. Report incomplete coverage. |
| Daily reconciliation | `daily` | After successful relevant intake, reconcile current operations and offer one useful evidence-led coaching touch. |
| Evening follow-through | `evening` | Review meaningful changes to accepted commitments, due reviews and completion evidence. Avoid manufacturing catch-up debt. |
| Dream | `dream` | Use `glide-dream` to consolidate changed evidence, connect useful concepts and propose supported procedural lessons. |
| Weekly integrity | `integrity` | Use `glide-integrity` for recovery/provenance checks and two uncertain plus one ordinary human spot-check candidates. |

Use fresh scheduled runs backed by durable checkpoints. Start with compact `glide_job_inputs` descriptors, page relevant bundle details through `glide_job_input_page`, and finish only successfully processed work. A scheduled start is not proof that intake finished. Preserve failed batches and pending decisions. With no changed inputs or meaningful findings, stay quiet; do not append repetitive run summaries. A routine can report a review proposal as pending, but cannot claim its proposed changes were applied.

Explicit manual knowledge mode requires separate conversational review/application before those knowledge changes are considered applied. Explicit automatic mode enforces the configured source prefixes and keeps derived knowledge AI-authored and unreviewed; it does not need an interactive UI. An existing instance with no knowledge-policy key retains its previously authorized job scope. Follow the full protocol rather than copying its transaction rules into each scheduled prompt.

Choose cadence, local timezone, model/effort and output destination with the owner. Verify the actual next run, awake host, tool access and one successful durable checkpoint. Intake → daily → evening → dream is a dependency design, not a requirement to use particular hours. Weekly integrity and deterministic monthly finance can remain separate. Native Apple sources are optional and macOS-specific; project activity resolves available repositories through a private local project index. Finance data access, account actions and external messages require their existing explicit authority.

For model selection, use the [repeatable synthetic screen](https://github.com/DiogoNeves/glide/blob/main/examples/model-screen/README.md) as a small exclusion check, then evaluate representative work. Terra high for routine intake, Astra high for coaching/dreaming and Sol high for integrity are provisional role choices, not established quality rankings. Do not change a provider or billing arrangement implicitly.

## Mapping existing starters

The daily starter maps to `daily`, the nightly research starter to `dream`, and the drift-review starter to `integrity`. Where a follow-through starter exists, it maps to `evening`. Retain separate business reviews, release/update checks and other narrowly authorized jobs; do not run a legacy file-writing prompt alongside its replacement against the same state.

At cutover, install the appropriate enabled-memory branch in each actual scheduler entry and record the chosen job ID and configuration path privately. Updating this repository does not update a saved automation. If the host cannot schedule, use the same procedures manually.

## Optional Obsidian progress notes

When the owner has enabled the project-progress category and installed the Obsidian companion, append `glide-project-progress` after successful relevant project intake. Reuse the intake job; do not create a second overlapping writer or change its model/schedule. Follow the skill for bounded continuation and review-needed cases. [Daily-note setup](../docs/DAILY-NOTES.md) is the canonical permission and recovery procedure. Disabled categories produce no output and need no daily permission prompt.

## Optional conversation recovery

When personal history recovery is authorized, install `glide-conversation-learning`. Daily performs its bounded capture/recovery pass; dream resumes pending coverage and consolidates useful candidates. Harness review checks captured feedback against later behavior and the protected principles. Coverage and permitted outputs commit through the existing job transaction; knowledge requiring separate review stays pending until its own application receipt. Follow the [canonical procedure](../templates/Agent%20HQ/Checklists/Conversation%20Learning.md); a bundle checkpoint alone does not prove conversation coverage.

## Owner input

Follow `Agent HQ/Checklists/Input and Collaboration.md`. Deliver required questions and human spot checks in the configured conversation with their context and proposed choice; an internal Now entry, queue item or review record does not establish delivery. If delivery fails, retain pending input and report the gap through an available authorized conversation. Quiet internal maintenance needs no shared note. Update actual saved prompts within their approved scope; keep schedules, models and permissions unchanged.
