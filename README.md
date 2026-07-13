# Skills

A focused collection of reusable skills for Codex and Claude Code. Each skill adds a bounded workflow that is hard to execute consistently from a general prompt alone.

## Included skills

| Skill | Use it for |
| --- | --- |
| [agent-relay](.codex/skills/agent-relay/SKILL.md) | Exchanging one safe, turn-based message with another AI through a shared Markdown file. |
| [architecture-review](.codex/skills/architecture-review/SKILL.md) | Reviewing an existing repository plan, design, deployment proposal, or production-readiness decision before implementation. |
| [code-rewrite](.codex/skills/code-rewrite/SKILL.md) | Reviewing or making a small, behavior-preserving cleanup to explicitly named source files. |
| [codex-context-handoff](.codex/skills/codex-context-handoff/SKILL.md) | Saving a fact-bounded handoff for a fresh Codex task. |
| [context-pickup](.codex/skills/context-pickup/SKILL.md) | Resuming safely from a selected handoff, plan, or artifact. |
| [contract-impact](.codex/skills/contract-impact/SKILL.md) | Mapping compatibility and coordination risks before a contract change. |
| [deps-audit](.codex/skills/deps-audit/SKILL.md) | Auditing Python manifests with a clear boundary between local and live security evidence. |
| [error-triage](.codex/skills/error-triage/SKILL.md) | Diagnosing a concrete failure from evidence and taking the smallest safe next action. |
| [execute](.codex/skills/execute/SKILL.md) | Implementing an approved, scoped repository task with focused verification. |
| [local-sast-analyzer](.codex/skills/local-sast-analyzer/SKILL.md) | Reviewing a local codebase or exported SAST findings with evidence-backed triage. |
| [multi-review](.codex/skills/multi-review/SKILL.md) | Reconciling independent review lenses into one evidence-backed verdict. |
| [plan-diff](.codex/skills/plan-diff/SKILL.md) | Comparing an external plan against a selected, current baseline. |
| [plan-it](.codex/skills/plan-it/SKILL.md) | Creating or revising an evidence-backed implementation plan. |
| [ponytail](.codex/skills/ponytail/SKILL.md) | Choosing the smallest correct change for an explicitly scoped coding task. |
| [ponytail-debt](.codex/skills/ponytail-debt/SKILL.md) | Reporting deliberate, structured implementation shortcuts without changing code. |
| [ponytail-review](.codex/skills/ponytail-review/SKILL.md) | Finding evidence-backed unnecessary complexity without applying fixes. |
| [project-handoff](.codex/skills/project-handoff/SKILL.md) | Preserving durable, evidence-bounded project context for a future session. |
| [project-start](.codex/skills/project-start/SKILL.md) | Bootstrapping a safe Codex workspace from verified repository evidence. |
| [sub-task](.codex/skills/sub-task/SKILL.md) | Turning a named plan into traceable, independently executable work units. |
| [test-writer](.codex/skills/test-writer/SKILL.md) | Planning, auditing, or writing focused behavior tests for a named target. |
| [verify](.codex/skills/verify/SKILL.md) | Performing a bounded, evidence-backed skeptical review before work is relied on. |

## Using a skill

Invoke a skill explicitly by name, for example `@architecture-review`. Use its slash form as well when the environment supports slash-style invocation. Read the skill's description for its scope and inputs.

## Adding a skill

Give each skill a folder under `.codex/skills/` containing `SKILL.md`. Keep its trigger description concise, add only instructions or context that are genuinely specific to the workflow, and validate real examples before relying on it.
