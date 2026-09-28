# Google 搜索广告实战手册

> **用途**：本文件为 Google 广告模块的内部参考文件，用于设计、创建和优化搜索广告系列。

---

## 一、DTC 搜索广告架构

### 1.1 推荐账户架构

```
Google Ads 账户
│
├── 品牌搜索系列
│   ├── 广告组：品牌名精确
│   ├── 广告组：品牌名 + 产品
│   └── 广告组：品牌名 + 评价/对比
│
├── 非品牌搜索系列（高意图）
│   ├── 广告组：产品类别词
│   ├── 广告组：产品特性词
│   ├── 广告组：购买意图词（"buy"、"best"、"review"）
│   └── 广告组：价格/促销词（"discount"、"sale"）
│
├── 非品牌搜索系列（信息型）
│   ├── 广告组：问题/痛点词
│   ├── 广告组：教程/指南词
│   └── 广告组：对比/评测词
│
├── 竞品搜索系列
│   ├── 广告组：竞品品牌名
│   ├── 广告组：竞品 + 替代
│   └── 广告组：竞品 + 对比
│
└── DSA 系列（动态搜索广告）
    ├── 广告组：全站（排除品牌和已覆盖页面）
    └── 广告组：特定品类页面
```

### 1.2 关键词匹配类型策略（2026）

```
2026 匹配类型最佳实践：

广泛匹配（Broad Match）：
├── 适用：与智能出价配合使用
├── 优势：最大覆盖范围，AI 优化匹配
├── 风险：可能匹配不相关搜索词
├── 必须：配合否定关键词列表
└── 推荐场景：PMax 无法覆盖的长尾搜索

词组匹配（Phrase Match）：
├── 适用：需要一定控制的核心词
├── 优势：平衡覆盖和精准度
├── 风险：可能遗漏变体
└── 推荐场景：主力关键词

精确匹配（Exact Match）：
├── 适用：高价值、高竞争的核心词
├── 优势：最精准的控制
├── 风险：覆盖范围有限
└── 推荐场景：品牌词、核心转化词

推荐策略：
├── 品牌词：精确匹配（控制成本）
├── 核心产品词：词组匹配（平衡）
├── 长尾词：广泛匹配 + 智能出价（扩展覆盖）
└── 竞品词：词组匹配（避免过度扩展）
```

---

## 二、RSA（响应式搜索广告）撰写指南

### 2.1 标题撰写框架

```
15 个标题的分配策略：

标题 1-3（固定位置候选）：
├── 标题 1：品牌名 + 核心卖点
│   └── 示例："Glossier | Clean Beauty That Works"
├── 标题 2：核心产品/服务
│   └── 示例："Award-Winning Skincare Essentials"
└── 标题 3：行动号召 + 促销
    └── 示例："Shop Now - Free Shipping Over $30"

标题 4-8（价值主张变体）：
├── 差异化优势
│   └── 示例："Dermatologist-Tested Formulas"
├── 社会证明
│   └── 示例："Loved by 2M+ Customers"
├── 产品特性
│   └── 示例："Vegan & Cruelty-Free Products"
├── 用户利益
│   └── 示例："Get Your Best Skin in 30 Days"
└── 紧迫感
    └── 示例："Limited Edition - While Supplies Last"

标题 9-12（关键词变体）：
├── 包含目标关键词的自然表达
├── 不同角度描述同一产品/服务
├── 针对不同搜索意图的变体
└── 包含品类词和属性词

标题 13-15（测试变体）：
├── 大胆的创意表达
├── 数据/统计驱动
└── 问题式标题

⚠️ 重要规则：
├── 每个标题必须独立有意义（不依赖其他标题）
├── 至少 3 个标题包含目标关键词
├── 至少 2 个标题包含行动号召
├── 避免标题之间过度重复
└── 使用固定位置功能锁定最重要的标题
```

### 2.2 描述撰写框架

```
4 个描述的分配策略：

描述 1（核心价值主张）：
├── 完整的价值主张 + 信任信号 + CTA
├── 示例："Discover clean, effective skincare backed by science. 
│   Dermatologist-tested, vegan formulas loved by 2M+ customers. 
│   Free shipping on orders over $30. Shop now."
└── 长度：尽量用满 90 字符

描述 2（产品特性 + 保障）：
├── 核心产品特性 + 购买保障
├── 示例："Our bestselling Cloud Paint blush delivers a natural, 
│   dewy finish in seconds. 100% satisfaction guaranteed with 
│   free returns within 30 days."
└── 长度：尽量用满 90 字符

描述 3（社会证明 + 差异化）：
├── 评论/媒体/奖项 + 竞争优势
├── 示例："Rated #1 by Allure Best of Beauty 2024. Made with 
│   clean ingredients you can trust. Join millions who've 
│   simplified their skincare routine."
└── 长度：尽量用满 90 字符

描述 4（促销/紧迫感）：
├── 当前促销 + 限时信息
├── 示例："Spring Sale: 20% off sitewide with code SPRING20. 
│   Plus free deluxe samples with every order. Limited time 
│   only - don't miss out!"
└── 长度：尽量用满 90 字符
```

---

## 三、广告扩展完整指南

### 3.1 必须使用的扩展

