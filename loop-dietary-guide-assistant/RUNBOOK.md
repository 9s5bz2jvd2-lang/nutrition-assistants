# RUNBOOK — loop-dietary-guide-assistant execution guide

Core rule:

> Start sparse. Expand on demand. Always run the missed-case sweep for special populations and medical boundaries. The maker-checker split is non-negotiable for dietary advice.

## 0. Before you run

1. What is the task type?
   - single dietary question → use `cspi-uncompromised-dga`, not this skill
   - design a dietary loop → load loop-architecture + triage-loop
   - verify dietary claims → load maker-checker + guidelines-content
   - audit the loop's safety → load dangers-in-context + eval-cases
2. Is the DGA content current? (monthly check)
3. Is the state file accessible and current?

## 1. Standard loop invocation

1. Read `SKILL.md`
2. Read `ROUTING.yaml`
3. Load triage-loop + guidelines-content
4. For each question: triage → maker/checker → respond/escalate
5. Update state file
6. Write route log

## 2. Reading modes

| Mode | Read first | Expand when | Stop when |
|---|---|---|---|
| loop design | SKILL.md, loop-architecture, triage-loop | danger detected | design passes all checks |
| claim verification | SKILL.md, maker-checker, guidelines-content | special population or alcohol | checker returns PASS |
| safety audit | SKILL.md, dangers-in-context, eval-cases | any danger flag | all three dangers addressed |
| full redesign | all modules | always | new loop validated + route log |

## 3. Mandatory sweep (every run)

- [ ] Special population check
- [ ] Medical advice boundary
- [ ] Official vs. uncompromised clarification (if alcohol)
- [ ] Maker-checker split enforced (for VERIFY and ESCALATE)
- [ ] State file updated

## 4. When to expand

- Triage misclassification suspected
- Checker returns REVISE
- New life stage or population mentioned
- Stale guideline suspected
- Comprehension debt accumulating (review sample)
