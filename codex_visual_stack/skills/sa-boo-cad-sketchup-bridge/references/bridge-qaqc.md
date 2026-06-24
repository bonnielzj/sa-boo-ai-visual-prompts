# CAD SketchUp Bridge QA/QC

## Common failure modes

### CAD import creates messy SketchUp model

Causes:

- raw construction drawing imported directly,
- hatches and blocks kept,
- far-away CAD geometry,
- wrong units,
- duplicate linework.

Fix:

- create `SU_IMPORT_CLEAN`, strip clutter, check extents, verify units, lock reference, rebuild clean geometry.

### SketchUp model cannot become construction drawing

Causes:

- design is only atmospheric render,
- no dimensions,
- no material boundaries,
- too much downloaded mesh geometry,
- no confirmed plan relationship.

Fix:

- define confirmed decisions, export aligned views/sections, redraw in CAD with layers and dimensions.

### CAD and SU versions diverge

Causes:

- no revision suffix,
- direct overwrite of original files,
- untracked SketchUp changes,
- CAD updated after SU import without re-sync.

Fix:

- use R versions, revision log, bridge notes, and conflict reporting.

## Conflict report format

```text
冲突位置：
CAD 事实：
SketchUp 状态：
影响：尺寸 / 模型 / 出图 / 施工
建议处理：以 CAD 为准 / 以 SU 方案为准后回改 CAD / 需要 Bonnie 确认
```

## Bridge-ready checklist

CAD→SU ready:

- [ ] original CAD preserved
- [ ] SU clean CAD saved
- [ ] units confirmed
- [ ] extents checked
- [ ] clutter removed
- [ ] key layers named
- [ ] known dimension selected for verification

SU→CAD ready:

- [ ] design decision confirmed
- [ ] camera/elevation/section exported
- [ ] raw SU linework isolated as reference
- [ ] CAD layers applied
- [ ] dimensions and notes authored in CAD
- [ ] revision status updated

Visual-ready:

- [ ] at least one plan-like view
- [ ] at least two perspective/white-model views
- [ ] key elevation or section view
- [ ] material/light intent if moving to render
- [ ] image assets are readable and high quality
