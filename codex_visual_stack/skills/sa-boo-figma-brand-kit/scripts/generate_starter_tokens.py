#!/usr/bin/env python3
"""Generate SA&BOO starter design tokens as JSON and CSS variables."""
from __future__ import annotations
import argparse, json, pathlib, re

TOKENS = {
    "color": {
        "bg-deep": "#111111",
        "bg-ivory": "#F7F3EA",
        "surface-paper": "#EFE7D8",
        "text-primary": "#111111",
        "text-inverse": "#F7F3EA",
        "text-muted": "#8A8177",
        "border-subtle": "#E6DFD4",
        "accent-gold": "#C8AA73",
        "accent-bronze": "#8B6438",
        "accent-silver": "#9B9B9A",
        "accent-red": "#8A1F2D",
    },
    "spacing": {"2xs": 4, "xs": 8, "sm": 12, "md": 16, "lg": 24, "xl": 32, "2xl": 48, "3xl": 64, "4xl": 96},
    "radius": {"none": 0, "sm": 4, "md": 8, "lg": 16, "full": 999},
}

def css_name(*parts: str) -> str:
    raw = "-".join(parts)
    raw = re.sub(r"[^a-zA-Z0-9-]+", "-", raw).strip("-").lower()
    return f"--samboo-{raw}"

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=".", help="Output directory")
    args = p.parse_args()
    out = pathlib.Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    json_path = out / "samboo-brand-kit.tokens.flat.json"
    css_path = out / "samboo-brand-kit.css"

    json_path.write_text(json.dumps(TOKENS, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [":root {"]
    for group, values in TOKENS.items():
        for name, value in values.items():
            v = f"{value}px" if isinstance(value, (int, float)) else value
            lines.append(f"  {css_name(group, name)}: {v};")
    lines.append("}")
    css_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {css_path}")

if __name__ == "__main__":
    main()
