# Automation Registry

Proposed and active Glide automations.

Glide itself does not run automations. The selected harness decides whether automations are supported and how they are configured.

| Name | Status | Cadence | Scope | Skill | Output | Last Review |
| --- | --- | --- | --- | --- | --- | --- |
| [[Automations/Daily Glide Check-In|Daily Glide Check-In]] | Proposed | Daily or weekdays | User profile, open questions, active goals, ponders, areas, contradictions, action candidates | `glide-daily-check-in` calling `glide-update-user-profile` | Profile update pass, one useful touch, and light evaluation when useful | |
| [[Automations/Harness Drift Review|Harness Drift Review]] | Proposed | Weekly or twice weekly | Operational instructions, checklists, skills, and stale collection candidates | `glide-harness-drift-review` | Small operational corrections, stale-candidate cleanup, or short drift report | |

## Candidate Automations

- Daily Glide Check-In.
- Harness Drift Review.
- Weekly life systems review.
- Monthly area reviews.
- Ongoing research reviews for active opportunities.
- Skill and checklist improvement review.

## Automation Rule

Do not create or enable automations without user confirmation.

## Install Notes

Installable starter prompts ship in the Glide repo under `automations/` and `adapters/<harness>/`.

When an automation is enabled, update its status, cadence, destination, and last review date here.
