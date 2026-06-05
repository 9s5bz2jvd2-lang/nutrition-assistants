# Nutrition History Literature Research Anti-Hallucination Skill

English version translated from the existing Chinese README.

This is an anti-hallucination workflow skill for major work in **nutrition history, diet-therapy history, the history of dietary medicine, and Eastern/Western nutrition history**. Its core goal is not to save tokens, but to strictly separate “search snippets, model common sense, encyclopedia summaries, classical-text experience, and modern nutrition evidence,” so that clues are not mistakenly written as conclusions in historical literature research.

This repository was organized from the local custom skill `.library/custom/nutrition-history-anti-hallucination/` and can be published and reused as an independent small repository.

## Use Cases

Enable this skill when a task involves:

- Organizing nutrition history, diet-therapy history, or Eastern/Western dietary-medicine history;
- Verifying classical-text authors, dates, editions, compilations, alternate names, and OCR issues;
- Comparing traditional sources such as *Shiliao Bencao*, *Qianjin Fang*, *Yinshan Zhengyao*, *Bencao Gangmu*, and *Huangdi Neijing*;
- Comparing Western historical clues around dietetics, regimen, vitamins, RDA/DRI, and public-health nutrition;
- Crawling full texts, distilling them line by line or paragraph by paragraph, and comparing historical documents;
- Building a “historical time × East/West” literature matrix, timeline, and stage reports.

## Core Principles

1. **Full-text status first** — Every source must have a source record and a `full_text_status`. Without complete text or an authoritative source page, it can only enter the clue table, not a strong conclusion.
2. **Search snippets are not evidence** — `search_snippet_only` is only an unverified clue. Do not use search summaries, model impressions, or second-hand retellings as conclusions.
3. **Distill the full text, not just a few quotes** — For acquired full texts, return to volume, chapter, page, paragraph, or URL anchors; record quotations, plain-language interpretations, terminology, supported/unsupported judgments, and evidence boundaries.
4. **Historical-philology checks** — For classical and old literature, check title, authorship, date, edition, variant characters/OCR risks, and scope limits for claims such as “first” or “earliest.”
5. **Ancient diet therapy is not modern efficacy evidence** — Classical dietary therapy and materia medica can support historical thought or knowledge systems, not modern clinical efficacy unless separately verified by modern medical and nutrition evidence.
6. **Do not force East/West equivalence** — Dietetics, regimen, 食治, materia medica, and modern nutrition science belong to different historical contexts and knowledge systems; comparisons should explain differences rather than equate them directly.

## Not Medical Advice

This skill is only for historical literature research, evidence stratification, and anti-hallucination writing workflow. It does not provide medical advice, diagnosis, treatment plans, or individualized nutrition prescriptions. Any disease, treatment, supplement, food-medicine, or clinical-effect statement must be separately verified against modern medical and nutrition evidence.

## Repository Files

- `SKILL.md`: Original skill definition and complete workflow.
- `USAGE.md`: Installation, triggers, output formats, and examples.
- `CONTRIBUTOR_NOTE.md`: Notes for public maintenance and contribution.
- `README.md`: Chinese project description.

## Quick Use

Place `SKILL.md` into an agent environment that supports custom skills, for example:

```text
.library/custom/nutrition-history-anti-hallucination/SKILL.md
```

Then explicitly request this workflow in nutrition-history or diet-therapy-history research tasks.

## Typical Outputs

Recommended outputs for each batch include:

- sources catalog: source list and `full_text_status`;
- distillation notes: line-by-line or paragraph-by-paragraph records;
- timeline update;
- open questions and evidence gaps;
- stage report.

## License

No dedicated license file is currently attached. Before public release, the repository owner may add a `LICENSE` file if an explicit open-source license is needed.

<!-- Maintainer update: Runyuan Wang (9s5bz2jvd2-lang). -->
