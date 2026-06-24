# SA&BOO CAD QA/QC Checklist

## Before drawing starts

- [ ] Units are millimeters.
- [ ] Project base file/xref is locked or read-only.
- [ ] Standard layers loaded.
- [ ] Text, dimension, multileader styles set.
- [ ] Title block and sheet size selected.
- [ ] Plot style/lineweight test PDF checked.

## Layer audit

- [ ] No important geometry on `0`, `Defpoints`, random imported layers, or `NPLT`.
- [ ] New/existing/demolition elements are separated.
- [ ] Annotation is not mixed with geometry layers.
- [ ] Xrefs are on `X-*` layers and use relative paths.
- [ ] Viewport layer is non-plot.

## Annotation audit

- [ ] Text heights are readable at final plot scale.
- [ ] Dimensions are associative and not exploded.
- [ ] Dimensions do not conflict with each other.
- [ ] Material tags match schedules.
- [ ] Door/window/furniture tags match schedules.
- [ ] Section/elevation/detail references are valid.

## Sheet audit

- [ ] Sheet number and title are correct.
- [ ] Scale shown matches locked viewport scale.
- [ ] North arrow/axis/grid used where needed.
- [ ] Title block project info/date/revision are correct.
- [ ] Revision table matches cloud/delta marks.
- [ ] PDF plot is visually checked at 100% and fit-to-page is not distorting scale.

## Issue audit

- [ ] Issued folder is dated and revision-coded.
- [ ] DWG/PDF filenames match sheet index.
- [ ] Change log/transmittal included.
- [ ] Superseded files archived, not overwritten.
- [ ] Fonts, xrefs, plot styles, images are packaged if sending editable DWG.

## High-risk interior checks

- [ ] Finished dimensions clear: finished face vs structural face.
- [ ] Ceiling heights and conflicts with HVAC/lighting checked.
- [ ] Door swings, clearances, and hardware conflicts checked.
- [ ] Wet areas show waterproofing/drain/slope where required.
- [ ] Fixed furniture/cabinetry dimensions, power, lighting, and appliance clearances coordinated.
