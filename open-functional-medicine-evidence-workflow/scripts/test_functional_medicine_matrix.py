#!/usr/bin/env python3
"""Dependency-free regression tests for the functional-medicine matrix generator."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_functional_medicine_matrix.py"
TEMPLATE = ROOT / "assets" / "functional-medicine-matrix-state-template.json"

TEXT_EXPECTED = {
    "functional_medicine_matrix.json",
    "functional_medicine_matrix.md",
    "functional_medicine_matrix_manifest.json",
}
IMAGE_EXPECTED = TEXT_EXPECTED | {"functional_medicine_matrix.svg"}

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(source: Path, output: Path, include_svg: bool = False):
    cmd = [sys.executable, str(GENERATOR)]
    if include_svg:
        cmd.append("--include-svg")
    cmd += [str(source), str(output)]
    return subprocess.run(
        cmd,
        check=False,
        capture_output=True,
        text=True,
    )


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def verify_core(output: Path, expected: set[str]):
    require({p.name for p in output.iterdir()} == expected, "unexpected bundle members")
    manifest = json.loads((output / "functional_medicine_matrix_manifest.json").read_text(encoding="utf-8"))
    require(set(manifest["files"]) == expected - {"functional_medicine_matrix_manifest.json"}, "manifest file set mismatch")
    for name, expected_hash in manifest["files"].items():
        require(sha256(output / name) == expected_hash, f"manifest hash mismatch: {name}")

    data = json.loads((output / "functional_medicine_matrix.json").read_text(encoding="utf-8"))
    require(data["artifact_schema_version"] == "2.0", "artifact version missing")
    require(len(data["normalized_input_sha256"]) == 64, "semantic input hash missing")
    require("AI-assisted" in data["ai_assistance_disclosure"], "JSON AI disclosure missing")

    found_domains = set()
    for item in data["items"]:
        found_domains.update(item.get("domains", []))
    for link in data["links"]:
        found_domains.update(link.get("domains", []))
    require(found_domains == set(SYSTEMS), f"expected exactly 7 systems, got {found_domains}")
    require("mindbody" not in found_domains, "mindbody domain must not appear")
    require(any(item.get("mes") for item in data["items"]), "MES support missing")
    require(set(data["lifestyle"]) == set(LIFESTYLE), "lifestyle lane set mismatch")
    if data["links"]:
        require(data["links"][0]["provenance"] == "professional_interpretation", "link provenance missing")


def verify_svg(output: Path):
    svg = (output / "functional_medicine_matrix.svg").read_text(encoding="utf-8")
    require("<line" not in svg, "SVG must not contain spokes/edges (<line>)")
    require("<image" not in svg and "url(http" not in svg and "href=" not in svg, "SVG contains a remote-resource surface")
    require(svg.count('data-system="') == 7, "SVG must contain exactly 7 fixed physiology panels")
    require(svg.count('data-lane="') == 5, "SVG must contain exactly 5 lifestyle panels")
    require('<ellipse cx="750" cy="400"' in svg, "SVG central MES geometry missing")
    for role in ("antecedent", "trigger", "mediator"):
        require(role in svg, f"SVG missing ATM story role: {role}")
    for token in ("viewBox=", "preserveAspectRatio=", "<title", "<desc", "AI-assisted", "max-width:100%"):
        require(token in svg, f"responsive/accessibility SVG token missing: {token}")
    center_label = "Mental · Emotional · Spiritual"
    for label in SYSTEMS + LIFESTYLE + [center_label]:
        require(label in svg, f"SVG missing expected label: {label}")


def data_language(output: Path) -> str:
    return json.loads((output / "functional_medicine_matrix.json").read_text(encoding="utf-8"))["language"]


def verify_markdown(output: Path):
    report = (output / "functional_medicine_matrix.md").read_text(encoding="utf-8")
    for token in ("AI-assisted", "Normalized input SHA-256", "provenance `professional_interpretation`", "evidence refs"):
        require(token in report, f"report token missing: {token}")
    data = json.loads((output / "functional_medicine_matrix.json").read_text(encoding="utf-8"))
    for item in data["items"]:
        require(item["text"] in report, f"report missing full item text: {item['id']}")
    for role in ("antecedent", "trigger", "mediator"):
        require(role in report, f"report missing ATM role: {role}")
    for system in SYSTEMS:
        require(system in report, f"report missing system: {system}")
    for lane in LIFESTYLE:
        require(lane in report, f"report missing lifestyle lane: {lane}")
    require("MES" in report, "report missing MES section")


def verify_bundle(output: Path, expected: set[str]):
    verify_core(output, expected)
    if "functional_medicine_matrix.svg" in expected:
        verify_svg(output)
    verify_markdown(output)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="functional-medicine-matrix-test-") as temp:
        base = Path(temp)
        input_path = base / "input.json"
        input_path.write_bytes(TEMPLATE.read_bytes())
        first = base / "first"
        second = base / "second"

        # Default invocation must emit the complete Markdown text matrix and no SVG.
        result = run(input_path, first, include_svg=False)
        require(result.returncode == 0, f"valid text-only generation failed: {result.stderr}")
        verify_bundle(first, TEXT_EXPECTED)
        require(not (first / "functional_medicine_matrix.svg").exists(), "default run emitted an SVG")
        require("include_svg\": false" in result.stdout, "default stdout did not report include_svg=false")

        # Deterministic default output.
        result = run(input_path, second, include_svg=False)
        require(result.returncode == 0, f"repeat text-only generation failed: {result.stderr}")
        verify_bundle(second, TEXT_EXPECTED)
        for name in TEXT_EXPECTED:
            require((first / name).read_bytes() == (second / name).read_bytes(), f"non-deterministic text output: {name}")

        # Explicit --include-svg must still produce the native SVG and validate structure.
        img_first = base / "img_first"
        img_second = base / "img_second"
        result = run(input_path, img_first, include_svg=True)
        require(result.returncode == 0, f"valid image generation failed: {result.stderr}")
        verify_bundle(img_first, IMAGE_EXPECTED)
        require((img_first / "functional_medicine_matrix.svg").exists(), "image opt-in did not emit an SVG")
        require("include_svg\": true" in result.stdout, "image stdout did not report include_svg=true")

        result = run(input_path, img_second, include_svg=True)
        require(result.returncode == 0, f"repeat image generation failed: {result.stderr}")
        verify_bundle(img_second, IMAGE_EXPECTED)
        for name in IMAGE_EXPECTED:
            require((img_first / name).read_bytes() == (img_second / name).read_bytes(), f"non-deterministic image output: {name}")

        # Returning the same directory to the default mode must remove the
        # previously opt-in SVG rather than expose a stale image.
        result = run(input_path, img_first, include_svg=False)
        require(result.returncode == 0, f"image-to-text transition failed: {result.stderr}")
        verify_bundle(img_first, TEXT_EXPECTED)
        require(not (img_first / "functional_medicine_matrix.svg").exists(), "text rerun left a stale SVG")

        # Invalid input must fail closed and must not overwrite prior outputs.
        before = {name: (first / name).read_bytes() for name in TEXT_EXPECTED}
        invalid = json.loads(input_path.read_text(encoding="utf-8"))
        invalid["unexpected"] = True
        invalid_path = base / "invalid.json"
        invalid_path.write_text(json.dumps(invalid), encoding="utf-8")
        result = run(invalid_path, first, include_svg=False)
        require(result.returncode == 1, "unknown-key input did not fail")
        require({name: (first / name).read_bytes() for name in TEXT_EXPECTED} == before, "invalid input overwrote a valid bundle")

        # Empty/no-case input must fail closed and must not overwrite prior outputs.
        empty = json.loads(input_path.read_text(encoding="utf-8"))
        empty["items"] = []
        empty["links"] = []
        empty["lifestyle"] = {lane: [] for lane in LIFESTYLE}
        empty_path = base / "empty.json"
        empty_path.write_text(json.dumps(empty, ensure_ascii=False), encoding="utf-8")
        result = run(empty_path, first, include_svg=False)
        require(result.returncode == 1, "empty/no-case input generated a matrix")
        require({name: (first / name).read_bytes() for name in TEXT_EXPECTED} == before, "empty input overwrote a valid bundle")

        # The English release rejects a non-English artifact language without
        # overwriting the previously valid bundle.
        wrong_language = json.loads(input_path.read_text(encoding="utf-8"))
        wrong_language["language"] = "zh"
        wrong_language_path = base / "wrong-language.json"
        wrong_language_path.write_text(json.dumps(wrong_language, ensure_ascii=False), encoding="utf-8")
        result = run(wrong_language_path, first, include_svg=False)
        require(result.returncode == 1, "non-English artifact language did not fail")
        require({name: (first / name).read_bytes() for name in TEXT_EXPECTED} == before, "wrong language overwrote a valid bundle")

        # Dynamic Unicode case text remains valid under the English artifact
        # contract. Escapes keep the source file itself English-only.
        unicode_case = json.loads(input_path.read_text(encoding="utf-8"))
        unicode_text = "\u4e2d\u6587 user-reported text"
        unicode_case["items"][0]["text"] = unicode_text
        unicode_path = base / "unicode.json"
        unicode_path.write_text(json.dumps(unicode_case, ensure_ascii=False), encoding="utf-8")
        unicode_out = base / "unicode_out"
        result = run(unicode_path, unicode_out, include_svg=False)
        require(result.returncode == 0, f"dynamic Unicode input failed: {result.stderr}")
        unicode_md = (unicode_out / "functional_medicine_matrix.md").read_text(encoding="utf-8")
        require(unicode_text.split(" ", 1)[0] in unicode_md, "dynamic Unicode characters were not preserved")
        require("user\\-reported text" in unicode_md, "dynamic Unicode text lost its escaped English suffix")

        # Active-markup escaping in Markdown (default) and SVG (image opt-in).
        malicious = json.loads(input_path.read_text(encoding="utf-8"))
        malicious["items"][0]["text"] = "<script>alert('x')</script> & observation ![remote](https://example.invalid/pixel.png) [click](javascript:alert(1))"
        malicious_path = base / "malicious.json"
        malicious_path.write_text(json.dumps(malicious, ensure_ascii=False), encoding="utf-8")

        malicious_text = base / "malicious_text"
        result = run(malicious_path, malicious_text, include_svg=False)
        require(result.returncode == 0, f"escaped-text generation failed: {result.stderr}")
        report = (malicious_text / "functional_medicine_matrix.md").read_text(encoding="utf-8")
        require("<script>" not in report, "active markup leaked into Markdown")
        require("&lt;script&gt;" in report, "Markdown did not preserve escaped source text")
        require("![remote](" not in report, "Markdown retained an active remote-image construct")
        require("[click](javascript:" not in report, "Markdown retained an active JavaScript-link construct")
        require("\\!\\[remote\\]" in report and "\\[click\\]" in report, "Markdown control characters were not escaped")

        malicious_img = base / "malicious_img"
        result = run(malicious_path, malicious_img, include_svg=True)
        require(result.returncode == 0, f"escaped-svg generation failed: {result.stderr}")
        svg = (malicious_img / "functional_medicine_matrix.svg").read_text(encoding="utf-8")
        require("<script>" not in svg, "active markup leaked into SVG")
        require("&lt;script&gt;" in svg, "SVG did not preserve escaped source text")
        require("href=" not in svg, "SVG retained a link surface")

        # Unknown reviewer status must still fail closed.
        bad_link = json.loads(input_path.read_text(encoding="utf-8"))
        bad_link["links"][0]["reviewer_status"] = "approved_by_everyone"
        bad_link_path = base / "bad-link.json"
        bad_link_path.write_text(json.dumps(bad_link, ensure_ascii=False), encoding="utf-8")
        result = run(bad_link_path, base / "bad-link", include_svg=False)
        require(result.returncode == 1, "unknown reviewer state did not fail closed")

    print("PASS: English text-default matrix, explicit SVG opt-in, exact layout, deterministic manifest/hash accounting, dynamic Unicode, language rejection, active-markup escape, empty/invalid no-overwrite and reviewer-state tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
