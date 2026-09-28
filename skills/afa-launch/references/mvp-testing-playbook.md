# MVP 广告测试完整操作手册

> 本文档为 `afa-launch` 的参考文件，提供从假设提炼到胜出者确认的完整 MVP 广告测试操作流程。

---

## 一、测试哲学

```text
核心原则：
├── 每一分钱的广告支出都是一个数据采集行为
├── 每一个创意都是一个可验证的假设
├── 测试的目的不是"找到好广告"，而是"找到有效的价值主张"
├── 先测试"说什么"（Message），再测试"怎么说"（Creative）
└── 统计显著性 > 直觉判断
```

---

## 二、假设提炼方法论

### 2.1 假设来源矩阵

| 来源 | 方法 | 输出 |
|------|------|------|
| 用户访谈 | 提取高频痛点词和期望表达 | 3-5 个痛点假设 |
| 竞品评论 | 分析 1-3 星差评中的未满足需求 | 2-3 个差异化假设 |
| 搜索数据 | Google Keyword Planner + 自动补全 | 2-3 个需求假设 |
| Reddit/论坛 | 品类相关讨论中的高赞回复 | 2-3 个语言假设 |
| Beta 测试 | 用户最常提及的正面体验 | 2-3 个价值假设 |

### 2.2 假设格式化

每个假设必须遵循以下结构：

```text
假设 ID：H[编号]
价值主张：[一句话描述产品解决的核心问题]
目标受众：[谁最在乎这个问题]
证据强度：[强/中/弱]（基于来源数据的充分程度）
测试优先级：[P0/P1/P2]

示例：
假设 ID：H1
价值主张：「30 秒解决晨间护肤，不再迟到」
目标受众：25-35 岁职场女性，通勤时间 > 30 分钟
证据强度：强（72% 访谈者主动提及时间痛点）
测试优先级：P0
```

### 2.3 假设数量控制

```text
最佳实践：
├── 首轮测试：3-5 个假设（不超过 5 个）
├── 每个假设：3-5 个钩子变体
├── 总创意数：15-25 个
└── 原因：假设过多 → 预算分散 → 无法达到统计显著性
```

---

## 三、钩子矩阵构建

### 3.1 六大钩子类型

| 类型 | 机制 | 模板 | 适用场景 |
|------|------|------|----------|
| **恐惧/痛点** | 放大问题的严重性 | "You're probably doing [X] wrong..." | 用户已意识到问题 |
| **好奇/悬念** | 制造信息缺口 | "I found out why [problem] keeps happening..." | 用户有模糊困扰 |
| **社会证明** | 借助他人验证 | "10,000 people switched to [product] last month" | 品类认知已建立 |
| **对比/颠覆** | 挑战现有认知 | "I threw away my [competitor] after trying this" | 竞品用户转化 |
| **结果/变化** | 展示使用前后 | "Day 1 vs Day 30 — I can't believe the difference" | 效果可视化品类 |
| **权威/专家** | 借助专业背书 | "As a dermatologist, this is the only [product] I recommend" | 高信任门槛品类 |

### 3.2 钩子矩阵示例

```text
假设 H1：「30 秒解决晨间护肤」

钩子矩阵：
├── 恐惧型：  "Your morning routine is stealing 20 minutes of sleep every day"
├── 好奇型：  "I replaced 5 skincare products with this one thing"
├── 社会证明："47,000 women ditched their 10-step routine for this"
├── 对比型：  "My old routine vs. now — same results, 30 seconds"
└── 结果型：  "Week 1 vs Week 4 using only ONE product"
```

---

## 四、广告账户测试结构

### 4.1 Meta Ads 测试结构

```text
Campaign (CBO, $50-100/day)
├── Ad Set 1: Hypothesis H1 — Broad Targeting
│   ├── Ad 1: H1 × 恐惧钩子 (Video)
│   ├── Ad 2: H1 × 好奇钩子 (Video)
│   ├── Ad 3: H1 × 社会证明钩子 (Video)
│   ├── Ad 4: H1 × 对比钩子 (Image)
│   └── Ad 5: H1 × 结果钩子 (UGC)
│
├── Ad Set 2: Hypothesis H2 — Broad Targeting
│   ├── Ad 1: H2 × 恐惧钩子 (Video)
│   ├── Ad 2: H2 × 好奇钩子 (Video)
│   ├── Ad 3: H2 × 社会证明钩子 (Video)
│   ├── Ad 4: H2 × 对比钩子 (Image)
│   └── Ad 5: H2 × 结果钩子 (UGC)
│
└── Ad Set 3: Hypothesis H3 — Broad Targeting
    ├── Ad 1: H3 × 恐惧钩子 (Video)
    ├── Ad 2: H3 × 好奇钩子 (Video)
    ├── Ad 3: H3 × 社会证明钩子 (Video)
    ├── Ad 4: H3 × 对比钩子 (Image)
    └── Ad 5: H3 × 结果钩子 (UGC)
```

