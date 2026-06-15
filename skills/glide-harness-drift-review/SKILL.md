---
name: glide-harness-drift-review
description: Review Glide operating files for drift against the protected harness design principles.
---

# Glide Harness Drift Review

## Load

- `Agent HQ/Harness Design Principles.md`
- `Agent HQ/Checklists/Harness Drift Review.md`
- Operational files listed in the checklist

## Process

1. Treat `Agent HQ/Harness Design Principles.md` as read-only unless the user explicitly asks to edit that file.
2. Follow `Agent HQ/Checklists/Harness Drift Review.md`.
3. Review operational files for drift against the design principles.
4. Make only small, clear, non-behavioral corrections to editable operations files.
5. Reduce verbosity in newly edited skills, checklists, and rules when brevity does not reduce clarity or change behavior.
6. Check collection-candidate files for obvious stale or irrelevant items, following the checklist.
7. Ask the user to confirm before making changes that could alter future behavior or require judgment.
8. Do not edit personal memory files except for allowed stale-item cleanup in collection-candidate files.
9. If the best fix would require changing the design principles, behavior, or personal data, report the issue and ask for approval.

## Output

- Drift found or not found.
- Files changed.
- Verbosity reductions made.
- Collection candidates cleared or recommended for cleanup.
- Behavior-changing recommendations requiring user approval.
