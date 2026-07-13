---
name: ponytail
description: "Choose and implement the smallest correct, evidence-backed change for a named coding task. Use only after explicit $ponytail or slash invocation; preserve explicit requirements, safety, accessibility, and supported-platform behavior rather than simplifying them away."
---

# Ponytail

Use this skill to minimize implementation surface area without minimizing correctness. It owns a focused implementation decision, not a broad review or debt report. Use `$ponytail-review` for a read-only complexity review and `$ponytail-debt` to report recorded shortcuts.

## Intensity

- `lite`: choose the simplest solution inside the explicit scope.
- `full`: follow the complete decision ladder. This is the default.
- `ultra`: surface unrequested or speculative work before adding it, while still preserving every explicit requirement.

## Start with the task

Require a named outcome and acceptance criteria. Read applicable `AGENTS.md` instructions, the relevant implementation, and nearby call paths before editing. Ask one focused question when an unresolved trade-off would change the design.

Do not replace explicitly requested behavior with a smaller version. Skip only unrequested, speculative work and explain that choice briefly.

## Decision ladder

Stop at the first option that meets the task's requirements:

1. Omit a speculative addition that is not part of the requested outcome.
2. Reuse an existing repository pattern, helper, or component.
3. Use the standard library.
4. Use a supported native platform or framework feature.
5. Use an already-installed dependency.
6. Make one small local code change.
7. Add the minimum new dependency needed now.

Before choosing a standard or native replacement, verify its supported runtime or browser coverage and its security, accessibility, localization, error-handling, and data-semantics fit. Read [platform-native candidates](references/platform-native.md) only when that comparison is relevant; it suggests candidates, not automatic replacements.

Before adding a dependency, inspect the manifest and existing imports. Add one only when the task needs it now, no existing or native option is suitable, and repository policy or the user's request permits it. State why the smaller options did not fit.

## Implement safely

- Keep the diff narrow and preserve public contracts unless the user explicitly changes them.
- For a bug fix, inspect sibling callers before choosing a shared-cause fix; do not apply the same patch blindly everywhere.
- Prefer deleting proven-unused code over adding abstraction, but do not remove externally consumed behavior without evidence.
- Do not add speculative interfaces, factories, configuration, wrappers, or future-proofing layers.

Record an intentional temporary shortcut only when it has a real ceiling and observable upgrade trigger. Use one comment in this exact shape:

```text
<comment prefix> ponytail: <shortcut>; ceiling: <limit>; upgrade: <observable trigger>
```

Do not add a `ponytail:` comment to explain ordinary code. `$ponytail-debt` reports these structured markers.

## Verify and report

Run the smallest relevant check only when repository policy and user approval allow it. If a check is not run, state why rather than implying success.

In the final response, keep to:

- **Choice:** the ladder rung used and why.
- **Changed or deliberately skipped:** the practical scope.
- **Verification:** checks run and their result.

Do not invoke other skills or create an artifact automatically.
