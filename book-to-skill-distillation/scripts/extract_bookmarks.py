#!/usr/bin/env python3
import sys,json,fitz
doc=fitz.open(sys.argv[1]); print(json.dumps({'page_count':doc.page_count,'toc':doc.get_toc()},ensure_ascii=False,indent=2))
