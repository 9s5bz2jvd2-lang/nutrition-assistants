#!/usr/bin/env python3
import sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
errs = []
for p in root.rglob('*.md'):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    if '[PLACEHOLDER]' in txt:
        errs.append(f'placeholder: {p}')
print('\n'.join(errs) if errs else 'quality_check: ok')
sys.exit(1 if errs else 0)
