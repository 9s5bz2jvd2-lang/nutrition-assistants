#!/usr/bin/env python3
"""Generate deterministic, dependency-free functional-medicine matrix artifacts.

Usage:
    python3 scripts/generate_functional_medicine_matrix.py [--include-svg] INPUT.json OUTPUT_DIR

By default writes functional_medicine_matrix.json, functional_medicine_matrix.md
and a manifest-last functional_medicine_matrix_manifest.json. The optional
--include-svg flag adds functional_medicine_matrix.svg. Malformed input fails
before any destination is replaced; consumers verify every manifest hash.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
import tempfile
from pathlib import Path

TOP_KEYS = {
    "schema_version", "language", "case_key", "generated_at", "items",
    "lifestyle", "links", "flags", "review",
}
ITEM_KEYS = {
    "id", "text", "provenance", "period", "domains", "mes",
    "story_role", "certainty", "contradictions",
}
LINK_KEYS = {
    "id", "source_item_ids", "domains", "relation_type", "provenance",
    "evidence_refs", "uncertainty", "contradictions", "reviewer_status",
}
FLAG_KEYS = {"red_flags", "safety_concerns", "missing_data", "uncertainty_notes"}
REVIEW_KEYS = {"status", "reviewer_role"}
SYSTEMS = [
    "assimilation",
    "defense_and_repair",
    "structural_integrity",
    "energy",
    "communication",
    "transport",
    "biotransformation_and_elimination",
]
LIFESTYLE = ["sleep", "movement", "nutrition", "stress", "relationships"]
PROVENANCE = {"user_reported", "record_verified", "professional_interpretation", "unknown"}
STORY_ROLES = {"antecedent", "trigger", "mediator", "unclassified"}
CERTAINTY = {"documented", "reported", "possible", "unknown"}
RELATIONS = {"temporal_precedes", "co_occurs", "possible_influence", "shared_context", "contradicts", "unknown"}
LINK_PROVENANCE = {"user_reported", "record_verified", "professional_interpretation", "model_assisted_candidate", "unknown"}
LINK_REVIEW_STATUSES = {"unreviewed", "accepted", "revised", "rejected", "disputed"}
REVIEW_STATUSES = {"draft", "reviewed", "rejected", "incomplete"}
LANGUAGES = {"en"}
SAFE_ID = re.compile(r"^[A-Za-z0-9_.:-]{1,64}$")
SAFE_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:/-]{0,159}$")
GENERATOR_VERSION = "2.0.0"
ARTIFACT_SCHEMA_VERSION = "2.0"
MAX_ITEMS = 200
MAX_LINKS = 300
MAX_LIST = 100
MAX_TEXT = 1200

# The published English release accepts the English artifact contract only.
# Dynamic user-supplied Unicode text is still accepted and escaped unchanged.
LABELS = {
    "title": "Functional Medicine Matrix Worksheet",
    "center": "Mental · Emotional · Spiritual",
    "assimilation": "Assimilation",
    "defense_and_repair": "Defense & Repair",
    "structural_integrity": "Structural Integrity",
    "energy": "Energy & Recovery",
    "communication": "Communication & Regulation",
    "transport": "Transport & Circulation",
    "biotransformation_and_elimination": "Biotransformation & Elimination",
    "story": "Story: antecedents · triggers · mediators",
    "lifestyle": "Lifestyle: sleep · movement · nutrition · stress · relationships",
    "boundary": "Organizational completeness view; not diagnosis, scoring, or causal proof",
}


def die(message: str) -> None:
    raise ValueError(message)


def ensure_dict(value, name):
    if not isinstance(value, dict):
        die(f"{name} must be an object")
    return value


def ensure_list(value, name, max_len=MAX_LIST):
    if not isinstance(value, list):
        die(f"{name} must be an array")
    if len(value) > max_len:
        die(f"{name} exceeds {max_len} entries")
    return value


def ensure_text(value, name, max_len=MAX_TEXT, allow_empty=True):
    if not isinstance(value, str):
        die(f"{name} must be a string")
    if len(value) > max_len:
        die(f"{name} exceeds {max_len} characters")
    if not allow_empty and not value.strip():
        die(f"{name} must not be empty")
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in value):
        die(f"{name} contains forbidden control characters")
    return value.strip()


def reject_unknown(obj, allowed, name):
    extra = sorted(set(obj) - set(allowed))
    if extra:
        die(f"{name} has unknown keys: {', '.join(extra)}")


def text_list(value, name):
    return [ensure_text(v, f"{name}[]") for v in ensure_list(value, name)]


def reference_list(value, name):
    refs = text_list(value, name)
    if any(not SAFE_REF.fullmatch(ref) for ref in refs):
        die(f"{name} contains an unsafe source-reference ID")
    if len(set(refs)) != len(refs):
        die(f"{name} contains duplicate source-reference IDs")
    return refs


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json_bytes(value) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def normalize(raw):
    root = ensure_dict(raw, "root")
    reject_unknown(root, TOP_KEYS, "root")
    if root.get("schema_version") != "2.0":
        die("schema_version must be 2.0")
    language = root.get("language")
    if language not in LANGUAGES:
        die("language must be en")
    case_key = ensure_text(root.get("case_key"), "case_key", 64, False)
    if not SAFE_ID.fullmatch(case_key):
        die("case_key contains unsafe characters")
    generated_at = ensure_text(root.get("generated_at", "not_provided"), "generated_at", 64, False)

    normalized_items = []
    item_ids = set()
    for idx, value in enumerate(ensure_list(root.get("items", []), "items", MAX_ITEMS)):
        item = ensure_dict(value, f"items[{idx}]")
        reject_unknown(item, ITEM_KEYS, f"items[{idx}]")
        iid = ensure_text(item.get("id"), f"items[{idx}].id", 64, False)
        if not SAFE_ID.fullmatch(iid) or iid in item_ids:
            die(f"invalid or duplicate item id: {iid}")
        item_ids.add(iid)
        domains = ensure_list(item.get("domains", []), f"items[{idx}].domains", len(SYSTEMS))
        if len(set(domains)) != len(domains) or any(d not in SYSTEMS for d in domains):
            die(f"items[{idx}].domains contains invalid/duplicate value")
        mes = item.get("mes")
        if not isinstance(mes, bool):
            die(f"items[{idx}].mes must be a boolean")
        provenance = item.get("provenance")
        story_role = item.get("story_role")
        certainty = item.get("certainty")
        if provenance not in PROVENANCE:
            die(f"items[{idx}].provenance invalid")
        if story_role not in STORY_ROLES:
            die(f"items[{idx}].story_role invalid")
        if certainty not in CERTAINTY:
            die(f"items[{idx}].certainty invalid")
        normalized_items.append({
            "id": iid,
            "text": ensure_text(item.get("text"), f"items[{idx}].text", MAX_TEXT, False),
            "provenance": provenance,
            "period": ensure_text(item.get("period", "unknown"), f"items[{idx}].period", 160, False),
            "domains": sorted(domains, key=SYSTEMS.index),
            "mes": mes,
            "story_role": story_role,
            "certainty": certainty,
            "contradictions": text_list(item.get("contradictions", []), f"items[{idx}].contradictions"),
        })

    if not normalized_items:
        die("items must include at least one source-grounded case item")

    lifestyle = ensure_dict(root.get("lifestyle", {}), "lifestyle")
    reject_unknown(lifestyle, LIFESTYLE, "lifestyle")
    normalized_lifestyle = {}
    for lane in LIFESTYLE:
        refs = text_list(lifestyle.get(lane, []), f"lifestyle.{lane}")
        for ref in refs:
            if ref not in item_ids:
                die(f"lifestyle.{lane} references unknown item: {ref}")
        normalized_lifestyle[lane] = refs

    normalized_links = []
    link_ids = set()
    for idx, value in enumerate(ensure_list(root.get("links", []), "links", MAX_LINKS)):
        link = ensure_dict(value, f"links[{idx}]")
        reject_unknown(link, LINK_KEYS, f"links[{idx}]")
        lid = ensure_text(link.get("id"), f"links[{idx}].id", 64, False)
        if not SAFE_ID.fullmatch(lid) or lid in link_ids:
            die(f"invalid or duplicate link id: {lid}")
        link_ids.add(lid)
        refs = text_list(link.get("source_item_ids", []), f"links[{idx}].source_item_ids")
        if not refs or any(ref not in item_ids for ref in refs):
            die(f"links[{idx}] has missing/unknown source item")
        domains = ensure_list(link.get("domains", []), f"links[{idx}].domains", len(SYSTEMS))
        if len(set(domains)) != len(domains) or any(d not in SYSTEMS for d in domains):
            die(f"links[{idx}].domains invalid")
        relation = link.get("relation_type")
        if relation not in RELATIONS:
            die(f"links[{idx}].relation_type invalid")
        provenance = link.get("provenance")
        if provenance not in LINK_PROVENANCE:
            die(f"links[{idx}].provenance invalid")
        reviewer_status = link.get("reviewer_status", "unreviewed")
        if reviewer_status not in LINK_REVIEW_STATUSES:
            die(f"links[{idx}].reviewer_status invalid")
        normalized_links.append({
            "id": lid,
            "source_item_ids": refs,
            "domains": sorted(domains, key=SYSTEMS.index),
            "relation_type": relation,
            "provenance": provenance,
            "evidence_refs": reference_list(link.get("evidence_refs", []), f"links[{idx}].evidence_refs"),
            "uncertainty": ensure_text(link.get("uncertainty", "unknown"), f"links[{idx}].uncertainty"),
            "contradictions": text_list(link.get("contradictions", []), f"links[{idx}].contradictions"),
            "reviewer_status": reviewer_status,
        })

    flags = ensure_dict(root.get("flags", {}), "flags")
    reject_unknown(flags, FLAG_KEYS, "flags")
    normalized_flags = {key: text_list(flags.get(key, []), f"flags.{key}") for key in sorted(FLAG_KEYS)}
    review = ensure_dict(root.get("review", {}), "review")
    reject_unknown(review, REVIEW_KEYS, "review")
    review_status = review.get("status", "draft")
    if review_status not in REVIEW_STATUSES:
        die("review.status invalid")
    normalized_review = {
        "status": review_status,
        "reviewer_role": ensure_text(review.get("reviewer_role", "not_recorded"), "review.reviewer_role", 160, False),
    }

    filled_systems = sum(
        any(system in item["domains"] for item in normalized_items)
        for system in SYSTEMS
    )
    normalized_input = {
        "schema_version": "2.0",
        "language": language,
        "case_key": case_key,
        "generated_at": generated_at,
        "items": sorted(normalized_items, key=lambda x: x["id"]),
        "lifestyle": normalized_lifestyle,
        "links": sorted(normalized_links, key=lambda x: x["id"]),
        "flags": normalized_flags,
        "review": normalized_review,
    }
    normalized_hash = sha256_bytes(canonical_json_bytes(normalized_input))
    return {
        "artifact_schema_version": ARTIFACT_SCHEMA_VERSION,
        "generator_version": GENERATOR_VERSION,
        "normalized_input_sha256": normalized_hash,
        "ai_assistance_disclosure": "AI-assisted organizational artifact; evidence, uncertainty and reviewer state remain visible.",
        **normalized_input,
        "model_boundary": "organizational completeness view; not diagnosis, score, or causal proof",
        "coverage": {"filled_systems": filled_systems, "total_systems": len(SYSTEMS)},
    }


def clip(text, limit=35):
    clean = " ".join(text.split())
    return clean if len(clean) <= limit else clean[: limit - 1] + "…"


def clip_for_panel(text, language, cjk_limit, latin_limit):
    """Bound unwrapped SVG text to the available panel width.

    The English artifact contract uses ``latin_limit`` for layout. ``language``
    and ``cjk_limit`` remain in the internal signature so existing bounded call
    sites do not need an unrelated rendering refactor; dynamic Unicode text is
    still accepted and escaped.
    """
    return clip(text, latin_limit)


def svg_text_block(parts, x, y, lines, fill="#27352c", font_size=13, line_height=18):
    for line in lines:
        parts.append(f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}">{html.escape(line)}</text>')
        y += line_height
    return y


def render_svg(data):
    lang = data["language"]
    label = LABELS
    by_system = {s: [x for x in data["items"] if s in x["domains"]] for s in SYSTEMS}
    mes_items = [x for x in data["items"] if x["mes"]]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 1000" role="img" aria-labelledby="fm-title fm-desc" preserveAspectRatio="xMidYMid meet" data-artifact-version="{ARTIFACT_SCHEMA_VERSION}" style="max-width:100%;height:auto;background:#fbfaf6">',
        f'<title id="fm-title">{html.escape(label["title"])}</title>',
        f'<desc id="fm-desc">{html.escape(label["boundary"])}. AI-assisted organizational artifact; review state {html.escape(data["review"]["status"])}. No spokes or causal edges are drawn.</desc>',
        '<rect width="1500" height="1000" fill="#fbfaf6"/>',
        f'<text x="750" y="48" text-anchor="middle" font-size="28" font-weight="700" fill="#27352c">{html.escape(label["title"])}</text>',
    ]

    # Central MES
    parts.append(f'<ellipse cx="750" cy="400" rx="140" ry="80" fill="#a69ec8" stroke="#5e5380" stroke-width="3"/>')
    parts.append(f'<text x="750" y="395" text-anchor="middle" font-size="18" font-weight="700" fill="white">{html.escape(label["center"])}</text>')
    parts.append(f'<text x="750" y="420" text-anchor="middle" font-size="14" fill="white">{len(mes_items)} item(s)</text>')

    # 7 physiological systems in fixed positions around MES
    positions = [
        ("assimilation", 420, 220),
        ("defense_and_repair", 750, 220),
        ("structural_integrity", 1080, 220),
        ("energy", 420, 400),
        ("communication", 1080, 400),
        ("transport", 420, 580),
        ("biotransformation_and_elimination", 750, 580),
    ]
    for system, x, y in positions:
        items = by_system[system]
        filled = bool(items)
        fill = "#6f8f72" if filled else "#e1e7de"
        stroke = "#425c47" if filled else "#9aa89b"
        parts.append(f'<rect data-system="{system}" x="{x-110}" y="{y-50}" width="220" height="100" rx="10" ry="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="{y-18}" text-anchor="middle" font-size="15" font-weight="700" fill="{("white" if filled else "#425047")}">{html.escape(label[system])}</text>')
        parts.append(f'<text x="{x}" y="{y+2}" text-anchor="middle" font-size="13" fill="{("white" if filled else "#425047")}">{len(items)} item(s)</text>')
        snippet_y = y + 24
        for item in items[:2]:
            snippet = clip_for_panel(item["text"], lang, 16, 28)
            parts.append(f'<text x="{x}" y="{snippet_y}" text-anchor="middle" font-size="11" fill="{("white" if filled else "#425047")}">{html.escape(snippet)}</text>')
            snippet_y += 14
        if len(items) > 2:
            note = f'+{len(items)-2} more in Markdown'
            parts.append(f'<text x="{x}" y="{snippet_y}" text-anchor="middle" font-size="11" fill="{("white" if filled else "#425047")}">{html.escape(note)}</text>')

    # Left ATM story sections
    parts.append(f'<text x="40" y="120" font-size="18" font-weight="700" fill="#425047">{html.escape(label["story"])}</text>')
    y = 160
    for role in ["antecedent", "trigger", "mediator"]:
        items = [x for x in data["items"] if x["story_role"] == role]
        parts.append(f'<text x="40" y="{y}" font-size="15" font-weight="700" fill="#8b4f3b">{html.escape(role)} ({len(items)})</text>')
        y += 22
        for item in items[:3]:
            snippet = clip_for_panel(item["text"], lang, 16, 32)
            parts.append(f'<text x="55" y="{y}" font-size="13" fill="#27352c">• {html.escape(snippet)}</text>')
            y += 18
        if len(items) > 3:
            parts.append(f'<text x="55" y="{y}" font-size="12" fill="#425047">+{len(items)-3} more in Markdown</text>')
            y += 18
        y += 14

    # Bottom lifestyle pillars
    parts.append(f'<text x="750" y="700" text-anchor="middle" font-size="18" font-weight="700" fill="#425047">{html.escape(label["lifestyle"])}</text>')
    lane_x = [180, 420, 660, 900, 1140]
    for lane, x in zip(LIFESTYLE, lane_x):
        refs = data["lifestyle"][lane]
        parts.append(f'<rect data-lane="{lane}" x="{x-90}" y="725" width="180" height="90" rx="8" ry="8" fill="#e8e0d4" stroke="#9e8f7d" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="750" text-anchor="middle" font-size="15" font-weight="700" fill="#425047">{html.escape(lane)}</text>')
        parts.append(f'<text x="{x}" y="770" text-anchor="middle" font-size="13" fill="#425047">{len(refs)} item(s)</text>')
        if refs:
            ids = ", ".join(refs[:4])
            if len(refs) > 4:
                ids += f" +{len(refs)-4}"
            ids = clip(ids, 24)
            parts.append(f'<text x="{x}" y="790" text-anchor="middle" font-size="11" fill="#27352c">{html.escape(ids)}</text>')
        else:
            parts.append(f'<text x="{x}" y="790" text-anchor="middle" font-size="11" fill="#425047">none recorded</text>')

    # Boundary / footer
    parts.extend([
        f'<text x="750" y="920" text-anchor="middle" font-size="17" font-weight="700" fill="#7b3f2f">{html.escape(label["boundary"])}</text>',
        f'<text x="750" y="948" text-anchor="middle" font-size="14" fill="#425047">Case {html.escape(data["case_key"])} · coverage {data["coverage"]["filled_systems"]}/7 · review {html.escape(data["review"]["status"])}</text>',
        '<text x="750" y="972" text-anchor="middle" font-size="13" fill="#425047">AI-assisted organizational artifact · evidence and reviewer state remain visible · no spokes or causal edges</text>',
        '</svg>',
    ])
    return "".join(parts) + "\n"


def md_escape(text):
    escaped = html.escape(text, quote=False).replace("|", "\\|")
    escaped = re.sub(r"([\\`*_{}\[\]()#+\-.!])", r"\\\1", escaped)
    return " ".join(escaped.split())


def item_detail(item):
    domains = ", ".join(item["domains"]) if item["domains"] else "none"
    lines = [
        f"- `{item['id']}` {md_escape(item['text'])} — {item['provenance']}; {item['certainty']}; period {item['period']}; systems `{domains}`",
    ]
    if item["mes"]:
        lines[-1] += "; **MES**"
    for contradiction in item["contradictions"]:
        lines.append(f"  - contradiction/alternative: {md_escape(contradiction)}")
    return lines


def render_markdown(data):
    lang = data["language"]
    label = LABELS
    lines = [
        f"# {label['title']}",
        "",
        f"- Case key: `{data['case_key']}`",
        f"- Generated at: `{data['generated_at']}`",
        f"- Artifact / generator: `{data['artifact_schema_version']}` / `{data['generator_version']}`",
        f"- Normalized input SHA-256: `{data['normalized_input_sha256']}`",
        f"- Review: `{data['review']['status']}` / `{data['review']['reviewer_role']}`",
        f"- Coverage: `{data['coverage']['filled_systems']}/7` systems with observations (documentation completeness only)",
        "- Disclosure: AI-assisted organizational artifact; evidence, uncertainty and reviewer state remain visible.",
        "",
        "> This is a functional-medicine organizational matrix worksheet. It is not a diagnosis, severity score, causal proof, treatment plan, or validated clinical instrument.",
        "",
        "## Timeline / story (ATM)",
        "",
    ]
    for role in ["antecedent", "trigger", "mediator", "unclassified"]:
        lines.append(f"### {role}")
        chosen = [x for x in data["items"] if x["story_role"] == role]
        if not chosen:
            lines.append("- None recorded")
        for item in chosen:
            lines.extend(item_detail(item))
        lines.append("")

    lines += ["## Physiology / function matrix", ""]
    for system in SYSTEMS:
        lines.append(f"### {label[system]} (`{system}`)")
        chosen = [x for x in data["items"] if system in x["domains"]]
        if not chosen:
            lines.append("- None recorded")
        for item in chosen:
            lines.extend(item_detail(item))
        lines.append("")

    lines += ["## Central MES (Mental · Emotional · Spiritual)", ""]
    mes_items = [x for x in data["items"] if x["mes"]]
    if not mes_items:
        lines.append("- None recorded")
    for item in mes_items:
        lines.extend(item_detail(item))
    lines.append("")

    lines += ["## Lifestyle pillars", ""]
    for lane in LIFESTYLE:
        refs = data["lifestyle"][lane]
        lines.append(f"### {lane}")
        if not refs:
            lines.append("- None recorded")
        for rid in refs:
            item = next((x for x in data["items"] if x["id"] == rid), None)
            if item:
                lines.append(f"- `{rid}` {md_escape(item['text'])} — {item['provenance']}; {item['certainty']}")
            else:
                lines.append(f"- `{rid}` (missing item reference)")
        lines.append("")

    lines += ["## Candidate relationships / hypotheses", ""]
    lines.append("> These are candidate relationships only. They are not drawn as edges or spokes in the matrix and do not establish causality.",
    )
    lines.append("")
    if not data["links"]:
        lines.append("- None recorded")
    for link in data["links"]:
        lines.append(
            f"- `{link['id']}` {link['relation_type']}: systems `{', '.join(link['domains'])}`; items {', '.join(link['source_item_ids'])}; provenance `{link['provenance']}`; reviewer `{link['reviewer_status']}`"
        )
        lines.append(f"  - evidence refs: {', '.join(link['evidence_refs']) if link['evidence_refs'] else 'none recorded'}")
        lines.append(f"  - uncertainty: {md_escape(link['uncertainty'])}")
        for contradiction in link["contradictions"]:
            lines.append(f"  - contradiction/alternative: {md_escape(contradiction)}")
        lines.append("")

    lines += ["## Flags and missing information", ""]
    for key, values in data["flags"].items():
        lines.append(f"### {key}")
        lines.extend([f"- {md_escape(v)}" for v in values] or ["- None recorded"])
        lines.append("")

    lines += [
        "---",
        "",
        "**Boundary statement**: This worksheet organizes source-grounded observations into a functional-medicine matrix. It does not diagnose, score severity, prove causality, authorize treatment, or replace review by a qualified professional.",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def atomic_write(path: Path, payload: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
        try:
            dfd = os.open(path.parent, os.O_DIRECTORY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        except (AttributeError, OSError):
            pass
    except Exception:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


def main(argv):
    args = list(argv[1:])
    include_svg = False
    if "--include-svg" in args:
        include_svg = True
        args.remove("--include-svg")
    if len(args) != 2:
        print(f"Usage: {argv[0]} [--include-svg] INPUT.json OUTPUT_DIR", file=sys.stderr)
        return 2
    source = Path(args[0])
    output = Path(args[1])
    try:
        source_bytes = source.read_bytes()
        raw = json.loads(source_bytes.decode("utf-8"))
        data = normalize(raw)
        payloads = {
            "functional_medicine_matrix.json": (json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"),
            "functional_medicine_matrix.md": render_markdown(data).encode("utf-8"),
        }
        if include_svg:
            payloads["functional_medicine_matrix.svg"] = render_svg(data).encode("utf-8")
        manifest = {
            "schema_version": "2.0",
            "artifact_schema_version": ARTIFACT_SCHEMA_VERSION,
            "generator_version": GENERATOR_VERSION,
            "case_key": data["case_key"],
            "input_file_sha256": sha256_bytes(source_bytes),
            "normalized_input_sha256": data["normalized_input_sha256"],
            "files": {name: sha256_bytes(payload) for name, payload in sorted(payloads.items())},
            "completion_rule": "valid only when every listed file hash matches this manifest",
        }
        manifest_name = "functional_medicine_matrix_manifest.json"
        manifest_payload = (json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
        # Parse, normalize and render the whole bundle before any destination is replaced.
        # Write the manifest last: consumers fail closed on a mixed or interrupted bundle
        # because the file hashes will not match the last completed manifest.
        for name in sorted(payloads):
            atomic_write(output / name, payloads[name])
        if not include_svg:
            # A successful text-only rerun must not leave a stale SVG from an
            # earlier explicit image run in the same output directory.
            try:
                (output / "functional_medicine_matrix.svg").unlink()
            except FileNotFoundError:
                pass
        atomic_write(output / manifest_name, manifest_payload)
        payloads[manifest_name] = manifest_payload
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "ok", "output_dir": str(output), "include_svg": include_svg, "files": sorted(payloads)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
