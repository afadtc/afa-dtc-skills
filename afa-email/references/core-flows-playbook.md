# 核心流程手册

> 本文件为邮件营销模块的内部参考文件，用于邮件核心流程的编排、冲突排除与执行说明。
> 如需整理为用户可见交付物，必须删除内部路由标签、模块代号和系统字段，只保留自然语言、业务角色与行动建议。
> 节点语法规范见 `work-modes-and-templates.md` 第 3 章 A.1 节。

---

## 1. Welcome Series (欢迎序列)

**目标**: 将新订阅者转化为首次购买者，建立品牌信任，设定沟通期望。

### 1.1 入口条件

```
[TRIGGER] Subscribes to List (新订阅邮件列表)
  └─ 条件过滤：尚未购买过 (Placed Order = 0)
  └─ 排除条件：
      • 已经在 Welcome Series 中的用户不重复进入
      • 通过 Checkout 页面订阅的用户不进入（他们会进入 Post-Purchase Flow）
```

### 1.2 流程拓扑

```
[TRIGGER] Subscribes to List
  │
  ▼
[EMAIL] #1: The Welcome & The Offer
  └─ 延迟：交易确认后尽快发送（通常为事件触发后即时出发）
  └─ 标题变体：
      A (Safe): "Welcome to [Brand]! Here's your [X]% off"
      B (Bold): "You're in! Your [X]% off code is inside"
      C (Personal): "[First Name], welcome to the family"
  └─ 预览文本："Your exclusive discount code + what makes us different"
  └─ 正文框架：
      1. Header：醒目的折扣码 + "Shop Now" 按钮
      2. Hero Image：高质量品牌形象图或畅销产品图
      3. The "Why"：一段话说明品牌为什么存在、解决什么问题
      4. Product Showcase：3-4 款畅销产品（动态推荐块）
      5. Footer：社交媒体链接 + 客服联系方式
  └─ CTA："Shop Now with [X]% Off" → 首页或畅销品集合页（自动应用折扣码）
  │
  ▼
[WAIT] 按欢迎序列节奏设置下一触达窗口（常以约 1 天为起点）
  └─ 发送窗口：以收件人当地时间的品牌适配时段为准，避免深夜或明显打扰窗口
  └─ 智能发送：可按平台能力与品牌策略启用
  │
  ▼
[EMAIL] #2: The Brand Story / Founder's Note
  └─ 标题变体：
      A (Safe): "Why I started [Brand]"
      B (Bold): "The story behind our [Product] (it's personal)"
      C (Personal): "A note from [Founder Name]"
  └─ 预览文本："The real reason this brand exists"
  └─ 正文框架：
      1. Format：纯文本或轻量级设计，看起来像私人邮件
      2. Sender：创始人或 CEO 的名字（非品牌名）
      3. Story：创立初衷 → 遇到的困难 → 对质量的坚持
      4. Soft CTA："Reply to this email — I read every one"
  └─ CTA："Read the full story" → 品牌故事页面
  │
  ▼
[WAIT] 按欢迎序列节奏继续推进下一触达窗口（常以约 1-2 天为参考）
  └─ 发送窗口：以收件人当地时间的品牌适配时段为准，避免深夜或明显打扰窗口
  └─ 智能发送：可按平台能力与品牌策略启用
  │
  ▼
[EMAIL] #3: Social Proof & Education
  └─ 标题变体：
      A (Safe): "See what everyone is talking about"
      B (Bold): "Don't just take our word for it"
      C (Personal): "[First Name], here's why people love us"
  └─ 预览文本："Real reviews from real customers"
  └─ 正文框架：
      1. Testimonials：若干条带客户照片的高质量评价，数量按版面与证据强度决定
      2. UGC：客户在 Instagram/TikTok 上的使用视频截图
      3. Press Mentions：媒体 Logo + 引言（如有）
      4. Reminder：提醒首单折扣码仍未使用
  └─ CTA："Shop Our Bestsellers" → 畅销品集合页
  │
  ▼
[WAIT] 按欢迎序列节奏继续推进下一触达窗口（常以约 1-2 天为参考）
  └─ 发送窗口：以收件人当地时间的品牌适配时段为准，避免深夜或明显打扰窗口
  └─ 智能发送：可按平台能力与品牌策略启用
  │
  ▼
[SPLIT] 已打开前 3 封邮件中的任意一封？
  ├─ YES →
  │   [EMAIL] #4: The Urgency / Last Chance
  │     └─ 标题变体：
  │         A (Safe): "Your [X]% off expires tonight"
  │         B (Bold): "Final hours: your welcome gift is disappearing"
  │         C (Personal): "[First Name], last chance to save"
  │     └─ 预览文本："Your discount code expires in [X] hours"
  │     └─ 正文框架：
  │         1. Urgency：如确有时间边界，可说明折扣码将在当前设定窗口后失效；若无真实失效机制，则不用伪造倒计时
  │         2. Friction Reduction：免运费 + 退换货政策 + 满意度保证
  │         3. Bestseller Block：动态展示 3 款畅销品
  │     └─ CTA："Claim My Discount Now" → 畅销品集合页（自动应用折扣码）
  │
  └─ NO (全部未打开) →
      [SMS] #1: Welcome SMS (仅当品牌启用 SMS 时)
        └─ 正文："Hey [First Name]! Welcome to [Brand] 🎉 Your welcome offer is ready here → [短链]"（长度按平台与品牌写作规范控制）
        └─ 发送窗口：以收件人当地时间的短信适配时段为准，避免打扰窗口
      │
      ▼
      [WAIT] 按该分支节奏安排下一触达窗口（通常接近 1 天）
      │
      ▼
      [EMAIL] #4-ALT: 纯文本版最后机会
        └─ 标题："Quick question, [First Name]"
        └─ 正文：纯文本，创始人语气，"我注意到你还没用你的折扣码，有什么我能帮忙的吗？"
        └─ CTA：回复邮件 或 点击链接购物
```

