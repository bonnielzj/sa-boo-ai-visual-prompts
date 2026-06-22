# SA&BOO 文字转图片 Prompt 操作系统

## 一、核心公式

中文公式：

```text
为{用途/平台}生成{主体}视觉，核心概念是{视觉母题}。画面采用{风格机制}，构图{位置/比例/留白/网格}，材质为{材质与触感}，光线{光型/方向/氛围}，色彩{主色/辅色/饱和度}，镜头/渲染{摄影/3D/插画/线稿}。预留{文字/Logo/CTA}区域。整体气质{情绪关键词}。避免{负面词}。
```

英文公式：

```text
Create a {channel/use} visual of {subject}, built around {visual metaphor}. Use {style mechanism}, {composition}, {material/texture}, {lighting/color}, {camera/render mode}. Reserve a clean area for {text/logo/CTA}. Mood: {mood}. Avoid {negative constraints}.
```

## 二、必须包含的变量

| 变量 | 说明 | 示例 |
|---|---|---|
| Subject 主体 | 人、空间、产品、花、符号、品牌物件 | office lobby, silver flower, perfume bottle |
| Style 风格机制 | 不是形容词，而是视觉生成逻辑 | liquid silver, editorial grid, cinematic stage |
| Material 材质 | 控制高级感的关键 | chrome, frosted glass, silk, wax, paper fiber |
| Composition 构图 | 决定画面是否可用 | centered, symmetrical, wide hero, large negative space |
| Light 光线 | 决定情绪与质感 | soft diffusion, rim light, spotlight, Tyndall effect |
| Color 色彩 | 决定品牌气质 | black-silver, cream-gold, off-white, muted earth |
| Camera / Render 镜头 | 决定真实度与媒介 | product photography, 3D render, cinematic still |
| Typography Zone 文字区 | 封面/海报必写 | clean title-safe area, empty upper third |
| Constraints 约束 | 防止跑偏 | no watermark, no random text, no clutter |

## 三、负面词库

### 通用负面词

```text
low quality, blurry, noisy, messy composition, watermark, fake logo, random text, distorted hands, extra objects, cluttered background, overexposed, cheap plastic, generic AI look
```

### 高级商业视觉负面词

```text
cheap glitter, gaudy decoration, overly saturated, messy reflections, low-end stock photo, crowded layout, childish cartoon look
```

### 线稿/矢量负面词

```text
photorealistic, shaded render, blurry lines, jagged edges, unreadable annotations, messy handwriting, low resolution
```

### 室内概念负面词

```text
impossible structure, distorted furniture, unrealistic scale, unsafe stairs, blocked circulation, fake materials, overdecorated, poor lighting
```

### 小红书/封面负面词

```text
unreadable title area, text behind busy background, random letters, low contrast, too many stickers, messy title placement
```

## 四、Prompt QA 清单

生成前检查：

- 是否说明了用途和平台？
- 是否明确主体？
- 是否写了材质、光线、构图、色彩？
- 是否预留标题/Logo/CTA区域？
- 是否有负面词？
- 是否需要后期在 Figma / Canva / PPT 中排文字？
- 是否涉及客户隐私、版权、商标或文化符号风险？

