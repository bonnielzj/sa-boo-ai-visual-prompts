# SketchUp to CAD Checklist

Use this when returning SketchUp design decisions to CAD construction drawings.

## 1. What should return to CAD

Return confirmed design information:

- new or changed wall positions,
- openings and door/window changes,
- fixed furniture/cabinet outlines,
- ceiling levels and light positions,
- floor/wall/ceiling panel divisions,
- material boundaries,
- section/cut geometry,
- elevation linework,
- custom profiles or curved-panel flattened references.

Do not return as construction fact:

- unapproved AI-render decoration,
- approximate furniture staging,
- purely atmospheric lighting effects,
- non-buildable render details,
- random imported model mesh noise.

## 2. Export strategies from SketchUp

Choose by need:

- Aligned wall elevation: use Curic Align View or SketchUp standard scenes, then export 2D DWG/PDF/image as reference.
- Section/cutaway: use section planes and/or s4u Slice to create cut linework.
- Panel layout: use Floor Panel Grid, then export/trace confirmed divisions.
- Curved/soft surface panels: use Flatten Faces when a 2D panel reference is needed.
- Construction detail: model only enough to explain geometry, then redraw cleanly in CAD.

## 3. CAD standardization after SU return

- Put raw SU-exported linework on `X-SU-REF-*` first.
- Redraw final construction linework onto SA&BOO layers.
- Add dimensions using CAD annotation standards.
- Add material tags and references.
- Add revision cloud/delta only when it changes issued work.
- Update change log and title block revision table.

## 4. QA before issue

Check:

- scale matches known CAD dimension,
- elevation/section alignment matches plan reference,
- lineweights are not raw SketchUp lineweights,
- imported SU curves are simplified enough for CAD readability,
- dimensions are CAD-authored, not screenshot-only,
- issued PDF matches DWG revision.

## 5. Visual-first bridge output

A good SU→CAD handoff should include:

- screenshot/render showing design intent,
- CAD/elevation sheet showing construction translation,
- short note linking visual asset to CAD detail,
- unresolved assumptions list.
