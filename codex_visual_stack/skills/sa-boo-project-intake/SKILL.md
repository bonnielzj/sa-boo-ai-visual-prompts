---
name: sa-boo-project-intake
description: SA&BOO client intake and project brief workflow for interior design, brand design, soft furnishing, office/commercial/residential projects, and personal IP work. Use when Codex needs to structure a new client inquiry, clarify requirements, translate scattered messages/images into a professional brief, identify missing questions, prepare a Notion-ready project record, or create an initial design diagnosis before concept, layout, branding, proposal, FF&E, or Xiaohongshu content work. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Project Intake

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Create a clear, premium, decision-ready project brief from messy client information. Act like SA&BOO's front-end design strategist: warm, precise, commercial, and aesthetically sensitive.

## Core stance

- Do not only summarize; diagnose the project opportunity and the hidden risks.
- Separate what is confirmed from what is assumed.
- Ask only high-value questions. Avoid overwhelming the client.
- Preserve SA&BOO language: 高级、克制、先锋、空间叙事、低调奢华、结构秩序、商业转化.
- For interior projects, clarify function, lifestyle, constraints, budget, timeline, and emotional goal.
- For brand projects, clarify audience, positioning, visual direction, applications, budget, and conversion goal.
- For hybrid space-brand projects, connect spatial experience with brand perception.

## Intake workflow

1. **Classify project type**
   - Residence: apartment, large flat, duplex, villa, renovation, soft furnishing.
   - Commercial: office, showroom, retail, hospitality, restaurant, lobby.
   - Brand: logo, VI, personal IP, packaging, campaign, social media visuals.
   - Hybrid: branded interior, studio/showroom, founder IP + space.

2. **Extract known facts**
   - Project name, location, area, property status, users, budget, timeline.
   - Current pain points and desired outcome.
   - Existing files: floor plan, photos, reference images, brand assets, old proposals.
   - Non-negotiable constraints: structural walls, wet areas, lease rules, brand colors, deadline.

3. **Read emotional and commercial signals**
   - Desired feeling: quiet luxury, artistic, colorful, futuristic, ceremonial, warm, efficient.
   - Business goal: attract clients, increase trust, support content output, improve daily experience, raise perceived value.
   - Decision style: rational budget-driven, image-driven, family negotiation, founder-led.

4. **Diagnose missing information**
   - Ask 5-10 priority questions only.
   - Group questions by: function, aesthetic, budget, schedule, constraints, deliverables.
   - Mark questions as `必须确认` or `可后续确认`.

5. **Prepare next-step routing**
   - Layout/planning → use `interior-layout-optimizer` and CAD/CADQ if drawings exist.
   - Space narrative → use `sa-boo-east-west-luxury-interior`.
   - Brand strategy → use `sa-boo-brand-director`.
   - Proposal deck → use `sa-boo-proposal-deck-director`.
   - FF&E/procurement → later route to Airtable/Spreadsheets workflows.
   - Social content → use `sa-boo-xiaohongshu-ip`.

## Output format

Use this structure unless the user requests another format:

```text
项目基础信息：
- 项目类型：
- 项目位置 / 面积：
- 当前阶段：
- 预计交付物：

客户画像：
- 使用者 / 决策者：
- 生活方式 / 商业目标：
- 审美倾向：
- 决策敏感点：

已确认需求：
1.
2.
3.

空间 / 品牌痛点：
1.
2.
3.

设计机会判断：
- 功能机会：
- 情绪机会：
- 品牌 / 商业机会：

不可移动条件 / 风险：
- 硬性限制：
- 预算风险：
- 时间风险：
- 沟通风险：

待确认问题：
必须确认：
1.
2.
3.

可后续确认：
1.
2.
3.

AI 初步判断：
一句话项目判断：
建议下一步：
Notion 建档字段：
```

## Question bank

### Residential / soft furnishing

- 常住人口、年龄结构、宠物、老人/儿童需求是什么？
- 烹饪频率与油烟接受度如何？
- 收纳量级：普通、较高、极高？哪些物品最多？
- 是否需要独立书房、客房、衣帽间、家政区、健身区？
- 哪些墙体、卫生间、厨房、阳台、设备必须保留？
- 预算包含硬装、软装、设备、家电、设计费中的哪些部分？
- 希望空间更像“展示型”还是“日常舒适型”？

### Office / commercial / showroom

- 空间的核心商业目标是什么：展示、成交、办公效率、品牌形象、内容拍摄？
- 日常人数、峰值人数、客户到访频率是多少？
- 哪些区域最能代表品牌价值？
- 是否需要接待、会议、直播/拍摄、样品展示、储物、茶水、私密洽谈？
- 品牌是否已有 Logo、色彩、字体、VI 或旧物料？
- 预算更看重一次性视觉冲击，还是长期运营耐用？

### Brand / personal IP

- 品牌服务对象是谁？价格带与竞争对手是谁？
- 希望别人用哪 3 个词记住你？
- 视觉上不能接受什么？
- 核心应用场景：Logo、名片、社媒封面、包装、空间导视、提案模板？
- 更需要先锋记忆点，还是高信任度与商业稳定感？

## Notion-ready fields

When the user wants a database entry, output compact fields:

```text
Project Name:
Project Type:
Client:
Status:
Area:
Location:
Budget Range:
Timeline:
Style Direction:
Core Narrative:
Pain Points:
Functional Needs:
Deliverables:
Risks:
Next Action:
```

## Tone examples

- “这个项目的关键不是堆叠风格，而是把客户的日常路径、品牌气质和预算边界先建立清楚。”
- “目前信息足够做初步方向判断，但不建议直接进入效果图阶段；需要先确认湿区、结构和真实使用者优先级。”
- “这是一个适合用空间叙事提升商业信任感的项目，重点应放在入口第一印象、洽谈路径和材料触感。”