### 1.3 冲突排除规则

- 进入本 Flow 时，自动抑制：Browse Abandonment Flow
- 本 Flow 被以下 Flow 抑制：Abandoned Cart Flow（如果用户在 Welcome 期间发起了结账又放弃，优先进入 Abandoned Cart）
- 与 Campaign 的协调：Welcome Series 活跃期间，通常抑制常规促销 Campaign；具体抑制时长按序列长度、触达密度与品牌促销节奏决定

### 1.4 SMS 层叠策略

- SMS #1 位置：在 Email #4 的条件分支中，仅当前 3 封邮件全部未打开时触发
- SMS 发送窗口：以收件人当地时间的短信适配时段为准
- SMS 与 Email 的最小间隔：应保留足够缓冲，避免短时间内多通道连续打扰

### 1.5 KPI 目标

| 指标 | 参考判断口径 | 外部参考区间 |
|:---|:---|:---|
| 打开率 | 以品牌自身欢迎序列历史表现、名单质量与标题测试结果综合判断 | 可参考常见欢迎序列区间，但不得替代品牌真实基线 |
| 点击率 | 优先与同账户历史优胜版本、折扣力度与落地页匹配度联动判断 | 可参考外部区间做辅助对照 |
| 首购转化率 | 结合首单优惠、品类决策周期与页面承接质量判断 | 仅作辅助对比，不写统一红线 |
| RPR | 以品牌客单价、折扣策略与欢迎序列定位综合判断 | 仅作外部参考 |

---

## 2. Abandoned Cart (废弃购物车挽回)

**目标**: 挽回高意向但未完成结账的客户。

### 2.1 入口条件

