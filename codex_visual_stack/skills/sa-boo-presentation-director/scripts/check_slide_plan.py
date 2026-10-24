#!/usr/bin/env python3
"""Validate a presentation layout plan before authoring."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = ("number", "title", "message", "purpose", "silhouette", "density")
VALID_DENSITIES = {"open", "medium", "dense"}
MAX_TITLE_CHARS = 90


def add_issue(issues, severity, slide, code, message):
    issues.append(
        {
            "severity": severity,
            "slide": slide,
            "code": code,
            "message": message,
        }
    )


def validate(plan):
    issues = []
    slides = plan.get("slides") if isinstance(plan, dict) else None
    if not isinstance(slides, list) or not slides:
        add_issue(issues, "error", None, "missing_slides", "Plan must contain a non-empty slides array.")
        return issues

    seen_numbers = set()
    asset_uses = {}

    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            add_issue(issues, "error", index, "invalid_slide", "Slide entry must be an object.")
            continue

        slide_number = slide.get("number", index)
        if slide_number in seen_numbers:
            add_issue(issues, "error", slide_number, "duplicate_number", "Slide number is duplicated.")
        seen_numbers.add(slide_number)

        for field in REQUIRED_FIELDS:
            value = slide.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                add_issue(
                    issues,
                    "error",
                    slide_number,
                    "missing_field",
                    f"Required field '{field}' is missing.",
                )

        title = str(slide.get("title", ""))
        if len(title) > MAX_TITLE_CHARS:
            add_issue(
                issues,
                "warning",
                slide_number,
                "long_title",
                f"Title has {len(title)} characters; confirm it stays on one line.",
            )

        density = slide.get("density")
        if density and density not in VALID_DENSITIES:
            add_issue(
                issues,
                "error",
                slide_number,
                "invalid_density",
                f"Density must be one of {sorted(VALID_DENSITIES)}.",
            )

        body_words = slide.get("body_words")
        if isinstance(body_words, (int, float)):
            limits = {"open": 55, "medium": 95, "dense": 130}
            limit = limits.get(density)
            if limit and body_words > limit:
                add_issue(
                    issues,
                    "warning",
                    slide_number,
                    "word_budget",
                    f"{int(body_words)} body words exceed the {density} review threshold of {limit}.",
                )

        purpose = str(slide.get("purpose", "")).lower()
        asset = slide.get("primary_asset")
        text_only = bool(slide.get("text_only"))
        if purpose not in {"cover", "transition", "close"} and not asset and not text_only:
            add_issue(
                issues,
                "warning",
                slide_number,
                "missing_asset_decision",
                "Declare a primary asset or set text_only to true.",
            )

        if asset:
            asset_uses.setdefault(str(asset), []).append(slide_number)

        if slide.get("claim") and not slide.get("source"):
            add_issue(
                issues,
                "warning",
                slide_number,
                "claim_without_source",
                "Slide contains a claim but no source is recorded.",
            )

    for start in range(len(slides) - 2):
        trio = slides[start : start + 3]
        silhouettes = [item.get("silhouette") for item in trio if isinstance(item, dict)]
        if len(silhouettes) == 3 and len(set(silhouettes)) == 1:
            add_issue(
                issues,
                "warning",
                trio[0].get("number", start + 1),
                "repeated_silhouette",
                f"Silhouette '{silhouettes[0]}' repeats for three consecutive slides.",
            )

        densities = [item.get("density") for item in trio if isinstance(item, dict)]
        if len(densities) == 3 and densities == ["dense", "dense", "dense"]:
            add_issue(
                issues,
                "warning",
                trio[0].get("number", start + 1),
                "dense_run",
                "Three dense slides run consecutively; add a synthesis or breathing slide.",
            )

    for asset, slide_numbers in asset_uses.items():
        if len(slide_numbers) > 1:
            add_issue(
                issues,
                "warning",
                slide_numbers[0],
                "reused_asset",
                f"Primary asset '{asset}' is reused on slides {slide_numbers}.",
            )

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="JSON slide-plan path")
    parser.add_argument("--out", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read slide plan: {exc}", file=sys.stderr)
        return 2

    issues = validate(plan)
    errors = [issue for issue in issues if issue["severity"] == "error"]
    warnings = [issue for issue in issues if issue["severity"] == "warning"]
    report = {
        "valid": not errors,
        "errors": len(errors),
        "warnings": len(warnings),
        "issues": issues,
    }

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
