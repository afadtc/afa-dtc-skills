# Win-Back 流程手册

> 本文件为留存增长模块的内部参考文件，用于定义 Win-Back 流程、触发条件与执行策略。
> 如需整理为用户可见交付物，必须删除内部路由标签、模块代号和系统字段，只保留自然语言、业务角色与行动建议。

---

## 1. 召回策略核心原则 (Win-Back Core Principles)

1. **时机胜于折扣 (Timing > Discount)**: 在客户真正需要补货或准备流失的边缘触达，比盲目给大折扣更有效。
2. **分层召回 (Segmented Win-Back)**: 不要对所有流失客户一视同仁。高价值客户值得更高的召回成本（如直邮、高额折扣），低价值客户应使用低成本渠道（如邮件）。
3. **渐进式优惠 (Escalating Offers)**: 召回序列中的折扣应逐步增加，而不是一开始就给出底牌。
4. **频率优先级与渠道抑制 (Frequency First)**: 同一召回阶段只允许一个主渠道先行触达；若用户在近窗口期已收到其他营销消息，应延后、降频或跳过当前触达，避免跨渠道叠加轰炸。
5. **情感共鸣 (Emotional Connection)**: 承认客户的离开，表达想念，展示品牌的改变和进步。
6. **降低门槛 (Low Friction)**: 召回邮件中的链接应直接带参数，自动应用折扣，甚至直接跳转到预填充的结账页面。
7. **可退出与可静默 (Exit & Silence Windows)**: 用户明确无兴趣、持续不打开或已投诉后，必须立即退出召回序列，并进入静默窗口。

---

## 2. 核心召回工作流 (Core Win-Back Workflows)

### 2.1 标准流失召回序列 (Standard Win-Back Flow)

**触发条件**: 客户超过预期购买周期 [X] 天未购买（通常为 60-90 天，取决于品类）。
**目标群体**: 曾经购买过 1-2 次，但未达到高价值标准的客户。

| 触点 | 时间点 | 渠道 | 主题/核心信息 | 优惠策略 | 目的 |
|------|--------|------|---------------|----------|------|
| 1 | Day 0 | Email | "We've missed you / It's been a while" | 无折扣或小额折扣 (如免邮) | 情感唤醒，测试是否只是忘记购买 |
| 2 | Day 7 | Email | "Come back and see what's new" | 10% Off | 展示新品或畅销品，提供轻度激励 |
| 3 | Day 14 | Email | "A special gift just for you" | 15% Off | 增加紧迫感，明确的限时优惠 |
| 4 | Day 21 | SMS（仅当最近窗口期无其他营销触达且已具备该渠道许可） | "Hey [Name], your 15% off expires tonight!" | 15% Off (Last Chance) | 作为补充提醒，而非与 Email 并行轰炸 |
| 5 | Day 30 | Email | "Did we do something wrong? / Tell us why" | 调查问卷 (填完送 20% Off) | 收集流失原因，最后一次尝试 |
| 6 | Day 31+ | Silence / Exit | 无进一步营销触达，转入静默观察或退出名单 | 无 | 防止过度触达，保护发件人信誉 |

### 2.2 高价值客户专属召回 (VIP Win-Back Flow)

**触发条件**: RFM 模型中的 "At Risk" 或 "Can't Lose Them" 客户（高频/高客单价，但近期未购买）。
**目标群体**: 历史 LTV 排名前 20% 的客户。

| 触点 | 时间点 | 渠道 | 主题/核心信息 | 优惠策略 | 目的 |
|------|--------|------|---------------|----------|------|
| 1 | Day 0 | Email | 创始人/CEO 个人名义的纯文本邮件 | 专属高额折扣 (如 20% Off 或 高价值赠品) | 彰显重视，建立一对一的沟通感 |
| 2 | Day 3 | SMS | 专属客服/VIP 经理的问候 | 同上 | 提供专属服务通道 |
| 3 | Day 10 | Direct Mail | 精美的实体明信片或信件 | 专属折扣码 (如 VIPBACK25) | 突破数字渠道的噪音，提供物理触感 |
| 4 | Day 20 | Retargeting | 社交媒体定向广告 | 强调品牌价值和社区 | 保持品牌在视线内，不显得过于推销 |

