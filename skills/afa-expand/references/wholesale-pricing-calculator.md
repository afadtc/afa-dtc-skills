# 批发定价模型与 MAP 政策工具包

> 本文件为 afa-expand 的深度参考文件，提供批发定价计算、阶梯定价设计、MAP 政策模板和批发条款文档模板。

---

## 一、批发定价计算器

### 1.1 基础定价模型

```
输入变量：
├── MSRP（建议零售价 / DTC 价格）：${msrp}
├── COGS（产品成本）：${cogs}
├── DTC 履约成本（每单）：${dtc_fulfillment}
├── 批发履约成本（每单，通常更低）：${wholesale_fulfillment}
└── 品牌最低毛利率要求：{min_margin}%

计算公式：
├── 标准批发价 = MSRP × 0.50（Keystone 定价）
├── 批发毛利 = 批发价 - COGS - 批发履约成本
├── 批发毛利率 = 批发毛利 / 批发价 × 100%
├── DTC 毛利 = MSRP - COGS - DTC 履约成本
└── DTC 毛利率 = DTC 毛利 / MSRP × 100%

可行性判断：
├── 批发毛利率 ≥ 50% → 绿灯（强烈推荐启动批发）
├── 批发毛利率 40-50% → 黄灯（可行但需谨慎管理成本）
├── 批发毛利率 30-40% → 橙灯（仅在有战略价值时启动）
└── 批发毛利率 < 30% → 红灯（不建议启动批发）
```

### 1.2 计算示例

```
示例 1：护肤品品牌
├── MSRP：$68
├── COGS：$9.50
├── DTC 履约成本：$5.00
├── 批发履约成本：$2.00（大批量发货，单件成本更低）
├── 标准批发价：$68 × 0.50 = $34
├── 批发毛利：$34 - $9.50 - $2.00 = $22.50
├── 批发毛利率：$22.50 / $34 = 66.2% ✅ 绿灯
├── DTC 毛利：$68 - $9.50 - $5.00 = $53.50
└── DTC 毛利率：$53.50 / $68 = 78.7%

示例 2：家居用品品牌
├── MSRP：$45
├── COGS：$14.00
├── DTC 履约成本：$6.00
├── 批发履约成本：$3.00
├── 标准批发价：$45 × 0.50 = $22.50
├── 批发毛利：$22.50 - $14.00 - $3.00 = $5.50
├── 批发毛利率：$5.50 / $22.50 = 24.4% ❌ 红灯
├── 解决方案：
│   ├── 选项 A：降低 COGS（优化供应链 → 参考 afa-ops）
│   ├── 选项 B：提高 MSRP（如果品牌定位支持）
│   ├── 选项 C：设定更高的批发价（55% off 而非 50% off）
│   └── 选项 D：暂不启动批发
└── 如果 COGS 降至 $10：批发毛利率 = ($22.50-$10-$3)/$22.50 = 42.2% ✅ 黄灯
```

### 1.3 阶梯定价设计

```
阶梯定价模板：

| 订单量 | 折扣 | 批发价（基于 $68 MSRP） | 适用场景 |
|--------|------|----------------------|---------|
| 12-47 件 | 50% off MSRP | $34.00 | 小型精品店首单 |
| 48-95 件 | 52% off MSRP | $32.64 | 中型零售商 |
| 96-239 件 | 55% off MSRP | $30.60 | 大型零售商/连锁 |
| 240+ 件 | 57% off MSRP | $29.24 | 战略合作伙伴 |

设计原则：
├── 最低阶梯的折扣不低于 50%（行业标准）
├── 最高阶梯的折扣不超过 60%（保护利润）
├── 每个阶梯之间的差距 = 2-3 个百分点
├── 阶梯门槛设置要合理（不要让小零售商觉得门槛太高）
└── 确保最高折扣下的毛利率仍 > 40%
```

---

## 二、特殊定价策略

### 2.1 首单优惠

```
首单优惠模板：
├── 优惠方式：首单额外 10% off（在标准批发价基础上）
├── 适用条件：仅限新零售商首次订单
├── 最低订单量：$150 或 12 件（取较高者）
├── 有效期：开户后 30 天内
└── 目的：降低零售商试错门槛，加速首单转化

示例：
├── 标准批发价：$34.00
├── 首单优惠价：$34.00 × 0.90 = $30.60
├── 首单毛利率：($30.60 - $9.50 - $2.00) / $30.60 = 62.4%
└── 判断：仍然高于 50% 毛利率门槛 ✅
```

### 2.2 季节性预购折扣

```
预购折扣模板：
├── 优惠方式：提前 3 个月预购享额外 5% off
├── 适用条件：
│   ├── Q4 节日季产品：7-8 月预购
│   ├── 春季新品：11-12 月预购
│   └── 夏季产品：2-3 月预购
├── 付款条件：预购订单 50% 预付，发货前付清余款
├── 好处（品牌）：提前锁定订单 + 优化库存规划 + 改善现金流
└── 好处（零售商）：更低的进货成本 + 确保有货
```

### 2.3 渠道专属 SKU 定价

