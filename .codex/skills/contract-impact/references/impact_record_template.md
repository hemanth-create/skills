---
skill: contract-impact
created: YYYY-MM-DD HH:mm TZ
task: <proposed change>
status: compatible | coordination-required | insufficient-context
source: <user request, plan, issue, or diff>
---

# Contract impact: <change>

## Proposed change

- <What changes and why.>

## Contract inventory

| Boundary | Canonical source | Producer / owner | Consumer / owner | Evidence or unknown |
| --- | --- | --- | --- | --- |
| API, event, schema, data, file, or config | `<path:symbol>` | <path or unknown> | <path or unknown> | <evidence> |

## Change classification

- Type: `additive-optional` | `additive-required` | `semantic` | `rename-removal` | `data-transform` | `operational-config`
- Missing/default behavior: <evidence or unknown>
- Compatibility concerns: <serialization, auth, ordering, tenancy, retention, or `None identified from reviewed evidence.`>

## Required coordination

| Area | Required action | Dependency / approval | Evidence |
| --- | --- | --- | --- |
| Producer, consumer, storage, docs, config, or tests | <action> | <gate or `None known`> | <source> |

## Rollout and rollback

- Safe order: <reasoned sequence>
- Compatibility window or translation: <need or `None identified from reviewed evidence.`>
- Rollback: <safe recovery condition or unknown>

## Verification

- <Contract, consumer, migration, or safe-environment check.>
- Not run: <important check and reason.>

## Unknowns and verdict

- <unknown dependency or `None identified from reviewed evidence.`>
- Verdict: `COMPATIBLE WITH COORDINATED CHANGE` | `VERSIONING OR MIGRATION REQUIRED` | `INSUFFICIENT CONTEXT`

## Suggested next action

<Explicit action only; do not run it automatically.>
