# Automation Registry

Proposed and active Glide automations.

Glide itself does not run automations. The selected harness decides whether automations are supported and how they are configured.

| Name | Status | Cadence | Scope | Skill | Output | Last Review |
| --- | --- | --- | --- | --- | --- | --- |
| [[Automations/Daily Glide Check-In|Daily Glide Check-In]] | Proposed | Daily or weekdays | User profile, follow-through ledger, area reminders, open questions, active goals, ponders, areas, contradictions, action candidates | `glide-daily-check-in` calling `glide-update-user-profile` | Profile update pass, follow-through scan, reminder scan, and one useful touch by default | |
| [[Automations/Harness Drift Review|Harness Drift Review]] | Proposed | Weekly or twice weekly | Operational instructions, checklists, skills, evals, and stale collection candidates | `glide-harness-drift-review` | Small operational corrections, stale-candidate cleanup, or short drift report | |
| [[Automations/Nightly Research Review|Nightly Research Review]] | Proposed | Daily at 4am | Recent exchanges, open loops, open research, eval signals, area connections, stale working-memory candidates, and concise process improvements | `glide-nightly-research-review` | Internal Agent HQ updates and rolling 4-day audit; approval requests only when needed | |
| [[Automations/Weekly Glide Update Check|Weekly Glide Update Check]] | Proposed | Weekly | Upstream releases, migration notes, local instructions, installed skills, checklists, and automation notes | `glide-check-for-updates` | Quiet no-op when current; update plan or approval request when a new release exists | |

## Candidate Automations

- Daily Glide Check-In.
- Harness Drift Review.
- Nightly Research Review.
- Weekly Glide Update Check.
- Weekly life systems review.
- Monthly area reviews.
- Ongoing research reviews for active opportunities.
- Skill and checklist improvement review.

## Automation Rule

Do not create or enable automations without user confirmation.

## Install Notes

Installable starter prompts ship in the Glide repo under `automations/` and `adapters/<harness>/`.

When an automation is enabled, update its status, cadence, destination, and last review date here.
