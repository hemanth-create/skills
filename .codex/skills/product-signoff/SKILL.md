---
name: product-signoff
description: "Create an evidence-backed, multi-file product sign-off bundle for a named product, feature, or release. Use only after explicit $product-signoff or slash invocation; inspect accessible context and supplied chat or handoff material, distinguish evidence from gaps, and never claim an unavailable chat or human approval was reviewed."
---

# Product Sign-off

Create a decision-ready sign-off bundle from evidence actually accessible in the current task. This is a recommendation and documentation workflow, not a human approval, deployment, merge, compliance attestation, or release action.

## Invocation and output mode

Run only after explicit `$product-signoff` invocation, or its supported slash form. Require a named product, feature, release, or sign-off decision. Ask one focused question if the target or decision owner is materially unclear.

Choose the requested mode:

- **Full sign-off bundle (default):** create a directory under `.codex/artifacts/product-signoff/YYYY-MM-DD_HHmm_<topic>/`.
- **Revise a named bundle:** update only the exact directory or file named by the user.
- **Inline assessment:** return the recommendation in chat and create no files.

For a new bundle, never overwrite an existing directory; append `-2`, `-3`, and so on. A direct `$product-signoff` request authorizes writing this documentation bundle, but not source, configuration, test, deployment, or release changes.

## Evidence boundaries

Read applicable `AGENTS.md` instructions, then inspect only sources relevant to the decision. Prefer evidence in this order:

1. named requirements, product context, acceptance criteria, decisions, and release documentation;
2. relevant code, configuration, contracts, diffs, tests, and existing validation records;
3. named plans, handoffs, issues, PRs, and review artifacts;
4. the current conversation and user-provided statements;
5. an explicitly supplied chat export, transcript, or handoff; and
6. task transcript or local memories only when the current environment actually exposes them and the user permits their use.

When the user has not named sources, first check only relevant existing context files such as `PRODUCT_CONTEXT.md`, `PROJECT_CONTEXT.md`, `DECISIONS.md`, release notes, named plans, and project handoffs. Do not scan every artifact merely to make the bundle look complete.

Never assume access to arbitrary past ChatGPT, Codex, IDE, or project chats. If a requested past chat is unavailable, record `Not accessed` with the needed export, handoff, or source path. Treat memories and conversations as supporting context, not sole proof of current product state. When sources conflict, record the conflict instead of choosing a winner without evidence.

Separate repository evidence, user-provided context, inference, and unavailable evidence. Cite paths, symbols, report sections, issue or PR identifiers, or supplied transcript labels. Redact secrets, credentials, tokens, PHI, raw transcripts, customer identifiers, and sensitive logs.

## Workflow

1. Define the sign-off target, intended users or outcome, decision needed, scope, and excluded work.
2. Build a source inventory. State what was read, what was not accessible, and which source could resolve each material gap.
3. Read the smallest set of context files, plans, handoffs, requirements, changes, tests, contracts, and evidence records needed to trace the target from intended behavior to current proof.
4. Map acceptance criteria, user flows, contracts, data or privacy constraints, and operational assumptions to evidence. Mark each item `supported`, `partially supported`, `unsupported`, or `not applicable`.
5. Assess readiness: behavior, verification, compatibility, security and privacy, data handling, observability, rollout, rollback, ownership, and limitations. Do not run builds, tests, version-control, network, cloud, database, deployment, or live-service commands unless repository policy and the user explicitly allow them.
6. Read and complete all [bundle templates](references/signoff_summary_template.md): `00-signoff.md`, `01-context-and-evidence.md`, `02-requirements-traceability.md`, `03-release-readiness.md`, and `04-open-items.md`.
7. Re-read the bundle for consistency. Ensure every positive claim has cited evidence, every missing check is visible, and no document implies a human approved, deployed, or released the product.

## Verdicts

Return exactly one evidence verdict:

- `EVIDENCE SUPPORTS PRODUCT SIGN-OFF`
- `SIGN-OFF POSSIBLE WITH RECORDED RISKS`
- `NOT READY FOR PRODUCT SIGN-OFF`
- `INSUFFICIENT EVIDENCE`

Use a positive verdict only for the evidence reviewed. Record human approvals separately as `Recorded`, `Not recorded`, or `Not applicable`; never invent an approver, owner, date, or release decision.

## Safety and next actions

Do not edit application code, configuration, schemas, tests, CI/CD, deployment state, issue state, or existing project documentation. Do not commit, push, open a PR, merge, or invoke another skill automatically.

Recommend a narrowly scoped next action for each blocker or material gap. Use `$verify`, `$architecture-review`, `$contract-impact`, or `$ponytail-review` only as explicit follow-up recommendations when their specific evidence is needed.

In the final response, report the verdict, artifact path or inline status, sources not accessed, and the most important next decision.
