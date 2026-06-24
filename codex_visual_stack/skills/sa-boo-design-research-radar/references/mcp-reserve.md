# MCP / Tool Reserve Plan for SA&BOO

Use this when the user asks to strengthen future MCP or tool reserves. Do not install tools unless the user explicitly asks and an install tool is available.

## Usable in this Codex environment now

- **Figma skills/MCP**: create/edit Figma files, generate design screens, diagrams, libraries, Code Connect. Best for brand kits, proposal templates, social cover systems, component libraries.
- **imagegen skill**: generate/edit bitmap visuals when native image generation is needed.
- **AutoCAD MCP + autocad-drafting skill**: create/modify drawings, P&ID/site plans, layers, annotations, blocks.
- **cadq MCP + cadq skill**: semantic query of DWG/DXF, areas, layers, elevation, features.
- **documents / presentations / spreadsheets / pdf skills**: produce polished proposals, decks, budgets, schedules, QA PDFs.
- **browser/control and web browsing**: inspect local apps/sites and current public sources.
- **node_repl / shell**: data cleaning, file conversion, automation scripts, scraping only when permitted.
- **automations**: schedule recurring trend radar, weekly learning tasks, monthly source checks.
- **multi-agent**: parallel research by domain: interior, brand, social, AI tools.

## MCP/connectors worth adding if available

1. **Notion MCP**
   - Use: client briefs, trend database, material library, project retrospectives, content calendar.
   - Watch: permissions and private client data.

2. **Google Drive / Dropbox / OneDrive MCP**
   - Use: retrieve project files, moodboard assets, contracts, photos, supplier PDFs.
   - Watch: folder permissions and accidental exposure.

3. **Google Sheets / Airtable MCP**
   - Use: FF&E, budgets, supplier/spec database, source scoring, content tracker.
   - Watch: formula integrity and version control.

4. **Figma remote MCP / design system integrations**
   - Use: stronger design-to-code, Code Connect, component audit, proposal template generation.
   - Watch: team/library access scopes.

5. **Canva MCP / Canva AI Connector**
   - Use: create/edit/export Canva designs from natural language, search design libraries, manage assets/brand kits, resize/export social/deck assets.
   - Watch: account OAuth, plan-specific features, possible allowlist/waitlist for some integrations, and do not assume it is active unless a callable Canva tool exists.

6. **Browser automation / Playwright MCP**
   - Use: recurring public trend checks, screenshots, landing-page QA, visual regression.
   - Watch: website terms; avoid private/social scraping.

7. **Pinterest / Behance / Dribbble connectors**
   - Use: inspiration board search, portfolio benchmarking, visual trend clustering.
   - Watch: API limits, copyright, and do-not-copy rules.

8. **Social analytics connectors: 小红书/抖音/巨量/千瓜/新榜**
   - Use: keyword trends, competitor monitoring, content performance.
   - Watch: official API access may be limited; prefer exported reports/CSVs if no compliant connector.

9. **Adobe / Firefly / Creative Cloud connectors**
   - Use: brand-safe generation, asset management, batch creative production.
   - Watch: enterprise plan requirements, licensing.

10. **3D/render connectors: Blender, Rhino/Grasshopper, SketchUp, D5, Enscape/Twinmotion**
   - Use: automate model conversion, render batch, material library, camera sets.
   - Watch: local licensing and plugin stability.

11. **Research memory: Zotero / Readwise / Obsidian MCP**
    - Use: citation library, design theory notes, trend clippings.
    - Watch: duplicate notes and source quality.

## Reserve priorities

- **First**: Notion + Sheets/Airtable + Drive, because they turn SA&BOO knowledge into reusable memory.
- **Second**: Figma/Adobe/Browser automation, because they increase output speed and visual consistency.
- **Third**: social analytics connectors, because they improve content conversion but may have access limits.
- **Fourth**: 3D/render automation, because it is powerful but depends heavily on local software setup.

## Suggested recurring automations

- Weekly: scan design tools and AI model updates; output “what changed / should SA&BOO care?”.
- Biweekly: 小红书/抖音 keyword radar from user-provided screenshots or compliant data source.
- Monthly: interior trend radar + brand visual trend radar + learning backlog update.
- Quarterly: purge stale prompt templates and update source whitelist.

## Prompt/style skill reserve

- Use `sa-boo-visual-style-prompt-lab` as the main routing skill for current visual trends, text-to-image prompt systems, and Canva/Figma/imagegen tool decisions.
