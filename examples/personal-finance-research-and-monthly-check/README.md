# Personal Finance Research And Monthly Check

## Situation

The user wants better financial defaults without spending much personal attention on finance.

They do not need investment advice from a template. They need a system that can:

- research how to organize personal and family finance context
- identify what should be tracked
- spot missing information
- propose recurring checks
- keep financial recommendations as decision support, not execution

## Request

```text
Research how I should organize personal finance in Glide and set up a monthly check.
```

## What Glide Should Do

1. Use `glide-deep-research-subject` to research personal finance organization, budgeting, cash flow, resilience, debt, investing context, and early-warning signals.
2. Separate evidence from opinion: lived experience, expert practice, empirical evidence, and weak signals.
3. Update or propose updates to `Agent HQ/Areas/Finance/Context.md`, `Reminders.md`, `Questions.md`, `Sources.md`, and `Research/`.
4. Identify the minimum recurring data needed for useful reviews.
5. Create a proposed monthly finance check in `Agent HQ/Automations/` and `Agent HQ/Automation Registry.md`.
6. Ask before enabling the automation or touching external accounts, statements, email, banks, or spreadsheets.

## Monthly Check Shape

The monthly check could review:

- cash flow
- upcoming irregular expenses
- debt and interest changes
- subscriptions and recurring charges
- emergency buffer
- investment and pension context
- missing statements or missing assumptions
- decisions that need approval

It should surface risks, opportunities, and questions. It should not execute financial actions without explicit approval.

## Daily Check-In Connection

The daily morning check can run multiple relevant checks and skills before deciding what to show the user.

For example, the user might ask Glide to:

- track whether finance statements are missing
- surface finance reminders only when due, approaching, or newly relevant
- summarize interesting finance newsletters from email
- archive newsletters after summarizing them, if that exact action and approval boundary has been configured
- flag a recurring payment change
- remind the user of one finance question that would improve future recommendations

The user-facing output should stay short. The system can do several checks; the user should only see what matters.