```
[TRIGGER] Started Checkout (开始结账但未完成购买)
  └─ 条件过滤：触发后未完成购买
  └─ 排除条件：
      • 正在经历 Welcome Series 的用户不进入（避免新客同时收到两条流）
      • 最近刚完成购买、已明显脱离挽回场景的用户不进入
      • 已被标记为 Chronic Returner 的用户不进入
```

### 2.2 流程拓扑

```
[TRIGGER] Started Checkout (未完成购买)
  │
  ▼
[WAIT] 以较短时效窗口启动首轮挽回（常从数小时内开始测试）
  └─ 发送窗口：优先兼顾挽回时效与收件人当地时间体验，不默认无差别全天候触达
  │
  ▼
[SPLIT] 购物车价值是否达到品牌定义的高价值分层门槛？
  │
  ├─ YES → 高价值路径 (High-Value Path)
  │   │
  │   ▼
  │   [EMAIL] #1A: 高价值购物车提醒
  │     └─ 标题变体：
  │         A (Safe): "You left something behind"
  │         B (Bold): "Your [Product Name] is selling fast"
  │         C (Personal): "[First Name], still thinking it over?"
  │     └─ 预览文本："We saved your items — complete your order before they're gone"
  │     └─ 正文框架：客服语气 + 动态购物车商品块 + 免运费提醒 + 退换保障
  │     └─ CTA："Complete My Order" → 结账页面（自动填充购物车）
  │     └─ 动态内容块：是 — 展示购物车中实际商品的图片、名称和价格
  │   │
  │   ▼
  │   [WAIT] 按高价值挽回节奏安排下一触达窗口（常在首封后约 1 天内复查）
      └─ 发送窗口：以收件人当地时间的品牌适配时段为准
0
  │   │
  │   ▼
  │   [SPLIT] 已打开 Email #1A?
  │     ├─ YES 但未点击 →
  │     │   [EMAIL] #2A: 社会认同强化
  │     │     └─ 标题："People are loving your picks"
  │     │     └─ 正文框架：购物车商品的客户评价 + 库存紧张暗示
  │     │     └─ CTA："Return to My Cart"
  │     │
  │     └─ NO (未打开) →
  │         [SMS] [SMS] #1: 购物车提醒短信
          └─ 正文："Hey [First Name]! You left items in your cart at [Brand]. Pick up where you left off → [短链]"（长度按平台与品牌写作规范控制）
          └─ 发送窗口：以收件人当地时间的短信适配时段为准
0
  │   │
  │   ▼
  │   [WAIT] 按标准路径第二轮复查节奏推进下一触达窗口
        └─ 发送窗口：以收件人当地时间的品牌适配时段为准
  │   │
  │   ▼
  │   [EMAIL] [EMAIL] #3A: 补偿型挽回激励
    └─ 标题："Here’s an extra reason to complete your order"
    └─ 正文框架：如需提供激励，则使用经利润与品牌策略校准的补偿方案 + 购物车商品 + 真实时效说明
    └─ CTA："Complete My Order" → 结账页面（如有激励则按实际规则自动应用）
扣码）
  │
  └─ NO → 标准路径 (Standard Path)
      │
      ▼
      [EMAIL] #1B: 标准购物车提醒
        └─ 标题变体：
            A (Safe): "We saved your cart"
            B (Bold): "Still thinking about the [Product Category]?"
            C (Personal): "[First Name], your cart misses you"
        └─ 预览文本："Your items are waiting — tap to pick up where you left off"
        └─ 正文框架：友好提醒 + 动态购物车商品块 + 客服支持链接
        └─ CTA："Return to Checkout"
        └─ 动态内容块：是 — 展示购物车中实际商品
      │
      ▼
      [WAIT] 按标准路径节奏安排下一触达窗口（通常接近 1 天）
        └─ 发送窗口：以收件人当地时间的品牌适配时段为准
      │
      ▼
      [EMAIL] #2B: 社会认同 + 紧迫感
        └─ 标题："These are selling out fast"
        └─ 正文框架：社会认同 + 库存紧迫感
        └─ CTA："Complete My Order"
      │
      ▼
[WAIT] 按高价值路径的第二轮复查节奏推进下一触达窗口
      └─ 发送窗口：以收件人当地时间的品牌适配时段为准

      │
      ▼
      [EMAIL] #3B: 免运费激励
        └─ 标题："An extra shipping incentive is available on your cart"
        └─ 正文框架：如需使用免运费激励，则按利润结构与真实有效期说明，不默认统一写成“仅限今天”
        └─ CTA："Get Free Shipping"
```

