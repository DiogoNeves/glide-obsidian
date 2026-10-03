# WhatsApp Access

Use when the user asks Glide to inspect, summarize, draft, or prepare replies for WhatsApp on macOS.

## Safety Contract

- Treat WhatsApp as high-sensitivity interpersonal data.
- Start read-only, metadata-first, and narrow.
- Prefer local SQLite reads over opening WhatsApp or using WhatsApp Web.
- Do not open unread chats in the WhatsApp UI.
- Do not send, react, mark read, mark unread, delete, forward, block, pin, archive, mute, edit, change settings, or connect a new linked device unless the user explicitly confirms that exact action in the current interaction.
- For daily checks, never send anything and never mark conversations as read.
- For any outbound message, show the recipient or chat, exact message text, attachments, and transport/method if relevant, then wait for confirmation.
- Do not import full conversation transcripts into Obsidian by default.
- Capture only a short operational summary in Agent HQ when the user asks or when a configured workflow requires it.

## Daily Check

- Daily Glide may check for important WhatsApp items when safe local read-only access is available.
- Keep the daily scope narrow: unread/attention signals, likely reply needs, family/work/logistics messages, commitments, time-sensitive coordination, and stale important chats.
- Prefer the tested local WhatsApp Desktop database path in read-only SQLite mode.
- Do not open WhatsApp chats or WhatsApp Desktop to inspect unread conversations.
- Do not mark anything as read unless it was already read before the check and the user explicitly asks.
- Surface at most the highest-signal item or a tiny bundle. Do not create a broad WhatsApp digest by default.
- Treat large group-chat unread counts as low-signal unless there is evidence of a direct mention, commitment, deadline, family/work relevance, or other actionable item.

## Local Read Path

Use SQLite in read-only URI mode:

```sh
sqlite3 "file:$HOME/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite?mode=ro" \
  "SELECT count(*) AS chats,
          sum(CASE WHEN ZUNREADCOUNT > 0 THEN 1 ELSE 0 END) AS unread_chats,
          coalesce(sum(ZUNREADCOUNT),0) AS unread_messages
   FROM ZWACHATSESSION;"
```

Unread chat preview, limited and metadata-first:

```sh
sqlite3 -header -column "file:$HOME/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite?mode=ro" \
  "SELECT coalesce(nullif(c.ZPARTNERNAME,''), nullif(c.ZCONTACTIDENTIFIER,''), c.ZCONTACTJID, '(unknown)') AS chat,
          c.ZUNREADCOUNT AS unread,
          datetime(m.ZMESSAGEDATE + 978307200, 'unixepoch', 'localtime') AS last_at,
          CASE WHEN m.ZISFROMME = 1 THEN 'me' ELSE 'them' END AS from_side,
          substr(replace(replace(coalesce(m.ZTEXT, c.ZLASTMESSAGETEXT, ''), char(10), ' '), char(13), ' '), 1, 90) AS preview
   FROM ZWACHATSESSION c
   LEFT JOIN ZWAMESSAGE m ON m.Z_PK = c.ZLASTMESSAGE
   WHERE c.ZUNREADCOUNT > 0
   ORDER BY m.ZMESSAGEDATE DESC
   LIMIT 10;"
```

Important local tables and fields:

- `ZWACHATSESSION`: chat rows, `ZUNREADCOUNT`, `ZLASTMESSAGE`, `ZLASTMESSAGETEXT`, `ZPARTNERNAME`, `ZCONTACTIDENTIFIER`, `ZCONTACTJID`, `ZLASTMESSAGEDATE`.
- `ZWAMESSAGE`: message rows, `ZTEXT`, `ZISFROMME`, `ZMESSAGEDATE`, `ZSENTDATE`, `ZFROMJID`, `ZTOJID`, `ZCHATSESSION`, `ZGROUPMEMBER`, `ZMESSAGETYPE`, `ZMESSAGESTATUS`.
- `ZWAMEDIAITEM`: media metadata linked from messages.
- `fts/ChatSearchV5f.sqlite`: WhatsApp full-text search index. Prefer the main DB for daily attention checks unless search is specifically requested.

Notes:

- Use `mode=ro`; do not write to the live database.
- Do not use `immutable=1` while WhatsApp may be running or WAL files may have recent committed rows.
- WhatsApp timestamps in this store use the Apple/Core Data epoch; add `978307200` seconds to convert to Unix time.
- The tested read path does not open chats and should not send read receipts. Unread counts may still change while querying if new messages arrive or WhatsApp syncs in the background.
- If the database is unavailable, locked, or schema changes, stop and report the limitation instead of opening WhatsApp.

## Other Access Paths

1. Direct local SQLite read-only access to the WhatsApp Desktop group container is the preferred daily path.
2. A configured CLI mirror may be useful for search or automation only if the user has explicitly chosen to pair it. Use read-only settings where available.
3. iOS/Android backup exporters are useful for archive/export work, not daily attention review.
4. WhatsApp UI, WhatsApp Desktop, WhatsApp Web, browser automation, or computer use should be avoided for unread-message review because opening a chat may change read state.

## Approval-Gated Send Path

Before sending, present:

- recipient or chat identifier,
- exact message text,
- attachments, if any,
- whether the message will be sent through WhatsApp Desktop, WhatsApp Web, a configured CLI, or another method.

Then wait for explicit approval.

## Avoid

- Opening unread WhatsApp chats.
- Connecting a new linked device without approval.
- Writing directly to WhatsApp SQLite databases.
- Requesting WhatsApp credentials or backup keys.
- Broad ingestion of all conversations.
- Storing private transcripts in the vault unless the user explicitly asks.
- Treating high unread counts in busy groups as automatically important.

## Scoped access audit

Append a compact attempted-access entry to `Agent HQ/WhatsApp Access Log.md`: requested scope, actual method, useful signal and material access gaps. This existing audit surface does not become a parallel current operations store after memory cutover; retain operational summaries through the selected writer.
