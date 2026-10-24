#!/usr/bin/env python3
"""Report SVG structure only; does not judge lettering, OCR or production suitability."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


def local(name):
    return name.rsplit("}", 1)[-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path, help="Local SVG to inspect")
    parser.add_argument("--require-outlined", action="store_true",
                        help="Require vector geometry and no image/feImage, live text or foreignObject elements")
    parser.add_argument("--text", help="Expected text to record; no OCR or glyph correctness assertion")
    args = parser.parse_args()
    try:
        data = args.svg.read_bytes()
        if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper():
            raise ValueError("DTD/entity declarations are not supported")
        root = ET.fromstring(data)
        if local(root.tag) != "svg":
            raise ValueError("Root element is not svg")
        counts = Counter(local(node.tag) for node in root.iter())
        hrefs, stroke_nodes, filters, masks, css_urls = [], [], [], [], []
        for node in root.iter():
            tag = local(node.tag)
            for key, value in node.attrib.items():
                if local(key) == "href":
                    kind = "embedded_data" if value.startswith("data:") else "fragment" if value.startswith("#") else "external"
                    hrefs.append({"element": tag, "kind": kind, "value": value if kind != "embedded_data" else "data:…"})
            if node.get("stroke") not in (None, "none") or re.search(r"(?:^|;)\s*stroke\s*:", node.get("style", "")):
                stroke_nodes.append({"element": tag, "stroke": node.get("stroke"),
                                     "stroke_width": node.get("stroke-width"), "style": node.get("style")})
            for attr, target in (("filter", filters), ("mask", masks)):
                if node.get(attr) not in (None, "none"):
                    target.append({"element": tag, "value": node.get(attr)})
            css = node.get("style", "") + (node.text or "" if tag == "style" else "")
            css_urls.extend(re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", css))
        live_text = sum(counts[k] for k in ("text", "tspan", "textPath"))
        images = counts["image"] + counts["feImage"]
        basic_shapes = {"rect", "circle", "ellipse", "line", "polyline", "polygon"}
        has_vector_geometry = any(
            (local(node.tag) == "path" and bool(node.get("d", "").strip()))
            or local(node.tag) in basic_shapes for node in root.iter())
        outlined = has_vector_geometry and not (live_text or images or counts["foreignObject"])
        report = {"file": str(args.svg), "dimensions": {k: root.get(k) for k in ("width", "height", "viewBox")},
            "element_counts": dict(sorted(counts.items())), "paths": counts["path"],
            "image_elements": images, "live_text_elements": live_text,
            "external_hrefs": [h for h in hrefs if h["kind"] == "external"], "hrefs": hrefs,
            "filters": {"definitions": counts["filter"], "attribute_uses": filters},
            "masks": {"definitions": counts["mask"], "attribute_uses": masks},
            "stroke_declarations": stroke_nodes, "style_elements": counts["style"], "css_urls": css_urls,
            "expected_text": args.text, "text_verified": False,
            "has_vector_geometry": has_vector_geometry,
            "outlined_structure": outlined, "require_outlined_pass": outlined if args.require_outlined else None,
            "limitations": ["Structure only; no OCR or character correctness check.",
                "Does not measure minimum stroke width or certify manufacturing suitability.",
                "Does not resolve CSS inheritance, external resources or use references.",
                "Geometry presence does not verify valid commands, visibility, lettering or correctness.",
                "An outlined structure may contain basic vector shapes rather than paths."]}
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if not args.require_outlined or outlined else 1
    except (OSError, ET.ParseError, ValueError) as exc:
        print(f"preflight_svg: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
