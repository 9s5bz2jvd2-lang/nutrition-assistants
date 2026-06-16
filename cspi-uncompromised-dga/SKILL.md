---
name: cspi-uncompromised-dga
description: |
  Agent-native skill distilled from CSPI & Center for Biological Diversity's "The Uncompromised Dietary Guidelines for Americans, 2025–2030" (January 2026).
  Use when answering dietary guidance questions based on the 2025 DGAC science-based recommendations — the version that USDA/HHS should have published but did not.
  Covers: 5 overarching Guidelines, "Eat Healthy Your Way" dietary pattern with quantitative targets, sustainable diet practices, alcohol guidance, glossary, and the political context of DGA compromise.
version: 1.0.0
tags: [dietary-guidelines, DGA, CSPI, 2025-DGAC, eat-healthy-your-way, sustainable-diet, nutrition-policy, uncompromised]
---

# cspi-uncompromised-dga

> The Uncompromised DGA demonstrates what the 2025–2030 Dietary Guidelines for Americans could have looked like if the Departments had not strayed from their mandate to publish Guidelines based on the preponderance of the evidence.

## Trigger

Use this skill when the task involves:
- Providing dietary guidance consistent with the 2025 DGAC's science-based recommendations
- Answering questions about the U.S. Dietary Guidelines (2025–2030 edition)
- Comparing the official DGA vs. the DGAC's original scientific recommendations
- Calculating or explaining the "Eat Healthy Your Way" dietary pattern
- Discussing sustainable healthy diets in the U.S. context
- Explaining alcohol guidance controversies in the DGA process

## Anti-triggers

Do NOT use this skill when:
- The user wants guidance based on the official (compromised) 2025–2030 DGA as published by USDA/HHS
- The question is about a non-U.S. dietary guideline
- The user wants clinical medical nutrition therapy (this is public health guidance, not medical treatment)
- The user wants to reproduce the full original PDF

## Exclusions

- This skill does not reproduce the original report verbatim. It contains distilled operational structures.
- This is **public health guidance for healthy populations**, not medical nutrition therapy. It does not diagnose, treat, or replace professional medical advice.
- The alcohol guidance in Guideline 4 reflects the 2020 DGAC's evidence-based recommendations, which were not adopted by the Departments. See `reference/alcohol-context.md` for the political context.

## Shared core

| Rule | Detail |
|---|---|
| **Science-first** | All 5 Guidelines are grounded in the 2025 DGAC Scientific Report, not political compromise |
| **"Eat Healthy Your Way"** | The three separate dietary patterns (HUSS, Mediterranean, Vegetarian) are consolidated into one flexible pattern |
| **Quantitative targets** | The 2,000-calorie dietary pattern provides specific daily/weekly amounts for each food group and subgroup |
| **Sustainability is health** | Guideline 5 (CSPI + Center addition) connects human health and environmental health |
| **No substitution for medical care** | This is population-level guidance; individuals with conditions need personalized professional advice |

## Red lines

- Do not present these guidelines as the official published 2025–2030 DGA (they are the *uncompromised* version based on DGAC science)
- Do not give personalized medical nutrition therapy based on population-level guidelines
- Do not present the alcohol recommendations without the context of the political compromise (see `reference/alcohol-context.md`)
- Do not ignore special populations: infants, toddlers, pregnant/lactating women, and children have specific sub-guidelines
- Mark any claim that depends on current law or current agency action with a verification note

## Router

| Situation | Read next |
|---|---|
| get the 5 Guidelines overview | `reference/guidelines-overview.md` |
| get the "Eat Healthy Your Way" dietary pattern with quantitative targets | `reference/dietary-pattern.md` |
| understand sustainable diet practices (Guideline 5) | `reference/sustainable-diet.md` |
| understand the alcohol guidance controversy | `reference/alcohol-context.md` |
| look up a term (cup eq, oz eq, nutrient-dense, etc.) | `reference/glossary.md` |
| evaluate whether a dietary claim aligns with the Guidelines | `assets/eval-cases.md` |

## Output test

A good use of this skill lets an agent answer: "What does the science say I should eat, and how much?" without rereading the original report. If the output only paraphrases general advice without quantitative targets or guideline references, it is not yet agent-native.

## Source notes

- Source: CSPI & Center for Biological Diversity, "The Uncompromised Dietary Guidelines for Americans, 2025–2030," January 7, 2026
- Bold + underlined text in the original = 2025 DGAC updates; all other text = from the existing 2020–2025 DGA
- This is a **public document**; operational distillation is copyright-safe
- 48 references in the original; this skill preserves source anchors for evidence verification
