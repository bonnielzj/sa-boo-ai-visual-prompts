---
name: sa-boo-design-research-radar
description: SA&BOO design research radar for current interior design, renovation, brand/visual identity, AI creative tools, model workflow, Chinese and global design/social trend scanning, learning roadmaps, and tool/MCP stack planning. Use when the user asks to research design公众号/论坛/设计网站/小红书/抖音/Behance/Pinterest trends, update SA&BOO knowledge, plan design learning, compare software skills, build AI prompt/model workflows, or recommend future MCP/tool reserves for interior design,装修,软装,品牌设计,视觉设计,个人IP内容. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Design Research Radar

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Run an evidence-based research loop for SA&BOO/Bonnie: scan current design signals, filter them through SA&BOO's aesthetic and business positioning, then translate them into learnable skills, workflows, content ideas, prompts, and tool/MCP reserves.

## Default stance

- Treat trends as **signals to translate**, not styles to copy.
- Prefer source triangulation: official reports + industry platforms + social/search data + project/business fit.
- For time-sensitive claims, browse current sources and cite links. Do not rely on memory for “latest/current/2026”.
- If公众号、小红书、抖音、Instagram content is login-gated or algorithmic, state the limitation and use alternatives: official trend reports, data platforms, search autocomplete, public case pages, platform ad/creative centers, exported CSV/screenshots from the user.
- Connect research back to existing SA&BOO skills when producing outputs:
  - `sa-boo-east-west-luxury-interior` for spatial narrative.
  - `sa-boo-brand-director` for brand systems.
  - `sa-boo-xiaohongshu-ip` for social content.
  - `sa-boo-prompt-translator`, `sa-boo-style-mixer`, and visual style skills for prompts.


## Anti-bot platform research access ladder

Use this ladder when research depends on platforms with heavy anti-crawling, login walls, algorithmic feeds, or fragile rendering: X/Twitter, 微信公众号/搜一搜, 小红书, 抖音, Instagram, Pinterest, and similar platforms.

1. **Official/API first** — Prefer official APIs, business/open platforms, exported analytics, or user-authorized platform downloads. Use API keys/tokens rather than cookies when available.
2. **Search triangulation** — Combine general web search, platform-native search, professional media, official reports, social signal screenshots, and saved URLs. Do not rely on one platform surface.
3. **Logged-in browser reading** — When the user has a legitimate account and content access, use the browser's visible logged-in session for human-scale reading, screenshots, and citation. Do not inspect browser cookies, local storage, passwords, or session stores.
4. **User-provided exports** — Prefer CSV exports, screenshots, saved links, browser bookmarks, platform collections, or downloaded images/videos from the user over automated scraping.
5. **Cookie file only as last resort** — Treat cookies as credentials equal to passwords. Never ask the user to paste cookies into chat. If a local cookie file is explicitly authorized, keep it local, domain-scoped, temporary, gitignored, permission-restricted, and never print/log it. Use only for user-authorized, ToS-aware research; do not use it to bypass paywalls, CAPTCHA, bans, rate limits, or access controls.
6. **Compliant data providers** — For large-scale monitoring, consider official enterprise products or reputable third-party data providers only after checking legality, rights, cost, and data provenance.
7. **Local knowledge base** — Cache allowed visual/text assets into `sa-boo-visual-asset-index`, OCR when useful, store source URLs and rights status, then build embeddings/search indices locally for repeat research.

Default decision: **manual/browser/API for depth, data provider for scale, local index for memory**. Never optimize for stealth; optimize for lawful access, repeatability, and high-quality visual evidence.

## Research workflow

1. **Define lens**
   - Industry: interior/renovation/soft furnishing, brand/visual identity, personal IP/content, or cross-over.
   - Market: China / global / specific city or client segment.
   - Output: trend radar, learning plan, tool comparison, AI workflow, content calendar, proposal section, or MCP reserve plan.

2. **Scan sources**
   - Read `references/source-map.md` when choosing sources or when the user asks “where to learn/follow”.
   - Use at least 3 source classes for substantial reports: authority/report, professional platform, and social/search signal.
   - Record date, platform, signal, relevance, and uncertainty.

3. **Classify trends**
   - Read `references/trend-taxonomy.md` for SA&BOO categories and scoring.
   - Classify each signal by: aesthetic, software/tool, workflow, business/channel, AI/model, risk.
   - Score: relevance to SA&BOO, monetization potential, learnability, durability, evidence strength.

4. **Translate into action**
   - For interior: translate into space narrative, plan logic, materials, lighting, FF&E, client package, and delivery checklist.
   - For brand: translate into symbol, typography, palette, motion, image style, campaign/social system, and portfolio case structure.
   - For AI: translate into model choice, prompt variables, reference image rules, controllability method, and QA checklist.

5. **Create learning roadmap**
   - Read `references/learning-roadmap.md` when asked what Bonnie/SA&BOO should learn next.
   - Prioritize 80/20 skills: those that improve conversion, design quality, speed, or repeatability within 30-90 days.

6. **Plan tool/MCP reserves**
   - Read `references/mcp-reserve.md` when asked to strengthen future MCP/tool stack.
   - Read `references/mac-interior-tool-stack.md` when asked to find Mac-suitable plugins, GitHub tools, MCP servers, or interior/CAD/SketchUp/render workflow upgrades.
   - Separate “usable now”, “worth installing if available”, and “avoid/only manual due to platform rules”.

7. **Run risk check**
   - Read `references/risk-checklist.md` for AI images, copyrighted references, client privacy, platform claims, and health/sustainability claims.

## Output patterns

### Trend radar

```text
研究口径：时间 / 地域 / 平台 / 限制
核心判断：一句话
趋势信号表：趋势｜证据｜为什么重要｜SA&BOO翻译｜学习/工具｜风险
30天行动：3-5项
90天沉淀：skills / 模板 / 素材库 / SOP
来源链接：...
```

### Learning plan

```text
学习目标：
优先级A（30天必须）：技能｜产出物｜练习任务｜验证标准
优先级B（90天建立壁垒）：...
优先级C（观察即可）：...
不建议投入：原因
```

### AI/model workflow

```text
任务类型：概念探索 / 可控风格 / 平面品牌 / 空间渲染 / 短视频
模型选择：为什么选
输入素材：允许/禁止
流程：brief → references → prompt → generation → edit → QA → client-safe output
可复用变量：风格 / 材质 / 构图 / 镜头 / 平台尺寸
风险检查：版权 / 肖像 / 隐私 / 可施工性 / 可印刷性
```

## Quality bar

- Give concrete platform names and learning resources, not generic “多看案例”.
- Separate “行业趋势” from “SA&BOO should actually do this”.
- Cite sources for current facts and product capabilities.
- Avoid overclaiming: say “signal suggests” when evidence is weak.
- End with a small, practical implementation plan.

## Visual asset reference requirement

When researching visual/design trends, do not stop at textual summaries. Use or create a `sa-boo-visual-asset-index` entry for representative visuals. Trend outputs should include `asset_id`, thumbnail path, original local path, source link, category, tags, and rights status.

If the user asks for “learn”, “visual reference”, “style”, “mood”, “原视觉资产”, or “向量索引”, route through `sa-boo-visual-asset-index` first.

