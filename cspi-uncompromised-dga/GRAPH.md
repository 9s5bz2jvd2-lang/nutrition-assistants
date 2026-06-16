# GRAPH.md — cspi-uncompromised-dga skill graph

## 1. Upstream inputs

- **CSPI & Center for Biological Diversity** — "The Uncompromised Dietary Guidelines for Americans, 2025–2030" (Jan 2026)
- **2025 DGAC Scientific Report** — the evidence base for Guidelines 1–4
- **FAO/WHO Sustainable Healthy Diets** — the definition for Guideline 5
- **book-to-skill-distillation** — the distillation methodology

## 2. Downstream outputs

- Dietary guidance responses for agents
- Loop-dietary-guide-assistant (combined with loop-engineering)
- Eval cases for nutrition AI validation
- Evidence-anchored dietary claims

## 3. Internal node graph

```
SKILL.md (router + shared core)
  ├── reference/guidelines-overview.md
  │     ├── Guideline 1 (life stages)
  │     ├── Guideline 2 (customization)
  │     ├── Guideline 3 (food groups + nutrient-dense)
  │     ├── Guideline 4 (limits: sugar, fat, sodium, alcohol)
  │     └── Guideline 5 (sustainable diet)
  ├── reference/dietary-pattern.md
  │     └── 2,000-calorie "Eat Healthy Your Way" table
  ├── reference/sustainable-diet.md
  │     └── 5 sustainable practices + FAO/WHO definition
  ├── reference/alcohol-context.md
  │     └── Political timeline + 3 recommendations
  ├── reference/glossary.md
  │     └── 12 key terms
  └── assets/eval-cases.md
        └── 4 positive + 3 anti-trigger + 3 danger scenarios
```

## 4. Edge types

| Edge type | When to traverse | Example |
|---|---|---|
| prerequisite | Need guidelines before pattern details | SKILL.md → guidelines-overview.md |
| quantitative detail | Moving from principle to specific amounts | guidelines-overview.md → dietary-pattern.md |
| safety/context | Any alcohol question | guidelines-overview.md → alcohol-context.md |
| sustainability extension | Health + environment question | guidelines-overview.md → sustainable-diet.md |
| term lookup | Unfamiliar measurement unit | any node → glossary.md |
| danger check | Special population or medical boundary | any node → eval-cases.md danger scenarios |

## 5. Adjacent skills

| Neighbor | Relationship | When to co-use |
|---|---|---|
| loop-engineering | Loop infrastructure | Building the loop dietary guide assistant |
| food-agent-methodology | Nutrition AI safety boundaries | Any agent giving dietary advice |
| nutrition-ai-productization | Product pathway | Turning this skill into a deployable product |
| book-to-skill-distillation | Distillation methodology | When upgrading this skill from new sources |

## 6. Return-to-cache surfaces

After a dietary-guidance session, compress into:
- `ROUTING.yaml`: new trigger terms discovered
- `GRAPH.md`: new edges found
- `CACHE.md`: gotchas (e.g., common confusions about official vs. uncompromised)
- `assets/eval-cases.md`: new test scenarios
