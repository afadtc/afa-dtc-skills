# 产品页 (PDP) SEO 优化手册

> **用途**：本文件为 SEO 增长模块的内部参考文件，用于优化具体产品页面（PDP）。产品页不仅要转化，还要能被搜索到，并且能被 AI 购物助手理解。

---

## 一、核心理念：为什么 PDP SEO 如此重要？

大多数 Shopify PDP 对 Google 来说是"隐形"的。
- **默认 Meta Title**：只是产品名称，没有修饰词。
- **默认描述**：通常只有三个卖点列表，缺乏长尾词。
- **缺乏结构化数据**：只有基础的 Shopify 默认 Schema。
- **AI 发现障碍**：AI 购物助手（如 ChatGPT, Perplexity）通常只读取页面的前 ~6,000 个字符。如果关键信息不在前面，产品就不会被推荐。

---

## 二、PDP SEO 优化框架

### 2.1 交易型关键词研究 (Transactional Keyword Research)

PDP 的目标不是获取广泛的流量，而是获取**准备购买**的流量。

- **关键词模式**：
  - `[product] buy` (如 "buy lightweight hiking backpack")
  - `[product] review` (如 "Osprey Exos 58 review")
  - `[brand] vs [competitor]` (如 "Osprey vs Gregory backpacks")
  - `[product] for [use case]` (如 "best backpack for Appalachian Trail")
- **长尾变体**：包含颜色、尺寸、材质、特定功能（如 "waterproof 50L hiking backpack"）。

### 2.2 基础元数据优化 (Meta Data)

- **Meta Title**：≤ 60 字符。
  - **结构**：[主关键词] + [品牌名] + [独特卖点/修饰词]
  - **示例**：`Osprey Exos 58 Lightweight Hiking Backpack | Waterproof`
- **Meta Description**：≤ 155 字符。
  - **结构**：包含主关键词 + 核心利益点 + 行动号召 (CTA)。
  - **示例**：`Buy the Osprey Exos 58 lightweight hiking backpack. Features a ventilated suspension system and waterproof cover. Free shipping on orders over $50. Shop now!`

### 2.3 扩展产品描述 (Extended Product Description)

这是为 Google 和 AI 助手提供丰富上下文的关键。

- **长度**：应按产品复杂度与搜索意图提供足够上下文，不写死统一字数。
- **位置**："完整描述"或首屏以下的区域。
- **内容结构**：
  - **AI 发现前置 (Front-loaded for AI)**：在描述的前 6,000 字符内，清晰陈述产品身份、规格、核心利益和差异化优势。
  - **买家导向 (Buyer-focused)**：不要只列出功能（Features），要解释这些功能带来的利益（Benefits）。
  - **长尾词自然融入**：在描述使用场景、材质和对比时，自然使用长尾关键词。

### 2.4 常见问题 (FAQ) 与异议处理

- **来源**：从 Google 的 "People Also Ask" (PAA) 提取，或针对该产品的常见客户异议。
- **数量**：按真实高频异议整理，保持覆盖充分且不过度堆叠。
- **格式**：宜优先使用 JSON-LD 格式部署 `FAQPage` Schema，并确认其与页面可见内容一致。
- **目的**：解答购买前的最后疑虑，同时在 SERP 中占据更多空间。

### 2.5 图像与多媒体优化

- **Alt 文本 (Alt Text)**：为每张产品图片提供描述性的 Alt 文本，包含相关关键词。
  - **错误**：`backpack-1.jpg`
  - **正确**：`Osprey Exos 58 lightweight hiking backpack front view`
- **视频优化**：如果包含产品视频，提供字幕，并部署 `VideoObject` Schema。

### 2.6 内部链接与防蚕食 (Internal Linking & Cannibalization)

- **内部链接地图**：
  - 链接到相关的分类页（如 "Back to [Lightweight Backpacks]"）。
  - 链接到相关的配件或补充产品（如 "Pairs well with [Hydration Reservoir]"）。
  - 链接到相关的博客文章（如 "Read our review of the [Osprey Exos 58]"）。
- **防蚕食检查 (Cannibalization Check)**：确保 PDP 的主关键词不与分类页或博客文章冲突。如果冲突，调整 PDP 的关键词定位（更具体、更长尾）。

### 2.7 增强型结构化数据 (Enhanced Schema Markup)

超越 Shopify 默认的 Schema，提供更丰富的实体信号。

- **Product Schema**：通常应优先补齐 `name`, `image`, `description`, `sku`/`gtin`, `brand`, `offers` (price, priceCurrency, availability), `aggregateRating` 等关键字段，并结合页面真实可见信息校验。
- **Review Schema**：集成真实用户评论的评分。
- **Brand Schema**：明确品牌实体。
- **Offer Schema**：详细说明价格、货币、库存状态和有效期。

---

## 三、Google Shopping Feed 优化

PDP 的 SEO 优化应与 Google Merchant Center 的 Feed 优化同步进行。

- **产品标题 (Product Title)**：在 Feed 中，标题应包含品牌、产品类型、关键属性（如颜色、尺寸）。
  - **示例**：`Osprey Exos 58 Lightweight Hiking Backpack - Blue - Medium`
- **产品描述 (Product Description)**：确保 Feed 中的描述包含最重要的关键词和属性。
- **Google 产品类别 (Google Product Category)**：选择最具体、最准确的类别。
- **产品类型 (Product Type)**：使用网站的分类结构（如 `Gear > Backpacks > Lightweight Backpacks`）。

### Shopping Feed 优化效果基准

| 优化项 | 常见影响方向 | 说明 |
|:---|:---:|:---|
| 完善产品标题 | 常见改善 CTR | 加入品牌、属性、使用场景等关键词 |
| 添加促销标注 | 常见改善 CTR | 使用 Merchant Center 促销功能 |
| 优化产品图片 | 常见改善点击与停留质量 | 高质量白底图 + 场景图 |
| 完善产品属性 | 常见改善展示完整度与匹配度 | 填写全部可选属性（GTIN/颜色/尺码等） |
