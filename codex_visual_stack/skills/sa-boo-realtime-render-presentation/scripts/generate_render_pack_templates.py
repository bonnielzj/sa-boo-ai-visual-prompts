#!/usr/bin/env python3
"""Generate SA&BOO render pack CSV templates."""
from __future__ import annotations
import argparse, csv, pathlib

SHOT_ROWS = [
    ["01", "Entry_Overall", "D5/Enscape/Twinmotion", "01_Entry_Overall", "After", "Soft Morning", "A", "establish layout and first impression", "Planned", ""],
    ["02", "Living_Overall", "D5/Enscape/Twinmotion", "02_Living_Overall", "After", "Soft Morning", "A", "main client decision view", "Planned", ""],
    ["03", "Living_BeforeAfter", "D5/Enscape/Twinmotion", "09_BeforeAfter_Main", "Before/After", "Matched", "A", "transformation proof", "Planned", "lock camera"],
    ["04", "Material_Detail", "D5/Enscape/Twinmotion", "07_Material_Detail", "After", "Gallery Accent", "A", "material confidence", "Planned", "check texture scale"],
    ["05", "Lighting_Evening", "D5/Enscape/Twinmotion", "08_Lighting_Evening", "After", "Warm Evening", "A", "lighting emotion", "Planned", ""],
    ["06", "Social_Cover_Crop", "D5/Enscape/Twinmotion", "10_Social_Cover_Crop", "After", "Editorial", "A", "XHS/Douyin cover", "Planned", "leave title safe space"],
]
QA_ROWS = [
    ["Model", "Units/scale correct", ""],
    ["Model", "No missing/duplicate surfaces", ""],
    ["Lighting", "One clear lighting story", ""],
    ["Lighting", "Exposure consistent across before/after", ""],
    ["Material", "Texture scale correct", ""],
    ["Material", "Reflection/roughness controlled", ""],
    ["Camera", "Verticals corrected", ""],
    ["Camera", "Before/after cameras locked", ""],
    ["Export", "Correct platform sizes", ""],
    ["Export", "Disclaimer added if conceptual", ""],
]

def write_csv(path: pathlib.Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=".")
    args = p.parse_args()
    out = pathlib.Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "render_shot_log_template.csv", ["Shot No", "File Name", "Tool", "Camera", "Scene State", "Lighting Story", "Material Option", "Purpose", "Status", "Notes"], SHOT_ROWS)
    write_csv(out / "render_qaqc_template.csv", ["Category", "Check", "Result/Notes"], QA_ROWS)
    print(f"Generated render pack templates in {out}")

if __name__ == "__main__":
    main()
