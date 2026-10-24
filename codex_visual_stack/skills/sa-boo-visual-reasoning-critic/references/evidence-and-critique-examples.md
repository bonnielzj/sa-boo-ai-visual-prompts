# Evidence and Critique Examples

These examples demonstrate reasoning structure, not fixed answers. Replace facts with what is actually visible in the current source.

## 1. Garment source: do not invent the set

### Weak

```text
这是一套可爱的毛绒睡衣，上衣和裤子都很宽松，整体很梦幻。
```

### Grounded

```text
分析范围：只判断画面中可见外袍；不判断人物身份或未展示的配套单品。

可见事实：正面可见一件长款连帽宽松外袍，袖身连续放量，衣身覆盖到小腿/踝部附近。画面中没有清晰展示独立裤装全貌。
结构与关系：帽体连接领口；袖量从腋下连续展开；下摆是独立边界。正面构件可判断，背面和内层结构不可判断。
材质线索：表面低光泽、边缘柔化并有绒毛扩散，呈毛绒外观；无法仅凭照片确认纤维成分。
无法确认：是否存在配套裤装、背面构造、准确面料成分。
```

Rule: a common category convention is not a visible fact.

## 2. Position is not quantity

User direction:

```text
在下摆约 1/3 处加云朵装饰。
```

Incorrect translation:

```text
在下摆 1/3 区域密集铺满云朵。
```

Correct production parsing:

```text
component: 云朵装饰
position: 下摆附近，约占整件高度的下部 1/3 带状区域
quantity: 未指定
scale: 未指定
attachment: 未指定
minimum sufficient proposal: 先用 3 个有节奏的离散节点，不铺满
question only if needed: 是 3 个、4 个，还是沿整圈连续？
```

## 3. Material cue vs material fact

### Weak

```text
这是羊羔绒，质感很高级。
```

### Grounded

```text
袖口边缘呈短而密的绒毛扩散，主体反光较弱，折叠处圆钝且有压缩感，因此视觉上接近密短绒。图片不能证明它就是羊羔绒，也不能证明克重。
```

## 4. Embroidery, appliqué, and print

```text
VISIBLE_FACT: 图形边缘有连续凸起线迹和局部投影。
SUPPORTED_INFERENCE: 更像刺绣而非平面印花。
UNKNOWN: 分辨率不足，无法确认针法和线材。
ACTION: 若生产要求“刺绣原样转移”，必须使用批准的高清局部图或原始刺绣资产；禁止模型重绘成贴片或印花。
```

## 5. Interior critique with causal logic

### Weak

```text
空间有点平，材质也不够高级，可以加强层次感。
```

### Grounded

```text
意图：形成安静、温暖但有深度的现代客厅。
证据：墙、柜、沙发和地面都集中在接近的中高明度；主要界面使用相似漫反射，接缝阴影也很弱。
效果：前中后景缺少明度和光泽差，体块边界在远看时合并，空间被读成一张平面。
判断：色温方向成立，但层级不足来自“材质与明度同质”，不是缺少装饰。
修改：保留整体暖色；把一个大体块压低约一档明度，给木/石/织物建立不同反射宽度，并恢复柜体与墙面的细窄阴影缝。不要新增零碎摆件来制造假层次。
```

## 6. Photography critique

```text
分析范围：判断产品是否是画面的主角以及图片是否能用于电商首图。
可见事实：最高对比落在人脸和背景高光；产品边缘部分被手遮挡；包装文字在缩略图尺度不可读。
效果：人物吸引力强，但产品证明不足，首图任务被叙事抢占。
判断：适合作为 campaign/context 图，不适合作为唯一 PDP hero。
修改：保留人物状态；新增一张产品无遮挡、正面信息可读、反光受控的 proof shot。不要把 campaign 图强裁成首图替代品。
```

## 7. Reference-role decoding

Given three references:

```text
A: SOURCE_GEOMETRY — authorizes silhouette and component placement only
B: SOURCE_MATERIAL — authorizes pile length, sheen, thickness, edge behavior only
C: REFERENCE_MOOD — authorizes diffused light, haze, palette transition only
```

Do not copy A's material, B's silhouette, or C's decorative motifs unless separately approved.

## 8. Source vs candidate comparison

```text
Requested change: only recolor the existing glasses frame.

Stable anchors:
- face geometry
- glasses shape and position
- hair silhouette
- garment white

Requested differences:
- frame hue and saturation

Collateral differences to reject:
- lens transparency changed
- face softened
- hair strands lost
- glasses duplicated or edge halo added
```

Machine similarity may localize the changed area but cannot approve glasses identity or edge quality.

## 9. Multi-view consistency

Create an entity table:

| Entity | Front | Side | Back | Verdict |
|---|---|---|---|---|
| hood seam | visible center seam | seam turns over crown | continues to back | consistent / unknown / conflict |
| cuff width | measured relative to sleeve | foreshortened | not visible | likely consistent; back unknown |
| charm count | 3 | 2 visible + 1 occluded | attachment points visible | do not call missing until occlusion checked |

Do not compare only color histograms. Track identity, count, attachment, scale, material, and view-dependent occlusion.

## 10. Moodboard analysis

Do not summarize each image separately. Determine roles and system:

```text
anchor image: defines spatial scale and emotional center
material proof: shows actual surface behavior
lighting reference: defines softness/direction/haze
composition reference: defines framing and negative space
outlier: introduces an unrelated color or form language
```

Critique the system:

```text
The board is coherent in warm diffuse light, but two images introduce glossy chrome and hard specular highlights. If the target is tactile warmth, those images are material outliers even though their palette matches.
```

## 11. Generated-image artifacts

```text
VISIBLE_FACT: lower-left cloud edge appears twice, with a semitransparent offset contour.
RELATION: the duplicate overlaps the approved cloud rather than forming a separate object.
JUDGMENT: this is ghosting, not intentional layering.
ACTION: reject the candidate; return to the approved master and re-edit only the target mask. Do not sharpen or blur the duplicate to hide it.
```

## 12. Default concise answer

```text
分析范围：...

可见事实：
- ...

结构与关系：
- ...

设计判断：
- ... because ...

修改指令：
1. ...
2. ...

无法确认：
- ...; 需要 ... 才能确认
```

The user may ask for natural prose. Preserve the evidence chain even when headings are removed.
