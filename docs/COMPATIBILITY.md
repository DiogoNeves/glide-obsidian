# Compatibility

The package's `compatibility.json` pins the optional shared runtime and documents the storage role. Runtime 0.1.0 requires Python 3.11 or later, SQLite FTS5 and POSIX file locking. macOS is the validated execution platform; the protected runner and Apple adapters are macOS-only, and native Windows is unsupported. See [setup](SETUP.md) for platform and dependency details. The source implementation and its actual `--help`/verification output define the supported format; do not change a format-version field by hand to force acceptance.

The general Glide repository owns `runtime/glide_memory/`. The Obsidian repository consumes the same version from a supplied matching checkout or release archive. There is no assumed unreleased download endpoint and no separately maintained Obsidian database implementation.

Legacy Markdown-only installations remain usable and are not automatically migrated. Schema changes require an explicit compatible migration, backup/restore test and interrupted-upgrade recovery. Unknown/newer formats are not safe to rewrite with an older runtime.

The install manifest is private per instance. Record package/runtime version, runtime artifact hash, baseline hashes for installed managed files, selected components, installed schema format and migration/cutover state. Local path, account, connector and writer configuration stays local. See the intentionally incomplete [example manifest](../examples/install-manifest.example.json); populate measured hashes during installation.

CLI capabilities are not equivalent to harness capabilities. A scheduler, source-reading boundary, model choice and interactive submission bridge must each be configured and verified separately. The initial adapters do not establish tested Hermes support or cross-machine execution.

Automatic learned overlays in runtime 0.1.0 support only `retrieval_aliases` and `context_priority`. Other procedural, routing or presentation lessons can be recorded for human review but are not automatically activated by this runtime.

Bundle readers preserve the recorded format version and its rendering contract. A new renderer must retain the older reader/rendering behavior needed to validate historical bundles; changing current formatting must not retroactively invalidate history. Pin a local build by its measured artifact/file hashes as well as its version label.

## Shared Content Pin

Both distributions require runtime **0.1.0, build `df711b913f09`**. `optional_memory_runtime.build` and `expected_build_required` in each `compatibility.json` are the consuming adapter contract. `package_manifest` resolves within the owner repository, Glide; its `runtime/package-manifest.json` records the same build and the exact runtime/helper/template file hashes. The installer must receive `--expected-build df711b913f09`; it rejects a differing build or inconsistent supplied package manifest before loading runtime code. These checks identify compatible content; they are not a substitute for obtaining the package from a trusted source.

For a future runtime revision, validate the changed implementation and preserve supported historical formats first. Regenerate the owner package manifest from the actual `.py` and `.html` files under `runtime/glide_memory/`, using the installer's `runtime_manifest` and build calculation (SHA-256 of `json.dumps(files, sort_keys=True)`, first 12 hex characters). Update runtime version metadata when releasing a new version, then update both consuming `compatibility.json` files, their example install manifests and documented `--expected-build` invocations together. Verify the two version/build pins match the owner manifest and exercise rejection of tampered or wrong-build packages. Do not edit a manifest merely to accept unexplained file differences or reuse an old build identifier for changed content. Keep the preceding content-pinned package for rollback.

The runtime package includes core storage/MCP code, its HTML review asset and reusable native helper source. Private configurations, credentials, model binaries, recordings and the live database are not distribution files. Review preference flags are independent of the shared Markdown format; upgrades preserve omitted local preferences.

For the Obsidian distribution, `optional_memory_runtime.runtime_git_ref` identifies the exact full commit SHA in the owner repository. Publish the verified owner commit before a consumer CI/release depends on fetching it. The content pin still validates runtime bytes; a Git ref and a content build serve different checks. Local paired checkouts can be validated before either is pushed.
