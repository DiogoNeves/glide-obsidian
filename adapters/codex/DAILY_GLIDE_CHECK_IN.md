# Daily Glide Check-In Automation Prompt

Run `$glide-daily-check-in` for this vault.

Use the Glide skill as the source of truth for context loading, morning checks, daily-output selection, subagent parallel focus scanning, guardrails, and light evaluation.

Before choosing the daily output, run `$glide-update-user-profile`, then scan `Agent HQ/Follow-Through Ledger.md`, `Agent HQ/Areas/*/Reminders.md`, `Agent HQ/Open Loops.md`, active goals, questions, ponders, contradictions, recent decisions, and relevant area files. Surface follow-through items only when stale, due, important, or newly actionable. Surface area reminders only when due, within lead time, newly relevant, or high-stakes enough to prepare. When configured, also check relevant inbox, calendar, task, newsletter, or app-action sources. When several daily focus areas are plausible, use narrow subagents to explore each candidate focus area, then integrate their findings and choose the smallest useful user-facing output.

If a tracked item has high stakes, an approaching or missed deadline, a stale unanswered thread, or a likely new app development, look into relevant available connectors safely and consider surfacing it.

When signals compete, rank candidates by concrete deadline, date, amount, safety/account/family/work stakes, source reliability, and whether the user can usefully act today. If email, calendar, Things, Messages, or app data disagree, prefer the source of record, confirmation email, or official app over auto-created calendar or task artifacts, and mention the caveat briefly.

Continue background research only when it would materially improve future recommendations or autopilot, and do not let background research bloat the daily message.

Keep the output conversational and short. Prefer one item. Use two or three only when each is genuinely urgent or very important. Never surface more than three items. If more than three may matter, say: `Hey, there are other things that might be important. Do you want me to continue?` If there is no useful question, insight, advice, tracked open-loop update, or low-risk action today, say so briefly instead of manufacturing homework.

Do not suggest financial, legal, medical, interpersonal, public, or work-sensitive actions as executable; draft or ask for approval instead. Do not modify external systems unless the user explicitly configured that exact action and approval boundary.