### 2.3 冲突排除规则

- 进入本 Flow 时，自动抑制：Browse Abandonment Flow, Win-Back Flow
- 本 Flow 不被任何其他 Flow 抑制（最高优先级）
- 与 Campaign 的协调：本 Flow 活跃期间，抑制常规促销 Campaign（但不抑制交易类邮件）

### 2.4 SMS 层叠策略

- SMS #1 位置：在 Email #2A 的条件分支中，仅当 Email #1A 未被打开时触发
- SMS 发送窗口：以收件人当地时间的短信适配时段为准
- SMS 与 Email 的最小间隔：应保留足够缓冲，避免短时间内多通道连续打扰
- BFCM 期间调整：可在首封邮件后适度提前短信提醒，但仍需结合拥挤度、时区与疲劳风险决定

### 2.5 KPI 目标

| 指标 | 参考判断口径 | 外部参考区间 |
|:---|:---|:---|
| 打开率 | 以品牌自身挽回流历史表现、名单温度与发送时机综合判断 | 可参考常见挽回流区间做辅助对照 |
| 点击率 | 结合购物车价值、提醒强度与落地页承接质量判断 | 外部区间仅作辅助参考 |
| RPR | 以购物车金额结构、激励策略与利润空间综合判断 | 不写统一营收红线 |
| 转化率 | 优先与同账户历史版本和商品意图强度对比 | 外部区间仅作参考 |
| 挽回率 | 按品牌品类、购物车门槛与促销环境综合判断 | 仅作外部辅助对标 |

---

## 3. Browse Abandonment (浏览放弃)

**目标**: 重新吸引浏览了特定产品页面但未加入购物车的客户。

### 3.1 入口条件

```
[TRIGGER] Viewed Product (浏览了产品页面)
  └─ 条件过滤：
      • 未加入购物车 (Added to Cart = 0)
      • 未开始结账 (Started Checkout = 0)
      • 未购买 (Placed Order = 0)
      • 在较短观察窗口内浏览了多个高相关产品页面（用于过滤随意浏览）
  └─ 排除条件：
      • 正在经历 Abandoned Cart Flow 的用户不进入
      • 正在经历 Welcome Series 的用户不进入
      • 最近已收到 Browse Abandonment 邮件的用户不重复进入
```

### 3.2 流程拓扑

```
[TRIGGER] Viewed Product (满足过滤条件)
  │
  ▼
[WAIT] 以较短观察窗口后触发首轮浏览挽回（常从数小时内开始测试）
  └─ 发送窗口：以收件人当地时间的品牌适配时段为准
  └─ 智能发送：可按平台能力与品牌策略启用
  │
  ▼
[EMAIL] #1: The Soft Nudge
  └─ 标题变体：
      A (Safe): "Still thinking about the [Product Name]?"
      B (Bold): "We saw you looking... good taste!"
      C (Personal): "[First Name], here's more about the [Product Name]"
  └─ 预览文本："Here's why people love it"
  └─ 正文框架：
      1. Dynamic Block：展示他们浏览过的产品（图片 + 名称 + 价格）
      2. Education：突出该产品的 3 个核心卖点或成分
      3. Social Proof：若干条与当前产品高度相关的客户评价，数量按版面与证据质量决定
  └─ CTA："Take another look" → 产品页面
  └─ 动态内容块：是 — 基于浏览历史自动填充产品
  │
  ▼
[WAIT] 按浏览挽回节奏安排下一触达窗口（通常接近 1 天）
  └─ 发送窗口：以收件人当地时间的品牌适配时段为准
  │
  ▼
[SPLIT] 已打开 Email #1?
  ├─ YES 但未点击 →
  │   [EMAIL] #2: Alternative Recommendations
  │     └─ 标题："Not quite right? Check these out"
  │     └─ 正文框架：
  │         1. Dynamic Block：浏览过的产品
  │         2. Cross-sell Block：同类目下其他畅销产品（动态推荐）
  │     └─ CTA："Explore More" → 集合页面
  │
  └─ NO (未打开) →
      [EXIT] 不再发送（避免对低意向用户过度触达）
```

