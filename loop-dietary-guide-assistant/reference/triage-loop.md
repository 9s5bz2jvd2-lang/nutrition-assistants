# Triage Loop — Daily Dietary Question Classification

## The triage skill

The triage skill is the entry point for every dietary question entering the loop. It classifies each question into one of three categories, then routes accordingly.

## Classification decision tree

```
Dietary question arrives
│
├── Does it involve a special population?
│   (infant, child <2, pregnant, lactating, elderly with conditions)
│   ├── YES → VERIFY (must check life-stage-specific guidance)
│   └── NO → continue
│
├── Does it involve alcohol?
│   ├── YES → VERIFY (must clarify official vs. uncompromised)
│   └── NO → continue
│
├── Is it a straightforward food-group/servings question?
│   (e.g., "How many cups of vegetables per day?")
│   ├── YES → SAFE (direct answer from dietary-pattern skill)
│   └── NO → continue
│
├── Does it involve a medical condition or treatment?
│   (e.g., "I have diabetes, what should I eat?")
│   ├── YES → ESCALATE (medical nutrition therapy boundary)
│   └── NO → continue
│
├── Does it involve a quantitative claim about nutrients?
│   (e.g., "Is 500mg sodium per meal too much?")
│   ├── YES → VERIFY (needs calculation against Guidelines limits)
│   └── NO → continue
│
├── Is it a sustainability + health intersection question?
│   ├── YES → VERIFY (needs sustainable-diet skill)
│   └── NO → continue
│
└── General healthy eating advice
    └── SAFE (answer from guidelines-overview skill)
```

## Three categories

| Category | What happens | Example |
|---|---|---|
| **SAFE** | Maker drafts → Checker confirms → respond | "How many cups of fruit per day?" → 2 cup eq/day (2,000-cal) |
| **VERIFY** | Maker drafts → Checker verifies against Guidelines + safety gates → respond with source labels | "Is 1 drink/day safe for everyone?" → Must add alcohol context, pregnancy warning, official vs. uncompromised |
| **ESCALATE** | Log to state file → flag for human review → do NOT respond automatically | "I'm on blood thinners, can I drink alcohol?" → Requires medical consultation |

## Triage checklist

For every question:
- [ ] Special population identified or confirmed not applicable
- [ ] Alcohol mentioned? → official vs. uncompromised clarification required
- [ ] Medical condition mentioned? → medical advice boundary check
- [ ] Quantitative claim? → needs verification against Guidelines limits
- [ ] Sustainability dimension? → load sustainable-diet skill
- [ ] Life stage specified? → if not, ask or provide all-stage default

## Batch triage pattern

When multiple questions arrive (daily batch):

```
1. Load all questions
2. Run triage decision tree on each
3. Group by category:
   - SAFE batch → one maker can handle all, checker spot-checks
   - VERIFY batch → each gets full maker-checker cycle
   - ESCALATE batch → all go to state file for human review
4. Update state file with counts and details
5. Run compliance check: did any SAFE answer accidentally cross a boundary?
```

## Escalation rules

Always escalate when:
- The user has a diagnosed medical condition (diabetes, kidney disease, celiac, eating disorder, etc.)
- The user is asking about interactions between diet and medication
- The user is pregnant or lactating and asking about alcohol, supplements, or restricted diets
- The claim contradicts the Guidelines
- The checker sub-agent returns REVISE twice on the same question
- The question involves children < 2 and the answer requires specific dosage amounts
