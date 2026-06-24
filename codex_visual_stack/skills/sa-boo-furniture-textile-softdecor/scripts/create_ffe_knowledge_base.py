#!/usr/bin/env python3
"""Create a starter SA&BOO furniture/textile/soft-decor knowledge base as CSV files."""
from __future__ import annotations
import argparse, csv, datetime as dt
from pathlib import Path

TABLES = {
    "objects.csv": [
        "item_id", "category", "subcategory", "room", "function", "visual_asset_ids", "source_url",
        "rights_status", "brand_or_designer", "product_or_archetype", "approx_dimensions_mm",
        "clearance_notes", "materials", "textile_performance", "construction_notes", "style_lineage",
        "aesthetic_verdict", "cad_layer_block", "sketchup_component", "render_notes", "supplier_status",
        "budget_band", "lead_time", "maintenance_risk", "related_items", "updated_at",
    ],
    "textiles.csv": [
        "textile_id", "fiber", "weave_or_surface", "use_case", "color_pattern", "supplier_source",
        "performance_tests", "cleaning_code", "flammability", "sustainability_certifications",
        "tactile_notes", "visual_asset_ids", "maintenance_risk", "updated_at",
    ],
    "sources.csv": [
        "source_id", "source_name", "url", "category", "license_rights", "access_date", "what_it_teaches",
        "usable_assets", "risks", "related_visual_asset_ids", "cad_su_relevance", "procurement_relevance",
    ],
    "cad_su_assets.csv": [
        "asset_id", "item_id", "file_path", "file_type", "units", "scale_verified", "polygon_weight",
        "tags_layers", "lod", "source_license", "quality_notes", "updated_at",
    ],
    "aesthetic_notes.csv": [
        "note_id", "project_or_context", "visual_asset_ids", "object_material", "why_it_worked",
        "why_it_fits_saboo", "what_to_avoid", "cad_su_render_implications", "updated_at",
    ],
}

EXAMPLES = {
    "objects.csv": [[
        "F-SOFA-0001", "seating", "sofa", "living room", "conversation + lounging", "", "", "reference-only",
        "custom/source TBD", "low modular sofa", "3200x1000x700", "verify 800-900mm main circulation",
        "linen blend upholstery; wood/hidden base", "abrasion/cleaning TBD", "wood frame; loose cushions",
        "low modern / East-West calm living", "quiet low silhouette; textile must carry warmth without visual noise",
        "I-FURN-LOOS-N / F-SOFA-001", "FFE_SEATING / LOD2", "show fabric grain in one detail view", "source", "TBD", "TBD", "light fabric staining risk", "", dt.date.today().isoformat(),
    ]]
}

def write_csv(path: Path, header: list[str], rows: list[list[str]] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows or []:
            w.writerow(row)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Output directory for CSV knowledge base")
    ap.add_argument("--with-example", action="store_true", help="Add one example sofa row")
    args = ap.parse_args()
    out = Path(args.out).expanduser().resolve()
    for filename, header in TABLES.items():
        write_csv(out / filename, header, EXAMPLES.get(filename, []) if args.with_example else [])
    (out / "README.txt").write_text(
        "SA&BOO furniture/textile/soft-decor starter knowledge base. "
        "Use with sa-boo-furniture-textile-softdecor and sa-boo-visual-asset-index.\n",
        encoding="utf-8",
    )
    print(f"Created {len(TABLES)} CSV tables in {out}")

if __name__ == "__main__":
    main()
