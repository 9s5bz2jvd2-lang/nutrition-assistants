# worked-example-legal-dd

Legal-DD case: 865-page scanned Chinese PDF, 《法律尽职调查指要（修订版）》. The goal is not to summarize the book, but to rewrite it into `legal-dd-prc`: an agent-native PRC legal due-diligence support skill.

## Source facts

- Scanned/image-only PDF; `pdftotext` blank.
- 865 PDF pages, clean scan, Chinese legal/professional text.
- TOC recovered from rendered pages; body begins around PDF page 31.
- Printed-page to PDF-page offset is approximately `printed + 8`.
- The lower part of the book uses a repeated schema: operating procedure plus common legal issues.

## Evolution of the distilled skill

1. **v0.1 skeleton** — router, workflow references, 25 issue-module stubs.
2. **v0.2 directory/TOC rewrite** — 25 issue modules expanded from TOC and representative pages into practical DD checklists, red flags, and report prompts.
3. **full-OCR rewrite track** — full-book OCR created as private substrate, split by topic, then used to deepen each module into agent-native issue leaves and workflow assets.

## Full-OCR pattern used

- Install Chinese OCR language data if needed (`tesseract-lang` on macOS Homebrew).
- Test `chi_sim+eng --psm 6` on representative pages at 250 DPI.
- Run a page-by-page PyMuPDF + Tesseract script writing:
  - `work/book-distill/legal-dd/full_ocr/pages/page_XXXX.txt`
  - `work/book-distill/legal-dd/full_ocr/pages/page_XXXX.json`
  - `work/book-distill/legal-dd/full_ocr/book_ocr.md`
  - `work/book-distill/legal-dd/full_ocr/manifest.json`
- Split by topic into `work/book-distill/legal-dd/topic_ocr/NN_slug.md` using the TOC page map.

## Rewrite target for each legal-DD topic

Each topic module should eventually contain:

- Scope and when to load.
- Documents to request and public searches.
- Operating procedure / review tests.
- Common issue leaves: facts, law/current-law check, risks, remediation, evidence, report language.
- Red flags and severity/transaction-impact triage.
- Cross-links to adjacent modules.
- Current-law deltas because the source book is from 2017.

## Copyright discipline in this example

The OCR files remain private extraction substrate under `work/`. Published skill files should transform the material into checklists, schemas, prompts, and abstracted issue patterns. Do not paste long source passages into `.library/custom/legal-dd-prc/`.
