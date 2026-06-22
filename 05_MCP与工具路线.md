# MCP 与工具路线｜SA&BOO AI视觉工作流

## 1. 当前最稳路线

### 概念图 / 位图生成

```text
brief → SA&BOO Prompt操作系统 → imagegen / gpt-image → 检查 → 迭代 → 保存
```

适合：产品KV、空间概念、小红书封面背景、品牌主视觉、材质图。

### 精准排版 / 社交封面 / 提案页

```text
imagegen生成背景或主体 → Figma / Canva / PPT排文字 → 导出PNG/PDF
```

适合：有中文标题、Logo、CTA、版式系统的视觉。

### Figma 设计系统 / 页面 / 组件

```text
视觉方向 → Figma变量/网格/组件 → 页面/封面/提案模板 → 导出
```

适合：品牌系统、官网页面、提案模板、封面模板、组件库。

## 2. Canva MCP 路线

Canva 官方 MCP 远程服务器：

```text
https://mcp.canva.com/mcp
```

Canva MCP 官方能力包括：

- 设计生成
- 设计编辑
- 设计搜索与发现
- 素材和品牌管理
- 多格式导出：PDF、PNG、JPG、PPTX、MP4 等
- 评论与协作

理想工作流：

```text
brief → Canva模板/品牌库搜索 → 生成或编辑设计 → resize → export → review
```

注意：当前 Codex 会话里没有直接暴露 Canva 工具，所以不能假装已经连接。后续如果你授权并接入 Canva AI Connector / MCP，就可以把这套 Prompt 包直接接入 Canva 工作流。

## 3. Figma MCP / Figma工具路线

Figma MCP 适合把设计上下文交给 AI，包括：

- 组件信息
- variables / styles
- 截图上下文
- 交互逻辑
- 文案和图层命名

当前更建议使用 Codex 中已有的 Figma skills 来做：

- 设计页面
- 组件库
- FigJam图表
- proposal版式
- 社交封面系统

## 4. 工具选择表

| 目标 | 推荐工具 | 原因 |
|---|---|---|
| 快速生成氛围图 | imagegen / gpt-image | 出图快，适合概念探索 |
| Midjourney风格探索 | Midjourney | 适合moodboard和艺术方向 |
| 中文商业封面 | 即梦 + Figma/Canva | 方便中文场景，但文字建议后期排 |
| 品牌系统 | Figma | 变量、组件、网格更稳定 |
| 提案PDF/PPT | Figma / PPT / PDF工具 | 客户交付稳定 |
| Canva模板批量化 | Canva MCP | 接入后适合模板、resize、导出 |
| 本地可控批量图 | Stable Diffusion / Flux | 适合固定风格和局部重绘 |

