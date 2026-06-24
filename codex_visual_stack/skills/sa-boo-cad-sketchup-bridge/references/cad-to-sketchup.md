# CAD to SketchUp Checklist

Use this when preparing DWG/DXF linework for SketchUp white modeling.

## 1. Source preservation

- Never overwrite the original drawing.
- Copy source CAD into `01_CAD_Original`.
- Create working clean file in `02_CAD_Clean_For_SU`.
- Keep revision suffix: `R00`, `R01`, etc.

## 2. CAD audit

Check:

- Units: millimeters preferred for interiors.
- Model space: useful geometry should be in model space, not only paper space.
- Extents: no remote geometry far from the project.
- Xrefs: bind, detach, or keep only if intentionally needed.
- Blocks: explode or simplify only in the SU clean copy.
- Hatches: remove unless needed as material-zone reference.
- Text/dimensions: remove or keep only a small reference set.
- Duplicate lines and tiny gaps: clean before import or plan Edge Tools cleanup in SketchUp.

## 3. What to keep for SU import

Keep:

- Wall outlines and structural limits.
- Door/window openings and swing reference if useful.
- Fixed furniture/cabinetry outlines.
- Main ceiling control lines.
- Floor finish divisions if relevant.
- Key elevations and datum lines.
- Critical dimensions as optional reference layer.

Remove or isolate:

- Title blocks and layout frames.
- Dense hatches.
- General notes.
- Leader annotations.
- Repeated symbols.
- Electrical symbols unless modeling lighting positions.
- Plumbing/equipment details unless needed for spatial conflict.

## 4. Suggested SU-clean CAD layers

```text
X-SU-REF-PLAN
X-SU-REF-WALL
X-SU-REF-OPENING
X-SU-REF-FURN
X-SU-REF-CEILING
X-SU-REF-FLOOR
X-SU-REF-ELEV
X-SU-REF-DIM
X-SU-NPLT-GRID
```

## 5. Import into SketchUp

- Import units: millimeters unless evidence says otherwise.
- Preserve drawing origin only when project coordinates matter; otherwise work near SketchUp origin for modeling stability.
- Group imported CAD immediately and lock it.
- Put it on `CAD_REF_PLAN` or similar SketchUp tag.
- Check a known dimension with Tape Measure.
- Create a clean model group/component structure rather than modeling on raw imported edges.

## 6. SketchUp cleanup after import

Use:

- `sketchup-edge-tools-cleanup` for gaps, strays, and imported broken lines.
- `sketchup-flatten-faces-cleanup` for off-plane or projection cleanup when useful.
- `sketchup-1001bit-architectural-tools` for walls/openings/stairs.
- `sketchup-profile-builder` for trim, skirting, wall panels, frames.
- `sketchup-solid-inspector-repair` after boolean/solid operations.

## 7. Minimum output after CAD→SU bridge

Produce or request:

- one plan-like top screenshot,
- two white-model perspectives,
- one key elevation/focal wall view,
- a known-dimension verification note,
- a list of unresolved CAD ambiguity.
