# GRAPH.md — loop-dietary-guide-assistant skill graph

## 1. Upstream inputs

- **cspi-uncompromised-dga**: dietary content (5 Guidelines, dietary pattern, alcohol context, sustainable diet, glossary)
- **loop-engineering**: loop infrastructure (6 primitives, maker-checker, dangers, design patterns)
- **Addy Osmani — "Loop Engineering"** (2026-06-07): loop design philosophy
- **CSPI — "The Uncompromised DGA"** (2026-01-07): dietary evidence base

## 2. Downstream outputs

- A running dietary triage loop
- Verified dietary guidance responses
- State files tracking advice history
- Escalation reports for human review

## 3. Internal node graph

```
SKILL.md (combined router + shared core)
  ├── reference/loop-architecture.md
  │     ├── 6 primitives → dietary mapping
  │     ├── daily loop cycle
  │     ├── scaling rules
  │     └── tool-agnostic mapping
  ├── reference/triage-loop.md
  │     ├── SAFE / VERIFY / ESCALATE decision tree
  │     ├── triage checklist
  │     ├── batch triage pattern
  │     └── escalation rules
  ├── reference/maker-checker.md
  │     ├── MAKER instructions + output format
  │     ├── CHECKER safety checklist (8 items)
  │     ├── revision cycle (max 2)
  │     └── token cost discipline
  ├── reference/guidelines-content.md
  │     ├── 5 Guidelines quick reference
  │     ├── life-stage rules
  │     ├── quantitative limits
  │     ├── 2,000-calorie pattern
  │     └── alcohol + sustainability
  ├── reference/dangers-in-context.md
  │     ├── verification debt → dangerous nutrition claims
  │     ├── comprehension debt → knowledge gap
  │     └── cognitive surrender → "loop knows best"
  └── assets/eval-cases.md
        ├── 3 positive triggers
        ├── 3 anti-triggers
        ├── 3 danger scenarios
        └── 2 integration tests
```

## 4. Cross-skill edges

| From | To | Edge type | When to traverse |
|---|---|---|---|
| this skill → cspi-uncompromised-dga | downstream_content | Need full dietary content detail | Deep dietary question, not covered by guidelines-content summary |
| this skill → loop-engineering | upstream_infrastructure | Need loop primitive details | Configuring a specific agent runtime (Codex/Claude Code) |
| loop-architecture → triage-loop | prerequisite | Before running the loop | Design before execution |
| triage-loop → maker-checker | downstream_action | After triage classifies VERIFY | Verification needed |
| maker-checker → guidelines-content | content_lookup | Maker/Checker need Guideline details | Every advice cycle |
| dangers-in-context → eval-cases | validation | After loop design | Verify the design is safe |

## 5. Adjacent skills

| Neighbor | Relationship | When to co-use |
|---|---|---|
| cspi-uncompromised-dga | Content source | When the loop needs detailed dietary knowledge |
| loop-engineering | Infrastructure source | When configuring specific runtime primitives |
| food-agent-methodology | Safety boundary | Any agent giving dietary advice |
| nutrition-ai-productization | Product pathway | Deploying the loop as a product |

## 6. Return-to-cache surfaces

After a dietary loop session:
- `ROUTING.yaml`: new trigger terms, missed-case items
- `GRAPH.md`: new cross-skill edges discovered
- `CACHE.md`: gotchas (e.g., common triage misclassifications)
- `assets/eval-cases.md`: new test scenarios from real usage
- State file: updated with session results

## 7. The combined metaphor

> **The loop gives the dietary guidance persistence; the Guidelines give the loop a spine.**

Without the loop, the Guidelines are a book you read once. Without the Guidelines, the loop is an engine with no destination. Together: an autonomous, verifiable, stateful dietary assistant that compounds knowledge and protects safety boundaries across sessions.
