---
name: plan-it
description: "Create or revise an evidence-backed implementation plan for a repository task. Use only after explicit $plan-it or slash invocation; remain read-only during discovery, separate facts from assumptions, and save a reusable plan only when appropriate."
---

# Plan It

Use this skill to turn a scoped repository request into a plan another agent can safely implement. Planning is not implementation: do not modify application code or configuration while using this skill.

## Modes and artifact handling

Run only after explicit `$plan-it` invocation, or its supported slash form. Choose the requested mode:

- **New reusable plan (default):** save a new artifact under `.codex/artifacts/plan-it/`.
- **Revise a named plan:** update only the exact path named by the user.
- **Inline only:** return the plan in chat and create no artifact.

For a new artifact, use `YYYY-MM-DD_HHmm_<topic>.md`. Never overwrite an existing artifact; append `-2`, `-3`, and so on if needed. Do not select or overwrite a plan merely because it is newest. If the user asks to revise “the latest” and more than one candidate is plausible, list the candidates and ask them to choose.

## Workflow

1. Read applicable `AGENTS.md` instructions and confirm the requested outcome, constraints, and definition of done. Ask one focused question if an answer would materially change scope or design.
2. Perform only safe, read-only discovery. Use repository-prescribed inspection tools where available. Do not run tests, builds, installs, deployments, credential operations, or live service actions while planning.
3. Separate verified facts from assumptions. Cite the relevant file paths, symbols, or configuration evidence for each likely file change; do not invent files or APIs.
4. Read [the plan template](references/plan_template.md) and produce atomic, ordered implementation steps with a practical verification strategy, risks, approvals, and open questions.
5. Save the artifact only in new-plan or named-revision mode, then report its path and the important unresolved decision. In inline-only mode, state that no file was written.

## Planning standard

- Keep scope and out-of-scope work explicit.
- Include only implementation steps supported by evidence or clearly labeled assumptions.
- Make verification testable: specify the relevant automated checks, manual checks, or reasons a check needs later approval.
- Identify data, security, migration, compatibility, or deployment risks early.
- Do not invoke `$execute`, `$plan-diff`, or any other skill automatically. Offer an explicit next action only after the plan is complete.

Finish with a concise summary of the goal, artifact path or inline status, and the next decision or approval needed.
