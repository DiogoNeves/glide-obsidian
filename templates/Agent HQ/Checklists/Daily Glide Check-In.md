# Daily Glide Check-In

Purpose: run a concise morning pass that improves Agent HQ accuracy, checks relevant context, surfaces timely insight, or moves a small approved action forward.

## Load

- `Agent HQ/AGENTS.md`
- `Agent HQ/Operating Manual.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/User Profile.md`
- `Agent HQ/Goals/Active Goals.md`
- `Agent HQ/Open Loops.md`
- `Agent HQ/Follow-Through Ledger.md`
- `Agent HQ/Questions Queue.md`
- `Agent HQ/Ponder Log.md`
- `Agent HQ/Areas/*/Reminders.md`
- `Agent HQ/Checklists/App Interface And Computer Use.md` when checking external apps
- Relevant area `Questions.md`, recent reviews, decisions, and contradictions
- Available inbox, calendar, task, or app-action sources when access is configured and the run can check them safely

## Profile Update

Before choosing the daily output, run `$glide-update-user-profile` or follow `Agent HQ/Checklists/Update User Profile.md`.

## Morning Pass

Run the relevant checks and skills for the day before choosing what to show the user.

Possible morning checks:

- Active goals and open loops.
- Follow-through items, stale waiting threads, missed checks, and pending commitments.
- Questions that would improve future recommendations.
- Recent ponders and contradictions.
- Calendar, email, task, newsletter, or app-action sources when access is configured.
- Area-specific skills when an area has active questions or recurring reviews.
- Profile gaps that would materially improve future recommendations.

Keep the work internal unless the comparison helps the user.

## Choose The Daily Output

Pick the smallest useful output:

- One question that would materially improve future recommendations.
- One insight from existing context that the user may not be noticing.
- One small action that is low-risk, concrete, and worth doing soon.
- One recent ponder that would benefit from a gentle follow-up.
- One area reminder that is due, approaching, or newly relevant.
- One follow-through nudge when an item is stale, important, or newly actionable.
- One app follow-up or external action candidate that the user may want to handle.
- Two or three items only when each item is genuinely urgent or very important.

Prefer a question when missing context is the bottleneck. Prefer an insight when the system already has enough context to notice a pattern. Prefer an action when the next step is obvious and lightweight.

Prefer one item. Never surface more than three items. If more than three may matter, say: `Hey, there are other things that might be important. Do you want me to continue?`

When signals compete, rank candidates by concrete deadline, date, amount, safety/account/family/work stakes, source reliability, and whether the user can usefully act today. Keep one primary touch, with secondary items only for true urgency or importance.

When email, calendar, Things, Messages, or app data disagree, prefer the source of record, confirmation email, or official app over auto-created calendar or task artifacts, and mention the caveat briefly.

## Parallel Focus Scan

When there are multiple plausible daily focus areas, explore them in parallel before choosing the output.

Candidate focus areas:

- Open loops and linked trackers.
- Follow-through ledger.
- Active goals and high-uncertainty areas.
- Area reminders.
- Area questions.
- Recent ponders.
- Contradictions.
- Stale decisions.
- Project links.
- App-action candidates when access is configured.

For each focus area, ask for:

- Signal: what matters here today.
- Urgency: whether it needs attention now.
- Candidate output: one question, insight, action, follow-up, or up to three urgent or very important items.
- Profile update: whether there is a candidate for `$glide-update-user-profile`.
- Background research: whether more research should continue without blocking today's touch.

Then choose the daily output. Keep parallel exploration internal unless a comparison helps the user.

## Selection Rules

- Scan each area's `Reminders.md`.
- Scan `Follow-Through Ledger.md` for stale, due, or newly actionable items.
- Surface reminders only when they are due, overdue, within their lead time, newly relevant from available context, or high-stakes enough that preparation should start.
- Treat only active/open reminders as candidates; leave done or superseded reminders quiet.
- Keep far-future reminders quiet until their lead time or trigger.
- If the lead time is unclear, infer a conservative one from the stakes and ask only when that would change timing.
- If several reminders are active, surface the highest-signal one or a tiny bundle from the same area. Do not turn every reminder into a daily task.

## Interaction Shape

- Write naturally, like a thoughtful coach.
- Keep it short.
- Explain why it matters only if that makes the interaction easier to answer or act on.
- Do not expose tables, queues, or file structure unless it helps.
- Do not ask a question and assign an action unless both are genuinely tiny.
- Avoid generic motivation, trivia, or filler.

Good shape:

1. A one-sentence insight or context.
2. One question, one small action, or up to three urgent or very important items.
3. A short reason if useful.

## After The User Responds

- Update the relevant Agent HQ memory, area file, goal, question, decision, or contradiction as the conversation progresses.
- Update `Follow-Through Ledger.md` when the user creates, clarifies, completes, or retires a follow-through item.
- Run `$glide-update-user-profile` when the answer contains stable, recent, or right-now context that should shape future advice.
- Mark answered questions as answered, refine partial answers, or replace broad questions with better follow-ups.
- Keep the update mostly invisible unless the user needs to verify it.
- Continue naturally if the answer suggests an obvious next question.

## Guardrails

- Do not suggest financial, legal, medical, interpersonal, public, or work-sensitive action as executable. For those, suggest a decision packet or ask for approval.
- Do not send, archive, delete, schedule, reply, purchase, post, or modify external systems unless the user explicitly configured that exact action and approval boundary. Otherwise suggest or draft only.
- Do not make the daily check-in feel like homework.
- Do not optimise every day for productivity; sometimes the best daily output is context, reflection, or protecting capacity.
