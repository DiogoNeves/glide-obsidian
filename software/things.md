# Things

Use when the user wants Glide to inspect or prepare changes for Things tasks.

## Boundary

- Glide / Obsidian: thinking, memory, interpretation, reviews, and decisions.
- Things: commitments, dated work, active projects, and concrete tasks.

Default posture: read Things, synthesize, and propose changes. Write only after the user explicitly approves the exact change.

## Access Options

Preferred safe methods:

- a read-only MCP server or connector, when configured,
- AppleScript or JXA for documented read operations on macOS,
- Things URL Scheme or Shortcuts for approved writes,
- Mail to Things only when the user explicitly wants email capture.

Things does not have a general public API. Useful official references:

- Things support on automation options: https://culturedcode.com/things/support/articles/2967034/
- Things URL Scheme: https://culturedcode.com/things/support/articles/2803573/
- Things AppleScript guide: https://culturedcode.com/things/support/articles/4562654/

## Safe Workflow

1. Start with a narrow read, such as Today, Inbox, Upcoming, or a named project.
2. Prefer counts or short capped lists before reading lots of task detail.
3. Interpret list semantics before recommending changes.
4. Cross-check with Glide only when it changes priority or follow-through.
5. Show proposed changes before writing.

Never ask for Things Cloud credentials or write directly to Things' local database.

## Scheduling Rule

Do not assign dates just because something should not be forgotten.

Use Today, Upcoming, and deadlines only when there is a real timing constraint, a real commitment to act on that date, or a date that materially changes the decision. If the purpose is "do not lose this", route it to the right project, list, or Glide follow-through item.

## Weekly Sweep

During a weekly review, inspect Things at a high level when configured:

- Today overload or stale carryover.
- Inbox items that need routing, deletion, scheduling, or parking.
- Active projects with no next action.
- Important Glide open loops with no visible commitment.
- Duplicate or misplaced tasks.

Output a concise triage and ask before changing Things.

## Approval-Gated Writes

Before writing to Things, show:

- add,
- complete/cancel,
- reschedule,
- move/list/project/area,
- tags,
- notes,
- why.

Then wait for approval unless the user already gave a direct command.
