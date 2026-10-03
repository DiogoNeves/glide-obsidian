---
name: glide-create-area
description: Create or initialize a durable Glide area in Agent HQ.
---

# Glide Create Area

## Load

Read `Agent HQ/AGENTS.md` and `Agent HQ/Areas/AGENTS.md`. Retrieve relevant current goals, constraints and project links through `Memory Protocol.md` after recorded cutover; without cutover use only relevant legacy profile/goal/project evidence. Do not create speculative unused areas or load the full portfolio.

## Process

1. Identify the area name, purpose, and home boundary.
2. Use parallel subagents when creating the area requires searching many notes, projects, goals, or existing areas.
3. Create the standard area files:
   - `AGENTS.md`
   - `Area.md`
   - `Goals.md`
   - `Context.md`
   - `Reminders.md`
   - `Sources.md`
   - `Decisions.md`
   - `Questions.md`
   - `Reviews/README.md`
   - `Checklists/README.md`
   - `Research/README.md`
4. In `Reminders.md`, create an active reminders section with columns `Status`, `When / Trigger`, `Lead Time`, `Reminder`, `Surface When`, and `Source`, plus a done/superseded section with `Date`, `Reminder`, and `Outcome`. Reminders may be date-based or trigger-based, including far-future items that stay quiet until their lead time or trigger.
5. Link relevant goals and projects.
6. Add useful questions and reminders through managed records after cutover; otherwise use the area's selected legacy files. Do not duplicate migrated current state.
7. Do not move or rewrite existing vault notes unless the user explicitly asks.

## Output

- New area files.
- Summary of what was created.
- Open questions and initial reminders that would improve future reviews.
