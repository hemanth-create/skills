---
skill: claude-context-handoff
created: `<YYYY-MM-DD HH:MM timezone>`
updated: `<YYYY-MM-DD HH:MM timezone or same as created>`
task: `<human-readable topic>`
status: `<current | blocked | complete>`
source: visible conversation and files actually read
---

# Claude Context Handoff

## Current Goal

- `<What this task is trying to accomplish.>`

## Workspace State

- Root: `<absolute or repo-relative root>`
- Branch and commit: `<only when verified>`
- Working tree: `<clean | changed | unknown>`

## Confirmed Context

- `<High-signal confirmed fact.>`

## Decisions Made

- `<Decision and rationale.>`

## Files Read or Changed

- `<path>` — `<why it matters>`

## Work Completed

- `<Concrete completed action.>`

## Verification

- `<command or check>` — `<passed | failed | not run>` — `<important result or limitation>`

## Approval Boundaries

- `<What the next agent may safely do, and what still needs user approval.>`

## Open Questions

- `<Question or None known.>`

## Exact Next Steps

1. `<Next action.>`
2. `<Next action.>`

## Suggested Next Prompt

Read `CLAUDE.md` if present, then read `<this handoff path>`. Continue only from the confirmed context and Exact Next Steps; do not assume additional session history.

## Caveats

- This handoff preserves only visible conversation context and files actually read.
- Hidden reasoning, compacted context, private model state, and unread files are not preserved.
- Sensitive content is redacted or summarized.
