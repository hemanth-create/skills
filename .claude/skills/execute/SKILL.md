---
name: execute
description: "Implement a user-approved, scoped repository task or named plan. Use only when the user explicitly invokes /execute; inspect relevant code, make minimal changes, self-review the changes, and run focused verification."
---

# Execute

Implement an accepted task without losing its scope, approval boundaries, or verification requirements.

## Invocation and acceptance

Run only after explicit `/execute` invocation. A direct request to implement a clearly described task is approval to implement it. A draft plan is not approval unless the user explicitly asks to execute that plan.

Before editing, establish:

- the requested behavior and success condition;
- the named plan, files, or repository area in scope;
- the smallest useful verification; and
- any decision, side effect, or missing requirement that still needs approval.

Ask one concise question only when a reasonable implementation would make an incompatible product, architecture, or data decision.

## Workflow

1. Read applicable `CLAUDE.md` and repo-local helper guidance. Preserve unrelated working-tree changes and follow the repository's command, test, data, and approval rules.
2. Read the exact target files before editing. Read nearby callers, types, tests, and existing patterns only as needed to make the change safely.
3. Work in coherent slices. Each slice must leave the code more complete than before; do not leave stubs, placeholder behavior, or half-finished functions.
4. Before adding a module, class, interface, layer, dependency, configuration option, or generalized helper, identify the present task or source evidence that requires it. If it serves only imagined future reuse, prefer direct local code or surface the design decision.
5. Edit with `apply_patch`. Keep the diff focused, match local conventions, and avoid speculative abstractions or unrelated formatting.
6. Self-review each completed slice: re-read the changed code, check callers and error paths, compare it with the accepted task, and confirm each added concept has a current responsibility, caller, or boundary that justifies it.
7. Run the smallest focused verification allowed by the repository. If a check fails, fix the issue when it is in scope or report the failure; never present an unverified change as complete.
8. Review the final diff, simplify unnecessary code when safe, and summarize what changed, what was verified, and any remaining limitation. Do not invoke another skill automatically.

## Approval boundaries

Ask before a change needs any of the following, unless the user already approved it explicitly:

- a dependency install, file deletion or rename, generated-file update, schema or data migration;
- CI/CD, deployment, infrastructure, credential, network, or live-service action;
- a behavior or public-contract change beyond the accepted task; or
- a long-running or expensive verification command.

Do not commit, push, open a pull request, or write an execution artifact unless the user asks or repository instructions require it. When an artifact is requested, use `.claude/artifacts/execute/YYYY-MM-DD_HHmm_<topic>.md` and redact sensitive data.

## Response format

```markdown
Implemented <short description>.

Changed:
- `<path>` — <what changed>

Verified:
- <check and result, or why it was not run>

Remaining:
- <risk, decision, manual check, or "None known.">
```
