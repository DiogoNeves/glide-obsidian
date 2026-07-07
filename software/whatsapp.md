# WhatsApp

Optional macOS access guide for WhatsApp Desktop.

## Role

WhatsApp is usually high-sensitivity interpersonal context. Treat it as an attention source, not a default archive.

## Safe Read Methods

- Prefer local read-only SQLite access to WhatsApp Desktop's group container.
- Start with metadata and unread counts.
- Read short previews only when needed to decide whether something deserves attention.
- Keep daily checks narrow: likely reply needs, commitments, time-sensitive coordination, family/work/logistics, or stale important chats.

Recommended local read path:

```sh
sqlite3 "file:$HOME/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite?mode=ro" \
  "SELECT count(*) AS chats,
          sum(CASE WHEN ZUNREADCOUNT > 0 THEN 1 ELSE 0 END) AS unread_chats,
          coalesce(sum(ZUNREADCOUNT),0) AS unread_messages
   FROM ZWACHATSESSION;"
```

See `Agent HQ/Checklists/WhatsApp Access.md` for the fuller checklist and preview query.

## Approval-Gated Actions

Ask before:

- opening chats,
- sending, reacting, forwarding, deleting, pinning, archiving, muting, blocking, or editing,
- marking chats read or unread,
- connecting a new linked device,
- storing transcripts in the vault.

For any outbound message, draft the exact text and show the recipient/chat and method before asking for approval.

## Methods To Avoid

- Do not use WhatsApp UI or WhatsApp Web for unread-message review when opening a chat could change read state.
- Do not write to WhatsApp SQLite databases.
- Do not request WhatsApp credentials or backup keys.
- Do not broadly ingest private conversations by default.

## Notes

- WhatsApp timestamps in the local store use the Apple/Core Data epoch; add `978307200` seconds to convert to Unix time.
- Do not use `immutable=1` while WhatsApp may be running or WAL files may contain recent committed rows.
- If the database is unavailable, locked, or the schema changes, stop and report the limitation instead of opening WhatsApp.
