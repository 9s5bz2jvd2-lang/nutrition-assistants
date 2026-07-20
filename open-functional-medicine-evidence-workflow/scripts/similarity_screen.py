#!/usr/bin/env python3
"""
Similarity screen: compare the integrated candidate Markdown files against the
old functional-medicine corpus (33 chapter .txt files + 7 distilled .md files).

Method:
- Normalize each file by keeping CJK characters and ASCII alphanumerics,
  lower-casing ASCII, and dropping whitespace/punctuation.
- Build character n-gram sets (n=15).
- Compute containment = |intersection| / |new_file_shingles| and Jaccard.
- Report maxima per new file and globally. List example matching shingles
  when containment is above a low threshold.

This is an engineering screen, not a legal clearance.
"""

import os
import re
import json
import sys
from glob import glob

N = 15
CONTAINMENT_REPORT_THRESHOLD = 0.0010

def normalize(text):
    # Keep CJK and alphanumerics; lowercase ASCII; drop everything else.
    text = text.lower()
    text = re.sub(r"[^\u4e00-\u9fff\u3000-\u303f\uff00-\uffefa-z0-9]", "", text)
    text = re.sub(r"\s+", "", text)
    return text

def shingles(text, n=N):
    return set(text[i:i+n] for i in range(len(text) - n + 1))

def collect_files(root, patterns):
    files = []
    for pat in patterns:
        files.extend(glob(os.path.join(root, pat), recursive=True))
    return sorted(set(files))

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <candidate_root> <old_corpus_root> [output.json]")
        sys.exit(2)

    candidate_root = sys.argv[1]
    old_root = sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) >= 4 else None

    new_files = collect_files(candidate_root, ["**/*.md"])
    old_files = collect_files(old_root, [
        "knowledge/ch*.txt",
        "knowledge/fm2_ch*.txt",
        "knowledge/distilled_*.md",
    ])

    print(f"Candidate files: {len(new_files)}")
    print(f"Old corpus files: {len(old_files)}")

    old_sets = {}
    old_norms = {}
    for fp in old_files:
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            text = normalize(f.read())
        old_norms[fp] = text
        old_sets[fp] = shingles(text)

    results = []
    global_max = {"containment": 0.0, "jaccard": 0.0}

    for nfp in new_files:
        with open(nfp, "r", encoding="utf-8") as f:
            ntext = normalize(f.read())
        nset = shingles(ntext)
        if not nset:
            continue

        per_file_max = {"containment": 0.0, "jaccard": 0.0, "old_file": None}
        matches = []

        for ofp in old_files:
            oset = old_sets[ofp]
            if not oset:
                continue
            inter = nset & oset
            containment = len(inter) / len(nset)
            jaccard = len(inter) / len(nset | oset)

            if containment > per_file_max["containment"]:
                per_file_max = {
                    "containment": containment,
                    "jaccard": jaccard,
                    "old_file": os.path.relpath(ofp, old_root),
                }

            if containment >= CONTAINMENT_REPORT_THRESHOLD and inter:
                # Show up to 3 example matching shingles.
                examples = sorted(inter)[:3]
                matches.append({
                    "old_file": os.path.relpath(ofp, old_root),
                    "containment": containment,
                    "jaccard": jaccard,
                    "examples": examples,
                })

        if per_file_max["containment"] > global_max["containment"]:
            global_max = {
                "containment": per_file_max["containment"],
                "jaccard": per_file_max["jaccard"],
                "candidate_file": os.path.relpath(nfp, candidate_root),
                "old_file": per_file_max["old_file"],
            }

        results.append({
            "candidate_file": os.path.relpath(nfp, candidate_root),
            "max_containment": per_file_max["containment"],
            "max_jaccard": per_file_max["jaccard"],
            "closest_old_file": per_file_max["old_file"],
            "matches_above_threshold": matches,
        })

    report = {
        "method": f"character {N}-gram containment and Jaccard after normalization",
        "candidate_root": candidate_root,
        "old_corpus_root": old_root,
        "candidate_file_count": len(new_files),
        "old_corpus_file_count": len(old_files),
        "global_max": global_max,
        "per_file": results,
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\nReport written to {out_path}")

if __name__ == "__main__":
    main()
