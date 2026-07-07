---
name: glide-whatsapp-attention-review
description: Review local WhatsApp attention signals safely from macOS without opening chats or marking messages as read. Use when the user asks to inspect WhatsApp, find unread or important WhatsApp messages, summarize WhatsApp reply or action candidates, or when a daily Glide check includes configured WhatsApp sources.
---

# Glide WhatsApp Attention Review

## Load

- `Agent HQ/AGENTS.md`
- `Agent HQ/Communication Preferences.md`
- `Agent HQ/Checklists/App Interface And Computer Use.md`
- `Agent HQ/Checklists/WhatsApp Access.md`
- `Agent HQ/WhatsApp Access Log.md`
- Relevant goals, areas, projects, decisions, and recent Agent HQ context when interpreting a WhatsApp item

## Process

1. Follow `Agent HQ/Checklists/WhatsApp Access.md`.
2. Start read-only and metadata-first. Prefer the tested local SQLite path for WhatsApp Desktop on macOS.
3. For daily checks, use the configured daily scope: unread or attention signals, likely reply needs, commitments, family/work/logistics, time-sensitive coordination, and stale important chats.
4. Do not open WhatsApp chats, use WhatsApp UI/Web, connect a new linked device, mark chats read/unread, send, react, forward, delete, pin, archive, mute, block, or change settings unless the user explicitly confirms that exact action in the current interaction.
5. Avoid broad transcript dumps. Read only the rows needed for the requested scope, and summarize the signal rather than pasting private message text unless the user asks for exact wording.
6. Treat high-volume groups as low-signal by default unless names, timestamps, or snippets suggest a direct mention, commitment, deadline, work/family relevance, or another clear action.
7. For any outbound WhatsApp message, draft the exact text and show the recipient/chat, attachments, and method before asking for approval.
8. Keep durable updates small. Capture only decisions, commitments, open loops, or short operational summaries in Agent HQ unless the user explicitly asks to store more.
9. Append a compact entry to `Agent HQ/WhatsApp Access Log.md` when WhatsApp access is attempted.

## Output

- Scope requested:
- Access method:
- Signal found:
- Draft reply, if useful:
- Approvals needed:
- Durable Agent HQ updates:
- What was not accessed:
