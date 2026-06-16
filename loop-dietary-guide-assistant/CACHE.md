# CACHE.md — loop-dietary-guide-assistant cache layout

## 1. Stable prefix (200–800 tokens)

- Skill name: loop-dietary-guide-assistant
- Combined DNA: Loop Engineering (6 primitives) + Uncompromised DGA (5 Guidelines)
- Red lines: no medical advice; maker ≠ checker; special population checks; official vs. uncompromised
- Router table

## 2. Variable suffix

- Current triage batch
- Life stage context for current questions
- Triage classifications
- Maker/Checker drafts in progress
- Human escalation queue

## 3. On-demand reference

- Full loop architecture diagram
- Complete triage decision tree
- Maker-Checker detailed checklist
- Full 2,000-calorie dietary pattern
- Danger mitigation strategies

## 4. Budget

| Content | Default budget | When to upgrade |
|---|---:|---|
| Shared core | 200–800 tokens | Almost never |
| Loop architecture | 800–2000 tokens | Designing the loop |
| Triage loop | 400–1000 tokens | Running triage |
| Maker-checker | 800–2000 tokens | Verification cycle |
| Guidelines content | 400–1200 tokens | Drafting advice |
| Dangers in context | 400–1000 tokens | Safety review |

## 5. Gotchas

1. **Triage misclassification** — Questions about children are sometimes classified as SAFE when they should be VERIFY (child < 2 has different rules). Always check age before classifying.
2. **Alcohol always needs context** — Any question mentioning alcohol should be VERIFY at minimum, never SAFE, because the official vs. uncompromised distinction must be clarified.
3. **"Healthy eating" ≠ medical advice** — Users often ask "what should I eat for my [condition]?" — this is ESCALATE, not SAFE.
4. **Stale skills are invisible** — The loop can run smoothly on outdated Guidelines without anyone noticing. Monthly skill refresh check is mandatory.
5. **Maker-checker token budget** — Running both sub-agents doubles token cost. Budget accordingly, especially for batch triage.
6. **State file is the spine** — If the state file gets corrupted or lost, the loop loses continuity. Back it up.
7. **Comprehension debt accumulates silently** — The smoother the loop runs, the less you feel the need to check it. That's exactly when you should.
