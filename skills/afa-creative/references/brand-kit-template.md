# 品牌视觉记忆系统 (Brand Creative Kit Template)

本文件是品牌视觉一致性的核心参考。定义了品牌视觉记忆系统的构建方法、存储格式、5 向探索法和调用规则。

---

## 一、 为什么需要品牌视觉记忆？

AI 生成工具没有"记忆"。每次生成都是从零开始的。如果不提供系统化的品牌约束，AI 会在每次生成中产生风格漂移，导致品牌视觉不一致。

`creative-kit.md` 充当所有 Prompt 的"强制前缀/后缀"，确保跨渠道、跨格式的绝对视觉一致性。

---

## 二、 `creative-kit.md` 标准结构

当创意策略工作流初始化一个新品牌的视觉规范时，应生成并保存以下结构的 Markdown 文件：

```markdown
# [品牌名称] Creative Kit

## 1. 核心视觉定位 (Core Visual Identity)
- **品牌原型**：[如：The Creator / The Hero]
- **视觉情绪**：[3-5 个形容词]
- **目标受众感知**：[希望受众看到图片时的第一感觉]

## 2. 色彩锚点 (Color Anchors)
- **主色调 (Primary)**：[HEX 码 + 颜色名称]
- **辅助色 (Secondary)**：[HEX 码 + 颜色名称]
- **背景色 (Background)**：[HEX 码 + 颜色名称]
- **强调色 (Accent)**：[HEX 码 + 颜色名称]
- **色彩使用比例**：按品牌识别需求动态分配主色、辅色与强调色的使用占比

## 3. 光影与材质 (Lighting & Texture)
- **标准光影**：[如：Soft natural window light from the left]
- **材质质感**：[如：Medium format film grain]
- **色彩分级**：[如：Slightly desaturated, warm highlights]
- **相机锚定**：[如：shot on Fujifilm X-T5, 35mm equivalent]

## 4. 排版方向 (Typography Direction)
- **主标题**：[字体名称 + 字重]
- **正文**：[字体名称 + 字重]
- **CTA**：[字体名称 + 字重]
- **排版规则**：[对齐方式、间距等]

## 5. 摄影/插画风格 (Visual Style)
- **构图偏好**：[如：Rule of thirds, negative space on right]
- **人物呈现**：[如：Candid moments, diverse casting]
- **产品呈现**：[如：In-context lifestyle shots]
- **背景偏好**：[如：Natural materials, wood, marble]

## 6. 反模式清单 (The "Never Do This" List)
- [如：No neon or fluorescent colors]
- [如：No generic stock photo smiles]
- [如：No perfect symmetry]
- [如：No floating objects without context]
```

---

## 三、 5 向探索法 (The 5-Direction Exploration)

在确立 `creative-kit.md` 之前，如果品牌没有现成的视觉规范，创意策略工作流宜运行“5 向探索法”来帮助用户做决定。

不要问用户"你想要什么风格？"——大多数人不知道。给他们 5 个具体的选项：

### Direction 1: The Category Standard (安全牌)
- 描述：符合该行业最常见、最被接受的高质量视觉标准
- 目的：建立基准线

### Direction 2: The Opposite (反向牌)
- 描述：刻意违背行业常规。如果行业是明亮的，这个就是暗黑的
- 目的：测试用户对差异化的接受度

### Direction 3: The Borrowed Aesthetic (跨界牌)
- 描述：借用另一个完全不同行业的视觉语言
- 目的：创造高级感和新奇感

### Direction 4: Emotion-First (情感牌)
- 描述：弱化产品本身，极度放大使用产品时的情绪状态
- 目的：测试品牌是否准备好进行情感营销

### Direction 5: The Wild Card (外卡牌)
- 描述：大胆、破坏性、超现实或极具艺术感的视觉实验
- 目的：寻找强烈的模式中断

**执行流程**：
1. 为 5 个方向各生成一段详细的视觉描述（或直接生成示例图）
2. 让用户选择最喜欢的一个，或组合多个方向
3. 根据用户反馈，锁定最终的 `creative-kit.md`

---

## 四、 Brand Kit 构建信息收集

### 4.1 优先收集

1. 品牌名称和品类
2. 品牌色彩（至少主色和辅色的 Hex 值）
3. 品牌字体（或至少描述品牌的视觉感受）
4. 目标受众描述
5. 品牌调性（3-5 个形容词）

### 4.2 可选收集

6. 品牌网站 URL（用于提取视觉风格）
7. 现有的品牌规范文件
8. 竞品品牌（用于差异化定位）
9. 品牌故事/创始人故事

### 4.3 自动推断逻辑

| 已知信息 | 可推断信息 |
| :--- | :--- |
| 品牌品类 + 调性 | 色彩系统、字体推荐 |
| 品牌网站 URL | 色彩、字体、视觉风格 |
| 目标受众 | 视觉风格、摄影风格 |
| 竞品品牌 | 差异化的视觉方向 |

---

## 五、 Brand Kit 在 Prompt 中的注入方式

### 5.1 注入模板

每次构建 Prompt 时，宜在开头注入 Brand Kit 核心约束：

```text
[Brand Context]
Brand: [品牌名]
Color palette: [主色], [辅色], [强调色]
Visual style: [摄影风格描述]
Camera anchor: [相机锚定]
Lighting: [光影风格]
Mood: [品牌调性形容词]
Must avoid: [禁止元素]

[Creative Brief]
[具体的创意需求...]
```

### 5.2 注入优先级

当 Brand Kit 约束与具体创意需求冲突时：
1. **品牌色彩** > 创意色彩偏好（不可妥协）
2. **品牌字体** > 创意字体偏好（不可妥协）
3. **创意构图** > 品牌构图偏好（可灵活调整）
4. **创意光影** > 品牌光影偏好（可根据场景调整）

---

## 六、 Brand Kit 文件存储规范

Brand Kit 应保存在品牌的工作目录中：
```text
/brand-name/
├── creative-kit.md       (品牌视觉记忆系统)
├── voice-and-tone.md     (品牌声音系统 — 由品牌定位工作流生成)
├── assets/
│   ├── logo-full-color.png
│   ├── logo-white.png
│   ├── logo-black.png
│   └── mood-board.png
└── creatives/
    └── [生成的创意资产]
```

---

## 七、 Brand Kit 质量自检清单

- [ ] 色彩系统是否覆盖主色、辅助色与必要的强调色，并附带清晰的 HEX 码？
- [ ] 每种颜色是否有明确的使用场景描述？
- [ ] 字体系统是否包含标题、正文和 CTA 字体？
- [ ] 视觉风格描述是否可以直接注入 Prompt？
- [ ] 是否有明确的"禁止清单"？
- [ ] 是否有相机/胶片锚定？
- [ ] 是否考虑了深色模式适配？
- [ ] Brand Kit 是否已保存到品牌工作目录？


