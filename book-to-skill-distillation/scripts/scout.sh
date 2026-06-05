#!/usr/bin/env bash
set -euo pipefail
PDF="${1:?source pdf}"; OUT="${2:-work/book-distill/scout}"; mkdir -p "$OUT"
pdfinfo "$PDF" > "$OUT/pdfinfo.txt" 2>&1 || true
pdftotext -f 1 -l 20 -layout "$PDF" "$OUT/sample_p1_20.txt" 2>/dev/null || true
python3 "$(dirname "$0")/extract_bookmarks.py" "$PDF" > "$OUT/bookmarks.json" 2>/dev/null || true
chars=$(tr -d '\f[:space:]' < "$OUT/sample_p1_20.txt" 2>/dev/null | wc -c | tr -d ' ')
[ "${chars:-0}" -lt 200 ] && echo SCANNED || echo DIGITAL_OR_MIXED