```
站点链接扩展（Sitelink）：
├── 至少 8 个（系统选择最佳 4 个展示）
├── 推荐站点链接：
│   ├── "Shop Best Sellers" → 畅销品页面
│   ├── "New Arrivals" → 新品页面
│   ├── "Sale & Offers" → 促销页面
│   ├── "Customer Reviews" → 评论页面
│   ├── "About Our Story" → 品牌故事页面
│   ├── "Free Shipping Policy" → 配送政策页面
│   ├── "Gift Sets" → 礼品套装页面
│   └── "Subscribe & Save" → 订阅页面
└── 每个站点链接包含 2 行描述

摘要扩展（Callout）：
├── 至少 6 个
├── 推荐摘要：
│   ├── "Free Shipping Over $50"
│   ├── "30-Day Free Returns"
│   ├── "Vegan & Cruelty-Free"
│   ├── "2M+ Happy Customers"
│   ├── "Dermatologist Tested"
│   └── "Subscribe & Save 15%"
└── 每个 ≤ 25 字符

结构化摘要（Structured Snippet）：
├── 至少 2 个标题
├── 推荐标题：
│   ├── "Types"：产品类型列表
│   ├── "Brands"：品牌列表（如果多品牌）
│   └── "Destinations"：配送地区
└── 每个标题至少 3 个值

促销扩展（Promotion）：
├── 当前促销信息
├── 包含：折扣类型、促销代码、有效期
└── 按季节/节日更新

价格扩展（Price）：
├── 至少 3 个产品/服务
├── 包含：产品名、价格、描述、链接
└── 按品类或价格区间组织
```

---

## 四、否定关键词策略

### 4.1 DTC 通用否定关键词列表

```
信息型否定词（除非有内容营销策略）：
├── "how to"、"what is"、"tutorial"
├── "diy"、"homemade"、"recipe"
├── "free"、"sample"（除非提供免费样品）
└── "wiki"、"definition"、"meaning"

求职/招聘否定词：
├── "jobs"、"careers"、"hiring"
├── "salary"、"interview"、"resume"
└── "internship"、"employment"

竞品否定词（用于非竞品系列）：
├── 主要竞品品牌名
├── 竞品产品名
└── 竞品创始人名

不相关否定词：
├── "wholesale"、"bulk"（除非 B2B）
├── "used"、"second hand"、"refurbished"
├── "cheap"、"cheapest"（如果定位中高端）
├── "lawsuit"、"scam"、"complaint"
└── "stock"、"investor"、"ipo"

地域否定词（如果不配送）：
├── 不配送的国家/地区名
└── 不配送的城市名
```

### 4.2 否定关键词管理流程

```
每周流程：
├── 步骤 1：下载搜索词报告（过去 7 天）
├── 步骤 2：筛选无转化且花费 > $10 的搜索词
├── 步骤 3：评估每个搜索词的相关性
├── 步骤 4：将不相关搜索词添加为否定关键词
├── 步骤 5：选择合适的匹配类型
│   ├── 完全不相关 → 广泛匹配否定
│   ├── 部分相关但不精准 → 词组匹配否定
│   └── 特定变体不相关 → 精确匹配否定
└── 步骤 6：记录添加的否定词和原因

每月流程：
├── 审查否定关键词列表
├── 检查是否有误排除（搜索量突然下降）
├── 更新共享否定关键词列表
└── 与 PMax 账户级否定词同步
```

---

## 五、出价策略指南

### 5.1 出价策略选择矩阵

```
按月转化量选择：

月转化 < 15：
├── 推荐：手动 CPC（增强型）
├── 原因：数据不足以支撑智能出价
└── 目标：积累转化数据

月转化 15-30：
├── 推荐：最大化转化次数
├── 原因：开始积累足够数据
└── 目标：增加转化量

月转化 30-50：
├── 推荐：目标 CPA
├── 原因：数据足够支撑 CPA 优化
└── 目标：控制获客成本

月转化 50+：
├── 推荐：目标 ROAS
├── 原因：数据充足，可以优化价值
└── 目标：最大化广告回报

按系列类型选择：
├── 品牌搜索：手动 CPC（低出价控制成本）
├── 非品牌搜索（高意图）：目标 ROAS / 目标 CPA
├── 非品牌搜索（信息型）：最大化点击次数（设上限）
├── 竞品搜索：目标 CPA（设上限）
└── DSA：最大化转化次数
```

### 5.2 出价调整最佳实践

```
调整频率：
├── 智能出价：每 2 周评估一次，每次调整 ≤ 10%
├── 手动 CPC：每周评估，每次调整 ≤ 15%
└── 新系列：至少 2 周学习期不调整

调整方向判断：
├── ROAS > 目标 120% 且预算未用完 → 降低 tROAS 5-10%（扩量）
├── ROAS > 目标 120% 且预算已用完 → 增加预算 15-20%
├── ROAS 在目标 80-120% → 保持不变
├── ROAS 在目标 50-80% → 提高 tROAS 5-10%（收缩）
└── ROAS < 目标 50% → 检查根因（不要只调出价）

季节性调整：
├── BFCM 前 2 周：降低 tROAS 15-20%（允许更激进获客）
├── BFCM 期间：进一步降低 tROAS 10%（抢占流量）
├── BFCM 后 1 周：恢复正常 tROAS
├── Q1 淡季：提高 tROAS 10-15%（保护利润）
└── 新品上市：前 4 周使用最大化转化次数（积累数据）
```


