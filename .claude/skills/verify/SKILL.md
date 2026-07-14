---
name: verify
description: "Perform a bounded, skeptical, evidence-backed review of a named implementation, diff, plan, or artifact. Use only after explicit /verify invocation; return a scoped verdict and findings before any separately requested fix, and never imply unreviewed work is clean."
---

# Verify

Use this skill for an independent review before work is relied on. It is a focused validation pass, not a general summary, broad repository scan, or automatic fix workflow.

## Scope and evidence

Run only after explicit `/verify` invocation. Require a named target: files, a diff, plan, artifact, feature, or previous implementation summary. If “recent changes” has no safe, specific target, ask one focused question rather than scanning the repository or running version-control commands by default.

Read applicable `CLAUDE.md` instructions and the exact material under review. Use a named plan, acceptance criteria, handoff, or user request as the expected-behavior reference when available. Read nearby callers, tests, contracts, and configuration only when needed to assess a concrete risk.

## Review method

1. Trace relevant success, failure, empty, malformed, boundary, and external-state paths.
2. Compare behavior with the stated requirements, plan, or contract.
3. Check relevant validation, error handling, authorization, privacy, data integrity, compatibility, migration, deployment, and rollback risks.
4. Determine whether existing tests or a focused permitted check actually support the risky behavior. Do not run a check only to fill the report.
5. Report only material, evidence-backed findings. A finding needs a precise location or artifact section when possible, the realistic impact, and the smallest safe correction. Label incomplete evidence as `candidate` rather than overstating confidence.

Do not turn style preferences, speculative cleanup, or generic advice into findings. Use `/ponytail-review` for unnecessary complexity and `/multi-review` when two independent review lenses are needed.

Calibrate severity to realistic impact: `critical` for exploitable security, data loss, or release-blocking failure; `high` for likely user-visible or contract failure; `medium` for a credible constrained defect or missing protection; and `low` for a minor but real risk. A `candidate` is not a severity and must state what evidence would confirm it.

## Verdict and artifact

Return one scoped verdict:

- `NO MATERIAL FINDING IN REVIEWED SCOPE`
- `FINDINGS REQUIRE ACTION`
- `INSUFFICIENT CONTEXT`

When the target is readable, save the review under `.claude/artifacts/verify/YYYY-MM-DD_HHmm_<topic>.md` using [the verification record template](references/verification_record_template.md). Never overwrite an artifact; append `-2`, `-3`, and so on when needed. Do not create an artifact when the review target is unresolved.

## Fix mode

Review-only is the default. If the user explicitly asks to fix findings too, report findings first, then change only approved in-scope files. Ask before a dependency, deletion, rename, generated file, schema or data migration, deployment, credential, network, live-service action, or design-sensitive public-contract change. Re-read edited code and report any focused check after the fix.

## Response

Lead with findings, then state scope, checks run or not run, residual risk, verdict, and artifact path:

```markdown
## Findings
- [severity] `path:line` — problem, impact, evidence, and smallest safe correction.

## Verification
- Reviewed scope, checks run, and meaningful checks not run.

## Verdict
`NO MATERIAL FINDING IN REVIEWED SCOPE` | `FINDINGS REQUIRE ACTION` | `INSUFFICIENT CONTEXT`
```

Do not commit, push, open a pull request, or invoke another skill automatically.
