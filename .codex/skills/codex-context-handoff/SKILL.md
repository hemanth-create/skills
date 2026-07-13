---
name: codex-context-handoff
description: Create a fact-bounded Markdown handoff so a fresh Codex task can continue a repository workflow. Use only when the user explicitly invokes @codex-context-handoff or /codex-context-handoff to preserve confirmed state, decisions, validation, and exact next steps; do not use for a generic summary.
---

# Codex Context Handoff

Create one concise handoff that lets a fresh agent continue the active task without inventing unseen context.

## Inputs and boundaries

Run only after an explicit invocation. Accept an optional topic or an existing handoff path to update. Use the visible conversation and files actually read during this task as the source of truth; never claim to preserve hidden reasoning, unread files, compacted context, or private model state.

Read applicable repository instructions first. If a repo-local helper guide exists, follow it; otherwise use normal safe file-reading tools. Read no unrelated repository content just to make the handoff look complete.

## Workflow

1. Determine the active workspace root and the topic. Ask one concise question if the topic is unclear.
2. If the user named an existing handoff, read it first and preserve useful history. Otherwise prepare a new handoff.
3. Record only confirmed facts. Label inference, assumptions, and unverified work explicitly.
4. Use [references/handoff_template.md](references/handoff_template.md). Include workspace state only when it was safely verified during the task.
5. Write the handoff to `.codex/artifacts/codex-context-handoff/YYYY-MM-DD_HHmm_<topic>.md`. If that name already exists, append `-2`, `-3`, and so on.
6. Update an existing handoff's `updated` field rather than overwriting its original `created` value.
7. Maintain an artifact index only when one already exists or the user asks for it. Do not change `AGENTS.md`, runtime code, deployment files, schemas, or CI/CD while creating a handoff.

## Required quality

- State the current goal, decisions, completed work, files read or changed, verification, open questions, approval boundaries, and exact next steps.
- Keep commands and validation results short and factual; do not paste sensitive logs or raw clinical content.
- Give the fresh agent a copyable next prompt that names this handoff file and tells it not to assume additional context.
- Redact secrets, tokens, credentials, account identifiers, PHI, raw transcripts, and private data.

## Output

The handoff file is the artifact. In the final response, state its path and one sentence about what a fresh agent can safely continue. If the user asks for a summary without a file, answer normally instead of invoking this skill.
