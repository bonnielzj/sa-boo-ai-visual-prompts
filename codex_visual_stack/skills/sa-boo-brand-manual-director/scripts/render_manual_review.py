#!/usr/bin/env python3
"""Render a PDF into labeled page PNGs and contact sheets."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


def render_pdf(pdf: Path, pages_dir: Path, dpi: int) -> tuple[list[Path], str]:
    executable = shutil.which("pdftoppm")
    if executable:
        prefix = pages_dir / "page"
        subprocess.run(
            [
                executable,
                "-png",
                "-r",
                str(dpi),
                str(pdf),
                str(prefix),
            ],
            check=True,
        )
        renderer = "pdftoppm"
    else:
        clang = shutil.which("clang")
        helper = Path(__file__).with_name("render_pdf_pages.m")
        if sys.platform != "darwin" or not clang or not helper.is_file():
            raise RuntimeError(
                "PDF rendering requires pdftoppm, or macOS clang/PDFKit + "
                f"{helper.name} as the native PDFKit fallback"
            )
        with tempfile.TemporaryDirectory(prefix="brand-manual-pdfkit-") as temporary:
            renderer_binary = Path(temporary) / "render_pdf_pages"
            subprocess.run(
                [
                    clang,
                    "-fobjc-arc",
                    "-framework",
                    "AppKit",
                    "-framework",
                    "PDFKit",
                    str(helper),
                    "-o",
                    str(renderer_binary),
                ],
                check=True,
            )
            subprocess.run(
                [str(renderer_binary), str(pdf), str(pages_dir), str(dpi)],
                check=True,
            )
        renderer = "macos-pdfkit"

    def page_number(path: Path) -> int:
        match = re.search(r"(\d+)$", path.stem)
        return int(match.group(1)) if match else 0

    pages = sorted(pages_dir.glob("page-*.png"), key=page_number)
    return pages, renderer


def make_contact_sheet(
    page_paths: list[Path],
    output: Path,
    columns: int,
    thumb_width: int,
    gap: int,
) -> None:
    loaded = [Image.open(path).convert("RGB") for path in page_paths]
    ratios = [image.height / image.width for image in loaded]
    thumb_height = int(thumb_width * max(ratios))
    label_height = 34
    rows = math.ceil(len(loaded) / columns)
    sheet = Image.new(
        "RGB",
        (
            columns * thumb_width + (columns + 1) * gap,
            rows * (thumb_height + label_height) + (rows + 1) * gap,
        ),
        "white",
    )
    draw = ImageDraw.Draw(sheet)

    for index, (path, image) in enumerate(zip(page_paths, loaded)):
        row, column = divmod(index, columns)
        x = gap + column * (thumb_width + gap)
        y = gap + row * (thumb_height + label_height + gap)
        fitted_height = int(thumb_width * image.height / image.width)
        thumb = image.resize((thumb_width, fitted_height), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        draw.text((x, y + thumb_height + 7), path.stem, fill="black")
        image.close()

    sheet.save(output, quality=90)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--dpi", type=int, default=120)
    parser.add_argument("--pages-per-sheet", type=int, default=8)
    parser.add_argument("--columns", type=int, default=2)
    args = parser.parse_args()

    pdf = Path(args.pdf).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not pdf.exists():
        raise SystemExit(f"PDF does not exist: {pdf}")
    if args.dpi < 1 or args.pages_per_sheet < 1 or args.columns < 1:
        raise SystemExit("dpi, pages-per-sheet, and columns must be positive")

    pages_dir = output / "pages"
    sheets_dir = output / "contact_sheets"
    pages_dir.mkdir(parents=True, exist_ok=True)
    sheets_dir.mkdir(parents=True, exist_ok=True)

    for old_page in pages_dir.glob("page-*.png"):
        old_page.unlink()
    for old_sheet in sheets_dir.glob("contact_sheet_*.jpg"):
        old_sheet.unlink()
    page_paths, renderer = render_pdf(pdf, pages_dir, args.dpi)
    if not page_paths:
        raise SystemExit("No pages were rendered")

    sheets = []
    for start in range(0, len(page_paths), args.pages_per_sheet):
        chunk = page_paths[start : start + args.pages_per_sheet]
        sheet_path = sheets_dir / (
            f"contact_sheet_{start // args.pages_per_sheet + 1:02d}.jpg"
        )
        make_contact_sheet(chunk, sheet_path, args.columns, 700, 36)
        sheets.append(str(sheet_path))

    print(
        json.dumps(
            {
                "status": "rendered",
                "pdf": str(pdf),
                "page_count": len(page_paths),
                "renderer": renderer,
                "pages_dir": str(pages_dir),
                "contact_sheets": sheets,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