### 3.3 冲突排除规则

- 进入本 Flow 时，不抑制其他 Flow
- 本 Flow 被以下 Flow 抑制：Abandoned Cart Flow, Welcome Series
- 与 Campaign 的协调：本 Flow 不抑制 Campaign

### 3.4 KPI 目标

| 指标 | 参考判断口径 | 外部参考区间 |
|:---|:---|:---|
| 打开率 | 结合浏览意图强度、产品热度与主题行匹配度判断 | 外部区间仅作辅助对照 |
| 点击率 | 优先与同账户浏览挽回历史版本对比 | 可参考常见区间做辅助判断 |
| RPR | 以产品价格带、流量温度与推荐准确度综合判断 | 不写统一营收红线 |
| 转化率 | 结合产品决策难度、页面承接与流量温度判断 | 外部区间仅作参考 |

---

## 4. Post-Purchase (购后序列)

**目标**: 减少买家懊悔，提升开箱体验，获取评价，驱动复购。

### 4.1 入口条件

```
[TRIGGER] Placed Order (完成订单)
  └─ 条件过滤：无（所有购买者都进入）
  └─ 排除条件：
      • 正在经历 Win-Back Flow 的用户：退出 Win-Back，进入 Post-Purchase
```

### 4.2 流程拓扑

