---
name: sub-task
description: "Decompose a named plan into traceable, independently executable work units. Use only after explicit /sub-task invocation with a readable plan path; do not re-plan or implement, and write an artifact only after the plan can be verified."
---

# Sub Task

Use this skill to turn one plan into an ordered implementation backlog with a self-check against the plan. It does not revise the plan or execute any work.

## Input and readiness

Run only after explicit `/sub-task` invocation. Require a readable plan path. If it is missing, unreadable, or outside the available workspace, ask for a valid path and do not create an artifact.

Treat the named plan as the source of truth. Determine whether it is approved for execution:

- **Execute-ready:** the user or plan explicitly approves it.
- **Draft breakdown:** approval is absent or unclear; the breakdown may inform review but must not be handed to `/execute` yet.

Read the full named plan before decomposing it. If it is truncated, internally inconsistent, or references material needed to understand scope but unavailable, state the limitation and use `NEEDS ADJUSTMENT` rather than inventing work. Read applicable `CLAUDE.md` instructions and only the referenced files needed to establish a task's scope or dependency. Do not infer unmentioned work from conversation history.

## Workflow

1. Extract the plan goal and assign each explicit change a source identifier such as `P1`, citing its heading, path, or line range.
2. Separate stated facts from assumptions and open questions. Preserve plan risks and approval gates rather than hiding them inside a task.
3. Group changes into coherent, independently verifiable sub-tasks. Avoid splitting a tightly coupled behavior unless an explicit interface or checkpoint makes the pieces independently safe.
4. For each sub-task, specify goal, dependencies, parallelism, file evidence, implementation steps, acceptance criteria, focused verification, risks or approvals, and the exact plan source IDs it covers.
5. Build a traceability check: every `P` item must map to a sub-task or an explicit gap. Flag extras, overlaps, dependencies scheduled too late, and assumptions that prevent execution.
6. Save the valid breakdown under `.claude/artifacts/sub-task/YYYY-MM-DD_HHmm_<topic>.md`, using [the sub-task template](references/subtask_template.md). Never overwrite an artifact; append `-2`, `-3`, and so on when needed.

Use `EXECUTE-READY` only when the source plan is approved, every plan item is covered, no unapproved extra scope remains, and no unresolved dependency or approval gate blocks the first selected sub-task.

## Boundaries

- Do not edit code, modify the plan, run git, install packages, test, deploy, or perform live-service actions.
- Do not add setup, refactors, dependencies, migrations, or contract changes that the plan does not support. Record them as gaps or approval gates instead.
- Do not invoke `/execute`, `/plan-it`, `/plan-diff`, or `/verify` automatically.
- Redact secrets, credentials, tokens, account IDs, PHI, raw transcripts, and sensitive logs from the artifact.

## Final response

State the source plan, number of sub-tasks, readiness verdict, gaps or approval gates, and artifact path. Recommend `/execute` only when the result is execute-ready and the user explicitly chooses a sub-task.
