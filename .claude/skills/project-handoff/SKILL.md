---
name: project-handoff
description: "Create or update a durable, evidence-bounded project handoff at a selected repository path for a fresh session, machine, or reinstall. Use only after explicit /project-handoff invocation; preserve useful history, redact sensitive data, and never invent workspace state."
---

# Project Handoff

Use this skill for long-lived project context that a future operator can safely resume. For a single active-task artifact, use `/claude-context-handoff` instead.

## Resolve the destination

Run only after explicit `/project-handoff` invocation. Determine the target in this order:

1. Use the path explicitly named by the user.
2. Follow a handoff path named in applicable repository instructions.
3. Reuse an existing `mds/Claude Handoff.md` only when that legacy convention already exists.
4. Otherwise create `.claude/project-handoff.md` as the repo-local default.

Read an existing target before changing it. Do not create an arbitrary `mds/` directory or replace a useful handoff. Preserve history by appending a dated update; consolidate or delete prior entries only when the user explicitly asks.

## Evidence-first workflow

1. Read applicable `CLAUDE.md` instructions and determine the active project/topic. Ask one focused question only when scope or destination is materially unclear.
2. Inspect only durable, task-relevant sources: existing handoffs, project guidance, selected code or manifests, and known validation records. Read `mds/Clear Context.md` only if it exists and is relevant; it is not a universal source of truth.
3. Separate repository evidence, user statements, and assumptions. Record workspace or branch state only when it was safely verified during this task; do not run version-control commands merely to fill a handoff.
4. Redact secrets, credentials, private keys, tokens, connection strings, account identifiers, PHI, raw production data, raw transcripts, and sensitive logs.
5. Write a new snapshot or append an update using [the handoff template](references/handoff_template.md). For a new file, use the template before its divider; for an existing file, append only the dated update section. Keep paths repository-relative and commands/results short and factual.
6. Re-read the new section and report the path, primary sources, and material unknowns. Do not edit code, configuration, deployment files, schemas, or CI/CD as part of the handoff.

## Quality bar

- State only durable context: goal, verified work, important decisions, contracts, verification, risks, approval boundaries, and exact next steps.
- Mark each uncertain item as `Unverified / assumption`; never make an unknown look confirmed.
- Prefer one current, actionable snapshot over a conversation transcript or detailed shell log.
- Mention a fresh-agent next prompt that names the handoff path and tells the agent not to assume additional context.

The handoff itself is the output. In the final response, state whether it was created or updated, its path, and the important unknown if one remains.
