---
skill: verify
created: YYYY-MM-DD HH:mm TZ
task: <review target>
status: complete | findings | insufficient-context
source: <user request, plan, diff, or artifact>
---

# Verification record: <target>

## Scope and evidence

- Reviewed target: <paths, diff, plan, or artifact>
- Expected behavior reference: <source or `None supplied`>
- Files and sections read: <evidence>

## Findings

Use finding rows or the no-finding line below, not both.

- `[critical|high|medium|low|candidate]` `<path:line or artifact section>` — <problem, impact, evidence, and smallest safe correction.>
- `None identified in reviewed scope.`

## Checks and gaps

- Ran: <focused check and result, or `None`>
- Not run / missing: <important gap and reason>

## Open questions and residual risk

- <blocking question or residual risk, or `None identified from reviewed evidence.`>

## Verdict

`NO MATERIAL FINDING IN REVIEWED SCOPE` | `FINDINGS REQUIRE ACTION` | `INSUFFICIENT CONTEXT`

## Suggested next action

<Explicit action only; do not run it automatically.>
