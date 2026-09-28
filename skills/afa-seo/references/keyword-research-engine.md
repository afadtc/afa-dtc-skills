# 关键词研究引擎 (Keyword Research Engine)

> **核心理念**：关键词研究不是"找搜索量高的词"，而是发现用户的搜索意图，并将其映射到品牌的商业目标上。

## 一、种子词发现（5 大渠道）

```
1. 品牌核心产品/服务：
   ├── 产品名称、品类名称、核心功能
   ├── 示例：hiking backpack, trail running shoes, camping tent
   └── 方法：从 products.md 和分类结构中提取

2. 竞品分析：
   ├── 竞品排名的关键词（Ahrefs/SEMrush Organic Keywords）
   ├── 竞品排名但品牌未覆盖的关键词（Content Gap）
   ├── 竞品 Google Ads 投放的关键词（暗示高商业价值）
   └── 方法：输入若干直接竞品域名进行分析，数量按市场复杂度调整

3. 用户语言：
   ├── 客服常见问题和投诉
   ├── 产品评论中的高频词汇
   ├── 社交媒体讨论（Reddit, Facebook Groups）
   ├── Google Search Console 中的实际搜索词
   └── 方法：从 learnings.jsonl 和用户反馈中提取

4. Google 自动补全与相关搜索：
   ├── 在 Google 搜索框输入核心词，记录自动补全建议
   ├── 搜索结果底部的"相关搜索"
   ├── "People Also Ask" 问题
   └── 方法：系统化地遍历核心词的字母组合

5. 行业与趋势：
   ├── Google Trends 中的上升趋势词
   ├── 行业报告中的新兴术语
   ├── 季节性关键词（如 "best hiking gear for summer"）
   └── 方法：结合 brand-brain 中的行业洞察
```

## 二、六圈扩展法

```
从种子词出发，通过 6 个维度系统性扩展：

圈 1：修饰词扩展
├── 最佳/推荐：best, top, recommended
├── 价格：cheap, affordable, budget, premium, luxury
├── 年份：2026, latest, new
├── 评价：review, rating, comparison
└── 示例："best hiking backpack" → "best hiking backpack 2026"

圈 2：属性扩展
├── 材质：leather, nylon, waterproof
├── 颜色：black, red, blue
├── 尺寸：small, large, 40L, 60L
├── 特性：lightweight, durable, foldable
└── 示例："hiking backpack" → "lightweight waterproof hiking backpack"

圈 3：受众扩展
├── 性别：men's, women's, unisex
├── 年龄：kids, teens, seniors
├── 技能：beginner, professional, advanced
├── 身体：plus size, petite, wide feet
└── 示例："hiking backpack" → "hiking backpack for women beginners"

圈 4：场景/用途扩展
├── 活动：hiking, camping, travel, commuting
├── 时长：day trip, 3-day, week-long
├── 地点：mountains, desert, tropical
├── 季节：summer, winter, all-season
└── 示例："hiking backpack" → "hiking backpack for 3-day mountain trip"

圈 5：问题/意图扩展
├── How to：how to choose, how to pack, how to clean
├── What：what size, what brand, what to look for
├── Why：why is [product] expensive, why choose [brand]
├── vs：[product A] vs [product B]
└── 示例："hiking backpack" → "how to choose a hiking backpack"

圈 6：长尾组合扩展
├── 组合以上维度的交叉词
├── 示例："best lightweight hiking backpack for women 2026"
├── 示例："how to pack a 40L hiking backpack for a 3-day trip"
├── 验证：确保组合词有实际搜索量
└── 工具：Ahrefs Keywords Explorer [$$$], Google Keyword Planner [Free]
```

## 三、搜索意图分类（四大类型）

