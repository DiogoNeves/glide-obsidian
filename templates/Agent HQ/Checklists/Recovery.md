Purpose: make every required instance component reproducible, backed up, or explicitly reported as a recovery gap.

## Setup and upgrades

Inventory the actual instance, not just its SQLite index. Classify durable Markdown and evidence, private configuration and instruction customizations, exact runtime/helper versions, frozen evaluation cases, source-import manifests and pending captures, credentials, and rebuildable caches. Include the executing harness's job definitions and source permissions even when Glide is embedded in another project. Resolve local paths privately. Preserve prior choices; never overwrite customizations from a template.

Ask in conversation only for missing choices: an off-machine backup destination and optional private configuration repository. A local export is useful but is not protection against losing the machine. Record a declined or deferred choice without repeatedly asking; resurface it for a transfer, upgrade with recovery risk, or material failure. Never mark a configured destination as a completed backup.

Use the shared `tools/recovery_bundle.py` from the matching Glide source distribution. Install its exact hashed bytes outside the workspace and record the private helper path. Create a private `recovery.json` policy with an explicit list of reviewed UTF-8 configuration files. Include local skill customizations, frozen cases, package pins, relevant automation definitions and restore dependencies. Keep runtime code reproducible from its package rather than exporting installed executables. The helper is separate from the pinned memory runtime and does not install an MCP tool or bypass filesystem restrictions.

Only expand that allowlist after reviewing ownership and sensitive content. Never include credentials, transcripts, live databases, locks or bulk archives in a configuration repository. Put required raw imports, source evidence and private recovery material in encrypted backup coverage instead. Credentials need separate secure recovery or reauthentication. A private repository is optional and requires an approved destination and disclosure scope; automatic local export permission is not permission to commit or upload. No secrets scanner proves an export safe to publish.

## Export and prove recovery

Run `inspect --policy /absolute/path/recovery.json` to detect changed or missing allowlisted configuration. Run `export` with the same policy to publish an immutable content-addressed local configuration version, then `verify --bundle /absolute/path/to/version`. Unchanged inputs reuse the verified version. The helper creates no network connections, backup schedules or writer activations. If the harness lacks permission to run it, report that capability gap rather than claiming export succeeded or widening permissions.

Separately restore a completed export into a disposable location and compare its file hashes. Restore durable Markdown and required evidence from the selected backup or a clearly labelled local test copy. Keep restored jobs paused and writer_active=false; never execute restored active configuration or replay automation TOML. Install the pinned dependencies, rebuild SQLite in the disposable instance, and compare records, historical answers, evidence and applicable evaluation fixtures. Verify that the production writer configuration did not change. A local copied-store drill does not prove an off-machine backup exists or can be restored.

Record distinct states: inventory completed, configuration export verified, local restore tested, backup destination configured, backup completed, and restore from that backup tested. Include observation dates, source revision/head, tested scope and unresolved gaps. Keep the receipt internal and bring actionable gaps into conversation. For machine handover, stop the previous writer before activating one new writer; never restore machine identity or active schedules blindly.

## Ongoing Harness review

During the existing integrity/harness review, inspect current paths and newly added dependencies as well as allowlisted hashes. The helper checks only the approved list; it cannot discover every future component or verify a backup service. Refresh changed local exports within the approved scope and verify the result. Missing files, failed checks or newly uncovered dependencies remain findings. Verify actual backup completion/freshness and restore evidence using the selected service; preserve failures rather than silently advancing success.

Re-run the affected restore checks after meaningful recovery/schema/configuration changes and before a machine transfer. Routine unchanged checks stay quiet. Do not add another job, prune old exports/backups, upload files, change retention, alter encryption or activate writers autonomously. Keep protected principles and original writing unchanged.
