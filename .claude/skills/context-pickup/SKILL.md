---
name: context-pickup
description: Resume safely from a user-named handoff, plan, or repository artifact. Use only when the user explicitly invokes @context-pickup or /context-pickup to read selected context, distinguish known facts from unknowns, and prepare for the next instruction; do not create an artifact or edit files by default.
---

# Context Pickup

Read selected saved context and prepare to continue without pretending to remember a prior chat.

## Inputs

Accept one of these forms:

- `@context-pickup <path-to-file>`
- `@context-pickup <path-to-folder>`
- `@context-pickup latest handoff`
- `@context-pickup latest <skill-name>`
- `@context-pickup search "<query>"`

Use `/context-pickup` only where slash-style invocation is supported. If a folder or search returns more than five plausible context files, list the best matches and ask the user to choose. Do not guess.

## Workflow

1. Read applicable repository instructions. If a repo-local helper guide exists, follow it; otherwise use normal safe file-listing and reading tools.
2. Resolve the source in this order: a user-supplied path, a named artifact type, then a narrow artifact search. For `latest handoff`, limit results to `.claude/artifacts/claude-context-handoff/`; for `latest <skill-name>`, limit results to `.claude/artifacts/<skill-name>/`. If that folder does not exist, say so rather than searching elsewhere.
3. Restrict discovery to the active workspace and known artifact folders. Do not search session logs, home directories, credential files, or unrelated repository content.
4. Read the selected file first. Read referenced files only when necessary to understand the current goal or a listed next step.
5. Summarize confirmed facts, decisions, work completed, unknowns, and next likely actions. Explain any confidence limitation from missing, stale, or incomplete context.
6. Stop after the pickup. Do not plan, edit, test, deploy, or invoke another skill until the user explicitly asks.

## Output

Return this in chat; do not create a pickup artifact unless the user explicitly asks to save one:

```markdown
## Context Picked Up

- Source: `<path or query>`
- Confidence: `<high | medium | low>` — `<brief evidence-based reason>`

## Files Read

- `<path>` — `<why it mattered>`

## Current Goal

<Goal, or "Not clear from the selected context.">

## Confirmed Context

- <Known fact.>

## Decisions Already Made

- <Decision, or "None found.">

## Unknowns or Open Questions

- <Question, assumption, or "None found.">

## Next Likely Actions

1. <Likely next action.>
2. <Likely next action.>

## Ready State

Ready for `<the user's next instruction>`.
```

Use high confidence only for a recent, explicit source with concrete next steps. Never claim to know hidden reasoning, unread files, or unstated history.
