# Upgrade An Existing Instance

Versioned memory is an explicit upgrade. Do not replace a working instance merely because new templates exist. Preserve its customizations and source ownership.

## Inspect And Plan

Inspect installed instructions, selected skills, source ownership, current ledger/open-loop state, active automation configuration, existing runtime version and sync boundaries. Folder presence alone does not establish that a scheduled job exists or ran successfully.

Compare the recorded installation manifest with the supplied release. For each managed file, compare its installed baseline hash, current hash and new release hash. A changed local hash is a customization requiring an explicit merge; an absent baseline is unknown ownership, not permission to replace. Leave unrelated and protected files intact.

Write a reviewable plan identifying file changes, schema/runtime compatibility, source adapters, generated-store location, single writer, timezone and old/new jobs. New jobs remain disabled until cutover. Keep separate instances' private configuration separate.

## Back Up And Apply

Back up the current source/operational files and demonstrate restoration. Include the authoritative Markdown bundles, source evidence needed for historical claims and private configuration in appropriate private backups. A SQLite-only backup is insufficient. Keep the prior runtime release for rollback.

Install the supplied compatible `glide_memory` 0.1.0 release outside the vault/workspace, using Python 3.11 or later with SQLite FTS5 on the supported platform; see [setup requirements](SETUP.md). The Obsidian distribution uses the exact shared runtime; a local supplied checkout/archive is sufficient. For this distribution require build `df711b913f09` and pass `--expected-build df711b913f09` to `runtime/install.py`, alongside the supplied `--source` and private destination arguments shown in [installation](../INSTALL.md). The installer compares the exact packaged file hashes and expected build before importing the runtime or changing state. Record the verified version/build/file hashes rather than inventing a release URL. Omit `--knowledge-review`, `--review-ui` and source-prefix options to preserve existing preferences, including absent keys. Changing only presentation must not introduce an explicit manual policy into a legacy configuration. Review the [policy distinctions](MEMORY-RUNTIME.md#setup-and-review-preferences) before explicitly choosing a knowledge mode; fresh defaults are not silently imposed on an upgrade. Do not waive a mismatch; obtain the matching package or explicitly review a newer distribution with updated pins.

Create the new memory store alongside the old system. Index permitted history as source material without declaring every archived assertion trusted. Import active commitments, open loops and decisions with original evidence and unresolved ownership/meaning preserved. Relocate existing AI output only when ownership is proven and links remain valid; import markers alone do not prove the absence of later human edits.

Install selected skills and `Memory Protocol.md`, merging instructions against the local baseline. Record which pages are managed and when authority will change. Keep originals byte-identical. Copying template files must not enable automatic learned overlays or new external-action authority.

## Verify And Cut Over

Use an independent copied store to rebuild SQLite from Markdown. Compare current records, revisions, provenance, review decisions and historical answers. Verify duplicate application, stale proposals, interrupted publication and incomplete sync. Run the [behavior cases](../examples/memory-evaluation-cases.json), separating deterministic integrity checks from semantic judgment.

Reconcile new source changes. Stop superseded writers and pause old conflicting jobs, then activate the selected writer and the approved jobs. Confirm the actual job registry and runtime paths. An earlier scheduled start is not an intake-completion signal. Record the first successful durable revision and verify the visible views before declaring cutover complete.

Update the private installation manifest and `Agent HQ/Glide Updates.md` with the installed release, file hashes, selected components, runtime/schema versions, cutover status and pending work. Do not commit or publish private manifests as package examples.

## Roll Back Or Transfer Machines

For a failed upgrade, stop new jobs and deactivate its writer first. Preserve the failed/new bundles for diagnosis and any post-cutover decisions. Restore the prior runtime and verified backup, reconcile intervening changes, then resume only the previous nonconflicting jobs. Never discard new decisions merely to make the old index match.

For a machine transfer, stop the old writer and its jobs before activating the new one. Verify synchronized bundle completeness, install the same compatible runtime, and rebuild locally. Do not use automatic failover or assume that a sleeping/unreachable host is stopped.

A resumed upgrade compares the recorded completed steps, installed hashes and current head. It must not duplicate jobs, replay accepted actions, or overwrite local edits. `inspect → plan → apply → verify → rollback` describes this procedure; it is not a promise of a standalone automatic migration command.

For a future version/build, follow the coordinated pin-update procedure in [compatibility](COMPATIBILITY.md), then repeat inspection, backup/recovery and cutover checks. A changed pin is not itself a migration or permission to overwrite an instance.

## Complete the execution host

Use [SETUP.md](SETUP.md) to configure the fixed MCP entrypoint, read-only reader, separately installed skills and native helpers. Inspect optional native helper changes before updating their admitted hashes. Review captures, recordings, imports and finance adapters separately from the core database; packaging a helper does not enable its permissions. Confirm the actual executable, interpreter and private paths in every active job.

Before enabling the new writer, run the matching [validation guide](VALIDATION.md), inspect effective review preferences, verify a real source/proposal/receipt and reconcile pending inputs. Compact job descriptors can be expanded with `glide_job_input_page`; archive registration alone is not reviewed knowledge. Preserve pending proposals and durable decisions across upgrades.

For source control or Obsidian transport, follow [STORAGE-AND-GIT.md](STORAGE-AND-GIT.md). Keep the live local index out of commits and ordinary synchronization; `.gitignore` is not a removal or cleanup operation for already tracked data.

## Optional project-progress output

For an owner who wants daily unique project notes, follow [the Obsidian-only companion procedure](DAILY-NOTES.md). Inspect older progress-note jobs and examples before selecting scope. This additive upgrade keeps the shared runtime pin and schema unchanged. Install code outside the vault, preserve existing MCP permissions and local customizations, obtain category permission, and pause duplicate exporters before appending the optional step to successful project intake. A repository update alone does not enable an existing instance.
