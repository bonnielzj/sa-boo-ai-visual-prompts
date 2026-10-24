#!/usr/bin/env python3
"""Build a deterministic SHA-256 manifest for a brand-manual release package."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


RELEASE_STATUSES = (
    "INTERNAL_WORKING_MANUAL",
    "CLIENT_REVIEW",
    "APPROVED_GUIDELINE",
    "PRODUCTION_RELEASE",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def payload_files(release_root: Path) -> list[Path]:
    files = []
    for path in release_root.rglob("*"):
        if not path.is_file() or path.name == ".DS_Store":
            continue
        relative = path.relative_to(release_root)
        if relative.parts and relative.parts[0] == "manifest":
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(release_root).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Initialized project root")
    parser.add_argument("--status", choices=RELEASE_STATUSES, required=True)
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    release_root = root / "08_RELEASE_PACKAGE"
    if not release_root.is_dir():
        raise SystemExit(f"Release package does not exist: {release_root}")

    files = payload_files(release_root)
    if not files:
        raise SystemExit("Release package has no payload files")

    records = []
    for path in files:
        records.append(
            {
                "path": path.relative_to(release_root).as_posix(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    manifest = {
        "schema_version": "1.0",
        "project_root": str(root),
        "release_status": args.status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "file_count": len(records),
        "files": records,
    }
    manifest_dir = release_root / "manifest"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    output = manifest_dir / "release_manifest.json"
    temporary = output.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(output)

    print(
        json.dumps(
            {
                "status": "created",
                "release_status": args.status,
                "manifest": str(output),
                "file_count": len(records),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
