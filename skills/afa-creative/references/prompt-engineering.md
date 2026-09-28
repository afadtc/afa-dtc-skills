# Prompt 工程学

## 五、 Prompt 工程学 (Prompt Engineering System)

创意制作流程中的 Prompt 不是随意拼凑的词汇，而是遵循严格的 5 层约束模型。

### 5.1 五层 Prompt 约束模型

每个商业级 Prompt 必须包含以下 5 层，按顺序构建：

**第 1 层：主体与动作 (Subject & Action)**
定义画面中的核心主体和正在发生的事情。这是 Prompt 的骨架。
- 示例：`A woman in her 30s holding a ceramic skincare bottle`

**第 2 层：环境与语境 (Environment & Context)**
定义主体所处的物理空间和叙事语境。
- 示例：`in a bright bathroom with white subway tiles, morning routine`

**第 3 层：光影与色彩 (Lighting & Color)**
注入品牌 Creative Kit 中锁定的光影和色彩参数。这是消除 AI 塑料感的核心层。
- 示例：`soft natural window light from the left, warm golden hour tones, muted color palette`

**第 4 层：技术锚定 (Technical Anchor)**
将画面锚定在真实世界的摄影器材或胶片上，防止 AI 滑向"AI 艺术站"画风。
- 示例：`shot on Fujifilm X-T5 with 56mm f/1.2 lens, shallow depth of field, slight film grain`

**第 5 层：反模式护城河 (Anti-Pattern Guardrails)**
注入负面提示词和品牌反模式清单。
- 示例：`Avoid: plastic skin, over-saturated colors, perfect symmetry, stock photo smile, floating objects`

### 5.2 完整 Prompt 组装示例

将 5 层组装成一个完整的商业级 Prompt：

```text
A woman in her 30s holding a ceramic skincare bottle, genuine half-smile,
looking slightly off-camera, in a bright bathroom with white subway tiles
and morning sunlight, soft natural window light from the left, warm golden
hour tones, muted terracotta and cream color palette, shot on Fujifilm X-T5
with 56mm f/1.2 lens, shallow depth of field, slight film grain, candid
lifestyle photography, 4:5 portrait composition with negative space at top
for text overlay. Avoid: plastic skin, over-saturated colors, perfect
symmetry, stock photo smile, floating objects, HDR, lens flare.
```

### 5.3 Prompt 中的文本渲染规则

AI 生成图像中的文本往往是灾难。必须遵循严格的文本渲染协议：

**场景 A：文本融入环境**（如：霓虹灯招牌、产品包装标签）
- 策略：在 Prompt 中直接渲染。
- 规则：文本必须极短（1-3 个词），必须用双引号精确包裹，并描述材质。
- 示例：`a glowing red neon sign reading "OPEN" mounted on a dark brick wall`

**场景 B：UI 元素或营销文案**（如：广告标题、CTA 按钮、信息图表）
- 策略：**绝对禁止**在 AI 图像中渲染。
- 规则：生成干净的背景（留白），在后期处理中叠加文本。
- 示例：在 Prompt 中加入 `negative space on the right side for text overlay`

### 5.4 留白构图法 (Negative Space Composition)

为了给后期文本叠加留出空间，Prompt 必须包含构图指令：

| 文本位置需求 | Prompt 注入词 |
| :--- | :--- |
| 右侧留白 | `negative space on the right side for text overlay` |
| 上方留白 | `subject positioned on the lower third, empty sky/space above` |
| 左侧留白 | `clean uncluttered background on the left` |
| 底部留白 | `subject in upper half, solid color gradient at bottom` |
| 中央留白 | `subject framed around edges, open center for text` |

---

