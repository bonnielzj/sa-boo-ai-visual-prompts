# MCP and Tool Reserve

## Available now in this Codex environment

- `spreadsheets` skill: create XLSX workbooks, formulas, formatting, charts, QA render.
- shell/Python: generate CSV/XLSX templates, clean exported data, merge price lists.
- `documents` / `presentations` / `pdf`: create client-facing specifications, proposal pages, purchase summaries.
- `sa-boo-project-intake`: convert messy client info into project fields.
- `sa-boo-figma-brand-kit`: package material boards and budget summaries into branded Figma/PDF visuals.
- `sa-boo-realtime-render-presentation`: connect render/material outputs to client presentations.

## High-value MCP/connectors to add when available

1. **Notion MCP**
   - Use for: master material database, supplier CRM, project brief, approval history, content calendar.
   - Best because: flexible views, attachments, relations, easy human editing.
   - Risk: privacy and permission control.

2. **Airtable MCP**
   - Use for: structured relational database, views by project/status/supplier, forms for data entry.
   - Best because: more database-like than Notion for procurement.
   - Risk: plan limits, attachment storage, permissions.

3. **Google Sheets MCP**
   - Use for: collaborative budgets, formulas, vendor price import/export.
   - Best because: clients and suppliers understand spreadsheets.
   - Risk: formula errors and accidental edits.

4. **Google Drive / Dropbox / OneDrive MCP**
   - Use for: supplier PDFs, material photos, quotes, invoices, signed approvals.
   - Best because: databases should link to files, not store everything as text.
   - Risk: broken links and overshared folders.

5. **Email / Gmail / Outlook MCP**
   - Use for: quote intake, supplier correspondence, approval evidence.
   - Risk: private data and noisy automation.

6. **OCR / PDF extraction MCP**
   - Use for: extracting supplier quotes, catalog specs, invoices into database rows.
   - Risk: OCR mistakes; always verify numbers.

7. **Accounting / invoicing connector**
   - Use for: actual costs, invoices, payments.
   - Risk: financial permissions and reconciliation complexity.

8. **Figma MCP**
   - Use for: material board layout, spec cards, client-facing schedule pages.
   - Not the source of truth for prices.

## Installation note

Only install a plugin/connector if an exact available tool appears. If no install candidate/tool is exposed, create local templates and provide the user with a setup checklist instead.
