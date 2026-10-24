#!/usr/bin/env python3
"""Validate brand-manual project control files and release readiness."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


REQUIRED_DIRS = (
    "00_PROJECT_CONTROL",
    "01_SOURCE_OF_TRUTH",
    "02_SOURCE_AUDIT",
    "05_CONTENT_ARCHITECTURE",
    "06_WORKING_SOURCE",
    "07_REVIEW_EXPORTS",
    "08_RELEASE_PACKAGE",
    "99_SUPERSEDED",
)

REQUIRED_CONTROL_FILES = (
    "00_PROJECT_CONTROL/brand_manual_project.json",
    "00_PROJECT_CONTROL/asset_register.csv",
    "00_PROJECT_CONTROL/decision_register.csv",
    "00_PROJECT_CONTROL/workstream_register.csv",
    "00_PROJECT_CONTROL/approval_log.csv",
    "00_PROJECT_CONTROL/qa_checklist.csv",
    "05_CONTENT_ARCHITECTURE/page_plan.csv",
)

REQUIRED_APPROVAL_GATES = {
    "GATE_0_SOURCE_AUTHORITY",
    "GATE_1_BRAND_SYSTEM",
    "GATE_A_MANUAL_STYLE",
    "GATE_B_CONTENT_FREEZE",
    "GATE_C_RELEASE",
}

ALLOWED_APPROVAL_STATUS = {
    "PENDING",
    "APPROVED",
    "PASS",
    "NOT_APPLICABLE",
    "REJECTED",
    "BLOCKED",
}

OUTPUT_EXTENSIONS = {
    "ai": {".ai"},
    "afpub": {".afpub"},
    "affinity": {".afpub"},
    "docx": {".docx"},
    "eps": {".eps"},
    "html": {".html", ".htm"},
    "idml": {".idml"},
    "indd": {".indd"},
    "pdf": {".pdf"},
    "pptx": {".pptx"},
    "svg": {".svg"},
}

EDITABLE_EXTENSIONS = {
    ".ai",
    ".afpub",
    ".docx",
    ".html",
    ".htm",
    ".idml",
    ".indd",
    ".pptx",
    ".svg",
}

FINAL_RELEASE_STATUSES = {"APPROVED_GUIDELINE", "PRODUCTION_RELEASE"}

ALLOWED_RULE_STATUS = {
    "OFFICIAL_SOURCE",
    "MEASURED_EVIDENCE",
    "WORKING_PROPOSAL",
    "APPROVAL_REQUIRED",
    "APPROVED_STANDARD",
    "DEFERRED",
    "SUPERSEDED",
    "",
}

ALLOWED_WORKSTREAM_STATUS = {
    "PLANNED",
    "ACTIVE",
    "BLOCKED",
    "COMPLETE",
    "NOT_APPLICABLE",
    "SUPERSEDED",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def release_payload_files(release_root: Path) -> list[Path]:
    files = []
    for path in release_root.rglob("*"):
        if not path.is_file() or path.name == ".DS_Store":
            continue
        relative = path.relative_to(release_root)
        if relative.parts and relative.parts[0] == "manifest":
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(release_root).as_posix())


def validate_release_manifest(
    release_root: Path,
    payload: list[Path],
    errors: list[str],
) -> dict:
    manifest_path = release_root / "manifest" / "release_manifest.json"
    if not manifest_path.is_file():
        errors.append(f"Missing release manifest: {manifest_path}")
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as error:
        errors.append(f"Invalid release manifest JSON: {error}")
        return {}

    records = manifest.get("files")
    if not isinstance(records, list) or not records:
        errors.append("Release manifest has no file records")
        return manifest

    listed: dict[str, dict] = {}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"Release manifest record {index} is not an object")
            continue
        relative_text = str(record.get("path", "")).strip()
        relative = Path(relative_text)
        if (
            not relative_text
            or relative.is_absolute()
            or ".." in relative.parts
            or not relative.parts
            or relative.parts[0] == "manifest"
        ):
            errors.append(f"Unsafe release manifest path: {relative_text or '<empty>'}")
            continue
        normalized = relative.as_posix()
        if normalized in listed:
            errors.append(f"Duplicate release manifest path: {normalized}")
            continue
        listed[normalized] = record

    actual = {
        path.relative_to(release_root).as_posix(): path
        for path in payload
    }
    for relative in sorted(set(actual) - set(listed)):
        errors.append(f"Release payload is not listed in manifest: {relative}")
    for relative in sorted(set(listed) - set(actual)):
        errors.append(f"Manifest lists a missing release payload: {relative}")
    for relative in sorted(set(actual) & set(listed)):
        path = actual[relative]
        record = listed[relative]
        if record.get("size_bytes") != path.stat().st_size:
            errors.append(f"Release manifest size mismatch: {relative}")
        expected = str(record.get("sha256", "")).lower()
        if len(expected) != 64 or expected != sha256(path):
            errors.append(f"Release manifest SHA-256 mismatch: {relative}")
    if manifest.get("file_count") != len(records):
        errors.append("Release manifest file_count does not match its records")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--release", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for directory in REQUIRED_DIRS:
        if not (root / directory).is_dir():
            errors.append(f"Missing directory: {directory}")

    for relative in REQUIRED_CONTROL_FILES:
        if not (root / relative).is_file():
            errors.append(f"Missing control file: {relative}")

    config_path = root / "00_PROJECT_CONTROL" / "brand_manual_project.json"
    if not config_path.exists():
        errors.append(f"Missing config: {config_path}")
        config = {}
    else:
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except Exception as error:
            errors.append(f"Invalid config JSON: {error}")
            config = {}

    for key in ("brand", "mode", "languages", "outputs", "authority", "gates"):
        if not config.get(key):
            errors.append(f"Config field is missing or empty: {key}")

    if config.get("mode") != "manual-only" and not (
        root / "03_BRAND_SYSTEM"
    ).is_dir():
        errors.append("Missing directory required by project mode: 03_BRAND_SYSTEM")
    if config.get("style_direction", "open") == "open" and not (
        root / "04_STYLE_TERRITORIES"
    ).is_dir():
        errors.append(
            "Missing directory required by open style direction: "
            "04_STYLE_TERRITORIES"
        )

    template = config.get("template", {})
    template_path = template.get("path", "")
    if template_path and not Path(template_path).expanduser().exists():
        warnings.append(f"Configured template does not exist: {template_path}")
    if template_path and template.get("rights_status") in ("", "VERIFY"):
        warnings.append("Template rights are not resolved")

    assets_path = root / "00_PROJECT_CONTROL" / "asset_register.csv"
    assets = read_csv(assets_path)
    if not assets:
        warnings.append("Asset register has no rows")
    for row_number, row in enumerate(assets, start=2):
        status = row.get("authority_status", "")
        if status not in ALLOWED_RULE_STATUS:
            errors.append(
                f"Asset register row {row_number} has invalid authority status: "
                f"{status}"
            )
        source = row.get("source_path", "").strip()
        if source and not Path(source).expanduser().exists():
            warnings.append(
                f"Asset register row {row_number} source is missing: {source}"
            )
        elif source and row.get("source_sha256", "").strip():
            if sha256(Path(source).expanduser()) != row["source_sha256"].strip().lower():
                warnings.append(
                    f"Asset register row {row_number} source changed after registration"
                )
        protected = row.get("protected_copy_path", "").strip()
        protected_digest = row.get("protected_copy_sha256", "").strip().lower()
        if not protected:
            warnings.append(
                f"Asset register row {row_number} has no protected source copy"
            )
        elif not Path(protected).expanduser().is_file():
            errors.append(
                f"Asset register row {row_number} protected copy is missing: {protected}"
            )
        elif (
            len(protected_digest) != 64
            or sha256(Path(protected).expanduser()) != protected_digest
        ):
            errors.append(
                f"Asset register row {row_number} protected-copy hash mismatch"
            )
        if status == "APPROVED_STANDARD" and not row.get("rights_status", "").strip():
            warnings.append(
                f"Approved asset row {row_number} has no rights status"
            )

    page_plan_path = root / "05_CONTENT_ARCHITECTURE" / "page_plan.csv"
    page_rows = read_csv(page_plan_path)
    page_ids: set[str] = set()
    for row_number, row in enumerate(page_rows, start=2):
        page_id = row.get("page_id", "").strip()
        if page_id in page_ids:
            errors.append(f"Duplicate page_id in row {row_number}: {page_id}")
        if page_id:
            page_ids.add(page_id)
        status = row.get("rule_status", "")
        if status not in ALLOWED_RULE_STATUS:
            errors.append(
                f"Page plan row {row_number} has invalid rule status: {status}"
            )

    workstream_path = root / "00_PROJECT_CONTROL" / "workstream_register.csv"
    workstreams = read_csv(workstream_path)
    if not workstream_path.exists():
        warnings.append("Workstream register is missing (legacy project)")
    workstream_ids: set[str] = set()
    for row_number, row in enumerate(workstreams, start=2):
        workstream_id = row.get("workstream_id", "").strip()
        if not workstream_id:
            errors.append(f"Workstream row {row_number} has no workstream_id")
        elif workstream_id in workstream_ids:
            errors.append(
                f"Duplicate workstream_id in row {row_number}: {workstream_id}"
            )
        else:
            workstream_ids.add(workstream_id)
        if not row.get("skill", "").strip():
            errors.append(f"Workstream row {row_number} has no skill")
        if not row.get("trigger", "").strip():
            errors.append(f"Workstream row {row_number} has no trigger")
        status = row.get("status", "").strip()
        if status not in ALLOWED_WORKSTREAM_STATUS:
            errors.append(
                f"Workstream row {row_number} has invalid status: {status}"
            )
        if status == "COMPLETE" and not row.get("output_refs", "").strip():
            errors.append(
                f"Completed workstream row {row_number} has no output_refs"
            )

    approvals = read_csv(root / "00_PROJECT_CONTROL" / "approval_log.csv")
    qa_rows = read_csv(root / "00_PROJECT_CONTROL" / "qa_checklist.csv")

    approval_gates: set[str] = set()
    for row_number, row in enumerate(approvals, start=2):
        gate = row.get("gate", "").strip()
        if not gate:
            errors.append(f"Approval row {row_number} has no gate")
        elif gate in approval_gates:
            errors.append(f"Duplicate approval gate in row {row_number}: {gate}")
        else:
            approval_gates.add(gate)
        status = row.get("status", "").strip()
        if status not in ALLOWED_APPROVAL_STATUS:
            errors.append(
                f"Approval row {row_number} has invalid status: {status or '<empty>'}"
            )
    for gate in sorted(REQUIRED_APPROVAL_GATES - approval_gates):
        errors.append(f"Approval log is missing gate: {gate}")

    if not qa_rows:
        errors.append("QA checklist has no rows")

    if args.release:
        if config.get("approver") in ("", "TBD", None):
            errors.append("Release validation requires a named approver")
        if not page_rows:
            errors.append("Release validation requires a populated page plan")
        unresolved_approvals = [
            row.get("gate", "UNKNOWN")
            for row in approvals
            if row.get("status") not in ("APPROVED", "PASS", "NOT_APPLICABLE")
        ]
        if unresolved_approvals:
            errors.append(
                "Unresolved approval gates: " + ", ".join(unresolved_approvals)
            )
        unresolved_qa = [
            row.get("qa_id", "UNKNOWN")
            for row in qa_rows
            if row.get("status") not in ("PASS", "NOT_APPLICABLE")
        ]
        if unresolved_qa:
            errors.append("Unresolved QA items: " + ", ".join(unresolved_qa))
        unresolved_workstreams = [
            row.get("workstream_id", "UNKNOWN")
            for row in workstreams
            if row.get("status")
            not in ("COMPLETE", "NOT_APPLICABLE", "SUPERSEDED")
        ]
        if unresolved_workstreams:
            errors.append(
                "Unresolved companion workstreams: "
                + ", ".join(unresolved_workstreams)
            )
        unresolved_config_gates = [
            gate
            for gate, status in config.get("gates", {}).items()
            if status not in ("APPROVED", "PASS", "NOT_APPLICABLE")
        ]
        if unresolved_config_gates:
            errors.append(
                "Config gate summary is unresolved: "
                + ", ".join(unresolved_config_gates)
            )

        release_root = root / "08_RELEASE_PACKAGE"
        release_files = release_payload_files(release_root)
        if not release_files:
            errors.append("Release package contains no payload files")
        manifest = validate_release_manifest(release_root, release_files, errors)

        actual_extensions = {path.suffix.lower() for path in release_files}
        for output in [str(item).lower() for item in config.get("outputs", [])]:
            expected_extensions = OUTPUT_EXTENSIONS.get(output)
            if expected_extensions is None:
                warnings.append(
                    f"Configured output cannot be verified by extension: {output}"
                )
            elif not actual_extensions & expected_extensions:
                errors.append(f"Configured release output is missing: {output}")

        release_status = manifest.get("release_status")
        if release_status in FINAL_RELEASE_STATUSES and not (
            actual_extensions & EDITABLE_EXTENSIONS
        ):
            errors.append(
                f"{release_status} requires at least one editable source file"
            )

    result = {
        "status": "PASS" if not errors else "FAIL",
        "root": str(root),
        "release_mode": args.release,
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "assets": len(assets),
            "page_plan_rows": len(page_rows),
            "workstreams": len(workstreams),
            "approvals": len(approvals),
            "qa_items": len(qa_rows),
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