```
[TRIGGER] Placed Order
  │
  ▼
[EMAIL] #1: Order Confirmation & Excitement
  └─ 延迟：交易确认后尽快发送（通常为事件触发后即时出发）
  └─ 标题："Order confirmed! 🎉 Here's what's next"
  └─ 正文框架：
      1. 订单详情（动态块：商品、数量、价格）
      2. 预计发货时间
      3. "我们正在为您打包"的品牌化文案
      4. 品牌社交媒体关注引导
  └─ CTA："Track My Order" → 订单状态页面
  │
  ▼
[SPLIT] 是否为首次购买客户？
  ├─ YES →
  │   [WAIT] 按首次购后欢迎节奏安排下一触达窗口（通常接近 1 天）
  │   │
  │   ▼
  │   [EMAIL] #2-NEW: Welcome to the Family
  │     └─ 标题："Welcome to the [Brand] family, [First Name]!"
  │     └─ 正文框架：
  │         1. 感谢首次购买
  │         2. 品牌社区介绍（Instagram、Facebook Group）
  │         3. 使用指南预告
  │     └─ CTA："Join Our Community" → 社交媒体或社区页面
  │
  └─ NO (复购客户) →
      [WAIT] 按该分支节奏安排下一触达窗口（通常接近 1 天）
      │
      ▼
      [EMAIL] #2-REPEAT: Thank You + Loyalty Nudge
        └─ 标题："Thanks for coming back, [First Name]!"
        └─ 正文框架：
            1. 感谢复购
            2. 忠诚度计划进度（如有）
            3. 推荐朋友奖励提醒
        └─ CTA："Refer a Friend" → 推荐计划页面
  │
  ▼
[WAIT] 对齐发货节点与预计送达前的准备窗口，在商品到达前做适度预热
  └─ 发送窗口：收件人当地时间 09:00-21:00
  │
  ▼
[EMAIL] #3: How to Use / Preparation
  └─ 标题变体：
      A: "Your [Product] arrives tomorrow — here's how to get the most out of it"
      B: "Pro tips for your new [Product]"
  └─ 正文框架：
      1. 使用指南（步骤式）
      2. 视频教程链接（如有）
      3. 常见问题解答 (FAQ)
  └─ CTA："Watch the Tutorial" → 教程页面
  │
  ▼
[WAIT] 自预计送达日起保留一段体验消化窗口后，再发起首次评价触达
  └─ 发送窗口：收件人当地时间 09:00-21:00
  │
  ▼
[SMS] #1: Review Request SMS (仅当品牌启用 SMS 时)
  └─ 正文："Hey [First Name]! How are you liking your [Product]? Share your feedback here → [短链]"（长度按平台与品牌写作规范控制）
  └─ 发送窗口：以收件人当地时间的短信适配时段为准
  │
  ▼
[WAIT] 给予用户适度缓冲后再推进下一评价或复购相关触达
  └─ 发送窗口：收件人当地时间 09:00-21:00
  │
  ▼
[SPLIT] 已提交评价？
  ├─ YES →
  │   [EMAIL] #4-THANKYOU: 感谢评价 + 折扣奖励
  │     └─ 标题："Thanks for your review! Here's a little thank you"
  │     └─ 正文框架：感谢 + 下次购物折扣码
  │     └─ CTA："Shop with [X]% Off"
  │
  └─ NO →
      [EMAIL] #4-REVIEW: The Review Request
        └─ 标题变体：
            A: "What do you think of your [Product]?"
            B: "We'd love your honest feedback"
        └─ 正文框架：
            1. 简单的星级评分链接
            2. 提交图文评价可获得下次购物折扣
        └─ CTA："Leave a Review" → 评价页面
  │
  ▼
[WAIT] 按品类补货周期与真实消耗节奏，在更合适的购后阶段触发补货或搭配推荐
  └─ 发送窗口：收件人当地时间 09:00-21:00
  │
  ▼
[SPLIT] 产品类型？
  ├─ 消耗品 →
  │   [EMAIL] #5: Replenishment Reminder
  │     └─ 标题："Running low on [Product]?"
  │     └─ 正文框架：补货提醒 + 订阅省钱方案（如有）
  │     └─ CTA："Reorder Now" → 产品页面
  │
  └─ 非消耗品 →
      [EMAIL] #5: Cross-Sell Recommendation
        └─ 标题："Pairs perfectly with your [Product]"
        └─ 正文框架：搭配推荐 + 动态推荐块
        └─ CTA："Complete Your Set" → 推荐产品集合页
```

### 4.3 冲突排除规则

- 进入本 Flow 时，自动抑制：Win-Back Flow（用户已回归，无需召回）
- 本 Flow 被以下 Flow 抑制：无（购后体验是最高优先级之一）
- 与 Campaign 的协调：Post-Purchase 前 3 封邮件期间（Day 0-3），抑制常规促销 Campaign

### 4.4 SMS 层叠策略

- SMS #1 位置：在 Email #4 之前，作为轻量级评价请求
- SMS 发送窗口：收件人当地时间 09:00-20:00
- SMS 与 Email 的最小间隔：应保留足够缓冲，避免在购后与召回阶段形成多通道连续打扰

### 4.5 KPI 目标

| 指标 | 参考判断口径 | 外部参考区间 |
|:---|:---|:---|
| 打开率 | 以购后序列的交易属性、物流节点相关性与历史送达质量综合判断 | 可参考常见购后序列区间做辅助对照 |
| 评价提交率 | 结合产品满意度、评价入口摩擦与触达时机判断 | 外部区间仅作辅助参考 |
| 复购转化率 | 按品类补货周期、推荐准确度与客户生命周期阶段综合判断 | 不写统一复购红线 |
| RPR | 结合客单价、推荐策略与购后序列角色综合判断 | 仅作外部参考 |

