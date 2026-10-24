# 中文字形设计工具与 MCP 核查

核查日期：2026-09-23。范围：GitHub 原仓库 README、执行源码、许可证、默认分支最新 commit，以及现有本机运行环境。已在线查询 `fontforge mcp`、`font design mcp`、`inkscape mcp`、`glyphs mcp`。没有安装候选包、启动陌生服务或修改 MCP 配置。

**结论：已从源码确认部分开源 MCP 提供字形操作接口，但没有证据表明它们会自动产生优质中文字体设计。对当前两句单色字形创作，现有 FontTools 加矢量编辑比引入新服务器更直接。** MCP 负责把命令接到编辑器或字体库；语义转译、骨架设计、黑白关系、重心与光学校正仍须通过设计和视觉审查解决。

## 核查等级

- **repository-verified**：读过对应 commit 的原始源码、入口与许可证，确认功能存在。不能据此声称本机可调用或输出已通过视觉验收。
- **runtime-tested**：已在本机实际执行指定功能。本研究子任务直接实测既有 FontTools；主任务另已报告 VTracer 实测成功。4 个候选 MCP 均未安装或运行。
- 上游 README 或 CI 的“测试通过”属于上游记录，不等同于本机实测。

## 4 个 MCP 候选

| 候选 | 实际功能与中文边界 | 许可、依赖和维护 | 本机与执行边界 | 判断 |
|---|---|---|---|---|
| [LHxis/fontforge-mcp](https://github.com/LHxis/fontforge-mcp) | SVG path 绘字、轮廓变换/清理、字距、SFD 保存、字体导出和 PNG 预览。源码接受 Unicode 码点或单个字符，并使用 UnicodeFull；这支持中文字符映射，但未提供中文结构设计或整套 CJK 质量证据。 | MCP 为 MIT。另需 FontForge ≥2023-01-01、Python ≥3.10、mcp、Pillow、FontTools。默认分支最新 commit：2026-08-09，`acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623`。 | 未 runtime-tested；本机未发现 FontForge。上游明确称 macOS/Linux 路径已实现、但尚未在真实机器测试。暴露 `ff_python` 任意 Python 执行；绝对文件路径可以越过默认工作目录。 | 字体工程能力直接，适合已有 FontForge 的受控流程；当前不优先安装。 |
| [Kydaix/Font-Design-MCP](https://github.com/Kydaix/Font-Design-MCP) | 类型化矢量/节点编辑、原子批处理、UFO 修订、笔画网络、字距、HarfBuzz/FreeType 预览、TTF/WOFF2 和变量字体构建、几何检查。Unicode 字段允许到 U+10FFFF；**512 glyph 上限**，不适合完整常用汉字库。内置解剖/示例偏拉丁。 | LICENSE 实文为 MIT，虽然 GitHub API 的 license 字段为 NOASSERTION。Python 3.11–3.13；依赖 ufoLib2、fontmake、FontTools、HarfBuzz、FreeType、Pillow、booleanOperations 等。最新 commit：2026-09-11，`0544d650de5eb30d68c8bd3fc5b2beb7d386ca86`。 | 未 runtime-tested；本机缺少多项依赖。完整工具注册表中未见任意代码、shell、下载或安装工具；有工作目录边界和修订历史。**不支持任意 UFO/SVG 导入、自动描摹、OTF 或完整 GUI**。 | 4 个中最值得以后用小型 Unicode 项目作隔离试点。不能直接当成“导入已有汉字字体并美化”的现成功能。 |
| [grumpydevorg/inkscape-mcps](https://github.com/grumpydevorg/inkscape-mcps) | 5 个工具：列出/运行 Inkscape actions、SVG DOM 属性修改、清理和验证。支持 path union/difference、object-to-path、变换与导出。UTF-8 SVG 文本可以承载中文，但实际字形依赖安装字体和 Inkscape 文本渲染器；没有字体 cmap、字库编译或中文笔画理解接口。 | MIT。Python ≥3.10（以 pyproject 为准；README 写 ≥3.9）、Inkscape CLI、fastmcp、inkex、scour 等。最新 commit：2025-10-22，`e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea`。 | 未 runtime-tested；本机未发现 Inkscape。没有通用 Python/shell 工具，但能改写 SVG。静态审查发现 action 字符串只按首个冒号前缀校验，随后原样用分号拼接，且允许裸 export-filename/file-save；不应把 README 的“hardened”当成已验证完整沙箱。未做利用测试。 | 通用 SVG 控制器；成熟 CLI 本身比这层 MCP 更有价值。该仓库仍有发布占位信息，不建议仅因宣传而安装。 |
| [thierryc/Glyphs-mcp](https://github.com/thierryc/Glyphs-mcp) | 读取/修改 glyph path 和节点、创建/删除 glyph、字距、曲线分析、导出、Unicode 映射审查。源码直接写 GSGlyph.unicode；文档明确讨论 CJK gaiji/PUA，但这是编码管理，非中文造字质量证明。 | MCP 为 Apache-2.0；**Glyphs 本体是另行购买的商业应用**。需要 macOS ≥13、Glyphs 3 或 Glyphs 4 beta、Python 3.11–3.14、插件、PyObjC、FastMCP/MCP 等。默认分支最新 commit：2026-09-16，`590053fedd7bcab13a2027fb3bce99b724072b57`；repo pushed_at 为 2026-09-23，二者不可混称。 | 未 runtime-tested；本机未发现 Glyphs。含 `execute_code` 和 `execute_code_with_context`，执行环境保留完整 builtins 并调用 exec/eval；可改动字体和本机文件，不是只读沙箱。 | 已有 Glyphs 的专业字体流程中最完整；不属于全开源工具栈。 |

## 源码证据

### FontForge MCP

- [工具与预览机制，README 274–298](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/README.md#L274-L298)
- [Unicode 字符/码点解析，worker.py 78–100](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/worker.py#L78-L100)，[UnicodeFull 编码](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/worker.py#L430)
- [任意 Python 执行，worker.py 1002–1008](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/worker.py#L1002-L1008)，[绝对路径解析，server.py 53–60](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/server.py#L53-L60)
- [macOS 未实机测试的明确说明](https://github.com/LHxis/fontforge-mcp/blob/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623/README.md#L430-L434)

### Font Design MCP

- [全部工具注册表，service.py 78–189](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/src/font_design_mcp/service.py#L78-L189)
- [Unicode 输入契约，models.py 78–83](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/src/font_design_mcp/models.py#L78-L83)，[512 glyph/50000 点/256 字符限制](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/src/font_design_mcp/service.py#L47-L74)
- [路径边界实现，storage.py 27–45](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/src/font_design_mcp/storage.py#L27-L45)
- [格式、导入和复杂文字限制](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/README.md#L297-L313)，[许可证原文](https://github.com/Kydaix/Font-Design-MCP/blob/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86/LICENSE)
- 源码自己强调“技术验证不是艺术或人工认可”，并明确自动描摹为 false。该定位比“自动造好字体”准确。

### Inkscape MCP

- [动作 allowlist 与校验](https://github.com/grumpydevorg/inkscape-mcps/blob/e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea/src/inkscape_mcp/cli_server.py#L69-L108)
- [参数校验及原样拼接动作](https://github.com/grumpydevorg/inkscape-mcps/blob/e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea/src/inkscape_mcp/cli_server.py#L163-L210)
- [UTF-8 SVG 读写和 text selector](https://github.com/grumpydevorg/inkscape-mcps/blob/e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea/src/inkscape_mcp/dom_server.py#L197-L280)
- [依赖与 Python 最低版本](https://github.com/grumpydevorg/inkscape-mcps/blob/e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea/pyproject.toml)

### Glyphs MCP

- [节点路径读取/替换](https://github.com/thierryc/Glyphs-mcp/blob/590053fedd7bcab13a2027fb3bce99b724072b57/plugin-manager/Glyphs%20MCP.glyphsPlugin/Contents/Resources/mcp_tools_paths.py#L36-L56)
- [Unicode 与 CJK gaiji 范围说明](https://github.com/thierryc/Glyphs-mcp/blob/590053fedd7bcab13a2027fb3bce99b724072b57/content/contributor/unicode-assignment-tools.md#L8-L25)
- [代码执行保留 builtins](https://github.com/thierryc/Glyphs-mcp/blob/590053fedd7bcab13a2027fb3bce99b724072b57/plugin-manager/Glyphs%20MCP.glyphsPlugin/Contents/Resources/code_execution.py#L106-L118)，[exec/eval 执行](https://github.com/thierryc/Glyphs-mcp/blob/590053fedd7bcab13a2027fb3bce99b724072b57/plugin-manager/Glyphs%20MCP.glyphsPlugin/Contents/Resources/code_execution.py#L143-L172)
- [Glyphs 官方购买页](https://glyphsapp.com/buy)：应用以商业许可证销售；开源 MCP 不改变应用本身的许可。

## 更成熟的 CLI / 库替代

| 工具 | 能解决什么 | 无法替代什么 | 开源与本机状态 |
|---|---|---|---|
| **[FontTools](https://github.com/fonttools/fonttools)** | TTFont 读写 TTF/OTF、Unicode cmap、字形轮廓读取、SVGPathPen 输出矢量、子集和字体表检查；适合从有权使用的字体提取骨架、定位原始轮廓、生成可检查路径。 | 不自动理解具体文案的语义，不自动做中文字面率、重心或审美决策；不是交互式字体编辑器。 | MIT。既有本机 **4.63.0，runtime-tested**。用一个包含 20 个不重复汉字的测试集，实测 cmap 全部可映射，SVGPathPen 全部产生非空路径。没有改动或导出系统字体。上游最新 commit 2026-09-18。 |
| **[FontForge](https://github.com/fontforge/fontforge)** | 成熟 GUI + Python/CLI 字体工程：编辑 Bézier、导入轮廓、Unicode glyph、组合字、字距、字体验证与构建。完整字体生产比普通 SVG 编辑器合适。 | 缺少自动的高质量中文艺术字设计决策；批处理成功也不能证明造型成立。 | 整体 GPL-3.0-or-later，多数文件为 BSD-3-Clause，以原 LICENSE 为准。本机未发现 CLI、app 或 Python 模块；未运行。上游最新 commit 2026-09-22。 |
| **[Inkscape](https://gitlab.com/inkscape/inkscape)** | 通用矢量节点编辑、轮廓转路径、布尔切割、曲线处理、SVG/PDF/PNG 输出；对一组单色中文 lettering，比整套字体编译更贴合。 | 不管理完整字体的 cmap、字体度量、hinting 或 OTF/TTF 生产；SVG 可编辑不等于可安装字体。 | 官方 COPYING：大多数代码 GPL-2.0-or-later，另有列明例外。本机未发现 CLI/app；未运行。GitHub 官方仓库仅指向 GitLab，不能用其 2022 年 pushed_at 误判 Inkscape 停止维护。 |
| **[VTracer](https://github.com/visioncortex/vtracer)** | Rust 光栅转 SVG，有 CLI/Python/Node 入口；可把已确认的黑白手绘稿转成初始轮廓。 | 像素边界追踪，不识别汉字部件、笔顺、字义或字体度量。会保留原图瑕疵，不能修复错误字，也不能替代人工节点清理。 | MIT。本子任务检查的 PATH/两套 Python 未发现它；**主任务另已完成 VTracer 实测**，其实际 runtime 与版本以主任务测试记录为准。上游最新 commit 2026-09-20。 |
| **[Glyphs](https://glyphsapp.com/buy) / [RoboFont](https://robofont.com/)** | 成熟商业字体编辑器；Glyphs 有专业字体编辑与脚本接口，RoboFont 以 UFO、Python 和扩展生态为核心。 | 脚本生态或某个插件开源，不代表宿主应用开源。 | 商业产品；RoboFont 官方 [EULA](https://robofont.com/eula/) 是专有软件使用许可。两者在已检查的 /Applications 和 ~/Applications 未发现。没有采购、安装或启动。 |

成熟工具来源：[FontTools README](https://github.com/fonttools/fonttools/blob/4a4138d72bc40d3b744cbac6b6d198204762b974/README.rst)、[getBestCmap 实现](https://github.com/fonttools/fonttools/blob/4a4138d72bc40d3b744cbac6b6d198204762b974/Lib/fontTools/ttLib/ttFont.py#L1355-L1388)、[FontForge LICENSE](https://github.com/fontforge/fontforge/blob/2d950099fa4b9ee3a3b9faabd048af8f91e8db92/LICENSE#L1-L10)、[FontForge Python API](https://github.com/fontforge/fontforge/blob/2d950099fa4b9ee3a3b9faabd048af8f91e8db92/doc/sphinx/scripting/python/fontforge.rst#L4499)、[Inkscape 官方 COPYING](https://gitlab.com/inkscape/inkscape/-/raw/master/COPYING)、[VTracer README](https://github.com/visioncortex/vtracer/blob/b79628fa0ff3c735638e4fe949783479a9f2f97a/README.md#L26-L36)。

## 针对此次单色艺术字的最小路径

1. 先定义中文字形骨架、统一笔画逻辑、重心与字面率，用纯黑轮廓检验。文字转曲只是原料准备，不是完成设计。
2. 现有 FontTools 可提供准确原始轮廓和 Unicode 核查；Figma 的逐字矢量路径负责节点改形、切口、展开、透视和整体排布。保留原文字层及未改形源轮廓。
3. 只有在需要可键入的实验字体、持续增加字符、变量字重或正式字库生产时，才值得引入 Font Design MCP / FontForge / 商业 Glyphs 流程。若以后试用 Font Design MCP，先用“新、转、闪、星、缀、天、空”等少量字验证映射、轮廓、编译与黑白视觉，不能用其拉丁模板直接套中文。
4. 如果有已确认的手绘草图，再考虑 VTracer 建立初始路径。自动追踪和 Shader 均不能代替当前的字形结构设计。

## 已保存证据与局限

- `repository-index.json`：4 次在线查询结果、仓库元数据、固定 commit 与文件树。
- `source-evidence.json`：逐个下载源文件的 URL、commit、字节数与 SHA-256。
- `open_source_tools_evidence.json`：能力、Unicode、依赖、通用执行接口与建议的结构化结论。
- `local-preflight.json`：已检查命令、常见应用位置及两套 Python 环境。
- `fonttools-runtime-test.json`：此次 20 个不同汉字的只读 Unicode/轮廓实测。
- `official-web-evidence.json`：商业应用与 Inkscape 官方许可网页取证。

本机“未发现”仅指已检查的 PATH、/Applications、~/Applications、系统 Python 和 Codex 自带 Python，不证明磁盘任何位置都不存在该软件。Inkscape 官网许可页/CLI 手册请求超时；许可已由官方 GitLab COPYING 补证，未伪称手册读取成功。RoboFont /buy/ 返回 404，随后从官网实际导航定位 /eula/ 并读回。没有把搜索排序、star 数、源码编译或上游测试声明当成中文字形审美证据。


协作补充：主任务在本报告完成时确认 FontTools 与 VTracer 均已实测成功。VTracer 的测试不是本研究子任务执行，因此不将其归到这里保存的 FontTools 运行证据；引用时应附主任务的 VTracer 测试记录。