### 2.3 订阅流失挽回序列 (Subscription Win-Back Flow)

**触发条件**: 客户主动取消订阅后 [X] 天（通常为 30-60 天）。
**目标群体**: 曾经是订阅用户，现已取消。

| 触点 | 时间点 | 渠道 | 主题/核心信息 | 优惠策略 | 目的 |
|------|--------|------|---------------|----------|------|
| 1 | Day 30 | Email | "Running low on [Product]?" | 重新订阅首单 20% Off | 踩准产品可能用完的时间点 |
| 2 | Day 45 | Email | "We've made some improvements" | 强调产品升级或订阅体验优化 | 解决当初导致取消的痛点 |
| 3 | Day 60 | SMS | "Exclusive offer to reactivate your subscription" | 重新订阅送正装赠品 | 提供难以拒绝的价值 |

---

## 3. 召回邮件文案框架 (Copywriting Frameworks)

### 3.1 "The Check-In" (情感问候型)
- **Subject**: It's been a while, [Name] / We miss you!
- **Body**: 简单真诚地表达想念。不要显得绝望或过于推销。
- **Call to Action**: "Come say hi" 或 "See what's new"

### 3.2 "The Update" (品牌更新型)
- **Subject**: Look how much we've grown / You won't believe what's new
- **Body**: 强调自客户上次购买以来，品牌推出的新产品、改进的配方、更好的包装或更快的物流。
- **Call to Action**: "Explore the new collection"

### 3.3 "The Incentive" (直接利益型)
- **Subject**: $15 on us / A welcome back gift for you
- **Body**: 开门见山地提供优惠。明确说明如何使用以及何时过期。
- **Call to Action**: "Claim your $15" 或 "Shop with 20% off"

### 3.4 "The Survey" (收集反馈型)
- **Subject**: How can we do better? / We value your opinion
- **Body**: 承认客户已经有一段时间没来了，诚恳地请求反馈。提供完成问卷的奖励。
- **Call to Action**: "Take our 1-minute survey"

---

## 4. 召回活动的经济学评估 (Win-Back Economics)

在执行高成本的召回活动（如发送 30% Off 折扣或直邮）之前，必须计算召回经济学：

**核心公式：**
`召回价值 = (召回率 × 召回后预期 LTV) - 召回成本`

**评估步骤：**
1. **预估召回率**: 基于历史数据或行业基准（通常在 2% - 5% 之间）。
2. **计算召回成本**: 包括折扣成本、渠道成本（短信/直邮费用）、广告花费。
3. **预估召回后 LTV**: 被召回的客户通常比全新客户的 LTV 低，建议按原 LTV 的 50%-70% 估算。
4. **计算 ROI**: 确保召回活动的 ROI 为正，且优于获取新客的 ROI。

*经验法则：如果召回一个流失客户的成本高于获取一个新客的 CAC，那么应该放弃召回，将预算投入到拉新中。*

---

## 5. 常见召回误区 (Anti-Patterns to Avoid)

1. **过早触发 (Triggering Too Early)**: 客户的正常购买周期是 60 天，但在第 45 天就发送了 "We miss you" 邮件并附带折扣。这不仅浪费了利润，还训练了客户等待折扣。
2. **无差别轰炸 (Batch and Blast)**: 向所有 1 年未购买的客户发送相同的 50% Off 邮件，或在短时间内叠加 Email、SMS、广告并行追打。这会严重损害品牌资产，并吸引大量只看重折扣的低质量客户。
3. **忽视流失原因 (Ignoring the "Why")**: 如果客户是因为产品质量差或过敏而流失，再大的折扣也无法召回。必须结合客服工单和退货数据进行过滤。
4. **复杂的兑换流程 (High Friction Redemption)**: 邮件里给了折扣码，但客户点击后需要手动复制粘贴，或者发现折扣码不适用于他们想买的商品。
5. **没有退出机制 (No Exit Strategy)**: 客户已经明确表示不再需要（或连续多次未打开/未点击），仍然持续发送召回邮件，最终导致被标记为垃圾邮件，损害发件人信誉。
6. **忽视渠道抑制 (No Channel Suppression)**: 在刚发完邮件后又立即发送短信或广告追投，没有静默窗口、抑制规则和优先级，容易造成用户反感与渠道互相打架。
