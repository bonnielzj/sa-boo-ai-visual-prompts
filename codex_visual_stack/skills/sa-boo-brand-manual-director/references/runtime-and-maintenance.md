# Runtime and Maintenance

Read this reference only when the manual task will run bundled scripts, open an
Adobe backend, render a PDF, build a release package, or maintain this skill.
Pure strategy, audit planning, page architecture, and editorial discussion do
not need it.

## Python Interpreter

Resolve the skill directory from the loaded skill path; do not assume the
current working directory contains `scripts/`. Select an interpreter compatible
with its installed dependencies. A mismatched `PYTHONPATH` can cause binary-package
import failures; a named interpreter alone does not prove a usable runtime.

```bash
VI_PYTHON="${VI_PYTHON:-$(command -v python3)}"
"$VI_PYTHON" -c 'from PIL import Image, ImageDraw'
```

Use the resolved `$VI_PYTHON` for bundled Python commands that need Pillow. No
machine-specific environment or native application wrapper is included.

## Creative Backend Gate

Before mutation, load `bonnie-creative-backend-routing` and prove the selected
backend with a real read-only connection call.

- Prefer `illustrator-mcp` for Illustrator; use
  an explicitly configured `VI_ILLUSTRATOR_JSX` adapter only as the native JSX
  fallback.
- Prefer the connected `indesign-uxp` plugin for supported InDesign work; use
  an explicitly configured `VI_INDESIGN_JSX` adapter when the bundled or
  project-specific ExtendScript is required.
- Never use Computer Use, `System Events`, mouse/keyboard automation, or
  screenshot-driven clicking.
- A disabled optional Figma skill is not a blocker. Choose another editable
  backend unless Figma is explicitly required.

No backend is successful until the real editable file opens, saves, exports when
required, and passes structural plus visual QA.

## PDF Review Backend

`scripts/render_manual_review.py` uses `pdftoppm` when available. On macOS it
otherwise compiles the bundled `scripts/render_pdf_pages.m` with `clang` and
PDFKit, renders every page, and builds contact sheets. Do not substitute a
first-page-only Quick Look thumbnail for the multi-page review.

## Maintainer Verification

After changing this skill or its scripts, run:

```bash
"$VI_PYTHON" scripts/test_brand_manual_tools.py
```

The suite must prove:

- protected-copy hashing;
- safe `--force` control-file backup;
- missing-ledger rejection;
- release manifest integrity and mutation detection;
- editable-source enforcement for final release statuses;
- multi-page PDF rendering, page-content pixel checks, and contact-sheet output.

After changing bundled JSX, run a no-document native-wrapper smoke test. Both
Illustrator and InDesign wrappers must surface the deliberate script error; a
silent exit-code `0` does not prove execution. Preserve the adapter configuration, frontmatter and relevant script compile/help
checks in the maintenance record. Use the host's actual skill-discovery mechanism
when checking installed availability.
