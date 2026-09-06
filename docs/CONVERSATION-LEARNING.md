# Conversation continuity and gradual improvement

Glide should remember useful things said in conversation and let the owner steer it without redesigning the harness. The [canonical procedure](../templates/Agent%20HQ/Checklists/Conversation%20Learning.md) separates immediate, scoped user guidance from inferred improvements. The protected principles stay stable.

Install these three files as one optional unit with versioned memory: `skills/glide-conversation-learning/SKILL.md` into the execution host's selected skill directory, plus `templates/Agent HQ/Checklists/Conversation Learning.md` and `Conversation Recovery.md` into `Agent HQ/Checklists/`. Link the procedure from the instance's active Agent HQ instructions and daily/dream/harness review. Reuse existing schedules and checkpoint transactions, including the protocol's separate knowledge-review rules. The review inbox and `conversation-coverage` are managed Markdown records; no new database or schema is needed.

Ask which accounts/devices and available history sources are in scope at initial setup. Already authorized personal conversation recovery needs no repeated permission. Local Codex history and reachable ChatGPT tasks are distinct sources: an unavailable connector is a visible gap, not permission to bypass app rules or import a separate work account.

The app's `list_threads`/`read_thread` tools are the primary history interface when available. Supplement their inventory with `tools/conversation_inventory.py`; it reads only local file metadata and the session header. Install that Python file under local application data outside the vault, record its SHA-256 and source commit in the private installation manifest, and use the recorded executable path. Do not copy Python into synced skills or edit the content-pinned shared runtime.

Record `conversation-intake.json` beside the private instance configuration, outside synchronization. This is declarative setup state read by the agent, not a new runtime schema or sandbox. Include `enabled`, explicitly selected `source_scope` and `excluded_scope`, `bootstrap_hours` (48), `max_tasks_per_pass` (5), `max_pages_per_task` (2), `coverage_record` (`conversation-coverage`), `inbox_record` (`conversation-inbox`), and `helper` with `python`, installed `path`, explicitly selected `codex_home`, `sha256`, `repository` and complete `source_commit`. Retain the setup date and authority/source reference. Disabled history recovery still permits already authorized live conversational capture.

Verify the installed helper with `--help`, then inspect one bounded metadata page. Substitute the recorded interpreter/path and the intended timezone-qualified starting time:

```sh
python3 -B '/absolute/local-app-data/Glide/tools/conversation_inventory.py' --help
python3 -B '/absolute/local-app-data/Glide/tools/conversation_inventory.py' --codex-home '/absolute/private/codex-history' --since '2026-09-05T00:00:00+01:00' --limit 20
```

The inventory's output is discovery information only. File modification does not prove a new user message, and a metadata page does not establish reviewed coverage. Follow stable message IDs and exact passages through the canonical procedure. If app tools are unavailable, selected local logs remain readable within the existing source permissions; report remote chat coverage as unavailable.

For upgrades, preserve local customizations, back up the affected instructions and jobs, install the helper alongside the existing packages, and verify existing source boundaries. Run its synthetic tests and the [behavioral scenarios](../examples/conversation-learning-cases.json). Record what was actually checked. This does not test long-term usefulness or guarantee every future conversation will be captured.

To roll back a workflow change, restore the recorded prior instructions and job prompt; preserve user decisions and capture receipts. Clear direct user guidance can be corrected or withdrawn through conversation. Inferred procedural candidates remain inactive until reviewed. Automatic activation is still limited to the shared runtime's supported typed retrieval/context overlays and its existing evaluation/rollback policy.

History-specific pagination and coverage details live in [Conversation Recovery](../templates/Agent%20HQ/Checklists/Conversation%20Recovery.md), loaded only for recovery work.
