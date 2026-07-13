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
| [deps-audit](.codex/skills/deps-audit/SKILL.md) | Auditing Python manifests with a clear boundary between local and live security evidence. |

## Using a skill

Invoke a skill explicitly by name, for example `@architecture-review`. Use its slash form as well when the environment supports slash-style invocation. Read the skill's description for its scope and inputs.

## Adding a skill

Give each skill a folder under `.codex/skills/` containing `SKILL.md`. Keep its trigger description concise, add only instructions or context that are genuinely specific to the workflow, and validate real examples before relying on it.
