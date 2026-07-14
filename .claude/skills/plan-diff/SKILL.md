---
name: plan-diff
description: "Compare a user-provided external plan with a selected local baseline plan. Use only after explicit /plan-diff invocation; verify scope, risk, approvals, and validation before returning an evidence-backed verdict without writing files."
---

# Plan Diff

Use this skill to decide whether an external agent's plan still matches the intended local plan. It compares plans; it does not authorize implementation or rewrite either plan unless the user asks.

## Resolve the two inputs

Run only after explicit `/plan-diff` invocation. Need both:

- an **external plan**, pasted in the conversation or supplied at a named path; and
- a **baseline**, preferably a user-named plan path.

Resolve the baseline in this order:

1. Use the explicit path the user names.
2. Use a clearly identified original plan in the current request.
3. Use the newest `.claude/artifacts/plan-it/` artifact only when the user explicitly asks for the latest one.

Do not guess from a merely recent artifact. If several plausible baselines remain, list up to three paths and ask the user to choose. If the external plan is missing, incomplete, or cannot be read, ask for it rather than pretending to compare it.

Read applicable `CLAUDE.md` instructions and verify that both plans refer to the same task and current repository state. Treat an unknown revision, stale file list, or missing acceptance criteria as a comparison risk.

## Compare

Check the external plan against the baseline for:

1. goal, user constraints, and explicit decisions;
2. in-scope and out-of-scope work;
3. dependency order, affected files, and assumptions;
4. acceptance criteria, verification, and rollback or error handling where relevant;
5. risks, required approvals, security or data boundaries; and
6. unsupported additions, missing steps, or changes that need a new decision.

Use evidence from the selected plans and repository instructions. Do not write files, create an artifact, run implementation checks, or perform installs, builds, deployments, or live operations.

## Verdict

Return exactly one verdict:

- `ACCEPT` — the external plan materially matches the selected baseline and is actionable.
- `NEEDS CHANGES` — it conflicts with, omits, or expands the baseline in a material way.
- `INSUFFICIENT CONTEXT` — either plan, its currency, or necessary acceptance context is missing.

```markdown
## Comparison
- Baseline: `path` (why it was selected)
- External plan: pasted response or `path`

## Aligns
- Evidence-backed matches.

## Required changes
- Only material corrections; use `None` for `ACCEPT`.

## Verdict
`ACCEPT` | `NEEDS CHANGES` | `INSUFFICIENT CONTEXT`

## Recommended next action
- One concise, non-implementing next step.
```
