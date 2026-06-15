# Apple Calendar

Use when the user wants Glide to inspect Calendar.app context on macOS.

## Safety Contract

Treat calendar data as sensitive personal data.

Start read-only and narrow. Do not create, edit, delete, invite, RSVP, reschedule, or change calendars unless the user explicitly approves that exact action.

Prefer summaries and operational signals over importing calendar details into Obsidian.

## Best Access Paths

1. Use an official calendar connector or API when the user has configured one.
2. Use Calendar.app AppleScript for simple read-only checks when it works reliably in the harness.
3. Use a read-only copy of Calendar's local SQLite store only as a fallback, and query the copy, not the live database.
4. Use browser or computer control only when the user chooses that workflow and the action remains reviewable.

## Safe Read Path

Start with a metadata-only probe:

```sh
osascript -e 'tell application "Calendar" to {count calendars, count events}'
```

If AppleScript access is unreliable, create a temporary read-only snapshot before querying Calendar's local store:

```sh
tmpdir="$(mktemp -d)"
cp "$HOME/Library/Group Containers/group.com.apple.calendar/Calendar.sqlitedb"* "$tmpdir/"
sqlite3 "$tmpdir/Calendar.sqlitedb" 'select count(*) from CalendarItem;'
```

Only query a narrow date window. Calendar date fields commonly use Apple's 2001-01-01 reference date, so convert times carefully in SQLite:

```sql
datetime(start_date + 978307200, 'unixepoch', 'localtime')
```

Useful tables may include `Calendar`, `Store`, `CalendarItem`, `Location`, and `OccurrenceCache`, but schema details can vary by macOS version.

## Approval-Gated Writes

Before changing Calendar, show:

- calendar,
- event title,
- date and time,
- location or meeting details,
- invitees or conferencing changes,
- exact action,
- why it is needed.

Then wait for explicit approval.

## macOS Permissions

AppleScript access requires macOS Automation permission for the harness, terminal, or parent app to control Calendar.

Direct reads of Calendar storage may require Full Disk Access for the process reading the files. Prefer temporary copies and read-only queries.

## Avoid

- Writing directly to Calendar's SQLite database.
- Broad calendar exports.
- Importing private calendar history into Obsidian by default.
- Treating a calendar event as a task unless the user uses Calendar that way.
- Marking missing or tentative details as fact.