### 4.2 TikTok Ads 测试结构

```text
Campaign (Minimum Spend, $50-100/day)
├── Ad Group 1: Hypothesis H1 — Auto Targeting
│   ├── Spark Ad 1: H1 × 创始人叙事
│   ├── Spark Ad 2: H1 × UGC 风格
│   └── Spark Ad 3: H1 × 教程/How-to
│
├── Ad Group 2: Hypothesis H2 — Auto Targeting
│   ├── Spark Ad 1: H2 × 创始人叙事
│   ├── Spark Ad 2: H2 × UGC 风格
│   └── Spark Ad 3: H2 × 教程/How-to
│
└── Ad Group 3: Hypothesis H3 — Interest Targeting
    ├── Spark Ad 1: H3 × 创始人叙事
    ├── Spark Ad 2: H3 × UGC 风格
    └── Spark Ad 3: H3 × 教程/How-to
```

### 4.3 Google Ads 测试结构

```text
Campaign 1: Brand Search ($10-20/day)
├── Ad Group: Brand Terms
│   ├── RSA 1: Brand + Value Prop H1
│   └── RSA 2: Brand + Value Prop H2

Campaign 2: Category Search ($20-30/day)
├── Ad Group 1: Problem-Aware Keywords
│   ├── RSA 1: Problem → Solution angle
│   └── RSA 2: Comparison angle
│
└── Ad Group 2: Product-Aware Keywords
    ├── RSA 1: Feature-benefit angle
    └── RSA 2: Social proof angle

Campaign 3: Shopping ($20-30/day)
└── Product Feed (optimized titles with top hypothesis keywords)
```

---

## 五、裁决标准与决策矩阵

### 5.1 数据采集最低要求

| 指标 | 最低样本量 | 说明 |
|------|-----------|------|
| 展示量 | 1,000+ / 创意 | 低于此数据无统计意义 |
| 点击量 | 100+ / 创意 | 用于评估 CTR |
| 加购量 | 20+ / 假设 | 用于评估购买意向 |
| 转化量 | 10+ / 假设 | 用于评估 CPA |
| 测试时长 | 至少 5 天 | 覆盖工作日和周末 |

### 5.2 三级裁决标准

```text
Level 1 裁决（D+3）：钩子级别
├── 钩子率 > 30% → 保留
├── 钩子率 20-30% → 观察至 D+5
└── 钩子率 < 20% → 关停，替换新钩子

Level 2 裁决（D+5）：假设级别
├── CTR > 1.5% 且 CPA ≤ 目标 130% → 胜出假设，进入扩展
├── CTR > 1.5% 但 CPA > 目标 130% → 优化落地页，继续测试
├── CTR 0.8-1.5% → 测试新钩子变体
└── CTR < 0.8% → 关停该假设

Level 3 裁决（D+7）：最终确认
├── 有 1+ 假设 CPA ≤ 目标 → 确认胜出者，进入阶段 2 引爆
├── 所有假设 CPA > 目标但 < 200% → 优化后再测 1 轮
└── 所有假设 CPA > 目标 200% → 暂停投放，回到假设提炼
```

### 5.3 胜出者确认清单

```text
一个假设被确认为"胜出者"需要满足：
□ CPA ≤ 目标价格（或目标 ROAS 的 80%+）
□ 至少 10+ 次转化
□ CTR ≥ 品类基准
□ 连续 3 天数据稳定（波动 < 20%）
□ 至少 2 个钩子变体表现合格（证明假设本身有效，而非单一创意偶然）
```

---

## 六、测试常见错误与纠正

| 错误 | 后果 | 纠正方法 |
|------|------|----------|
| 同时测试 > 5 个假设 | 预算分散，无法达到统计显著性 | 严格控制 3-5 个假设 |
| 在学习期内调整出价/预算 | 重置学习，浪费已积累数据 | 等待 50 次转化或 7 天 |
| 基于 < 1,000 展示做决策 | 数据随机性过高 | 等待最低样本量 |
| 只看 CPA 不看 CTR | 忽略了创意层面的信号 | 分层评估：钩子率 → CTR → CVR → CPA |
| 所有创意用同一受众 | 无法区分创意效果和受众效果 | 使用 Broad Targeting 让算法分配 |
| 测试期间频繁更换落地页 | 引入额外变量，无法归因 | 测试期间锁定落地页 |
| 过早宣布"胜出者" | 可能是数据波动 | 要求连续 3 天稳定 |