---

## 5. Win-Back (客户召回)

**目标**: 重新激活超过正常购买周期未复购的沉睡客户。

### 5.1 入口条件

```
[TRIGGER] 距离上次购买超过 [X] 天
  └─ X 的确定规则：
      • 消耗品（护肤、食品、补剂）：按实际使用/消耗节奏设定参考召回窗口
      • 时尚/服饰：按典型复购季节、上新节奏与购买决策周期设定参考召回窗口
      • 耐用品/家居：按更长决策周期与使用寿命设定参考召回窗口
      • 如果品牌有自己的数据，应基于自有复购分布与品类节奏设置放大系数，而不是默认套用单一倍数
  └─ 条件过滤：
      • 历史购买次数 ≥ 1
      • 最近仍有邮件互动（打开或点击）— 以确保不是已完全沉默的名单
  └─ 排除条件：
      • 正在经历 Post-Purchase Flow 的用户不进入
      • 已在 Sunset Flow 中的用户不进入
```

### 5.2 流程拓扑

```
[TRIGGER] 距离上次购买超过 [X] 天
  │
  ▼
[EMAIL] #1: The "We Miss You"
  └─ 延迟：进入召回条件后尽快启动首封触达
  └─ 标题变体：
      A (Safe): "It's been a while, [First Name]"
      B (Bold): "We miss you (and we have news)"
      C (Personal): "[First Name], a lot has changed since your last visit"
  └─ 预览文本："Here's what's new since you've been away"
  └─ 正文框架：
      1. 情感唤醒："我们注意到你已经有一段时间没来了"
      2. 新品/改进展示：自上次购买以来品牌推出的新产品或改进
      3. 无折扣或仅小额折扣（测试是否只是忘记购买）
  └─ CTA："See What's New" → 新品页面
  │
  ▼
[WAIT] 在首轮召回后保留一段适中缓冲，再推进下一轮跟进
  └─ 发送窗口：收件人当地时间 09:00-21:00
  └─ 智能发送：是
  │
  ▼
[SPLIT] 已打开 Email #1 或点击？
  ├─ YES (有互动但未购买) →
  │   [EMAIL] #2A: The Strong Incentive (个性化版)
  │     └─ 标题："A special gift to welcome you back, [First Name]"
  │     └─ 正文框架：
  │         1. 如需激励，使用按毛利空间与客户价值校准的补偿方案（不默认统一写成固定折扣或固定金额减免）
  │         2. 基于历史购买的个性化推荐（动态块）
  │         3. 如使用有效期，应写明真实且经策略校准的时效，不默认统一设置为固定小时数
  │     └─ CTA："See My Offer" → 首页（如有激励则按实际规则自动应用）
  │
  └─ NO (未互动) →
      [SMS] #1: Win-Back SMS (仅当品牌启用 SMS 时)
        └─ 正文："Hey [First Name], we miss you at [Brand]! Your return offer is here → [短链]"（长度按平台与品牌写作规范控制）
        └─ 发送窗口：以收件人当地时间的短信适配时段为准
      │
      ▼
      [WAIT] 结合召回节奏与互动信号安排下一轮跟进窗口
      │
      ▼
      [EMAIL] #2B: The Strong Incentive (标准版)
        └─ 标题："$15 on us — welcome back"
        └─ 正文框架：高额折扣 + 畅销品展示 + 限时有效
        └─ CTA："Shop with $15 Off"
  │
  ▼
[WAIT] 给予用户适度缓冲后再推进下一评价或复购相关触达
  └─ 发送窗口：收件人当地时间 09:00-21:00
  │
  ▼
[SPLIT] 已购买？
  ├─ YES → [EXIT] 进入 Post-Purchase Flow
  │
  └─ NO →
      [EMAIL] #3: The Breakup / Sunset Warning
        └─ 标题变体：
            A: "Is this goodbye, [First Name]?"
            B: "Should we stop emailing you?"
        └─ 正文框架：
            1. "如果您不再对我们的邮件感兴趣，我们理解"
            2. 一键退订链接（显眼位置）
            3. "如果您还想留下，这里是您最后使用 [X]% 折扣的机会"
            4. 如使用折扣码，应写明真实且经利润策略校准的有效期
        └─ CTA："Keep Me Subscribed + Shop" → 首页（自动应用折扣码）
      │
      ▼
      [WAIT] 在进入 Sunset 前保留一段更长的最终观察窗口
      │
      ▼
      [SPLIT] 在最终观察窗口内是否出现任何互动（打开/点击/购买）？
        ├─ YES → [EXIT] 保留在活跃列表
        └─ NO → [ACTION] 自动移至 Sunset 分段，降低发送频率，保护发件人声誉
```

