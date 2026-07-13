---
name: ponytail-review
description: "Find evidence-backed unnecessary complexity in a named diff, file set, or implementation without applying fixes. Use only after explicit $ponytail-review or slash invocation; preserve required behavior, safety, accessibility, compatibility, and tests."
---

# Ponytail Review

Use this skill for a read-only review of over-engineering. It complements a normal correctness or security review; it does not substitute for one and never applies fixes.

## Inputs and scope

Run only after explicit `$ponytail-review` invocation, or its supported slash form. Require a named diff, files, implementation, or plan plus its intended behavior. Ask one focused question if the target or expected behavior is missing.

Read applicable `AGENTS.md` instructions and inspect only the selected scope plus the minimum context needed to verify a finding. Do not create artifacts, run broad checks, or invoke other skills automatically.

## Finding bar

Report a finding only when the evidence shows that removing or replacing it preserves the intended behavior. Review for:

- dead code or unused flexibility;
- a repository-local or standard-library capability that already meets the need;
- a supported native feature that preserves the required behavior;
- an abstraction, configuration option, or layer with no demonstrated current use; or
- a clearly simpler local expression of the same behavior.

Do not flag validation at a trust boundary, error handling, security controls, accessibility behavior, compatibility handling, observability, or a targeted test solely because it adds lines. Do not replace a dependency merely because one call site is visible; first check its support and semantic requirements.

When evidence is incomplete, label the item `candidate` and state what would confirm it instead of presenting it as a required change. Route unrelated correctness, security, or performance concerns to the appropriate review rather than mixing them into this report.

## Output

List only material findings, ordered by likely safe impact:

```markdown
## Complexity findings
- `path:line` [delete|reuse|stdlib|native|yagni|shrink|candidate] — evidence. Smallest behavior-preserving replacement. Trade-off or confirmation needed.

## Scope and non-findings
- Reviewed: `<target>`
- Preserved intentionally: tests, validation, compatibility, or other necessary complexity.

## Verdict
`LEAN ALREADY` | `SIMPLIFICATION CANDIDATES FOUND` | `INSUFFICIENT CONTEXT`
```

Use `LEAN ALREADY` when no material candidate is supported by evidence. Do not estimate a line reduction unless the estimate is directly justified by the selected diff.
