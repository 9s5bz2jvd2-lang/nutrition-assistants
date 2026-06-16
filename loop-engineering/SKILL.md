---
name: loop-engineering
description: |
  Agent-native skill distilled from Addy Osmani's "Loop Engineering" (2026-06-07).
  Use when designing, evaluating, or operating autonomous coding-agent loops — not when merely prompting an agent interactively.
  Covers: the six loop primitives (automations, worktrees, skills, plugins/connectors, sub-agents, state), the maker-checker split, the three dangers (verification debt, comprehension debt, cognitive surrender), and concrete loop design patterns for Codex / Claude Code.
version: 1.0.0
tags: [loop-engineering, coding-agents, autonomous-loop, sparse-activation, sub-agents, worktrees, skills, automations, maker-checker]
---

# loop-engineering

> Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.

## Trigger

Use this skill when the task involves **designing, evaluating, debugging, or operating an autonomous coding-agent loop** — a system that discovers work, assigns it to agents, checks results, records progress, and decides next steps without continuous human prompting.

## Anti-triggers

Do NOT use this skill when:
- you only need to prompt an agent once or interactively (standard prompting is fine);
- the task is a simple single-step code generation;
- you want a summary of the article rather than operational guidance;
- you are avoiding understanding the work (cognitive surrender — see `reference/dangers.md`).

## Exclusions

- This skill does not reproduce the original article. It contains distilled operational structures.
- No specific tool vendor endorsement. The patterns are tool-agnostic; Codex and Claude Code are named as concrete examples, not as requirements.

## Shared core

| Rule | Detail |
|---|---|
| **Design the loop, don't just prompt** | Shift from "I type, agent responds" to "I design the system that types." |
| **Maker ≠ Checker** | The agent that writes code must not grade its own work. Split verification into a separate sub-agent. |
| **State lives on disk** | The agent forgets between runs. Memory must be a markdown file, a board, or any external artifact — not conversation context. |
| **Skills compound, prompts don't** | A skill is intent written down once where the agent reads it every run. Without skills, the loop re-derives your project from zero every cycle. |
| **Loops change work, not you** | Three problems get sharper, not easier: verification, comprehension debt, cognitive surrender. |

## Red lines

- Do not let the loop run unattended without a verification gate.
- Do not skip reading what the loop produced (comprehension debt).
- Do not surrender judgment to the loop (cognitive surrender).
- Do not design a loop to avoid understanding the work; design it to move faster on work you understand deeply.

## Router

| Situation | Read next |
|---|---|
| understand the six loop primitives | `reference/primitives.md` |
| design a concrete loop end-to-end | `reference/loop-design-pattern.md` |
| compare Codex vs. Claude Code primitives | `reference/primitives.md` (comparison table) |
| handle the three dangers | `reference/dangers.md` |
| check maker-checker split details | `reference/primitives.md` (sub-agents section) |
| evaluate whether a loop is well-designed | `assets/eval-cases.md` |

## Output test

A good loop design lets an agent answer "What do I do next?" without human prompting. If the loop requires human input at every step, it is not yet a loop — it is still prompting.

## Key quotations (source-anchored)

| Quotation | Attribution |
|---|---|
| "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." | Peter Steinberger |
| "I don't prompt Claude anymore. I have loops running that prompt Claude and figure out what to do. My job is to write loops." | Boris Cherny (Head of Claude Code, Anthropic) |
| "Your job is to ship code you confirmed works." | Addy Osmani, "Code Review in the Age of AI" |
| "Two people can build the exact same loop and get completely opposite results." | Addy Osmani |
| "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go." | Addy Osmani |

## Scope notes

This skill was distilled from a **single blog article** (not a multi-book source pack or database). Therefore:
- No source-map or schema-map is needed (source is a single web page).
- No multi-book / source-pack routing is applicable (single source).
- The missed-case sweep focuses on loop-design dangers (verification, comprehension, cognitive surrender), not on cross-source conflict or evidence gates.
- For database or multi-book distillation, use `book-to-skill-distillation` instead.

## Acceptance checks

1. `SKILL.md` has trigger, anti-triggers, router, red lines, output test.
2. Published skill contains transformed operational artifacts, not source-prose copies.
3. `ROUTING.yaml` identifies triggers, anti-triggers, neighbors, budget tiers.
4. `GRAPH.md` explains upstream, downstream, adjacent, safety gates.
5. `CACHE.md` separates stable prefix from variable suffix.
6. At least a small eval set covers positive triggers, anti-triggers, and danger scenarios.
