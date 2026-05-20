# Daily Glide Check-In Automation Prompt

Run `$glide-daily-check-in` for this vault.

Use the Glide skill as the source of truth for context loading, morning checks, daily-output selection, subagent parallel focus scanning, guardrails, and light evaluation.

Before choosing the daily output, scan `Agent HQ/User Profile.md`, `Agent HQ/Open Loops.md`, active goals, questions, ponders, contradictions, recent decisions, and relevant area files. When configured, also check relevant inbox, calendar, task, newsletter, or app-action sources. Refresh `User Profile.md` only when recent context contains durable signal; keep long-term updates conservative and let lately/right-now context move more often. When several daily focus areas are plausible, use narrow subagents to explore each candidate focus area, then integrate their findings and choose the smallest useful user-facing output.

If a tracked item has high stakes, an approaching or missed deadline, a stale unanswered thread, or a likely new app development, look into relevant available connectors safely and consider surfacing it.

Continue background research only when it would materially improve future recommendations or autopilot, and do not let background research bloat the daily message.

Keep the output conversational and short. It may include a small bundle when multiple checks produce genuinely useful results. If there is no useful question, insight, advice, tracked open-loop update, or low-risk action today, say so briefly instead of manufacturing homework.

Do not suggest financial, legal, medical, interpersonal, public, or work-sensitive actions as executable; draft or ask for approval instead. Do not modify external systems unless the user explicitly configured that exact action and approval boundary.
