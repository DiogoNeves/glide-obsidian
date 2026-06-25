---
name: glide-check-for-updates
description: Check the upstream Glide repository for new releases and migration notes. Use for weekly update schedules, release checks, or safely updating an installed Glide workspace while preserving user instructions and local customizations.
---

# Glide Check For Updates

## Load

- `Agent HQ/AGENTS.md`
- `Agent HQ/Glide Updates.md`
- `Agent HQ/Automation Registry.md`
- `Agent HQ/Skills Index.md`
- `Agent HQ/Harness Design Principles.md`
- Installed Glide skills, checklists, and automation notes when comparing changes

## Process

1. Read `Agent HQ/Glide Updates.md` for the upstream repo URL and last seen release.
2. Check upstream releases and compare the latest release with the last seen release.
3. If there is no new release, update the last checked date when useful and stop quietly.
4. Read release notes and migration instructions for every unseen release.
5. Build a small migration plan: new files, changed files, behavior changes, local conflicts, and approval-needed items.
6. Apply only updates that are clearly compatible with local instructions and user-provided preferences.
7. Ask before overwriting local customizations, changing behavior, enabling automations, deleting data, or applying anything that conflicts with user instructions.
8. Update `Agent HQ/Glide Updates.md` with the latest seen release, applied changes, pending approvals, and last checked date.
9. If the workspace uses git and the root instructions ask for it, commit successful update changes with a brief message.

## Output

- Keep scheduled runs quiet when nothing changed.
- When a new release exists, give a concise update plan or approval request.
- Record durable update state in `Agent HQ/Glide Updates.md`.
