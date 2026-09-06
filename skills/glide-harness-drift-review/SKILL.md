---
name: glide-harness-drift-review
description: Review Glide operating files for drift against the protected harness design principles.
---

# Glide Harness Drift Review

## Load

- `Agent HQ/Harness Design Principles.md`
- `Agent HQ/Checklists/Harness Drift Review.md`
- `Agent HQ/Checklists/Eval Loop.md`
- Operational files listed in the checklist
- `Agent HQ/Evals/*.md` as read-only evidence

## Process

1. Treat `Agent HQ/Harness Design Principles.md` as read-only unless the user explicitly asks to edit that file.
2. Follow `Agent HQ/Checklists/Harness Drift Review.md`.
3. Review operational files for drift against the design principles.
4. Interpret read-only eval signal through `Agent HQ/Checklists/Eval Loop.md`.
5. Treat recurring facets, signal clusters, `Improve Next` notes, and `Partial` outcomes in evals as candidates for small instruction updates.
6. Add or update compact signal clusters before making eval-derived instruction changes.
7. Make only small, clear, non-behavioral corrections to editable operations files.
8. Reduce verbosity in newly edited skills, checklists, and rules when brevity does not reduce clarity or change behavior.
9. Check collection-candidate files for obvious stale or irrelevant items, following the checklist.
10. Ask the user to confirm before making changes that could alter future behavior or require judgment.
11. Do not edit personal memory files except for allowed stale-item cleanup in collection-candidate files.
12. If the best fix would require changing the design principles, behavior, or personal data, report the issue and ask for approval.

## Output

- Drift found or not found.
- Files changed.
- Verbosity reductions made.
- Collection candidates cleared or recommended for cleanup.
- Eval clusters created or updated.
- Behavior-changing recommendations requiring user approval.

For an explicitly enabled memory store, delegate integrity and eligible learned-overlay evaluation to `glide-integrity` using `Agent HQ/Memory Protocol.md`. This exception does not authorize core-instruction changes. Managed record changes use the runtime and preserve revision history.
