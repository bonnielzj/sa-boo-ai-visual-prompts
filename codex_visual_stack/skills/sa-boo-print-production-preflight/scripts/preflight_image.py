#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

from PIL import Image


Image.MAX_IMAGE_PIXELS = None


def parse_mm(value: str) -> tuple[float, float]:
    cleaned = value.lower().replace("mm", "").replace(" ", "")
    for sep in ("x", "×", ","):
        if sep in cleaned:
            left, right = cleaned.split(sep, 1)
            return float(left), float(right)
    raise argparse.ArgumentTypeError("target size must look like 13000x3000")


def get_dpi(im: Image.Image) -> tuple[float | None, float | None]:
    dpi = im.info.get("dpi")
    if isinstance(dpi, tuple) and len(dpi) >= 2:
        return float(dpi[0]), float(dpi[1])
    return None, None


def pct(value: float) -> float:
    return round(value * 100, 4)


def main() -> int:
    parser = argparse.ArgumentParser(description="Preflight image physical size, DPI, and ratio for large-format print.")
    parser.add_argument("--input", required=True, type=Path, help="Image file to inspect")
    parser.add_argument("--target-mm", required=True, type=parse_mm, help="Expected trim size, e.g. 13000x3000")
    parser.add_argument("--expected-dpi", type=float, default=None, help="Expected embedded DPI")
    parser.add_argument("--ratio-tolerance", type=float, default=0.005, help="Allowed ratio mismatch as decimal; default 0.005 = 0.5%")
    parser.add_argument("--dpi-tolerance", type=float, default=1.0, help="Allowed DPI metadata difference")
    parser.add_argument("--warn-only", action="store_true", help="Exit 0 even when checks fail")
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []
    path = args.input
    target_w_mm, target_h_mm = args.target_mm

    if not path.exists():
        print(json.dumps({"status": "FAIL", "failures": [f"input does not exist: {path}"]}, indent=2))
        return 0 if args.warn_only else 2

    with Image.open(path) as im:
        width_px, height_px = im.size
        dpi_x, dpi_y = get_dpi(im)

    target_ratio = target_w_mm / target_h_mm
    output_ratio = width_px / height_px
    ratio_delta = abs(output_ratio - target_ratio) / target_ratio

    if ratio_delta > args.ratio_tolerance:
        failures.append(
            f"ratio mismatch {pct(ratio_delta)}%: output {output_ratio:.6f}, target {target_ratio:.6f}"
        )

    physical_w_mm = physical_h_mm = None
    effective_dpi_x = width_px / target_w_mm * 25.4
    effective_dpi_y = height_px / target_h_mm * 25.4

    if dpi_x is None or dpi_y is None:
        warnings.append("missing embedded DPI metadata")
    else:
        physical_w_mm = width_px / dpi_x * 25.4
        physical_h_mm = height_px / dpi_y * 25.4
        physical_delta_w = abs(physical_w_mm - target_w_mm) / target_w_mm
        physical_delta_h = abs(physical_h_mm - target_h_mm) / target_h_mm
        if physical_delta_w > args.ratio_tolerance or physical_delta_h > args.ratio_tolerance:
            warnings.append(
                "embedded-DPI physical size differs from target: "
                f"{physical_w_mm:.1f}x{physical_h_mm:.1f}mm vs {target_w_mm:.1f}x{target_h_mm:.1f}mm"
            )

    if args.expected_dpi is not None:
        if dpi_x is None or dpi_y is None:
            warnings.append(f"cannot verify expected DPI {args.expected_dpi}: metadata missing")
        elif abs(dpi_x - args.expected_dpi) > args.dpi_tolerance or abs(dpi_y - args.expected_dpi) > args.dpi_tolerance:
            failures.append(f"DPI mismatch: embedded {dpi_x:.3f}x{dpi_y:.3f}, expected {args.expected_dpi}")

    status = "FAIL" if failures else ("WARN" if warnings else "PASS")
    report = {
        "status": status,
        "input": str(path),
        "pixel_size": [width_px, height_px],
        "embedded_dpi": [dpi_x, dpi_y],
        "target_size_mm": [target_w_mm, target_h_mm],
        "target_ratio": target_ratio,
        "output_ratio": output_ratio,
        "ratio_delta_percent": pct(ratio_delta),
        "physical_size_from_embedded_dpi_mm": [physical_w_mm, physical_h_mm],
        "effective_full_size_dpi_for_target": [effective_dpi_x, effective_dpi_y],
        "failures": failures,
        "warnings": warnings,
    }
    print(json.dumps(report, indent=2))
    if failures and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
