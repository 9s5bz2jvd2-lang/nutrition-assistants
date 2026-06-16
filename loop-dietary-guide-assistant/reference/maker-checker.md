# Maker-Checker — Dietary Advice Verification Split

## Why maker ≠ checker matters for dietary guidance

The model that drafts dietary advice is too lenient grading its own work. A second agent with different instructions and a safety checklist catches the things the first one talked itself into.

This is especially critical in nutrition, where:
- A small omission (e.g., forgetting to check the user's age) can change the advice entirely
- "Close enough" answers can be dangerous (e.g., adult sodium limits applied to a child)
- The difference between official and uncompromised DGA matters politically and practically

## The MAKER sub-agent

### Input
- User's dietary question
- Relevant skills (guidelines-content, dietary-pattern, etc.)
- Food composition data (if quantitative)
- User's stated life stage and context

### Instructions
1. Identify the relevant Guideline(s) and life stage
2. Draft dietary advice based on the Uncompromised DGA
3. Include quantitative targets where applicable
4. Cite the specific Guideline and source (DGAC, CSPI, FAO/WHO)
5. Note any assumptions (e.g., "assuming 2,000-calorie level")
6. If the question involves alcohol, include both official and uncompromised positions
7. If the question involves a special population, flag it

### Output format
```markdown
## Draft Response

**Question:** [original question]
**Guideline(s):** [1–5]
**Life stage:** [specified or assumed]
**Assumptions:** [calorie level, cultural context, etc.]

**Answer:** [draft advice with quantitative targets]

**Sources:** [DGAC p.XX, CSPI Guideline Y, etc.]

**Flags:** [any safety concerns, special population notes, alcohol context needed]
```

---

## The CHECKER sub-agent

### Input
- Maker's draft response
- Same skills + safety checklist
- Triage classification (SAFE / VERIFY / ESCALATE)

### Safety checklist (always run)

- [ ] **Life stage check**: Is the advice appropriate for the user's stated life stage?
  - [ ] Infant (< 6 mo): human milk only, vitamin D supplement
  - [ ] Infant (6–12 mo): complementary foods, iron + zinc emphasis
  - [ ] Child (< 2): no added sugars, whole milk
  - [ ] Child (2–13): reduced sodium, age-appropriate portions
  - [ ] Adult (14+): standard Guidelines
  - [ ] Pregnant/lactating: specific sub-guidelines
  - [ ] Older adult: nutrient density emphasis

- [ ] **Alcohol check**: If alcohol mentioned:
  - [ ] Both official and uncompromised positions stated?
  - [ ] "Do not begin drinking for health" included?
  - [ ] Pregnancy/breastfeeding exclusion noted?

- [ ] **Medical boundary**: Does the question involve a medical condition?
  - [ ] If YES and not already escalated → ESCALATE now
  - [ ] If NO → proceed

- [ ] **Quantitative accuracy**: Are all numbers correct per the Guidelines?
  - [ ] Added sugars < 10% of calories
  - [ ] Saturated fat < 10% of calories
  - [ ] Sodium < 2,300 mg (less for children < 14)
  - [ ] Alcohol ≤ 1 drink/day (uncompromised)
  - [ ] Food group amounts match dietary pattern table

- [ ] **Source labeling**: Every dietary claim has a source?
  - [ ] DGAC Scientific Report
  - [ ] CSPI/Center addition
  - [ ] FAO/WHO definition

- [ ] **Official vs. uncompromised**: Clarified where relevant?

- [ ] **Sustainability**: If applicable, are sustainable practices mentioned?

### Output format
```markdown
## Checker Verdict

**Verdict:** PASS / REVISE / ESCALATE

**Issues found:** [list, or "None"]

**If REVISE:**
- [specific issue 1]: [what to fix]
- [specific issue 2]: [what to fix]

**If ESCALATE:**
- [reason for escalation]
- [recommended human action]

**Safety sweep:** [completed / issues noted]
```

---

## The revision cycle

```
Maker drafts → Checker checks
  ├── PASS → publish response
  ├── REVISE → Maker revises → Checker re-checks (max 2 cycles)
  │                └── Still REVISE after 2 cycles → ESCALATE
  └── ESCALATE → log to state file, flag for human, do NOT publish
```

**Max 2 revision cycles.** If the checker still finds issues after 2 rounds, the question needs human review. This prevents infinite loops and catches genuinely ambiguous cases.

---

## Token cost discipline

| Check type | Token budget | When to use |
|---|---|---|
| Quick safety sweep | Low | SAFE-category questions |
| Full checklist | Medium | VERIFY-category questions |
| Deep evidence verification | High | ESCALATE-category or alcohol/special-population |

> Sub-agents burn more tokens. Spend them where the risk of error is highest — special populations, alcohol, and quantitative claims.