### 5.3 冲突排除规则

- 进入本 Flow 时，不抑制其他 Flow
- 本 Flow 被以下 Flow 抑制：Abandoned Cart Flow, Post-Purchase Flow
- 与 Campaign 的协调：Win-Back 活跃期间，仅发送 Win-Back 邮件，抑制常规 Campaign

### 5.4 SMS 层叠策略

- SMS #1 位置：在 Email #1 未被打开时触发，作为渠道切换尝试
- SMS 发送窗口：收件人当地时间 09:00-20:00
- SMS 与 Email 的最小间隔：应保留足够缓冲，避免在购后与召回阶段形成多通道连续打扰

### 5.5 KPI 目标

| 指标 | 参考判断口径 | 外部参考区间 |
|:---|:---|:---|
| 打开率 | 以沉睡用户温度、主题行相关性与品牌记忆度综合判断 | 可参考常见召回流区间做辅助对照 |
| 点击率 | 结合激励强度、推荐准确度与回流门槛判断 | 外部区间仅作参考 |
| 召回转化率 | 按品类复购周期、客户价值与召回路径强度综合判断 | 不写统一召回红线 |
| RPR | 结合激励成本、客单价与回流用户质量综合判断 | 仅作外部参考 |
| 列表清洁率 | 按沉睡名单结构与 Sunset 策略综合判断 | 外部区间仅作辅助参考 |

---

## 6. Flow 优先级瀑布 (Flow Priority Waterfall)

当用户同时满足多个 Flow 的触发条件时，按以下优先级排序，高优先级 Flow 自动抑制低优先级 Flow：

```
优先级 1 (最高)：Abandoned Cart
优先级 2：Post-Purchase
优先级 3：Welcome Series
优先级 4：Browse Abandonment
优先级 5：Win-Back
优先级 6 (最低)：Sunset
```

**规则**：用户在任意时刻只能处于一个 Flow 中。当高优先级 Flow 被触发时，低优先级 Flow 自动暂停。高优先级 Flow 完成后，如果低优先级 Flow 仍然有效，用户从暂停点继续。

---

## 7. 全局 SMS 治理规则

以下规则适用于所有 Flow 中的 SMS 触点：

| 规则 | 说明 |
|:---|:---|
| 每日上限 | 每个用户每天最多收到 1 条 SMS |
| 每周上限 | 每个用户每周最多收到 2 条 Flow 触发的 SMS（促销类 SMS 每月不超过 4-6 条，按客群分层；交易类/服务类 SMS 不受此限） |
| 静默时段 | 避开收件人当地时间的明显打扰窗口，具体静默边界以品牌合规政策、地区规则与人群体验标准决定 |
| 合规要求 | 所有 SMS 需包含适用地区要求的退订指令与必要披露信息 |
| 与 Email 协调 | SMS 与 Email 之间应保留足够缓冲；旺季可适度压缩，但仍需结合时区、拥挤度与疲劳风险判断 |
| 成本控制 | SMS 仅在 Email 未被打开时作为备选渠道触发（避免双重触达） |
