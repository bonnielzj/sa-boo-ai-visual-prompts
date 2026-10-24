#!/usr/bin/env python3
"""Check actual page readback for text boundaries, fonts, and bilingual omissions.

Consumes {"pages": [{"id", "name", "width", "height", "nodes": [...]}]}.
Node geometry is page-relative. Copy names use "Copy / zh / role" and
"Copy / en / role". This checks declared constraints, never aesthetic quality.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


COPY_NAME = re.compile(r"^Copy\s*/\s*(zh|en)\s*/\s*(.+?)\s*$", re.IGNORECASE)
BLEED_NAME = re.compile(r"\ballow[ _-]?bleed\b", re.IGNORECASE)


def number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def check_pages(payload: dict, *, margin: float = 96, content_bottom: float = 824,
                tolerance: float = 0.75, baseline_step: float = 0,
                baseline_origin: float | None = None) -> dict:
    pages = payload.get("pages")
    if not isinstance(pages, list):
        raise ValueError("Input must contain a pages array.")
    if not pages:
        raise ValueError("Readback contains no authored pages to check.")
    violations = []
    text_count = 0
    pair_count = 0

    def add(page: dict, node: dict | None, code: str, message: str, **details: Any) -> None:
        violations.append({"pageId": page.get("id"), "pageName": page.get("name"),
                           "nodeId": node.get("id") if node else None,
                           "nodeName": node.get("name") if node else None,
                           "code": code, "message": message, **details})

    for page in pages:
        if not isinstance(page, dict):
            raise ValueError("Each page must be an object.")
        width, height = page.get("width"), page.get("height")
        if not all(number(v) and v > 0 for v in (width, height)):
            add(page, None, "invalid_page_geometry", "Provide positive finite page width and height.")
            continue
        nodes = page.get("nodes")
        if not isinstance(nodes, list):
            add(page, None, "missing_nodes", "Provide actual node readback as a nodes array.")
            continue
        bottom = min(content_bottom, height - margin)
        pairs: dict[str, dict] = {}
        for node in nodes:
            if not isinstance(node, dict):
                add(page, None, "invalid_node", "Each node must be an object.")
                continue
            name = str(node.get("name", ""))
            copy_match = COPY_NAME.match(name.strip())
            characters = node.get("characters")
            if copy_match:
                language, role = copy_match.groups()
                language, role = language.lower(), role.casefold().strip()
                pair = pairs.setdefault(role, {"required": False, "zh": [], "en": []})
                pair[language].append(node)
                pair["required"] |= node.get("bilingualRequired", True) is not False
            if characters is None:
                if copy_match:
                    add(page, node, "missing_text_readback", "Read actual characters for this Copy node.")
                continue
            text_count += 1
            if not isinstance(characters, str):
                add(page, node, "invalid_text_readback", "characters must be the actual text string.")
                continue
            if node.get("missingFont"):
                add(page, node, "missing_font", "Resolve this text node's missing font before export.")
            geometry = [node.get(k) for k in ("x", "y", "width", "height")]
            if not all(number(v) for v in geometry) or geometry[2] < 0 or geometry[3] < 0:
                add(page, node, "invalid_node_geometry", "Provide finite page-relative x, y, width and height.")
                continue
            x, y, w, h = geometry
            font_size = node.get("fontSize")
            if characters.strip() and number(font_size) and font_size > 0 and h < 0.6 * font_size:
                add(page, node, "degenerate_text_height",
                    f"Nonempty text height {h:g} is below 60% of font size {font_size:g}. Check resizing order and export visibility.",
                    fontSize=font_size, lineHeight=node.get("lineHeight"), actualHeight=h)
            allow_bleed = node.get("allowBleed") is True or bool(BLEED_NAME.search(name))
            footer = name.strip().casefold().startswith("footer") or str(node.get("role", "")).casefold() == "footer"
            if not allow_bleed and (x < -tolerance or y < -tolerance or
                                    x + w > width + tolerance or y + h > height + tolerance):
                add(page, node, "outside_page", "Text extends beyond page bounds without an AllowBleed declaration.")
            if not allow_bleed and not footer:
                if x < margin - tolerance or x + w > width - margin + tolerance:
                    add(page, node, "side_margin", f"Text must stay between x={margin:g} and x={width - margin:g}.")
                if y < margin - tolerance:
                    add(page, node, "top_margin", f"Ordinary text starts above y={margin:g}.")
                if y + h > bottom + tolerance:
                    add(page, node, "content_bottom", f"Text bottom {y + h:g} exceeds content boundary y={bottom:g}.")
            # A text-box edge is not a typographic baseline. Check only supplied
            # authored anchors explicitly declared for grid alignment.
            anchor = node.get("baselineY")
            if baseline_step > 0 and node.get("snapBaseline") is True:
                if not number(anchor):
                    add(page, node, "missing_baseline_anchor", "Provide an authored baselineY; do not infer it from the text box.")
                else:
                    origin = margin if baseline_origin is None else baseline_origin
                    distance = abs(anchor - (origin + round((anchor - origin) / baseline_step) * baseline_step))
                    if distance > tolerance:
                        add(page, node, "baseline_drift", f"Authored baseline {anchor:g} is {distance:g} from the declared grid.")
        for role, pair in pairs.items():
            if not pair["required"]:
                continue
            pair_count += 1
            for language in ("zh", "en"):
                members = pair[language]
                if not any(isinstance(n.get("characters"), str) and n["characters"].strip() for n in members):
                    related = members[0] if members else next(iter(pair["zh"] + pair["en"]), None)
                    add(page, related, "missing_bilingual_copy", f"Role '{role}' needs nonempty Copy / {language} / {role} text.")

    return {"checkedPages": len(pages), "checkedTextNodes": text_count,
            "checkedBilingualRoles": pair_count, "violations": violations,
            "scope": "Declared text geometry, font availability and bilingual presence. Optical composition, translation quality and image finish require visual review."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON exported from actual authored page readback")
    parser.add_argument("--margin", type=float, default=96)
    parser.add_argument("--content-bottom", type=float, default=824)
    parser.add_argument("--tolerance", type=float, default=0.75)
    parser.add_argument("--baseline-step", type=float, default=0, help="0 disables optional authored-baseline checks")
    parser.add_argument("--baseline-origin", type=float)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    values = (args.margin, args.content_bottom, args.tolerance, args.baseline_step)
    if not all(number(v) and v >= 0 for v in values) or (args.baseline_origin is not None and not number(args.baseline_origin)):
        parser.error("Boundary, tolerance and baseline values must be finite; margins and steps cannot be negative.")
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("Input must be a JSON object.")
        result = check_pages(payload, margin=args.margin, content_bottom=args.content_bottom,
                             tolerance=args.tolerance, baseline_step=args.baseline_step,
                             baseline_origin=args.baseline_origin)
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 1 if result["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
