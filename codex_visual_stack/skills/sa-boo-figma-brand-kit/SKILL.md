---
name: sa-boo-figma-brand-kit
description: SA&BOO Figma Brand Kit workflow for building practical brand asset libraries, design tokens, variables, styles, components, proposal/social templates, and AI/MCP-assisted Figma production. Use when the user asks to create, learn, audit, or operationalize a Figma Brand Kit, design system, brand guideline file, social cover system, proposal template system, interior/brand presentation library, Figma variables/styles/components, Tokens Studio workflow, or Figma MCP/tool/plugin recommendations for SA&BOO. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Figma Brand Kit

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Build a practical Figma Brand Kit for SA&BOO: not a generic UI kit, but a reusable brand production system for proposals, social covers, brand cases, moodboards, client reports, and visual identity applications.

## Required companion skills

- For actual Figma write work, load `figma-use` before every `use_figma` call.
- For variables/components/library structure, load `figma-generate-library` alongside this skill.
- For brand strategy language, use `sa-boo-brand-director`.
- For Xiaohongshu/Douyin packaging, use `sa-boo-xiaohongshu-ip`.

## What to build first

Use a 3-level kit:

1. **Foundations**: colors, typography, spacing, radius, shadows, material/image rules.
2. **Components**: logo locks, title blocks, section headers, cards, quote blocks, image masks, CTA/footer, label chips.
3. **Templates**: proposal page, social cover, case-study spread, moodboard, invoice/quote cover, project recap carousel.

This is more useful to SA&BOO than starting with buttons/inputs unless the user is building an app.

## Workflow

1. **Discovery**
   - If a Figma file exists, inspect pages, variables, styles, components first.
   - If no file exists, propose v1 scope and ask for brand inputs: logo, colors, fonts, core visual motifs, output platforms.
   - Read `references/brand-kit-operating-method.md` for the v1 structure.

2. **Token plan**
   - Read `references/token-schema.md`.
   - Use SA&BOO defaults unless user provides exact brand specs.
   - Keep token names slash-separated and semantic: `color/bg/deep`, `color/text/primary`, `spacing/md`.

3. **Create foundations**
   - In Figma: create variable collections first, then text/effect styles.
   - In files: run `scripts/generate_starter_tokens.py` to create editable JSON/CSS tokens.
   - Never build components before variables exist.

4. **Create file structure**
   - Pages: `00 Cover`, `01 Foundations`, `02 Brand Assets`, `03 Components`, `04 Templates`, `05 Examples`, `99 Archive`.
   - Add documentation frames so the file teaches future collaborators how to use it.

5. **Build components**
   - Build one component at a time and validate with screenshot.
   - Prioritize SA&BOO components: `Logo Lockup`, `Proposal Header`, `Section Divider`, `Image Card`, `Moodboard Tile`, `XHS Cover`, `Case Study Spread`, `CTA Footer`.

6. **Template packaging**
   - Read `references/template-recipes.md`.
   - Build 3-5 templates first; leave everything else as future backlog.

7. **MCP/plugin decision**
   - Read `references/plugin-mcp-evaluation.md` when the user asks which tools/plugins/GitHub resources to use.
   - Do not install unrequested broad tools; recommend or use available MCP first.

8. **QA**
   - Read `references/qa-checklist.md` before handing off.
   - Check naming, variables, text styles, contrast, template constraints, export sizes, client privacy.

## Output format

For planning:

```text
Brand Kit v1目标：
需要的输入：
Figma页面结构：
Tokens：
Components：
Templates：
MCP/插件：
执行步骤：
风险检查：
下一步：
```

For implementation status:

```text
已完成：
Figma/文件路径：
创建的变量/样式/组件/模板：
待确认：
下一阶段：
```

## Practical rule

A good SA&BOO Brand Kit should let Bonnie create a client-ready cover, a proposal page, a social carousel, and a case-study spread in under 10 minutes without redesigning from scratch.

## Visual asset reference requirement

For Brand Kit, template, moodboard, or visual system planning, use `sa-boo-visual-asset-index` when available. Every proposed visual direction should cite original indexed assets by `asset_id`, thumbnail, original local path, source page URL, and rights status.

Use indexed assets as references for structure, proportion, material/image rules, and case-study composition; do not copy third-party brand visuals into public/client work unless licensed.

