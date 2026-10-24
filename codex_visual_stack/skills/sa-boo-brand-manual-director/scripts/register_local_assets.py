#!/usr/bin/env python3
"""Register local brand-manual source assets in the project control ledger."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path


FIELDS = [
    "asset_id",
    "asset_role",
    "authority_status",
    "source_path",
    "source_sha256",
    "protected_copy_path",
    "protected_copy_sha256",
    "working_copy_path",
    "rights_status",
    "editability",
    "notes",
]

ALLOWED_STATUS = (
    "OFFICIAL_SOURCE",
    "MEASURED_EVIDENCE",
    "WORKING_PROPOSAL",
    "APPROVAL_REQUIRED",
    "APPROVED_STANDARD",
    "DEFERRED",
    "SUPERSEDED",
)


def split_extensions(value: str) -> set[str]:
    return {
        item.strip().lower().lstrip(".")
        for item in value.split(",")
        if item.strip()
    }


def infer_editability(path: Path) -> str:
    extension = path.suffix.lower()
    if extension in {".ai", ".eps", ".svg"}:
        return "EDITABLE_VECTOR"
    if extension in {".indd", ".idml", ".afpub"}:
        return "EDITABLE_LAYOUT"
    if extension in {".pptx", ".docx", ".xlsx", ".key"}:
        return "EDITABLE_DOCUMENT"
    if extension == ".pdf":
        return "INSPECT_REQUIRED"
    if extension in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".gif"}:
        return "RASTER_REFERENCE"
    if extension in {".otf", ".ttf", ".woff", ".woff2"}:
        return "FONT_FILE"
    return "UNKNOWN"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def protected_copy(
    source: Path,
    source_digest: str,
    destination_dir: Path,
    asset_id: str,
) -> tuple[Path, str]:
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / f"{asset_id}__{source.name}"
    shutil.copy2(source, destination)
    copied_digest = sha256(destination)
    if copied_digest != source_digest:
        destination.unlink(missing_ok=True)
        raise RuntimeError(f"Protected-copy hash mismatch: {source}")
    return destination, copied_digest


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def next_asset_number(rows: list[dict[str, str]]) -> int:
    numbers = []
    for row in rows:
        match = re.search(r"(\d+)$", row.get("asset_id", ""))
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def source_files(
    sources: list[Path],
    extensions: set[str],
    include_hidden: bool,
) -> list[Path]:
    files: set[Path] = set()
    for source in sources:
        if source.is_file():
            candidates = [source]
        elif source.is_dir():
            candidates = [path for path in source.rglob("*") if path.is_file()]
        else:
            raise SystemExit(f"Source does not exist: {source}")
        for path in candidates:
            if not include_hidden and any(part.startswith(".") for part in path.parts):
                continue
            if extensions and path.suffix.lower().lstrip(".") not in extensions:
                continue
            files.add(path.resolve())
    return sorted(files, key=lambda path: str(path).casefold())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Initialized project root")
    parser.add_argument(
        "--source",
        action="append",
        required=True,
        help="Source file or directory; repeat for multiple sources",
    )
    parser.add_argument("--asset-role", default="source-evidence")
    parser.add_argument(
        "--authority-status",
        choices=ALLOWED_STATUS,
        default="MEASURED_EVIDENCE",
    )
    parser.add_argument("--rights-status", default="VERIFY")
    parser.add_argument(
        "--extensions",
        default="",
        help="Optional comma-separated extension filter",
    )
    parser.add_argument("--include-hidden", action="store_true")
    parser.add_argument(
        "--snapshot-mode",
        choices=("copy", "none"),
        default="copy",
        help=(
            "Copy each source into 01_SOURCE_OF_TRUTH and verify SHA-256 "
            "(default: copy). Use none only when a protected snapshot already exists."
        ),
    )
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    register = root / "00_PROJECT_CONTROL" / "asset_register.csv"
    if not register.exists():
        raise SystemExit(
            "Asset register does not exist. Initialize the project first: "
            f"{register}"
        )

    sources = [Path(item).expanduser().resolve() for item in args.source]
    files = source_files(
        sources,
        split_extensions(args.extensions),
        args.include_hidden,
    )
    rows = read_rows(register)
    existing = {
        str(Path(row["source_path"]).expanduser().resolve())
        for row in rows
        if row.get("source_path", "").strip()
    }
    number = next_asset_number(rows)
    added = []
    protected_dir = root / "01_SOURCE_OF_TRUTH"

    for path in files:
        if str(path) in existing:
            continue
        asset_id = f"ASSET-{number:04d}"
        source_digest = sha256(path)
        protected_path = ""
        protected_digest = ""
        if args.snapshot_mode == "copy":
            copied_path, protected_digest = protected_copy(
                path,
                source_digest,
                protected_dir,
                asset_id,
            )
            protected_path = str(copied_path)
        row = {
            "asset_id": asset_id,
            "asset_role": args.asset_role,
            "authority_status": args.authority_status,
            "source_path": str(path),
            "source_sha256": source_digest,
            "protected_copy_path": protected_path,
            "protected_copy_sha256": protected_digest,
            "working_copy_path": "",
            "rights_status": args.rights_status,
            "editability": infer_editability(path),
            "notes": args.note,
        }
        rows.append(row)
        added.append(row["asset_id"])
        existing.add(str(path))
        number += 1

    with register.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(
        json.dumps(
            {
                "status": "updated",
                "register": str(register),
                "scanned_files": len(files),
                "added_count": len(added),
                "added_ids": added,
                "total_rows": len(rows),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
