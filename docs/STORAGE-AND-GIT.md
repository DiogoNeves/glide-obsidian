# SQLite, Git and synchronization

Sync readable `Agent HQ/Memory/` records, evidence and complete Markdown history. Keep the live SQLite index, Python, dependencies and private machine configuration outside the vault and synchronization roots. Another device can read the Markdown without installing anything; an executing device installs the pinned runtime and rebuilds locally.

The shared [SQLite and Git guide](SHARED-REFERENCES.md#storage-and-git) explains this decision using SQLite and Git's primary documentation. In a matching unpublished checkout, read Glide's local `docs/STORAGE-AND-GIT.md` instead.

SQLite supports portable database files and consistent backup snapshots. The unsafe part is ordinary copying while the database and required journal state are changing. Git and Obsidian do not merge SQL records. A verified immutable snapshot is an optional transfer shortcut; rebuilding from Markdown remains the recovery path. Sources: [SQLite copying](https://sqlite.org/howtocorrupt.html#_backup_or_restore_while_a_transaction_is_active), [SQLite backup API](https://sqlite.org/backup.html), [Git binary merging](https://git-scm.com/docs/gitattributes#_performing_a_three_way_merge), [Obsidian conflict handling](https://help.obsidian.md/sync/troubleshoot).

The package's `.gitignore` excludes the runtime's specific `index.sqlite3` and journals, rather than every database or finance dataset. An ignore rule does not remove already tracked files. Inspect tracked files before migration and keep private manifests, connectors and exports out of this public package. See [gitignore](https://git-scm.com/docs/gitignore), [privacy](PRIVACY.md) and [machine handover](UPGRADING.md).
