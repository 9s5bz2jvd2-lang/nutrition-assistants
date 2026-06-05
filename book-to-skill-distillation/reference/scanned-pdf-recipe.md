# scanned-pdf-recipe

Use this when `pdftotext` is blank, garbled, or clearly incomplete. A scanned book needs a reproducible OCR substrate before serious rewriting.

## Pipeline

1. **Inspect**
   - `pdfinfo <file>` for page count, creator, encryption, size.
   - `pdftotext <file> - | head` to test text layer.
   - Render a few pages at 150–250 DPI for visual quality.

2. **Install/select OCR**
   - Tesseract is usually enough for clean Chinese legal scans if `chi_sim`/`chi_tra` language data are installed.
   - Use `tesseract --list-langs` and install language packs if needed.
   - Test representative pages before full OCR.

3. **Representative quality test**
   - Cover/front matter page.
   - TOC page with dense headings.
   - Body page with prose.
   - Body page with enumerated issue schema or tables.
   - Record DPI/lang/psm and known noise patterns.

4. **Full OCR substrate**
   - Render page-by-page and OCR to `work/book-distill/<slug>/full_ocr/pages/page_XXXX.txt`.
   - Write per-page metadata and a manifest with status, char counts, errors, settings, and timestamps.
   - Keep it idempotent: reruns should skip completed pages unless `--force` is set.
   - Combine into `book_ocr.md` only as a private convenience file.

5. **Page map and topic split**
   - Recover printed-page ↔ PDF-page offset from TOC/body headers.
   - Build `topic_ocr/NN_slug.md` by inclusive PDF page ranges.
   - Keep `topic_ocr/index.json` with ranges, missing pages, and char counts.

6. **Rewrite, do not republish**
   - Daemons may read OCR substrate, but their deliverables should be structured transformations.
   - Published skill files should contain checklists, issue maps, prompts, and abstracted patterns — not long OCR passages.

## Practical Tesseract pattern

For clean Chinese scanned pages:

```bash
pdftoppm -r 250 -f <page> -l <page> -png source.pdf sample
 tesseract sample-<page>.png out -l chi_sim+eng --psm 6 txt
```

For full books, prefer a Python script using PyMuPDF rendering + `subprocess.run(['tesseract', ...])` with a small worker pool. Six workers at 250 DPI is often reasonable on a modern laptop; tune down if memory or heat becomes a problem.

## Quality notes

OCR is evidence for rewriting, not authoritative law. Preserve uncertainty:

- Regulation names, article numbers, dates, and thresholds require verification.
- Dense tables and headers may lose characters.
- Page ranges from TOC are often ±1 page until checked against body headers.
- If a page is missing or unreadable, mark it in the split index rather than silently dropping it.
