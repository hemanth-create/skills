---
name: multi-review
description: "Reconcile two independent read-only review lenses for a named implementation, plan, or subtask. Use only after explicit $multi-review or slash invocation; produce one evidence-backed verdict without editing or broad exploration."
---

# Multi Review

Use this skill to decide whether a named target is ready, needs fixes, or lacks enough evidence. It reviews only; it never implements fixes.

## Inputs and boundaries

Run only after explicit `$multi-review` invocation, or its supported slash form. Require:

- a named target (files, diff, plan, task, or prior-agent output); and
- the expected behavior, approved plan, or acceptance criteria.

If either is missing, ask one focused question before reviewing. Read applicable `AGENTS.md` instructions and preserve unrelated working-tree changes.

Use at most two independent, read-only child reviewers when the environment and repository policy permit it. A child may inspect the target, but must not edit files, create artifacts, run side-effecting commands, spawn agents, or invoke this skill. If children are unavailable or disallowed, perform the same two lenses locally and say so.

## Workflow

1. Define two non-overlapping lenses:
   - **Correctness:** request and plan compliance, contracts, error paths, security, scope, test coverage, and verification gaps.
   - **Maintainability:** clarity, local conventions, unnecessary complexity, duplication, and whether a small rewrite is justified.
2. Give each reviewer its lens, the exact target, and an evidence requirement: cite `path:line` when possible and return `clean`, `findings`, or `insufficient context`.
3. Inspect only enough additional context to resolve material or disputed claims. Run a focused check only when repository policy and the user's approval allow it; never run a command merely to populate the report.
4. Reconcile by evidence rather than vote count. Deduplicate findings, verify disagreements locally when possible, and label unresolved claims as uncertain.
5. Do not edit, invoke other skills, or create a review artifact unless the user separately asks.

## Response format

Return findings first, ordered by impact:

```markdown
## Findings
- [severity] `path:line` — issue, evidence, and the smallest required correction.

## Verification
- Checks run, their result, and important checks not run.

## Reconciliation
- Lenses run: child reviewers or local review.
- Agreement, disagreement, and how evidence resolved it.

## Verdict
`CLEAN` | `FIX BEFORE PROCEEDING` | `INSUFFICIENT CONTEXT`
```

Use `CLEAN` only when the reviewed scope has no material finding. If fixes are needed, describe them precisely without making them.
