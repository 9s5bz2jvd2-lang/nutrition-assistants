#!/usr/bin/env bash
set -euo pipefail
PDF="${1:?pdf}"; START="${2:?start}"; END="${3:?end}"; OUT="${4:?outdir}"; DPI="${5:-200}"
mkdir -p "$OUT"; pdftoppm -f "$START" -l "$END" -png -r "$DPI" "$PDF" "$OUT/page"