```
渠道专属 SKU 策略：
├── 目的：避免渠道间直接价格比较
├── 方法：
│   ├── 不同渠道提供不同规格（如 DTC 50ml / 批发 30ml）
│   ├── 不同渠道提供不同配色/款式
│   ├── 批发渠道提供独家套装/礼盒
│   └── 不同渠道使用不同 SKU 编号
├── 定价：渠道专属 SKU 可以有独立的定价体系
└── 注意：核心产品仍需保持跨渠道价格一致（MAP 政策保护）
```

---

## 三、MAP 政策完整模板

### 3.1 MAP 政策文档模板

```markdown
# {Brand Name} Minimum Advertised Price (MAP) Policy

Effective Date: {date}

## 1. Purpose
{Brand Name} has established this Minimum Advertised Price ("MAP") Policy to 
maintain the value and integrity of our brand and products, and to ensure a 
fair and competitive marketplace for all authorized retailers.

## 2. Scope
This Policy applies to all authorized retailers and distributors of 
{Brand Name} products in the United States.

## 3. MAP Prices
The MAP for each {Brand Name} product is equal to the Manufacturer's 
Suggested Retail Price (MSRP) as listed in the current {Brand Name} 
wholesale price list, unless otherwise specified.

## 4. Covered Advertising
This Policy applies to all forms of advertising, including but not limited to:
- Website product pages and shopping carts
- Email marketing and newsletters
- Social media posts and advertisements
- Google Shopping and other comparison shopping engines
- Print advertisements
- Television and radio advertisements

## 5. Exclusions
The following are NOT covered by this Policy:
- In-store pricing (physical retail locations)
- Prices communicated verbally to individual customers
- Prices shown only after adding to cart (if not visible in search results)

## 6. Compliance
{Brand Name} will monitor advertised prices across all channels. 
Retailers found in violation of this Policy may face the following 
consequences:

- First Violation: Written warning with 48-hour correction deadline
- Second Violation: 30-day suspension of product supply
- Third Violation: Permanent termination of authorized retailer status

## 7. Unilateral Policy
This is a unilateral policy of {Brand Name} and is not an agreement 
between {Brand Name} and any retailer. {Brand Name} reserves the right 
to modify or discontinue this Policy at any time.

## 8. Contact
For questions regarding this Policy, contact:
{Brand Name} Wholesale Team
Email: wholesale@{brand}.com
```

---

## 四、批发条款文档模板

### 4.1 Wholesale Terms & Conditions

```markdown
# {Brand Name} Wholesale Terms & Conditions

## 1. Ordering
- Minimum Opening Order: ${amount} or {units} units
- Minimum Reorder: ${amount} or {units} units
- Orders can be placed via {Faire / Shopify B2B / Email}
- All orders are subject to product availability

## 2. Pricing
- Wholesale prices are as listed in the current price list
- Volume discounts available (see tiered pricing schedule)
- Prices are subject to change with 30 days' notice
- All prices are in USD

## 3. Payment Terms
- New accounts: Prepayment or credit card on file
- Established accounts (3+ orders): Net 30
- Preferred accounts (12+ months, $10K+ annual): Net 60
- Late payment fee: 1.5% per month on overdue balance

## 4. Shipping
- Orders ship within {3-5} business days
- Free shipping on orders over ${threshold}
- Standard shipping via {carrier}: ${rate} flat rate
- Expedited shipping available at additional cost
- International shipping quoted per order

## 5. Returns & Exchanges
- Defective products: Full credit within 30 days of receipt
- Non-defective returns: Not accepted (all sales final)
- Damaged in transit: File claim with carrier within 48 hours
- Contact wholesale@{brand}.com for all return requests

## 6. MAP Policy
- All retailers must comply with {Brand Name}'s MAP Policy
- MAP price = MSRP for all products
- See separate MAP Policy document for details

## 7. Authorized Retailer Requirements
- Must have a physical retail location or established online store
- Must maintain product presentation standards per Brand Guidelines
- Must not sell on Amazon, eBay, or other marketplaces without written approval
- Must not sell to other wholesalers or distributors

## 8. Brand Guidelines
- Retailers must follow {Brand Name}'s visual merchandising guidelines
- Product images must be official {Brand Name} images only
- Brand name must be spelled and capitalized correctly
- Marketing materials must be approved by {Brand Name} before use
```

---

## 五、Linesheet 内容模板

### 5.1 Linesheet 结构

```
Linesheet 必须包含的元素：
├── 品牌 Logo + 联系信息
├── 季节/系列名称
├── 每个产品：
│   ├── 产品图片（白底，高清）
│   ├── 产品名称
│   ├── SKU 编号
│   ├── 批发价
│   ├── MSRP
│   ├── 可用颜色/尺寸
│   ├── 最小起订量（per SKU）
│   ├── 包装规格（如 6-pack / 12-pack）
│   └── 预计交货时间
├── 订购条款摘要
├── 联系方式（批发邮箱/电话）
└── 页码和日期

设计原则：
├── 简洁专业（买手每天看几十份 Linesheet）
├── 产品图片是核心（占页面 60%+ 面积）
├── 价格信息清晰易读
├── 使用品牌色彩但不过度设计
└── PDF 格式，文件大小 < 10MB（方便邮件发送）
```

---

*本工具包持续更新。定价策略应根据品牌实际情况和市场反馈定期调整。*
