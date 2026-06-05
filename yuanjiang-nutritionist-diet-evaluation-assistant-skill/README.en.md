# Yuanjiang's Nutritionist Diet Evaluation Assistant Skill

**Chinese attribution:** Created by Runyuan Wang + LingTai AI  
**English attribution:** Created by Runyuan Wang + LingTai AI

[中文 README](README.md)

## Author

**Runyuan Wang**  
M.Sc. in Nutrition and Food Hygiene, Kunming Medical University; Chinese Registered Dietitian; astronomy enthusiast; popular-science contributor.

**Co-created with:** LingTai AI

I am learning to use AI for nutrition science communication. Feedback, suggestions, and GitHub stars are very welcome.

## What this skill is for

This skill is a professional workflow assistant for nutritionists and nutrition teams. It turns messy three-day diet records, chat-based meal check-ins, spreadsheet logs, or speech-to-text diet descriptions into structured materials that a nutrition professional can review, discuss, and reuse.

It is designed to support:

1. Structured three-day diet tables.
2. Record-completeness checks and follow-up question lists.
3. Daily dietary pattern analysis.
4. Rough energy and macronutrient trend estimates with confidence labels.
5. DRIs 2023 gap assessment when the input and reference values are sufficient.
6. B-limited food-composition lookup for records that include both food names and edible portion weights.
7. Main dietary problem and risk-level identification.
8. Internal analysis summaries for nutrition professionals.
9. Actionable intervention suggestions.
10. Client-friendly communication wording.
11. Trend-chart data and visualization suggestions.
12. Visual briefs for long images, slides, or client reports.

## Intended users

The default users are **nutritionists, clinical dietitians, health managers, or members of a nutrition team**. The client or visitor is the analysis subject, not the default operator.

- **Internal layer:** structured tables, confidence labels, evidence boundaries, DRIs gaps, risk levels, follow-up questions, and intervention priorities for professional review.
- **Client layer:** warm, plain-language wording, chart notes, and 1-3 small actions that a nutritionist may choose to share after review.
- **Do not use it as:** a self-diagnosis tool, a self-treatment tool, an extreme weight-loss plan generator, or a replacement for professional nutrition judgment.

## Data capability boundaries

The skill currently includes a **DRIs 2023 reference-intake framework** and a **B-limited Section A food-composition table** extracted from a Tencent Docs PDF provided by Runyuan. Cross-checking indicates that this PDF is highly likely to be a subset or simplified excerpt from the 1991 edition lineage of *China Food Composition Tables*, **not** the 2018 Standard Edition, 6th edition, and **not** a complete current official database.

Therefore, outputs must keep data-version boundaries clear:

- **Level A (default):** structuring, dietary pattern analysis, follow-up questions, rough ranges, trend charts, and evidence-boundary notes.
- **Level B-limited (currently available):** lookup calculation for “food + edible grams” covering energy, protein, fat, carbohydrate, dietary fiber, vitamin A, B1, B2, niacin, vitamin E, sodium, calcium, iron, vitamin C, and cholesterol. The output must label the source as a Tencent Docs PDF extraction / Section A sampled validation / likely 1991-lineage subset, not the 2018 6th edition.
- **Level B-full (future):** more complete food-composition and micronutrient calculation if a compliant full dataset is available.
- **Level C (no suitable database):** do not pretend to calculate precise vitamin or mineral intake; provide only rough estimates and verification prompts.

Always preserve source-version fields when using food-composition or reference-intake data: source version/year, link, collection date, whether it is the latest version, and which fields have been verified.

## When to use this skill

Use it when the input contains any of the following:

- Three-day diet text records.
- Client meal check-ins from WeChat, group chats, private chats, or similar sources.
- Spreadsheet diet logs with inconsistent columns.
- Speech-to-text diet descriptions that are colloquial, repetitive, incomplete, or out of order.
- Fragmented feedback such as “ate a little,” “normal meal,” “had milk tea,” or “dinner party.”
- A nutrition professional wants structured review, dietary pattern analysis, rough energy/macronutrient trends, risk prompts, improvement suggestions, client communication wording, or internal team summaries.

## When not to make strong conclusions

Mark the output as unreliable or require professional/manual review when:

- Dates are missing or it is unclear whether the record covers three days.
- Many meals are missing, or the record only says “ate normally.”
- Portion sizes are absent and the food has a wide energy range.
- The client is a child, pregnant or lactating, elderly, chronically ill, taking medication, post-operative, undergoing cancer treatment, or may have an eating disorder.
- The question asks for diagnosis, disease treatment, prescription-level advice, or extreme weight loss.

## Core principle

> It is better to say “the record is unclear; follow-up is needed” than to turn incomplete records into falsely precise conclusions.

Do not package rough estimates as accurate nutrient calculation. Do not replace nutritionist judgment, clinical diagnosis, or individualized treatment prescriptions.

## Repository structure

- `SKILL.md` — main skill instructions.
- `assets/analysis-template.md` — output template for nutrition professionals.
- `assets/user-context-template.md` — user context and personalization constraints.
- `assets/trend-chart-data-template.csv` — trend-chart data template.
- `assets/visual-brief-template.md` — visual brief template.
- `assets/dri2023-*.csv` — DRIs 2023 templates / verified-draft data.
- `assets/food-composition-data/` — B-limited food-composition data and source manifest.
- `reference/food-composition-data/` — original-source comparison, cross-checking, and lookup rules.
- `reference/` — calculation design, source-layer rules, and external skill synthesis notes.

## Privacy and safety

- Do not place identifiable client data, phone numbers, addresses, ID numbers, full medical record numbers, or raw private screenshots into public examples or public issues.
- De-identify cases, screenshots, and reports before sharing.
- Cases involving children, pregnancy, older adults, chronic disease, medication, surgery, cancer treatment, or eating disorders require professional review and should not rely only on AI output.

## License

MIT
