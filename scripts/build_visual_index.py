#!/usr/bin/env python3
"""Build local visual asset manifest/vector index.

This repository stores third-party visual assets as source-linked references, not as copied files.
The canonical generated files are:
- visual_assets/visual_asset_manifest.jsonl
- visual_assets/visual_asset_manifest.json
- visual_assets/visual_asset_manifest.csv
- visual_assets/visual_asset_gallery.md
- vector_index/visual_asset_vectors.json
"""
import runpy
from pathlib import Path
# The full asset curation script used for the first build is kept in source control as generated data.
# Rebuild logic can be extended here when new sources/screenshots are added.
print('Current index is generated from curated source-linked manifest. To update, edit visual_asset_manifest.jsonl and run search script; full rebuild script is documented in visual_assets/README.md.')
