---
name: book-to-skill-distillation
description: End-to-end workflow for rewriting a book, long PDF, EPUB, or manual into an agent-native LingTai skill/knowledge structure; covers source triage, scanned/image-only PDF OCR, page maps, topic splitting, progressive-disclosure outline design, daemon fan-out, copyright-safe transformation, validation, and publishing.
version: 0.3.0
tags: [workflow, meta-skill, distillation, ocr, daemons, progressive-disclosure, agent-native-rewrite]
---

# book-to-skill-distillation

Convert a linear human text into a branching **agent-native** skill. Distillation here is not a summary and not a compressed copy: it is a rewrite into the forms an agent can call while working — routers, decision trees, checklists, schemas, prompts, scripts, validation gates, worked examples, and reference modules.

Keep `SKILL.md` as the router; put depth in `reference/`, reusable forms in `assets/`, deterministic helpers in `scripts/`, and project-private extraction substrate under `work/book-distill/<slug>/`.

## Lifecycle

`Scout source → Recover structure → Extract/OCR substrate → Design target skill → Split by agent-native units → Rewrite in parallel → Reconcile → Return to hub → Validate & publish`

## Router

| Situation | Read next |
|---|---|
| understand the core transformation | `reference/agent-native-rewrite.md` |
| classify PDF/EPUB/source | `reference/source-triage.md` |
| scanned PDF / blank pdftotext / full OCR | `reference/scanned-pdf-recipe.md` |
| recover table of contents | `reference/toc-recovery.md` |
| map book to skill tree | `reference/outline-design.md` |
| add cyclic return / low-power / trajectory discipline | `reference/cyclic-low-power-distillation.md` |
| use daemons in parallel | `reference/daemon-orchestration.md`, `assets/daemon-task-template.md` |
| copyright concern | `reference/copyright-discipline.md` |
| validate/publish | `reference/validation-checklist.md`, `reference/publishing.md` |
| calibrate on this run | `reference/worked-example-legal-dd.md` |

## Quick start

1. Create `work/book-distill/<slug>/` and keep source-derived OCR/transcripts there, not inside the published skill.
2. Run `scripts/scout.sh <source.pdf> work/book-distill/<slug>` or equivalent inspection; decide whether the source has a text layer.
3. Recover the source structure: TOC, headings, page offsets, chapter boundaries, appendices, and repeated schemas.
4. If scanned/image-only, build full-text OCR as private substrate, then split it into topic files by page range.
5. Design the target skill tree before rewriting: trigger, exclusions, primary routing axis, reference modules, assets, scripts, caveats, and validation plan.
6. Fan out daemons: each daemon rewrites one topic or coherent topic group into agent-native structures, **not** into a chapter summary.
7. Parent reconciles, removes duplication, verifies current-law/current-fact deltas, and enforces copyright-safe abstraction.
8. Validate, refresh, and smoke-test realistic prompts.

## Output test

A good distilled skill lets an agent answer: “What do I do next on this task?” without rereading the book. If the output mostly says what the book said in the same order, it is not yet agent-native.

<!-- Maintainer update: Runyuan Wang (9s5bz2jvd2-lang). -->
