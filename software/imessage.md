# Messages / iMessage

Use when the user wants Glide to inspect, summarize, draft, or prepare replies for Messages on macOS.

Messages may include iMessage, SMS, MMS, and RCS conversations depending on the user's Apple Account, iPhone setup, carrier, and macOS version.

## Safety Contract

Treat Messages as high-sensitivity interpersonal data.

Start read-only and narrow. Do not send, react, mark read, delete, forward, block, pin, edit, change settings, or modify conversations unless the user explicitly confirms that exact action in the current interaction.

For any outbound message, show the recipient or chat, exact message text, attachments, and transport if relevant, then wait for confirmation.

Do not import full conversation transcripts into Obsidian by default. Capture only a short operational summary in Glide when the user asks or when a configured workflow requires it.

## Best Access Paths

1. Use a purpose-built local tool such as `imsg` when the user chooses to install and authorize it. It reads `~/Library/Messages/chat.db` and can emit JSON, while sends go through Messages AppleScript automation.
2. Use Messages AppleScript for metadata checks and approval-gated sending. The local Messages scripting dictionary exposes accounts, chats, participants, file transfers, and a `send` command. It does not expose a full transcript-reading API.
3. Use direct SQLite reads of `~/Library/Messages/chat.db` only as a fallback, read-only, narrowly scoped, and preferably against a temporary copy of `chat.db`, `chat.db-wal`, and `chat.db-shm`.
4. Use Shortcuts or computer use only when the user has chosen that workflow and the action remains reviewable.

## Safe Read Path

Start with a metadata-only probe:

```sh
osascript -e 'tell application "Messages" to {count accounts, count chats}'
```

If `imsg` is installed and the user has granted the needed permissions, list recent chats before reading content:

```sh
imsg chats --limit 10 --json
```

Read message history only after the user scopes the chat and purpose:

```sh
imsg history --chat-id <id> --limit 20 --json
```

For direct SQLite fallback, do not write to the live database and do not run broad history exports. Message text can be stored in multiple fields, so prefer a maintained reader over hand-written SQL when accuracy matters.

## Approval-Gated Send Path

Sending can be done through Messages AppleScript or a wrapper such as `imsg send`, but only after confirmation.

Before sending, present:

- recipient or chat identifier,
- exact message text,
- attachments, if any,
- whether this is iMessage, SMS, MMS, RCS, or automatic routing when known,
- the command or method that will be used.

Then wait for explicit approval.

## macOS Permissions

- Messages must be configured on the Mac. For SMS, MMS, or RCS relay, the user's iPhone and Mac must use the same Apple Account and text message forwarding must be enabled.
- AppleScript access requires macOS Automation permission for the harness, terminal, or parent app to control Messages.
- Reading `~/Library/Messages/chat.db` requires Full Disk Access for the process that reads it.
- Contacts permission is optional and only needed for resolving names from handles.

## Avoid

- Sending, reacting, marking read, or changing Messages state without explicit confirmation.
- Writing directly to `~/Library/Messages/chat.db`.
- Requesting Apple Account credentials or Messages/iCloud credentials.
- Broad ingestion of all conversations.
- Storing private transcripts in the vault unless the user explicitly asks.
- Relying on the `sms:` URL scheme for macOS automation. Apple's archived URL scheme docs describe `sms:` composition and note SMS links are iOS-only.

## Sources

- Apple Support, Messages on Mac setup and SMS/MMS/RCS forwarding: https://support.apple.com/guide/messages/set-up-messages-on-mac-ichte16154fb/14.0/mac/26
- Apple Support, text message forwarding: https://support.apple.com/en-gb/102545
- Apple URL Scheme Reference, SMS links: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/SMSLinks/SMSLinks.html
- Apple Shortcuts URL scheme on Mac: https://support.apple.com/guide/shortcuts-mac/run-a-shortcut-from-a-url-apd624386f42/mac
- `imsg` Messages.app CLI docs: https://imsg.sh/
- Local Messages AppleScript dictionary checked with `sdef /System/Applications/Messages.app` on 2026-05-25.
