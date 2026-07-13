---
name: test-writer
description: "Plan, audit, or write focused behavior tests for a named target using its repository's test conventions. Use only after explicit $test-writer or slash invocation; change test files only, never claim unsupported coverage or execution, and do not modify production code."
---

# Test Writer

Use this skill to make tests that catch meaningful regressions in a named scope. It is not a production-code implementation or a generic test explanation workflow.

## Modes and intake

Run only after explicit `$test-writer` invocation, or its supported slash form. Select the user's requested mode:

- **Plan:** identify tests, fixtures, and mock boundaries; write no test files.
- **Audit:** identify evidence-backed test gaps; write no test files.
- **Write:** create or update focused test files only after the target and intended behavior are clear.

Require a named file, symbol, module, feature, or accepted plan section. Read applicable `AGENTS.md` instructions, the source under test, relevant existing tests, and the repository's actual test configuration before choosing a framework, file location, fixture style, imports, or command. If the target or test setup remains unclear, ask one focused question rather than assuming pytest or inventing conventions.

## Design tests from behavior

1. State the behavior, contract, or regression each test should protect.
2. Cover meaningful success, failure, boundary, and regression cases supported by the target's behavior. Do not add generic cases just to increase a count.
3. Reuse existing fixtures and helpers where they match the test's needs. Keep fixtures deterministic and scoped as narrowly as practical.
4. Mock at external or nondeterministic boundaries such as network, filesystem, time, random values, databases, queues, or third-party clients. Do not mock the behavior being tested or duplicate its implementation in assertions.
5. Use parameterization only when the scenarios share the same behavior and assertion shape. Keep each test focused on one observable outcome.
6. Treat integration, database, network, and live-service tests as explicit choices; follow repository setup and approval boundaries before using them.

## Write and validate

- Use `apply_patch` for every test-file edit or creation. Preserve existing passing tests unless the user asks to change them.
- Do not modify production source. If a production change is required for testability, report the limitation and proposed change separately.
- Match local test naming and style. Do not add type hints, docstrings, abstractions, or fixtures solely because they seem stylistically ideal.
- Re-read edited tests and confirm that assertions observe public behavior rather than implementation details.
- Run the smallest relevant test command only when repository policy and the user's approval allow it. Report the exact command and result, or why it was not run. Do not report a coverage percentage without measured coverage evidence.

## Artifact and response

Once a valid target is known, save a concise record under `.codex/artifacts/test-writer/YYYY-MM-DD_HHmm_<topic>.md` using [the test record template](references/test_record_template.md). Never overwrite an artifact; append `-2`, `-3`, and so on when needed. Do not create an artifact when the target is unresolved.

In the final response, state the mode, target, tests written or proposed, checks run, known gaps, and artifact path. Do not invoke `$verify`, `$execute`, or another skill automatically.
