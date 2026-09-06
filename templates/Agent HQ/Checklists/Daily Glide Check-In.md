# Daily Glide Check-In

Purpose: run a concise morning pass that improves Agent HQ accuracy, checks relevant context, surfaces timely insight, or moves a small approved action forward.

Follow `Checklists/Input and Collaboration.md`: bring required questions and review choices into conversation; internal records are optional evidence. Create a shared note outside Agent HQ only when useful or requested and within an authorized edit scope.

## With Versioned Memory Enabled

For an instance that has completed cutover, this branch replaces the legacy load, update and evaluation instructions below for migrated state. Read `Memory Protocol.md` and communication preferences; start with `glide_job_inputs(job_id="daily")`, Now/Ongoing and only relevant records/evidence. Successful intake receipts establish only their reported source scope; partial or unavailable ranges remain pending. Do not reload or maintain a parallel legacy portfolio.

If the optional conversation-learning unit is installed and history recovery authorized, run its bounded recovery before choosing the touch. Reconcile accepted commitments, current decisions and relevant source evidence. Use the source-app skills when needed, preserving their authority. Apply the selection and interaction guidance below: one useful candid touch, with extra items only for real urgency. After cutover, references there to reminder/ledger files mean the equivalent managed operations; do not rescan those legacy files unless their unmigrated context is relevant.

Commit permitted outputs and the checkpoint through `glide_finish_job`, including successful conversation coverage when inspected. Follow separate knowledge review when required; preserve failed/unread work and inactive inferred candidates. Record meaningful observed feedback through the writer; an unchanged run needs no growing narrative log. Use the legacy procedure below only for an instance without cutover or specifically unmigrated context.

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
- `Agent HQ/Checklists/WhatsApp Access.md` when WhatsApp access is configured
- `Agent HQ/Checklists/Eval Loop.md`
- `Agent HQ/Evals/Run Log.md`
- `Agent HQ/Evals/Signal Clusters.md` only when recent eval patterns affect today's selection
- `Agent HQ/Evals/Eval Cases.md` only when a run reveals a reusable test case
- Relevant area `Questions.md`, recent reviews, decisions, and contradictions
- Available inbox, calendar, task, WhatsApp, or app-action sources when access is configured and the run can check them safely

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
- One important WhatsApp item the user may need to pick up, when WhatsApp access is configured.
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
- WhatsApp attention items when access is configured.
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
- For WhatsApp, use `$glide-whatsapp-attention-review` or `Checklists/WhatsApp Access.md`. Keep it read-only, do not open unread chats, do not mark conversations as read, and do not send anything during the daily check.

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

## Evaluation

- Follow `Agent HQ/Checklists/Eval Loop.md`.
- When the run produces a useful touch or durable update, append a tiny entry to `Agent HQ/Evals/Run Log.md`.
- Record date, run, touch type, sources used, useful verdict, facets, eval decision, and one improvement.
- Use short facets such as `missed-deadline`, `stale-memory`, `too-broad-question`, `good-timing`, `approval-boundary`, `connector-failure`, `quiet-source-risk`, `goal-forward`, `maintenance-crowding`, `memory-update`, `source-provenance`, and `follow-through`.
- Choose an eval decision: `keep`, `tune`, or `case`.
- Promote a case only for a reusable failure, near-miss, repeated pattern, or unusually good behavior.
- Add or update `Agent HQ/Evals/Signal Clusters.md` only when a repeated or high-stakes pattern is emerging.

## Guardrails

- Do not suggest financial, legal, medical, interpersonal, public, or work-sensitive action as executable. For those, suggest a decision packet or ask for approval.
- Do not send, archive, delete, schedule, reply, purchase, post, or modify external systems unless the user explicitly configured that exact action and approval boundary. Otherwise suggest or draft only.
- Do not make the daily check-in feel like homework.
- Do not optimise every day for productivity; sometimes the best daily output is context, reflection, or protecting capacity.
