#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("audit_reference_library.py")


def valid_record(base: Path) -> dict:
    return {
        "asset_id": "VA-test",
        "title": "test asset",
        "source_page_url": "https://example.com/project",
        "original_image_url": "https://example.com/image.jpg",
        "local_image_path": str(base / "images" / "asset.jpg"),
        "local_thumbnail_path": str(base / "thumbs" / "asset.jpg"),
        "captured_at": "2026-01-01T00:00:00+00:00",
        "tags": ["test"],
        "category": "test",
        "quality_notes": "test fixture",
        "rights_status": "reference-only",
        "prev_id": None,
        "next_id": None,
    }


class AuditReferenceLibraryTest(unittest.TestCase):
    def test_hidden_non_image_files_do_not_change_asset_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for name in ["images", "thumbs", "index"]:
                (base / name).mkdir()
            (base / "images" / "asset.jpg").write_bytes(b"fixture")
            (base / "thumbs" / "asset.jpg").write_bytes(b"fixture")
            (base / "images" / ".DS_Store").write_bytes(b"metadata")
            (base / "thumbs" / ".DS_Store").write_bytes(b"metadata")
            record = valid_record(base)
            (base / "index" / "visual_assets.jsonl").write_text(
                json.dumps(record) + "\n", encoding="utf-8"
            )

            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(base)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["images"], 1)
            self.assertEqual(report["thumbs"], 1)


if __name__ == "__main__":
    unittest.main()
