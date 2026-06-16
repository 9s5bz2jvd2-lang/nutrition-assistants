# RUNBOOK — loop-engineering demand-sensitive reading

Core rule:

> Start sparse. Expand on demand. Full reading is allowed when the task requires it.

## 0. Before you read

1. What is the task type?
   - quick lookup (e.g., "what's /goal?")
   - normal loop design
   - danger/evaluation check
   - full loop redesign
2. Is this about designing an autonomous agent loop, or just prompting?
3. What would make sparse reading insufficient?

## 1. Reading modes

| Mode | Read first | Expand when | Stop when |
|---|---|---|---|
| quick lookup | `SKILL.md`, one expert | answer lacks boundary | answer is bounded |
| normal loop design | `SKILL.md`, `primitives.md`, `loop-design-pattern.md` | danger detected or high-risk | design passes danger check |
| danger evaluation | `SKILL.md`, `dangers.md`, `eval-cases.md` | existing loop has no verification gate | all three dangers addressed |
| full redesign | all modules | always | new design validated + route log produced |

## 2. Standard sparse invocation

1. Read `SKILL.md`
2. Read `ROUTING.yaml`
3. Classify task by trigger terms
4. Load top-k relevant experts
5. Run missed-case sweep (maker-checker? verification gate? comprehension debt? cognitive surrender?)
6. Produce deliverable
7. Write route log if serious run

## 3. Missed-case sweep

Before final answer, check:
- [ ] Maker-checker split enforced
- [ ] Verification gate present
- [ ] Comprehension debt addressed
- [ ] Cognitive surrender guard active
- [ ] State on disk (not in conversation context)
- [ ] Skills written (not re-prompted)
- [ ] Token cost budgeted for sub-agents
