---
skill: test-writer
created: YYYY-MM-DD HH:mm TZ
task: <target or feature>
status: planned | audited | written | blocked
source: <user request or accepted plan>
---

# Test record: <target>

## Scope and evidence

- Mode: `plan` | `audit` | `write`
- Target: `<path or symbol>`
- Files read: <source, tests, config>
- Test framework and conventions: <observed evidence>

## Test cases

| Test | Behavior protected | Inputs or setup | Expected observable result |
| --- | --- | --- | --- |
| `test_<name>` | <behavior> | <fixture/inputs> | <assertion> |

## Mocks and fixtures

- `<boundary or fixture>` — <why it is used and scope.>

## Changes

- `<test path>` — <created, updated, or `None in plan/audit mode.`>

## Execution and coverage evidence

- Ran: <command and result, or `Not run` with reason.>
- Covered scenarios: <behavioral categories covered.>
- Known gaps: <uncovered risk and reason, or `None identified from reviewed evidence.`>

## Suggested next action

<Explicit action only; do not run it automatically.>
