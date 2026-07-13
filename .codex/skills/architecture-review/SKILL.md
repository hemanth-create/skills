---
name: architecture-review
description: Review an existing repository plan, design, deployment proposal, or production-readiness decision before implementation. Use only when the user explicitly invokes @architecture-review or /architecture-review; do not use for source-code or diff review, or for drafting a new plan from scratch.
---

# Architecture Review

Review whether a proposed design is sound enough to implement. Produce an evidence-based decision, not a replacement implementation plan.

## Scope and inputs

Require a review target: a plan, design document, handoff, deployment proposal, architecture document, or clearly stated decision. If the target or decision is unclear, ask one concise question before reviewing.

Read applicable repository instructions first. If `.helpers/README.md` exists, follow it; otherwise use normal repository tools. Inspect only the target and the smallest set of code, configuration, tests, and documentation needed to validate its important claims.

## Review workflow

1. State the decision being reviewed, its intended outcome, and the review boundary.
2. Map the primary flow: entry point, trust boundaries, processing, storage, downstream consumers, and operational owner.
3. Cross-check material claims against current source. Distinguish confirmed facts, inferences, assumptions, and items that could not be verified.
4. Assess the risks that apply to this proposal:
   - contracts, schemas, and compatibility;
   - ordering, retries, idempotency, and partial failure;
   - data lifecycle, migration, tenancy, privacy, and deletion;
   - deployment ownership, permissions, environment/region assumptions, rollback, and observability;
   - maintainability, coupling, and missing verification.
5. For a clinical, PHI, LLM, or form-filling system, also read [references/clinical-ai-review.md](references/clinical-ai-review.md).
6. Give a decision-oriented review. Do not edit the plan or implementation unless the user explicitly asks for a revision after the review.

## Output

Return the review in chat by default:

```markdown
## Verdict

<Usable as-is | Usable with changes | Blocked | Not enough evidence> — one sentence.

## Blockers

- [high] Evidence: `path:line` | `Unverified` | `Not found` — issue, impact, and required change.

## Architecture Risks

- Risk, evidence, and practical mitigation.

## Confirmed Facts

- `path:line` — fact verified from source.

## Assumptions or Unknowns

- What remains unverified and how to resolve it.

## Recommended Next Steps

1. Concrete action.
2. Concrete action.
```

Use `critical` only for likely security/privacy exposure, unsafe deployment, data loss, or production breakage; use `high` for a gap that should block implementation. Say directly when there are no blockers, while preserving residual risks.

## Artifacts and boundaries

Create a Markdown artifact only when the user asks to save the review or repository instructions require it. Save it under `.codex/artifacts/architecture-review/` with a sortable `YYYY-MM-DD_HHmm_<topic>.md` name, include the evidence and files read, and mention its path in the final response.

Recommend a broader planning workflow when the review exposes substantial unresolved design work. Recommend a targeted code-review workflow for implementation or diff-level concerns. Do not turn this review into a broad repository audit without an explicit request.
