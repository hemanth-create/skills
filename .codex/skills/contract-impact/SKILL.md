---
name: contract-impact
description: "Map the compatibility impact of a named proposed change to an API, event, schema, data model, file format, or configuration contract. Use only after explicit $contract-impact or slash invocation; identify producers, consumers, versioning, migration, and rollout needs without editing or calling live services."
---

# Contract Impact

Use this skill before implementing a cross-boundary change. It answers what changes together, what remains compatible, and what must be verified or approved. It does not design the whole system, edit contracts, run migrations, or deploy.

## Inputs and boundaries

Run only after explicit `$contract-impact` invocation, or its supported slash form. Require:

- a named proposed change, plan section, diff, or issue; and
- the affected contract or boundary when known.

Ask one focused question if the change or boundary is materially unclear. Read applicable `AGENTS.md` instructions and inspect only relevant contract sources and likely producer/consumer paths. Do not treat a failed search as proof that no consumer exists; label incomplete discovery as unknown.

Use `$architecture-review` for the broader design decision, `$plan-it` for the implementation plan, and `$execute` only after the change is approved.

## Workflow

1. Identify the canonical contract source: API specification, type/schema, migration, event definition, file format, configuration declaration, or explicit requirement.
2. Map direct evidence for producers, transforms or storage, consumers, tests, documentation, and environment/configuration references. Cite paths, symbols, or sections.
3. Classify the proposed change: additive optional field, additive required field, semantic change, rename/removal, data transformation, or operational/configuration change. State defaults, null or missing behavior, ordering, authorization or tenancy, serialization, and retention concerns when relevant.
4. Decide compatibility for old and new producers/consumers. Identify required versioning, translation, backfill, dual-read/write, feature-flag, or coordination work only when evidence supports it.
5. Describe a safe rollout and rollback order with its reasoning; do not assume a fixed producer-first or consumer-first order. Identify approvals, owners, and unknown dependencies rather than inventing them.
6. Name focused verification: contract fixtures, compatibility tests, migration rehearsal, consumer tests, and safe-environment checks. Do not run them unless repository policy and the user allow it.

## Verdict

Return one decision:

- `COMPATIBLE WITH COORDINATED CHANGE`
- `VERSIONING OR MIGRATION REQUIRED`
- `INSUFFICIENT CONTEXT`

```markdown
## Contract impact
- Change: <proposed change>
- Canonical contract: `path:symbol` or `Unknown`

## Producer and consumer map
- Producer: evidence and required change.
- Consumer: evidence and required change.
- Unknown: gaps that could affect the decision.

## Compatibility and rollout
- Classification, compatibility result, safe rollout/rollback order, and approvals.

## Verification
- Required focused checks and checks not run.

## Verdict
`COMPATIBLE WITH COORDINATED CHANGE` | `VERSIONING OR MIGRATION REQUIRED` | `INSUFFICIENT CONTEXT`
```

Save an impact record only when the user asks or repository instructions require it. Use `.codex/artifacts/contract-impact/YYYY-MM-DD_HHmm_<topic>.md` and [the impact-record template](references/impact_record_template.md); never overwrite an existing record.

## Safety

Do not edit source, schemas, migrations, configuration, or existing project documentation; run version-control, build, test, install, deployment, database, network, or live-service commands; or create an impact record without the stated authority. Redact secrets, credentials, account identifiers, PHI, raw production data, and sensitive logs.
