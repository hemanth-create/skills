---
skill: sub-task
created: YYYY-MM-DD HH:mm TZ
task: <plan title>
status: execute-ready | draft-breakdown | needs-adjustment
source: <plan path>
---

# Sub-Tasks: <plan title>

## Source plan

- Path: `<path>`
- Goal: <one or two sentences>
- Readiness: <execute-ready or draft breakdown, with evidence>

## Plan items

| ID | Source | Change |
| --- | --- | --- |
| P1 | `<heading or line range>` | <explicit plan change> |

## Assumptions and open questions

- <assumption or `None.`>

## Sub-tasks

### ST-1: <short title>

- Status: `ready` | `blocked` | `draft`
- Goal: <one deliverable>
- Depends on: <ST IDs or `None`>
- Parallelizable: `yes` | `no` — <reason>
- Plan source: `P1`, `P2`
- Files:

  | Path | Evidence | Intended action |
  | --- | --- | --- |
  | `<path>` | <plan/source evidence> | CREATE / MODIFY / DELETE / UNKNOWN |

- Steps:
  1. <concrete action and expected behavior>
- Acceptance criteria: <observable result>
- Verification: <focused check or limitation>
- Risks and approvals: <approval gate, or `None identified from the plan.`>

## Traceability check

| Plan item | Covered by | Status | Notes |
| --- | --- | --- | --- |
| P1 | ST-1 | covered | <note> |

- Gaps: <plan item or `None.`>
- Extras: <sub-task not traceable to the plan or `None.`>
- Overlaps: <duplicated work or `None.`>
- Ordering: <dependency issue or `None.`>

## Verdict

`EXECUTE-READY` | `DRAFT BREAKDOWN` | `NEEDS ADJUSTMENT` — <one evidence-backed sentence>

## Suggested next action

<Explicit action only; do not run it automatically.>
