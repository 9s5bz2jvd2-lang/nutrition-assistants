---
name: loop-dietary-guide-assistant
description: |
  An autonomous, loop-capable dietary guideline assistant that combines CSPI's Uncompromised DGA (2025–2030) evidence-based nutrition science with Loop Engineering principles.
  The assistant can: run scheduled dietary compliance checks, auto-triage nutrition questions, verify dietary claims with a maker-checker split, track state across sessions, and operate as a self-improving loop — all while respecting medical/nutrition safety boundaries.
  Use when you need an agent that doesn't just answer dietary questions once, but runs as a persistent, verifiable, stateful loop.
version: 1.0.0
tags: [dietary-guidelines, loop-engineering, autonomous-agent, DGA, CSPI, maker-checker, nutrition-AI, sustainable-diet]
---

# loop-dietary-guide-assistant

> Design the loop that delivers dietary guidance, don't just prompt for it one question at a time.

## Trigger

Use this skill when the task involves:
- Running a **recurring** dietary guidance workflow (daily check, weekly review, compliance monitoring)
- Building an autonomous agent that **triages** dietary questions, **verifies** claims, and **tracks** progress over time
- Designing a dietary-assistant loop with maker-checker verification and on-disk state
- Combining the Uncompromised DGA nutrition science with Loop Engineering automation patterns

## Anti-triggers

Do NOT use this skill when:
- You only need a single dietary question answered (use `cspi-uncompromised-dga` directly)
- You need loop infrastructure only, without dietary content (use `loop-engineering` directly)
- You want clinical medical nutrition therapy (this is public health guidance + automation, not medical treatment)

## Exclusions

- This skill does not provide medical nutrition therapy. It automates **public health dietary guidance** delivery.
- The maker-checker split verifies **guideline alignment and safety boundaries**, not clinical correctness.
- Loop automation does not replace professional nutrition consultation for individuals with conditions.

## Shared core — The Loop + The Guidelines

### From Loop Engineering (6 primitives → dietary loop mapping)

| Primitive | Loop Engineering role | Dietary guide assistant role |
|---|---|---|
| **Automations** | Discovery + triage on a schedule | Daily scan of dietary questions/claims; auto-triage into: safe-answer / needs-verification / needs-human |
| **Worktrees** | Isolate parallel features | Parallel verification of multiple dietary claims without cross-contamination |
| **Skills** | Codify project knowledge | DGA guidelines + dietary pattern + glossary + alcohol context as immutable skills |
| **Plugins/Connectors** | Connect tools | Food composition DB connector; nutrition label API; evidence source lookup |
| **Sub-agents** | Maker ≠ checker | **Maker**: drafts dietary advice based on Guidelines. **Checker**: verifies against Guidelines + safety gates + special-population rules |
| **State** | Track what's done | Persistent log: questions answered, claims verified, safety flags, escalation history |

### From Uncompromised DGA (5 Guidelines → operational rules)

| Guideline | Operational rule for the loop |
|---|---|
| **1. Life stages** | Every dietary answer must specify the life stage; infant/child rules differ from adult rules |
| **2. Customize** | Never give one-size-fits-all advice; ask about cultural/economic context when possible |
| **3. Food groups** | Quantitative targets from "Eat Healthy Your Way" 2,000-calorie pattern are the default reference |
| **4. Limits** | Sugar <10%, sat fat <10%, sodium <2,300 mg, alcohol ≤1 drink/day (uncompromised); always clarify official vs. uncompromised for alcohol |
| **5. Sustainability** | When environment + health intersect, surface the 5 sustainable practices |

## Red lines

### From Loop Engineering
1. **Verification debt**: The loop must not ship dietary advice without a checker sub-agent
2. **Comprehension debt**: A human must periodically review what the loop has been advising
3. **Cognitive surrender**: The loop is a tool, not a replacement for professional judgment

### From Dietary Guidelines
4. **No medical advice**: This is population-level public health guidance, not clinical treatment
5. **Special populations**: Infant, child, pregnant/lactating, older adult — each has distinct rules that the loop must check before answering
6. **Official vs. uncompromised**: Always clarify which version is being cited, especially for alcohol
7. **Evidence labeling**: Every dietary claim must have a source label (DGAC, CSPI, FAO/WHO)

## Router

| Situation | Read next |
|---|---|
| understand the full loop architecture | `reference/loop-architecture.md` |
| configure the daily dietary triage loop | `reference/triage-loop.md` |
| understand the maker-checker dietary verification | `reference/maker-checker.md` |
| get the dietary guidelines content | `reference/guidelines-content.md` |
| check loop dangers in dietary context | `reference/dangers-in-context.md` |
| evaluate the loop design | `assets/eval-cases.md` |

## Output test

A good loop-dietary-guide-assistant lets an agent:
1. **Auto-triage** a batch of dietary questions without human prompting
2. **Draft + verify** dietary advice with maker-checker split
3. **Track state** across sessions (what was answered, what was flagged, what escalated)
4. **Know when to stop** and escalate to a human professional

If the assistant only answers one question at a time with no persistence or verification, it is not yet a loop.

## Source notes

- **Loop Engineering**: distilled from Addy Osmani's "Loop Engineering" (2026-06-07), public blog article
- **Uncompromised DGA**: distilled from CSPI & Center for Biological Diversity, "The Uncompromised Dietary Guidelines for Americans, 2025–2030" (2026-01-07), public report
- Both sources are public documents; operational distillation is copyright-safe
