#!/usr/bin/env python3
"""Integration tests for the reusable brand-manual control scripts."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


SCRIPTS = Path(__file__).resolve().parent
INIT = SCRIPTS / "init_brand_manual_project.py"
REGISTER = SCRIPTS / "register_local_assets.py"
VALIDATE = SCRIPTS / "validate_brand_manual_project.py"
MANIFEST = SCRIPTS / "build_release_manifest.py"
RENDER = SCRIPTS / "render_manual_review.py"
EDITORIAL = SCRIPTS / "check_editorial_pages.py"


def run(*args: object, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        check=check,
        capture_output=True,
        text=True,
    )


def initialize(root: Path, outputs: str = "pdf") -> None:
    run(
        INIT,
        "--root",
        root,
        "--brand",
        "Smoke Test Brand",
        "--mode",
        "manual-only",
        "--style-direction",
        "fixed",
        "--outputs",
        outputs,
        "--approver",
        "the user",
    )


def update_csv(path: Path, mutator) -> None:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    mutator(rows)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


class BrandManualToolTests(unittest.TestCase):
    def test_editorial_readback_catches_frozen_figma_text_height(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "readback.json"
            source.write_text(json.dumps({"pages": [{
                "id": "p1", "name": "Identity introduction", "width": 1600, "height": 1000,
                "nodes": [
                    {"id": "clipped", "name": "Title / zh", "characters": "作品走进日常",
                     "x": 96, "y": 100, "width": 800, "height": 10,
                     "fontSize": 40, "lineHeight": {"unit": "PIXELS", "value": 48}},
                    {"id": "reading", "name": "Introduction", "characters": "Art enters everyday life.",
                     "x": 96, "y": 200, "width": 800, "height": 60,
                     "fontSize": 32, "lineHeight": {"unit": "PIXELS", "value": 40}}
                ]
            }]}), encoding="utf-8")
            result = run(EDITORIAL, source, check=False)
            self.assertEqual(result.returncode, 1)
            report = json.loads(result.stdout)
            self.assertEqual(len(report["violations"]), 1)
            issue = report["violations"][0]
            self.assertEqual(issue["code"], "degenerate_text_height")
            self.assertEqual(issue["nodeId"], "clipped")
            self.assertEqual(issue["lineHeight"], {"unit": "PIXELS", "value": 48})

    def test_editorial_readback_catches_lower_margin_and_missing_english(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "readback.json"
            source.write_text(json.dumps({"pages": [{
                "id": "p1", "name": "Chapter bridge", "width": 1600, "height": 1000,
                "nodes": [{"id": "t1", "name": "Copy / zh / intro",
                           "characters": "作品走进日常。", "x": 96, "y": 800,
                           "width": 600, "height": 40, "bilingualRequired": True}]
            }]}), encoding="utf-8")
            result = run(EDITORIAL, source, check=False)
            self.assertEqual(result.returncode, 1)
            report = json.loads(result.stdout)
            self.assertEqual({item["code"] for item in report["violations"]},
                             {"content_bottom", "missing_bilingual_copy"})
            self.assertTrue(all(item["pageId"] == "p1" for item in report["violations"]))
            self.assertIn("Copy / en / intro", report["violations"][1]["message"])

    def test_editorial_readback_preserves_declared_bleed_and_footer(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "readback.json"
            source.write_text(json.dumps({"pages": [{
                "id": "p1", "name": "Chapter bridge", "width": 1600, "height": 1000,
                "nodes": [
                    {"id": "zh", "name": "Copy / zh / intro", "characters": "作品走进日常。",
                     "x": 96, "y": 100, "width": 600, "height": 40},
                    {"id": "en", "name": "Copy / en / intro", "characters": "Art enters everyday life.",
                     "x": 96, "y": 160, "width": 700, "height": 50},
                    {"id": "display", "name": "Display / AllowBleed", "characters": "COMMUNITY",
                     "x": -40, "y": 300, "width": 1700, "height": 300},
                    {"id": "footer", "name": "Footer / Number", "characters": "06",
                     "x": 16, "y": 960, "width": 30, "height": 24}
                ]
            }]}), encoding="utf-8")
            result = run(EDITORIAL, source)
            report = json.loads(result.stdout)
            self.assertEqual(report["violations"], [])
            self.assertEqual(report["checkedBilingualRoles"], 1)
            self.assertIn("require visual review", report["scope"])

    def test_force_reinitialize_backs_up_control_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"
            initialize(root)
            decision_register = root / "00_PROJECT_CONTROL" / "decision_register.csv"
            original = decision_register.read_bytes()

            result = run(
                INIT,
                "--root",
                root,
                "--brand",
                "Smoke Test Brand",
                "--mode",
                "manual-only",
                "--style-direction",
                "fixed",
                "--outputs",
                "pdf",
                "--approver",
                "the user",
                "--force",
            )
            payload = json.loads(result.stdout)
            backup = Path(payload["control_backup"])
            protected = backup / "00_PROJECT_CONTROL" / "decision_register.csv"
            self.assertTrue(protected.is_file())
            self.assertEqual(protected.read_bytes(), original)

    def test_register_creates_verified_protected_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / "project"
            source = base / "client-logo.svg"
            source.write_text("<svg xmlns='http://www.w3.org/2000/svg'></svg>\n")
            initialize(root)

            run(REGISTER, "--root", root, "--source", source)

            register = root / "00_PROJECT_CONTROL" / "asset_register.csv"
            with register.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            row = rows[0]
            protected = Path(row["protected_copy_path"])
            self.assertTrue(protected.is_file())
            self.assertEqual(row["source_sha256"], row["protected_copy_sha256"])
            self.assertEqual(len(row["source_sha256"]), 64)

            result = run(VALIDATE, "--root", root)
            self.assertIn('"status": "PASS"', result.stdout)

    def test_validator_rejects_missing_control_ledgers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"
            initialize(root)
            (root / "00_PROJECT_CONTROL" / "approval_log.csv").unlink()
            (root / "00_PROJECT_CONTROL" / "qa_checklist.csv").unlink()

            result = run(VALIDATE, "--root", root, "--release", check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing control file", result.stdout)
            self.assertIn("Approval log is missing gate", result.stdout)
            self.assertIn("QA checklist has no rows", result.stdout)

    def test_client_review_release_manifest_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"
            initialize(root)

            config_path = root / "00_PROJECT_CONTROL" / "brand_manual_project.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            for gate, status in list(config["gates"].items()):
                if status != "NOT_APPLICABLE":
                    config["gates"][gate] = "APPROVED"
            config_path.write_text(
                json.dumps(config, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            update_csv(
                root / "00_PROJECT_CONTROL" / "approval_log.csv",
                lambda rows: [row.update(status="APPROVED") for row in rows],
            )
            update_csv(
                root / "00_PROJECT_CONTROL" / "qa_checklist.csv",
                lambda rows: [row.update(status="PASS") for row in rows],
            )

            page_plan = root / "05_CONTENT_ARCHITECTURE" / "page_plan.csv"
            with page_plan.open(encoding="utf-8-sig", newline="") as handle:
                fields = list(csv.DictReader(handle).fieldnames or [])
            with page_plan.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow(
                    {
                        "page_id": "P-001",
                        "section": "cover",
                        "purpose": "review cover",
                        "rule_status": "APPROVED_STANDARD",
                        "copy_status": "APPROVED",
                    }
                )

            pdf = root / "08_RELEASE_PACKAGE" / "pdf" / "manual.pdf"
            pdf.write_bytes(b"%PDF-1.4\n% structural smoke fixture\n")
            run(MANIFEST, "--root", root, "--status", "CLIENT_REVIEW")

            result = run(VALIDATE, "--root", root, "--release")
            self.assertIn('"status": "PASS"', result.stdout)

            pdf.write_bytes(pdf.read_bytes() + b"changed\n")
            changed = run(VALIDATE, "--root", root, "--release", check=False)
            self.assertNotEqual(changed.returncode, 0)
            self.assertIn("SHA-256 mismatch", changed.stdout)

            run(MANIFEST, "--root", root, "--status", "APPROVED_GUIDELINE")
            final_without_source = run(
                VALIDATE,
                "--root",
                root,
                "--release",
                check=False,
            )
            self.assertNotEqual(final_without_source.returncode, 0)
            self.assertIn("requires at least one editable source file", final_without_source.stdout)

    @unittest.skipUnless(
        shutil.which("pdftoppm")
        or (sys.platform == "darwin" and shutil.which("clang")),
        "No supported PDF renderer is available",
    )
    def test_render_manual_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            pdf = base / "two-pages.pdf"
            first = Image.new("RGB", (240, 160), "white")
            second = Image.new("RGB", (240, 160), "black")
            Image.init()
            first.save(pdf, save_all=True, append_images=[second])
            first.close()
            second.close()

            output = base / "review"
            run(RENDER, "--pdf", pdf, "--output", output, "--dpi", "48")
            pages = sorted((output / "pages").glob("page-*.png"))
            self.assertEqual(len(pages), 2)
            with Image.open(pages[0]).convert("RGB") as rendered_first:
                center = rendered_first.getpixel(
                    (rendered_first.width // 2, rendered_first.height // 2)
                )
                self.assertTrue(all(channel > 240 for channel in center))
            with Image.open(pages[1]).convert("RGB") as rendered_second:
                center = rendered_second.getpixel(
                    (rendered_second.width // 2, rendered_second.height // 2)
                )
                self.assertTrue(all(channel < 15 for channel in center))
            self.assertTrue(
                (output / "contact_sheets" / "contact_sheet_01.jpg").is_file()
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
