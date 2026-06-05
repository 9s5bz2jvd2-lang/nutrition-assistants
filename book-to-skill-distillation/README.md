# book-to-skill-distillation

A [LingTai](https://github.com/Lingtai-AI/lingtai) / Anthropic-style **Agent Skill** that converts a book, long PDF, EPUB, or professional manual into an **agent-native skill/knowledge structure** — not a human-readable summary.

The output is something an agent can *call while working*: routers, decision trees, checklists, schemas, prompts, scripts, validation gates, worked examples, and progressive-disclosure reference modules. The source book disappears into operational memory; what remains is a skill an agent can route through to do work.

## Why this exists

Most "book → notes" tools produce shorter prose. That is the wrong shape for an LLM agent. A linear chapter does not help an agent route a task, choose a procedure, request the right documents, draft a finding, or know when to verify current law. This skill encodes a repeatable workflow for the *rewriting* step: taking a linear human text and turning it into the branching, callable artifacts an agent uses at runtime.

It also encodes the operational discipline around that workflow:

- **Copyright-safe**: extract operational know-how (procedures, checklists, taxonomies, decision trees); do not reproduce prose or examples beyond tiny necessary snippets.
- **Privacy-safe**: source-derived OCR substrate stays under a private `work/book-distill/<slug>/` workspace, *not* inside the published skill.
- **Verification-aware**: any claim that depends on current law, current pricing, current API behavior, etc. is marked for refresh against an authoritative source.

## What's in this repo

```
SKILL.md                     # Thin router — first file an agent loads
reference/                   # Progressive-disclosure depth
  agent-native-rewrite.md    # Core transformation: book forms → agent-native forms
  source-triage.md           # Classify the source (DIGITAL / SCANNED / MIXED / LOCKED)
  scanned-pdf-recipe.md      # Full OCR pipeline for image-only PDFs
  toc-recovery.md            # Recover structure from bookmarks/text/rendered TOC
  outline-design.md          # Design the target skill tree before rewriting
  daemon-orchestration.md    # Fan out parallel rewriting daemons
  copyright-discipline.md    # What to extract vs. what to leave behind
  validation-checklist.md    # Pre-publish gates
  publishing.md              # Custom → shared → external promotion path
  worked-example-legal-dd.md # End-to-end run on an 865-page scanned legal book
assets/                      # Reusable forms
  reference-doc-template.md  # Standard reference-module skeleton
  daemon-task-template.md    # Prompt template for one daemon
  toc-schema.yaml            # Canonical TOC data shape
  copyright-banner.md        # Standard disclaimer for distilled skills
scripts/                     # Deterministic helpers
  scout.sh                   # Quick DIGITAL vs. SCANNED verdict
  extract_bookmarks.py       # Dump PDF bookmarks + page count
  render_pages.sh            # Render page range to PNG at chosen DPI
  fanout_daemons.py          # Pointer to the daemon-task template
  quality_check.py           # Flag unfilled all-caps placeholder tokens
```

## Install (LingTai)

Drop the repo into your LingTai library as a custom skill:

```bash
git clone <this-repo> .library/custom/book-to-skill-distillation
```

Or, if you maintain LingTai elsewhere, copy this directory under whichever path your harness scans for custom skills. The skill self-describes via `SKILL.md`'s YAML frontmatter (`name`, `description`, `version`, `tags`).

After install, an agent that recognises the LingTai skill protocol can invoke `/book-to-skill-distillation` (or the equivalent in your harness) to load `SKILL.md` and route from there.

## Install (Anthropic Agent Skills convention)

The layout — `SKILL.md` with YAML frontmatter + sibling `reference/`, `assets/`, `scripts/` directories — also conforms to the general Anthropic Agent Skills convention. You can plug it into any agent runtime that follows that convention, not only LingTai.

## Example workflow

A worked, end-to-end pass on an 865-page scanned Chinese legal due-diligence treatise (see `reference/worked-example-legal-dd.md`):

1. **Scout**: `scripts/scout.sh source.pdf work/book-distill/legal-dd` → verdict: `SCANNED` (text layer empty).
2. **Triage**: classify as `SCANNED`, record title/edition/page count/language, define target skill scope (`legal-dd-prc` — PRC legal DD support).
3. **TOC recovery**: render TOC pages, OCR them, build `assets/toc-schema.yaml`-shaped chapter list with printed↔PDF page offset.
4. **OCR substrate**: render every page at 250 DPI, OCR `chi_sim+eng --psm 6`, write `work/book-distill/legal-dd/full_ocr/pages/page_XXXX.txt` + a manifest. This stays *private*.
5. **Topic split**: slice the OCR into `work/book-distill/legal-dd/topic_ocr/NN_slug.md` files by inclusive PDF page range.
6. **Outline design**: design the target `legal-dd-prc` skill *before* rewriting — pick the routing axis (issue taxonomy), decide which modules belong in `SKILL.md` vs. `reference/`, draft validation prompts.
7. **Daemon fan-out**: one daemon per topic, each using `assets/daemon-task-template.md`. Each daemon writes a reference module shaped by `assets/reference-doc-template.md` — *not* a chapter summary.
8. **Reconcile**: parent agent deduplicates, cross-links by issue relation, flags claims that need current-law verification (the source book is from 2017).
9. **Validate**: run `scripts/quality_check.py` for leftover placeholders, run any harness-level skill validator, smoke-test realistic prompts.
10. **Publish**: promote from `.library/custom/` → `.library_shared/` → external repo, after copyright/licensing review.

The output is `legal-dd-prc`: an agent-native skill an analyst-agent can route through to run a real PRC legal due-diligence engagement. The original book is no longer needed at runtime.

## The transformation in one table

| Book form | Agent-native form |
|---|---|
| chapter narrative | routing table + task entry points |
| conceptual explanation | decision rule / checklist / caveat |
| long legal discussion | issue schema: facts → law/current-law check → risk → remediation → evidence → report language |
| repeated examples | normalized finding patterns and red-flag leaves |
| document lists | DDQ / request list / evidence checklist |
| procedural prose | step-by-step workflow with stop/go gates |
| citations | statute/reference map with freshness warning and verification procedure |
| case anecdotes | abstracted risk pattern, **not** copied fact pattern |


## Cyclic low-power overlay

This repo also includes a cyclic discipline for larger distillation runs: [`reference/cyclic-low-power-distillation.md`](reference/cyclic-low-power-distillation.md).

> **网以通达，球以成身。心神合一，我圆如一。**
>
> Networks make knowledge reachable; cyclic return makes the system a body.

The overlay does not replace the core book-to-skill workflow. It adds boundary-setting, trajectory records, daemon return blocks, low-power budgets, human review protection, and a return-to-hub contract so that every outward branch returns reusable lessons to the center.

The framing was proposed by **Runyuan Wang** — a Chinese Registered Dietitian, member of Yunnan Astronomy Enthusiasts Association, and new explorer of AI workflows. Her bilingual contributor note is included in the reference module.

## Copyright and privacy discipline

This skill is opinionated:

- **Operational distillation only.** Extract procedures, checklists, taxonomies, decision trees, schemas. Do not reproduce prose, tables, or examples beyond the minimum necessary.
- **Keep OCR substrate private.** All page-by-page OCR output lives under `work/book-distill/<slug>/`, never inside the published skill folder. The published skill carries transformed artifacts, not source text.
- **No long passages.** Daemons must not reproduce more than ~2 consecutive source sentences in deliverables.
- **Mark uncertainty.** OCR is evidence, not authority. Article numbers, dates, and thresholds must be flagged for verification.
- **Mark staleness.** Any source-derived claim that depends on current law, current standards, or current API behavior must carry a verification note.

## "Is my distillation agent-native?" — the output test

> A good distilled skill lets an agent answer: *"What do I do next on this task?"* without rereading the book.
>
> If the output mostly says what the book said in the same order, it is not yet agent-native.

## License

MIT — see [LICENSE](LICENSE). The skill itself (the operational rewriting workflow) is original work. When you *use* the skill to distill a specific book, that derived skill carries the source book's licensing/copyright constraints; this skill enforces the discipline needed to stay on the right side of those, but you are responsible for compliance with the source's terms.

## Status

`version: 0.3.0`. Used in anger on a multi-hundred-page scanned professional treatise; matured enough to be worth sharing, still expected to evolve as it sees more source shapes.

<!-- Maintainer update: Runyuan Wang (9s5bz2jvd2-lang). -->
