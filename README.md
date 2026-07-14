# Skills

A focused collection of reusable skills for Codex and Claude Code. Each skill adds a bounded workflow that is hard to execute consistently from a general prompt alone. The same 21 workflows are maintained in two parallel trees — `.codex/skills/` for Codex and `.claude/skills/` for Claude Code — so either tool can invoke them natively.

## Included skills — `.codex/skills` (Codex)

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

## Included skills — `.claude/skills` (Claude Code)

| Skill | Use it for |
| --- | --- |
| [agent-relay](.claude/skills/agent-relay/SKILL.md) | Exchanging one safe, turn-based message with another AI through a shared Markdown file. |
| [architecture-review](.claude/skills/architecture-review/SKILL.md) | Reviewing an existing repository plan, design, deployment proposal, or production-readiness decision before implementation. |
| [claude-context-handoff](.claude/skills/claude-context-handoff/SKILL.md) | Saving a fact-bounded handoff for a fresh Claude Code task. |
| [code-rewrite](.claude/skills/code-rewrite/SKILL.md) | Reviewing or making a small, behavior-preserving cleanup to explicitly named source files. |
| [context-pickup](.claude/skills/context-pickup/SKILL.md) | Resuming safely from a selected handoff, plan, or artifact. |
| [contract-impact](.claude/skills/contract-impact/SKILL.md) | Mapping compatibility and coordination risks before a contract change. |
| [deps-audit](.claude/skills/deps-audit/SKILL.md) | Auditing Python manifests with a clear boundary between local and live security evidence. |
| [error-triage](.claude/skills/error-triage/SKILL.md) | Diagnosing a concrete failure from evidence and taking the smallest safe next action. |
| [execute](.claude/skills/execute/SKILL.md) | Implementing an approved, scoped repository task with focused verification. |
| [local-sast-analyzer](.claude/skills/local-sast-analyzer/SKILL.md) | Reviewing a local codebase or exported SAST findings with evidence-backed triage. |
| [multi-review](.claude/skills/multi-review/SKILL.md) | Reconciling independent review lenses into one evidence-backed verdict. |
| [plan-diff](.claude/skills/plan-diff/SKILL.md) | Comparing an external plan against a selected, current baseline. |
| [plan-it](.claude/skills/plan-it/SKILL.md) | Creating or revising an evidence-backed implementation plan. |
| [ponytail](.claude/skills/ponytail/SKILL.md) | Choosing the smallest correct change for an explicitly scoped coding task. |
| [ponytail-debt](.claude/skills/ponytail-debt/SKILL.md) | Reporting deliberate, structured implementation shortcuts without changing code. |
| [ponytail-review](.claude/skills/ponytail-review/SKILL.md) | Finding evidence-backed unnecessary complexity without applying fixes. |
| [project-handoff](.claude/skills/project-handoff/SKILL.md) | Preserving durable, evidence-bounded project context for a future session. |
| [project-start](.claude/skills/project-start/SKILL.md) | Bootstrapping a safe Claude Code workspace from verified repository evidence. |
| [sub-task](.claude/skills/sub-task/SKILL.md) | Turning a named plan into traceable, independently executable work units. |
| [test-writer](.claude/skills/test-writer/SKILL.md) | Planning, auditing, or writing focused behavior tests for a named target. |
| [verify](.claude/skills/verify/SKILL.md) | Performing a bounded, evidence-backed skeptical review before work is relied on. |

## Using a skill

Invoke a skill explicitly by name, for example `@architecture-review`. Use its slash form as well when the environment supports slash-style invocation (Claude Code skills are slash-invoked, e.g. `/architecture-review`). Read the skill's description for its scope and inputs.

## Adding a skill

Give each skill a folder containing `SKILL.md`: under `.codex/skills/` for Codex, under `.claude/skills/` for Claude Code. Keep its trigger description concise, add only instructions or context that are genuinely specific to the workflow, and validate real examples before relying on it.
