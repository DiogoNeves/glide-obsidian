---
name: glide-daily-check-in
description: Run a concise daily Glide pass that can coordinate multiple relevant checks or skills, then surface a useful question, insight, action, or follow-up.
---

# Glide Daily Check-In

## Load

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/User Profile.md`
- `Agent HQ/Checklists/Daily Glide Check-In.md`
- `Agent HQ/Goals/Active Goals.md`
- `Agent HQ/Open Loops.md`
- `Agent HQ/Follow-Through Ledger.md`
- `Agent HQ/Questions Queue.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Areas/*/Reminders.md`
- `Agent HQ/Checklists/App Interface And Computer Use.md` when checking external apps
- Relevant area questions, recent reviews, decisions, contradictions, and project links
- Available inbox, calendar, task, or app-action sources when access is configured and the run can check them safely
- `Agent HQ/Evals/Run Log.md`
- `Agent HQ/Evals/Eval Cases.md` only when a run reveals a reusable test case

## Process

1. Follow `Agent HQ/Checklists/Daily Glide Check-In.md`.
2. Run `$glide-update-user-profile` before choosing the daily output.
3. Scan area reminders and `Agent HQ/Follow-Through Ledger.md`, then identify candidate daily focus areas: follow-through items, open loops, active goals, area reminders, area questions, ponders, contradictions, project links, app action candidates, and stale decisions.
4. When more than one candidate focus area is plausible, use parallel subagents to explore them. Give each subagent one narrow focus area and ask for: signal, urgency, one possible daily output, whether there is a profile update candidate for `$glide-update-user-profile`, and whether background research should continue.
5. Integrate subagent findings yourself and choose the smallest useful user-facing output.
6. If a focus area needs deeper research but should not block the daily output, continue that research in the background or queue it in Agent HQ only when it would materially improve future advice.
7. Run multiple relevant checks or skills when useful, but keep the user-facing response short, natural, and coach-like.
8. Do not expose Agent HQ structure unless it helps the user answer or act.
9. Do not suggest financial, legal, medical, interpersonal, public, or work-sensitive actions as executable. Draft or ask for approval instead.
10. Do not send, archive, delete, schedule, reply, purchase, post, or modify external systems unless the user explicitly configured that exact action and approval boundary. Otherwise suggest or draft only.
11. After a useful run, append a light evaluation entry to `Agent HQ/Evals/Run Log.md`.
12. Promote a run to `Agent HQ/Evals/Eval Cases.md` only when it reveals a reusable regression test or unusually good behavior.

## Output

- One concise daily output, based on the relevant checks or skills.
- A `$glide-update-user-profile` pass before choosing the daily output.
- An area reminder scan before choosing the daily output.
- A follow-through scan before choosing the daily output.
- A tiny run-log entry when the run produced a useful touch or durable update.
- Optional Agent HQ updates after the user responds.
