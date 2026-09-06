# Protect and recover an instance

The application-data folder is not wholly disposable. SQLite and installed code can be recreated; private configuration, local instructions, evaluation cases and import/recovery material need a recovery plan. This applies to both standalone and embedded Glide instances.

Install the [canonical procedure](../templates/Agent%20HQ/Checklists/Recovery.md) during setup and existing-instance upgrades. It is used by the existing integrity review, with required input delivered in conversation. No new scheduler or backup provider is installed implicitly.

## What is protected where

| Component | Recovery method |
| --- | --- |
| Durable Markdown, history and necessary evidence | Workspace backup; synchronization alone is not a complete backup strategy |
| Configuration, custom instructions, evaluation cases and job definitions | Versioned local allowlisted export; optionally a reviewed private repository |
| Runtime and helper code | Exact source/package pins and installation instructions |
| Pending imports, transcripts and private diagnostic/rollback evidence | Private encrypted backup coverage; inspect before treating as redundant |
| Credentials | Separate secure recovery or reauthentication; never configuration Git |
| SQLite, locks and caches | Rebuild; do not continuously synchronize or commit |

## Repeatable local export

Use `tools/recovery_bundle.py` from the matching **glide** owner checkout. Install it outside the workspace, record its SHA-256, and supply a private policy:

```json
{
  "schema": 1,
  "instance_id": "example-instance",
  "export_root": "/absolute/private/recovery/exports",
  "files": [
    {"name": "instance/config.json", "source": "/absolute/private/instance/config.json"}
  ],
  "off_machine_backup": {"status": "pending"},
  "private_repository": {"status": "not-selected"}
}
```

This is a minimal shape, not a complete allowlist. Inspect the actual instance to include its customizations, frozen cases, helper/package manifests, harness configuration and selected automation definitions. Export policies and their source paths are private. Do not blindly copy an entire application-data or Codex folder.

```sh
python3 /installed/path/recovery_bundle.py inspect --policy /private/instance/recovery.json
python3 /installed/path/recovery_bundle.py export --policy /private/instance/recovery.json
python3 /installed/path/recovery_bundle.py verify --bundle /private/recovery/exports/CONTENT_HASH
```

The helper requires Python 3.11+, uses the standard library, and performs local operations only. It refuses symlink paths, traversal, duplicate export names, missing input, common credential assignments and database/lock files. The credential checks are tripwires, not a full security audit. Files are explicit, size-bounded UTF-8 entries; directories and raw transcripts are not automatically admitted. Content hashes detect changes and unchanged exports are reused. Incomplete staging directories are not successful versions. No deletion/retention policy is implied.

An export preserves original configuration for diagnosis, including possible active-writer settings. It is **not directly executable restore configuration**. Follow its restore instructions: recreate local paths and authentication, disable writers and jobs, then verify before activation. Hash verification proves file consistency, not trusted authorship, successful off-machine backup, or application recovery.

## Setup readiness and upgrade

Record each state separately: inventory, verified export, local restore drill, chosen backup destination, completed backup, and tested restoration from that backup. Preserve user deferrals and report them as gaps, not failures of unrelated runtime checks. Optional private Git provides reviewable configuration history; it does not replace encrypted data backup. Review exact contents before first upload or scope expansion, and preserve the owner's commit policy.

Existing instances merge the procedure and short skill routing while preserving custom instructions and prior hashes. Install the helper from reviewed source; no memory schema/build change is needed. Restore a disposable copy with jobs/writers disabled, compare configuration bytes, rebuild memory and check current/historical answers. Confirm the live writer remains unchanged. This local drill is narrower evidence than recovery on another physical machine.

During existing Harness review, refresh exports only when admitted configuration changes. Inspect newly introduced dependencies, backup freshness and unresolved gaps. The agent must not call an export current protection merely because the helper succeeded. No-change reviews are quiet; a deferred destination is raised again only when materially relevant.
