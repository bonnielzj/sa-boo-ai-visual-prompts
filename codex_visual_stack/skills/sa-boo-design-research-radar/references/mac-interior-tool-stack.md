# SA&BOO Mac Interior Tool Stack Radar

Use this when Bonnie asks for Mac-suitable plugins, MCPs, GitHub/open-source tools, or workflow upgrades for interior/CAD/SketchUp/render/material/asset-library work.

## First principle

Do not recommend tools because they are fashionable. Recommend only if they improve one of:

1. CAD/PDF/DWG/DXF reliability;
2. SketchUp model cleanup, scene export, material/UV, cabinetry/storage, or component quality;
3. visual asset memory/search for Bonnie's local libraries;
4. render/camera/material workflow on Apple Silicon;
5. proposal/FF&E/project database repeatability;
6. QA gates that prevent bad visuals from reaching Bonnie/client.

## Local Mac baseline to check

Before recommending installs, check:

```text
sw_vers
uname -m
python3 --version
node --version
brew --version
SketchUp extension list via SketchUp Ruby
available Codex workspace dependencies
```

If system Node/Homebrew is absent, do not panic: Codex may provide bundled Node/Python/Git. For permanent MCP/server installs, prefer a stable package manager only after Bonnie confirms system-level permission.

## Priority tiers

### P0 — likely worth adding soon

- **SketchUp CleanUp³ / cleanup tooling**: model hygiene before QA/render.
- **OpenCutList**: storage/cabinetry/cutlist/BOM logic; useful for small-home收纳 projects.
- **Local visual asset search**: build or adopt CLIP/LanceDB/FiftyOne-like image search for `/Users/bonnie/Desktop/设计资料`.
- **Document/reference ingestion**: use MarkItDown or Docling-style converters to turn PDFs, supplier brochures,公众号 screenshots/exports, and product sheets into local Markdown learning cards; keep sources and rights status.
- **GitHub MCP / repo workflow**: track skills, scripts, issue logs, tool candidates.
- **Notion or Airtable/Sheets MCP**: design knowledge base, FF&E, material/vendor status, trend radar.

### P1 — test in pilot project

- **Skimp / Transmutr**: simplify/convert furniture and 3D assets before SketchUp import.
- **QCAD/ODA conversion helper**: improve DWG→DXF outside AutoCAD MCP limits.
- **Twinmotion Datasmith / Enscape Mac**: real-time render alternatives; test with one scene only.
- **Playwright MCP / browser automation**: public trend/supplier screenshot workflows with rules.
- **Blender + Bonsai/IfcOpenShell / Blender MCP**: long-term BIM/IFC/open-source 3D capability, not urgent for small SU projects.
- **Hammerspoon/Raycast/Keyboard Maestro**: Mac launchers only; business logic stays in external scripts.
- **Eagle / visual asset manager**: useful if Bonnie wants a human-facing visual library UI; do not treat it as a replacement for project-level contact sheets and citations.

### P2 — observe or avoid for now

- More decorative SketchUp plugins before workflow stabilizes.
- Social scraping MCPs without official API/export permission.
- Heavy BIM stacks for tiny residential projects unless a client/project requires them.
- Render engines with unclear current native Mac support or licensing fit; verify before investing.

## Decision template

```text
Tool:
Type: SketchUp plugin / MCP / GitHub / Mac app / Python/Node package
Mac fit: native / works through SketchUp / CLI / uncertain
Project value:
SA&BOO value:
Install risk: low / medium / high
Cost/license:
Test artifact:
Decision: install now / trial / watch / reject
```

## Install safety

- Never modify AiMaMi/local proxy configuration without explicit user instruction.
- Do not install paid/commercial extensions without Bonnie confirming license/cost.
- For GitHub/MCP tools, inspect README, dependencies, last activity, license, and security scope.
- Prefer project-local wrappers and scripts before global system changes.
- Every new tool must produce one visible proof: contact sheet, model cleanup result, asset search demo, export report, or proposal page.

## Small residential project calibration rule

When a small residential interior project is underperforming, do **not** answer by adding more plugins or switching render engines. First check:

1. Is there a B00/A01/SU01 visual baseline and QA contact sheet?
2. Did local/reference assets inform furniture, material, and texture choices?
3. Are SketchUp cameras readable and internally QA-filtered?
4. Are cabinets/storage modeled with real depth, clearance, and use logic?
5. Does the tool candidate create a visible proof within one project round?

If not, prioritize local asset shortlist, SketchUp Ruby task library, QA scripts, and gate discipline before any new install.
