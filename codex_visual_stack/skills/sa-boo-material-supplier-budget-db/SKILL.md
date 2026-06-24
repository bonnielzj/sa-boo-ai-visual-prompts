---
name: sa-boo-material-supplier-budget-db
description: SA&BOO material, supplier, FF&E, procurement, and budget database workflow for interior design projects, covering material libraries, vendor qualification, price tracking, budget estimation, procurement status, maintenance/warranty records, substitutions, client-facing schedules, Excel/CSV/Notion/Airtable/Sheets structures, and MCP/tool reserves. Use when the user asks to build, learn, audit, template, or automate materials, suppliers, budgets, FF&E, procurement, cost plans, BOQ, quotes, purchase lists, material schedules, or project cost databases. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Material / Supplier / Budget Database

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Build a practical database system for SA&BOO interior projects: material intelligence + supplier relationship + project budget control + client-facing specification clarity.
When furniture, textile, soft decor, or FF&E knowledge is involved, proactively pair with `sa-boo-furniture-textile-softdecor` and its database at `/Users/bonnie/Documents/学习项目/sa-boo-design-knowledge-base/03-databases/furniture-textile-softdecor/` so supplier/budget decisions reuse object, textile, CAD/SU, source, and aesthetic records.

## Core rule

Separate **master data** from **project data**:

- Master data: materials, suppliers, price history, certifications, maintenance, risk notes.
- Project data: selected items, quantities, budgets, quotes, procurement status, approvals, substitutions.

Never let a one-off project spreadsheet become the only source of supplier/material knowledge.

## Workflow

1. **Choose operating format**
   - Start with Excel/CSV if no connected database exists.
   - Move to Notion/Airtable/Sheets when collaboration, attachments, and long-term tracking matter.
   - Read `references/mcp-tool-reserve.md` before recommending MCP/connectors.

2. **Define schema**
   - Read `references/database-schema.md` for tables and fields.
   - Minimum tables: Materials, Suppliers, Price History, Project Budget, Procurement Tracker, Approvals, Substitutions.

3. **Create templates**
   - Run `scripts/create_database_templates.py` to generate CSV and XLSX templates.
   - Use generated templates from `assets/` if already present.

4. **Classify materials**
   - Read `references/material-taxonomy.md`.
   - Use categories that match design decisions and procurement: floor, wall, ceiling, stone, wood, metal, glass, textile, lighting, sanitary, furniture, art.

5. **Score suppliers**
   - Read `references/supplier-scorecard.md`.
   - Score quality, price, lead time, reliability, service, documentation, sustainability, after-sales.

6. **Build budget control**
   - Read `references/budget-workflow.md`.
   - Track target budget, estimate, quote, approved amount, actual cost, variance, contingency, tax, freight, installation.

7. **Run QA / risk checks**
   - Read `references/qaqc-risk-checklist.md`.
   - Verify units, VAT/tax, lead time, warranty, certification, color/lot, stock, site constraints, client approvals.

## Output patterns

### Database plan

```text
数据库目标：
推荐工具：Excel / Notion / Airtable / Google Sheets / 混合
核心表：
关键字段：
预算公式：
供应商评分：
审批与变更流程：
MCP/插件储备：
下一步：
```

### Project budget summary

```text
项目预算状态：
目标预算：
当前估算：
已报价：
已批准：
风险项：
节省/替代建议：
待确认：
```

## SA&BOO priorities

- Make material choices defendable: beauty + cost + lead time + maintenance + installation risk.
- Make supplier data reusable across projects.
- Show clients premium clarity, not messy cost anxiety.
- Keep private vendor pricing and client budgets controlled.
