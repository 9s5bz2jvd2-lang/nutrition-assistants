# GRAPH.md — loop-engineering skill graph

## 1. Upstream inputs

This skill was distilled from:
- **Addy Osmani — "Loop Engineering"** (2026-06-07): the primary source article
- **book-to-skill-distillation**: the distillation methodology used to produce this skill
- **Agent Harness Engineering**: the concept of making the environment one agent runs inside
- **The Factory Model**: the system that builds the software

## 2. Downstream outputs

This skill's output can flow to:
- A concrete loop-design document for a specific project
- A `SKILL.md` + `reference/` structure for a project's loop configuration
- A Codex / Claude Code agent configuration (`SKILL.md`, `.codex/agents/`, `.claude/agents/`)
- An evaluation of whether an existing loop is well-designed

## 3. Internal node graph

```
SKILL.md (router + shared core)
  ├── reference/primitives.md
  │     ├── automations
  │     ├── worktrees
  │     ├── skills
  │     ├── plugins-connectors
  │     ├── sub-agents (maker-checker)
  │     └── state
  ├── reference/loop-design-pattern.md
  │     ├── morning-triage-loop
  │     └── generic-loop-checklist
  ├── reference/dangers.md
  │     ├── verification-debt
  │     ├── comprehension-debt
  │     └── cognitive-surrender
  └── assets/eval-cases.md
        ├── positive-trigger-tests
        ├── anti-trigger-tests
        └── danger-scenario-tests
```

## 4. Edge types

| Edge type | When to traverse | Example |
|---|---|---|
| prerequisite | Need primitive definitions before designing a loop | SKILL.md → primitives.md |
| downstream action | Moving from understanding to concrete design | primitives.md → loop-design-pattern.md |
| safety/danger | Any unattended loop must check dangers | loop-design-pattern.md → dangers.md |
| semantic neighbor | Related concepts affect the answer | sub-agents → maker-checker → verification debt |
| source anchor | Need attribution for a claim | any node → SKILL.md key quotations table |
| anti-trigger check | Verify the task is not a misfire | SKILL.md anti-triggers |

## 5. Adjacent skills

| Neighbor | Relationship | When to co-use |
|---|---|---|
| agent-harness-engineering | One floor below: the environment one agent runs inside | Designing the harness, not just the loop |
| the-factory-model | One floor below: the system that builds software | Thinking about the full production pipeline |
| coding-agent-orchestra | Multiple specialized agents working together | When loop uses >2 sub-agents |
| adversarial-code-review | Second agent reviews the first | When implementing maker-checker split |
| intent-debt | Gaps in intent filled by confident guesses | When skills are missing or incomplete |
| orchestration-tax | Human review bandwidth as bottleneck | When scaling parallel worktrees |
| code-review-in-age-of-ai | Your job is to ship code you confirmed works | Verification discipline |

## 6. Return-to-cache surfaces

After a loop-design session, compress into:
- `ROUTING.yaml`: new trigger terms, anti-triggers discovered
- `GRAPH.md`: new edges or neighbor relationships found
- `CACHE.md`: gotchas, repeated patterns, budget observations
- `assets/eval-cases.md`: new test scenarios encountered

## 7. Core loop metaphor

> **Network gives the skill reachability; the cycle gives it continuity.**

The six primitives form a network (each callable independently). The state file and return-to-cache form the cycle (each run feeds the next). A well-designed loop branches out, then returns to a usable state.
