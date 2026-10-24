#!/usr/bin/env python3
"""Initialize a brand-manual project with reusable control ledgers."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from datetime import date, datetime
from pathlib import Path


MODES = (
    "existing-governance",
    "brand-refresh",
    "new-identity",
    "manual-only",
)

BASE_DIRECTORIES = (
    "00_PROJECT_CONTROL",
    "01_SOURCE_OF_TRUTH",
    "02_SOURCE_AUDIT",
    "05_CONTENT_ARCHITECTURE",
    "06_WORKING_SOURCE",
    "07_REVIEW_EXPORTS/pages",
    "07_REVIEW_EXPORTS/contact_sheets",
    "08_RELEASE_PACKAGE/editable",
    "08_RELEASE_PACKAGE/pdf",
    "08_RELEASE_PACKAGE/assets",
    "08_RELEASE_PACKAGE/fonts_or_license_notes",
    "08_RELEASE_PACKAGE/approvals",
    "08_RELEASE_PACKAGE/qa",
    "08_RELEASE_PACKAGE/manifest",
    "99_SUPERSEDED",
)

ADOBE_OUTPUTS = {"ai", "indd", "idml"}

GENERATED_CONTROL_FILES = (
    "00_PROJECT_CONTROL/brand_manual_project.json",
    "00_PROJECT_CONTROL/asset_register.csv",
    "00_PROJECT_CONTROL/decision_register.csv",
    "00_PROJECT_CONTROL/workstream_register.csv",
    "00_PROJECT_CONTROL/approval_log.csv",
    "00_PROJECT_CONTROL/qa_checklist.csv",
    "05_CONTENT_ARCHITECTURE/page_plan.csv",
)


def backend_directories(outputs: list[str]) -> list[str]:
    lowered = {item.lower() for item in outputs}
    directories: list[str] = []
    if lowered & ADOBE_OUTPUTS:
        directories.extend(
            (
                "06_WORKING_SOURCE/adobe/illustrator",
                "06_WORKING_SOURCE/adobe/indesign",
                "06_WORKING_SOURCE/adobe/scripts",
            )
        )
    if "figma" in lowered:
        directories.append("06_WORKING_SOURCE/figma")
    if "pptx" in lowered:
        directories.append("06_WORKING_SOURCE/presentation")
    if "docx" in lowered:
        directories.append("06_WORKING_SOURCE/document")
    if "html" in lowered:
        directories.append("06_WORKING_SOURCE/web")
    if lowered & {"afpub", "affinity"}:
        directories.append("06_WORKING_SOURCE/affinity")
    if lowered & {"idml", "svg", "eps", "html"}:
        directories.append("08_RELEASE_PACKAGE/compatibility")
    return directories


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "brand"


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Project output directory")
    parser.add_argument("--brand", required=True)
    parser.add_argument("--mode", choices=MODES, required=True)
    parser.add_argument("--languages", default="en")
    parser.add_argument("--outputs", default="pdf")
    parser.add_argument("--template", default="")
    parser.add_argument("--approver", default="TBD")
    parser.add_argument(
        "--style-direction",
        choices=("open", "fixed"),
        default="open",
    )
    parser.add_argument("--applications", default="")
    parser.add_argument("--qualities", default="")
    parser.add_argument("--avoid", default="")
    parser.add_argument("--fixed", default="")
    parser.add_argument("--develop", default="")
    parser.add_argument("--verify", default="")
    parser.add_argument("--defer", default="")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reinitialize control templates after backing up every overwritten file",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    config_path = root / "00_PROJECT_CONTROL" / "brand_manual_project.json"
    if config_path.exists() and not args.force:
        raise SystemExit(
            f"Project already initialized: {config_path}. Use --force to replace "
            "control templates after creating a backup."
        )

    backup_root = None
    existing_control_files = [
        root / relative
        for relative in GENERATED_CONTROL_FILES
        if (root / relative).is_file()
    ]
    if args.force and existing_control_files:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup_root = root / "99_SUPERSEDED" / f"control_backup_{timestamp}"
        for source in existing_control_files:
            relative = source.relative_to(root)
            destination = backup_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    outputs = split_values(args.outputs)
    root.mkdir(parents=True, exist_ok=True)
    project_directories = list(BASE_DIRECTORIES) + backend_directories(outputs)
    if args.mode != "manual-only":
        project_directories.append("03_BRAND_SYSTEM")
    if args.style_direction == "open":
        project_directories.append("04_STYLE_TERRITORIES")
    for directory in project_directories:
        (root / directory).mkdir(parents=True, exist_ok=True)

    created = date.today().isoformat()
    brand_system_gate = (
        "NOT_APPLICABLE" if args.mode == "manual-only" else "PENDING"
    )
    manual_style_gate = (
        "NOT_APPLICABLE" if args.style_direction == "fixed" else "PENDING"
    )
    config = {
        "schema_version": "1.1",
        "project_id": f"{slugify(args.brand)}-brand-manual",
        "brand": args.brand,
        "mode": args.mode,
        "status": "INTAKE",
        "created": created,
        "languages": split_values(args.languages),
        "outputs": outputs,
        "style_direction": args.style_direction,
        "template": {
            "path": str(Path(args.template).expanduser()) if args.template else "",
            "rights_status": "VERIFY" if args.template else "NOT_APPLICABLE",
            "adaptation": "TBD" if args.template else "REBUILD_OR_CREATE",
        },
        "authority": {
            "fixed": split_values(args.fixed),
            "develop": split_values(args.develop),
            "verify": split_values(args.verify),
            "defer": split_values(args.defer),
        },
        "approver": args.approver,
        "reviewers": [],
        "priority_applications": split_values(args.applications),
        "style": {
            "qualities": split_values(args.qualities),
            "avoid": split_values(args.avoid),
            "variables": {
                "authority": None,
                "experimentation": None,
                "warmth": None,
                "play": None,
                "density": None,
                "image_dominance": None,
                "tactility": None,
                "motion": None,
            },
        },
        "gates": {
            "source_authority": "PENDING",
            "brand_system": brand_system_gate,
            "manual_style": manual_style_gate,
            "content_freeze": "PENDING",
            "release": "PENDING",
        },
    }
    config_path.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    control = root / "00_PROJECT_CONTROL"
    write_csv(
        control / "asset_register.csv",
        [
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
        ],
        [],
    )
    write_csv(
        control / "decision_register.csv",
        [
            "decision_id",
            "topic",
            "status",
            "decision",
            "owner",
            "decision_date",
            "evidence_path",
            "notes",
        ],
        [],
    )
    write_csv(
        control / "workstream_register.csv",
        [
            "workstream_id",
            "skill",
            "trigger",
            "stage",
            "input_refs",
            "output_refs",
            "status",
            "gate_dependency",
            "owner",
            "updated_at",
            "notes",
        ],
        [],
    )
    gate_rows = (
        ("GATE_0_SOURCE_AUTHORITY", "PENDING"),
        ("GATE_1_BRAND_SYSTEM", brand_system_gate),
        ("GATE_A_MANUAL_STYLE", manual_style_gate),
        ("GATE_B_CONTENT_FREEZE", "PENDING"),
        ("GATE_C_RELEASE", "PENDING"),
    )
    write_csv(
        control / "approval_log.csv",
        [
            "gate",
            "status",
            "approver",
            "approval_date",
            "approved_version",
            "evidence_path",
            "notes",
        ],
        [
            {
                "gate": gate,
                "status": status,
                "approver": args.approver,
                "approval_date": "",
                "approved_version": "",
                "evidence_path": "",
                "notes": "",
            }
            for gate, status in gate_rows
        ],
    )
    write_csv(
        root / "05_CONTENT_ARCHITECTURE" / "page_plan.csv",
        [
            "page_id",
            "section",
            "purpose",
            "rule_status",
            "source_assets",
            "copy_status",
            "density",
            "reviewer",
            "qa_risk",
            "notes",
        ],
        [],
    )

    qa_rows = [
        ("content", "authoritative sources named"),
        ("content", "rule statuses visible"),
        ("content", "approvals include owner date and version"),
        ("content", "activated companion workstreams link one bounded output"),
        ("source", "protected source copies exist and hashes match originals"),
        ("editorial", "contents and page numbering correct"),
        ("editorial", "smallest type and bilingual text legible"),
        ("editorial", "all languages render without missing glyph or tofu boxes"),
        ("editorial", "headings and brand terms have no accidental hyphenation"),
        ("editorial", "no silent auto-fit or font shrinking damages hierarchy"),
        ("editorial", "logo proportions and clear space intact"),
        ("source", "editable source opens and saves correctly"),
        ("source", "missing assets fonts or links equal zero"),
        ("source", "overflow or clipped content equals zero"),
        ("source", "requested exports complete without error"),
        ("visual", "all pages rendered and contact sheets inspected"),
        ("visual", "dense and full-bleed pages spot checked"),
        ("release", "template and asset rights recorded"),
        ("release", "requested review and compatibility exports open correctly"),
        ("release", "release manifest lists every payload file with verified SHA-256"),
        ("release", "all configured output formats are present"),
        ("release", "approval evidence is complete"),
        ("release", "no companion workstream remains planned active or blocked"),
    ]
    if {item.lower() for item in outputs} & ADOBE_OUTPUTS:
        qa_rows.extend(
            [
                ("adobe", "InDesign or Illustrator native preflight passed"),
                ("adobe", "Adobe links fonts and overset checks passed"),
                ("adobe", "rendered multilingual glyph coverage visually passed"),
            ]
        )
    if "idml" in {item.lower() for item in outputs}:
        qa_rows.append(("adobe", "IDML compatibility opens correctly"))
    write_csv(
        control / "qa_checklist.csv",
        ["qa_id", "category", "check", "status", "evidence_path", "notes"],
        [
            {
                "qa_id": f"QA-{index:02d}",
                "category": category,
                "check": check,
                "status": "PENDING",
                "evidence_path": "",
                "notes": "",
            }
            for index, (category, check) in enumerate(qa_rows, start=1)
        ],
    )

    print(
        json.dumps(
            {
                "status": "created",
                "brand": args.brand,
                "mode": args.mode,
                "root": str(root),
                "config": str(config_path),
                "control_backup": str(backup_root) if backup_root else "",
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
