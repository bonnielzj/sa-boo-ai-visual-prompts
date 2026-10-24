#!/usr/bin/env python3
"""Outline simple horizontal Han text from a local font; this is not shaping."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET


def codepoint(char):
    return f"U+{ord(char):04X}"


def reject_sequence_features(text):
    for char in text:
        cp = ord(char)
        if (unicodedata.category(char).startswith("M")
                or 0xFE00 <= cp <= 0xFE0F or 0xE0100 <= cp <= 0xE01EF):
            raise ValueError(f"{codepoint(char)}: combining marks and variation selectors require shaping; unsupported")
        if unicodedata.category(char) in ("Cc", "Cf", "Cs"):
            raise ValueError(f"{codepoint(char)}: control/format/surrogate characters are unsupported")


def simple_character(char):
    cp = ord(char)
    return (0x20 <= cp <= 0x7E or 0x3000 <= cp <= 0x303F
            or 0xFF01 <= cp <= 0xFF60 or 0xFFE0 <= cp <= 0xFFE6
            or unicodedata.name(char, "").startswith((
                "CJK UNIFIED IDEOGRAPH-", "CJK COMPATIBILITY IDEOGRAPH-")))


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        "Supports Han, ASCII and common CJK/fullwidth punctuation only. "
        "No shaping, kerning, vertical layout or font fallback. "
        "Font outlines are not original hand-drawn lettering; check the font license separately."))
    parser.add_argument("--font", required=True, type=Path, help="Local TTF/OTF/TTC font; font is not embedded")
    parser.add_argument("--font-index", type=int, default=0, help="Zero-based TTC face index (default: 0)")
    parser.add_argument("--text", help="Exact single-line text; optional with --inspect")
    parser.add_argument("--output", type=Path, help="SVG output path; written only after validation succeeds")
    parser.add_argument("--font-size", type=float, default=100, help="SVG units per em (default: 100)")
    parser.add_argument("--inspect", action="store_true", help="Report font names and Unicode coverage, write no SVG")
    args = parser.parse_args()
    try:
        if args.font_index < 0 or not 0 < args.font_size < float("inf"):
            raise ValueError("font-index must be nonnegative and font-size must be finite and positive")
        if not args.inspect and (not args.text or args.output is None):
            raise ValueError("--text (nonempty) and --output are required unless --inspect is used")
        text = args.text or ""
        reject_sequence_features(text)
        from fontTools.ttLib import TTFont
        from fontTools.pens.svgPathPen import SVGPathPen
        from fontTools.pens.boundsPen import BoundsPen

        with TTFont(str(args.font), fontNumber=args.font_index) as font:
            cmap = font.getBestCmap() or {}
            missing = sorted({codepoint(c) for c in text if cmap.get(ord(c), ".notdef") == ".notdef"})
            names = {label: font["name"].getDebugName(n) for label, n in (
                ("family", 1), ("style", 2), ("full_name", 4), ("postscript_name", 6))}
            report = {"font": str(args.font), "font_index": args.font_index, "names": names,
                      "unicode_cmap_entries": len(cmap), "text": text,
                      "missing_codepoints": missing, "coverage_complete": not missing,
                      "source": "existing font outlines; no license determination"}
            if missing:
                if args.inspect:
                    print(json.dumps(report, ensure_ascii=False, indent=2))
                    return 2
                raise ValueError("Font missing Unicode glyphs: " + ", ".join(missing))
            unsupported = sorted({codepoint(c) for c in text if not simple_character(c)})
            if unsupported:
                raise ValueError("Unsupported script/symbol; use a shaping-capable tool: " + ", ".join(unsupported))
            if args.inspect:
                print(json.dumps(report, ensure_ascii=False, indent=2))
                return 0

            units = font["head"].unitsPerEm
            scale = args.font_size / units
            ascent, descent = font["hhea"].ascent, font["hhea"].descent
            glyphs = font.getGlyphSet()
            x, left, right = 0, 0, 0
            top, bottom = 0, (ascent - descent) * scale
            groups = []
            for index, char in enumerate(text):
                glyph_name = cmap[ord(char)]
                glyph = glyphs[glyph_name]
                pen = SVGPathPen(glyphs)
                glyph.draw(pen)
                commands = pen.getCommands()
                if not commands and not char.isspace():
                    raise ValueError(f"{codepoint(char)} maps to a glyph without visible outlines")
                bounds = BoundsPen(glyphs)
                glyph.draw(bounds)
                if bounds.bounds:
                    x0, y0, x1, y1 = bounds.bounds
                    left, right = min(left, x + x0 * scale), max(right, x + x1 * scale)
                    top, bottom = min(top, (ascent - y1) * scale), max(bottom, (ascent - y0) * scale)
                advance = font["hmtx"][glyph_name][0] * scale
                group = ET.Element("g", {"id": f"glyph-{index:04d}", "data-character": char,
                    "data-codepoint": codepoint(char), "data-glyph-name": glyph_name,
                    "data-advance": f"{advance:.6g}",
                    "transform": f"translate({x:.6g} {ascent * scale:.6g}) scale({scale:.9g} {-scale:.9g})"})
                if commands:
                    ET.SubElement(group, "path", {"d": commands})
                groups.append(group)
                x += advance
            right = max(right, x)
            root = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg", "fill": "#000000",
                "width": f"{right-left:.6g}", "height": f"{bottom-top:.6g}",
                "viewBox": f"{left:.6g} {top:.6g} {right-left:.6g} {bottom-top:.6g}",
                "data-baseline": f"{ascent * scale:.6g}", "data-text": text})
            ET.SubElement(root, "metadata").text = json.dumps(report, ensure_ascii=False)
            root.extend(groups)
            data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=args.output.parent, delete=False) as handle:
                    temporary = Path(handle.name)
                    handle.write(data)
                os.replace(temporary, args.output)
            finally:
                if temporary and temporary.exists():
                    temporary.unlink()
            report.update({"output": str(args.output), "glyph_groups": len(groups),
                           "baseline": ascent * scale, "advance": x,
                           "viewBox": [left, top, right-left, bottom-top]})
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 0
    except Exception as exc:
        print(f"outline_text: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
