#!/usr/bin/env python3
"""Create deterministic local crops for visual-evidence inspection.

Examples:
  python crop_visual_regions.py image.png --output-dir /tmp/crops \
    --crop hood:0.20,0.00,0.60,0.35 --crop hem:0.05,0.65,0.90,0.30
  python crop_visual_regions.py image.png --output-dir /tmp/grid --grid 3x3

Crop coordinates are normalized when x,y,w,h are all between 0 and 1;
otherwise they are interpreted as pixels. Source files are never modified.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image


def safe_name(value: str) -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip()).strip("._")
    if not name:
        raise ValueError("crop name must contain a letter or number")
    return name


def parse_crop(spec: str, width: int, height: int) -> tuple[str, tuple[int, int, int, int], str]:
    try:
        name, raw = spec.split(":", 1)
        values = [float(part.strip()) for part in raw.split(",")]
    except ValueError as exc:
        raise ValueError(f"invalid crop {spec!r}; expected name:x,y,w,h") from exc
    if len(values) != 4:
        raise ValueError(f"invalid crop {spec!r}; expected four coordinates")

    x, y, w, h = values
    if w <= 0 or h <= 0:
        raise ValueError(f"invalid crop {spec!r}; width and height must be positive")

    normalized = all(0.0 <= value <= 1.0 for value in values)
    if normalized:
        left = round(x * width)
        top = round(y * height)
        right = round((x + w) * width)
        bottom = round((y + h) * height)
        mode = "normalized"
    else:
        left, top, right, bottom = round(x), round(y), round(x + w), round(y + h)
        mode = "pixels"

    left = max(0, min(width - 1, left))
    top = max(0, min(height - 1, top))
    right = max(left + 1, min(width, right))
    bottom = max(top + 1, min(height, bottom))
    return safe_name(name), (left, top, right, bottom), mode


def parse_grid(spec: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)x(\d+)", spec.lower().strip())
    if not match:
        raise ValueError("--grid must look like ROWSxCOLS, for example 3x3")
    rows, cols = int(match.group(1)), int(match.group(2))
    if not (1 <= rows <= 12 and 1 <= cols <= 12):
        raise ValueError("grid rows and columns must be between 1 and 12")
    return rows, cols


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--crop", action="append", default=[], help="name:x,y,w,h; normalized or pixels")
    parser.add_argument("--grid", help="ROWSxCOLS, for example 3x3")
    parser.add_argument("--upscale", type=float, default=1.0, help="crop preview scale, 1.0 to 8.0")
    args = parser.parse_args()

    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"input does not exist: {source}")
    if not args.crop and not args.grid:
        parser.error("provide at least one --crop or --grid")
    if not (1.0 <= args.upscale <= 8.0):
        parser.error("--upscale must be between 1.0 and 8.0")

    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as opened:
        image = opened.convert("RGB")
    width, height = image.size

    requests: list[tuple[str, tuple[int, int, int, int], str]] = []
    for spec in args.crop:
        requests.append(parse_crop(spec, width, height))

    if args.grid:
        rows, cols = parse_grid(args.grid)
        for row in range(rows):
            for col in range(cols):
                left = round(col * width / cols)
                top = round(row * height / rows)
                right = round((col + 1) * width / cols)
                bottom = round((row + 1) * height / rows)
                requests.append((f"grid_r{row + 1}_c{col + 1}", (left, top, right, bottom), "grid"))

    manifest = {
        "source": str(source),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_dimensions": [width, height],
        "upscale": args.upscale,
        "crops": [],
    }

    used: set[str] = set()
    for name, box, mode in requests:
        base = name
        suffix = 2
        while name in used:
            name = f"{base}_{suffix}"
            suffix += 1
        used.add(name)

        crop = image.crop(box)
        if args.upscale != 1.0:
            crop = crop.resize(
                (round(crop.width * args.upscale), round(crop.height * args.upscale)),
                Image.Resampling.LANCZOS,
            )
        output = output_dir / f"{name}.png"
        if output.exists():
            raise FileExistsError(f"refusing to overwrite existing crop: {output}")
        crop.save(output, format="PNG", optimize=True)
        manifest["crops"].append(
            {
                "name": name,
                "mode": mode,
                "source_box_px": list(box),
                "source_box_normalized": [
                    box[0] / width,
                    box[1] / height,
                    (box[2] - box[0]) / width,
                    (box[3] - box[1]) / height,
                ],
                "output": str(output),
                "output_dimensions": list(crop.size),
            }
        )

    manifest_path = output_dir / "crop-manifest.json"
    if manifest_path.exists():
        raise FileExistsError(f"refusing to overwrite existing manifest: {manifest_path}")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