```
信息型 (Informational) — 用户想学习/了解：
├── 信号词：how to, what is, why, guide, tips, tutorial
├── 内容匹配：博客文章、教程、指南
├── 商业价值：低（但建立主题权威）
├── 示例："how to choose a hiking backpack"
└── 策略：用深度内容建立信任，通过内部链接引导到商业页面

商业调研型 (Commercial Investigation) — 用户在比较/评估：
├── 信号词：best, top, review, comparison, vs, alternative
├── 内容匹配：对比文章、评测、推荐列表
├── 商业价值：中高（用户接近购买决策）
├── 示例："best hiking backpack 2026"
└── 策略：提供客观对比，突出品牌优势，引导到产品页

交易型 (Transactional) — 用户准备购买：
├── 信号词：buy, shop, order, price, discount, coupon, deal
├── 内容匹配：产品页、分类页
├── 商业价值：最高（直接转化）
├── 示例："buy Osprey Atmos 65 AG"
└── 策略：确保产品页/分类页完美匹配，优化转化路径

导航型 (Navigational) — 用户找特定品牌/网站：
├── 信号词：[brand name], [brand] + [product], [brand] login
├── 内容匹配：首页、品牌页
├── 商业价值：高（品牌忠诚用户）
├── 示例："Allbirds tree runner"
└── 策略：确保品牌词排名第一，优化 Knowledge Panel
```

## 四、关键词集群化流程

```
步骤 1：按主题分组
├── 将所有关键词按核心主题归类
├── 每个主题 = 一个潜在的主题集群
├── 示例主题："hiking backpacks", "trail running shoes", "camping tents"
└── 工具：Ahrefs Keywords Explorer 的 Clusters 功能 [$$$]

步骤 2：按意图细分
├── 在每个主题内，按搜索意图进一步分组
├── 信息型关键词 → 博客内容
├── 商业调研型关键词 → 对比/评测内容
├── 交易型关键词 → 产品页/分类页
└── 确保每个意图都有对应的页面

步骤 3：确定支柱词与集群词
├── 支柱词：搜索量最高的核心词（分配给支柱页面）
├── 集群词：长尾变体（分配给集群内容）
├── 规则：一个页面只针对一个主要关键词（避免内部竞争）
└── 映射：关键词 → 页面 的一对一映射表

步骤 4：输出关键词计划
├── 结构化输出（参考 keyword-plan schema）：
│   ├── brand_name：品牌名称
│   ├── seed_keywords：种子关键词列表
│   ├── clusters[]：关键词集群数组
│   │   ├── cluster_name：集群名称
│   │   ├── priority：优先级（high/medium/low）
│   │   ├── intent：主导搜索意图
│   │   ├── pillar_topic：推荐的支柱文章主题
│   │   ├── estimated_total_volume：集群总搜索量
│   │   └── keywords[]：关键词数组（含 volume, difficulty, opportunity_score）
│   ├── competitor_gaps[]：竞品覆盖但品牌未覆盖的关键词
│   └── content_roadmap[]：按优先级排序的内容生产计划
└── 格式：JSON 或 Markdown 表格
```

## 五、优先级矩阵（四维评估）

```
维度 1：商业价值 (Business Value) — 权重 35%
├── 高：直接与产品/服务相关的交易型词
├── 中：商业调研型词（对比、评测）
├── 低：纯信息型词（但有主题权威价值）
└── 评估：CPC 是商业价值的代理指标

维度 2：排名难度 (Ranking Difficulty) — 权重 25%
├── 低：相对容易切入，通常更适合新站或弱权重站点
├── 中：需要更好的内容质量与一定权威支撑
├── 高：通常需要更强域名权威、内容深度与外链支持
└── 策略：新站从低难度词开始，逐步攻克高难度词

维度 3：搜索量 (Search Volume) — 权重 20%
├── 高：在当前市场中具备较强需求规模
├── 中：在当前市场中具备稳定需求规模
├── 低：需求相对有限，但不代表没有商业价值
└── 注意：低搜索量但高商业价值的长尾词同样重要

维度 4：趋势方向 (Trend) — 权重 20%
├── 上升：搜索量持续增长（优先投入）
├── 稳定：搜索量平稳
├── 下降：搜索量持续减少（谨慎投入）
└── 工具：Google Trends [Free], Ahrefs Keyword Explorer [$$$]

综合评分公式：
Opportunity Score = (商业价值 × 0.35) + ((100 - 难度) × 0.25) + (搜索量标准化 × 0.20) + (趋势分 × 0.20)

优先级分配：
├── P0（优先执行）：Opportunity Score 处于最高分段，且商业价值明确
├── P1（近期排期）：Opportunity Score 处于中高分段
├── P2（后续排期）：Opportunity Score 处于中低分段
└── P3（观察列表）：Opportunity Score 当前较低，暂不优先
```
