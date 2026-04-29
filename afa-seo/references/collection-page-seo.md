# 分类页 (Collection Page) SEO 优化手册

> **用途**：afa-seo 在优化 Shopify Collection 页面时的标准操作程序 (SOP)。分类页是电商网站最具商业价值的页面，必须采用 3 层架构优化。

---

## 一、核心理念：为什么分类页最重要？

分类页（Category/Collection Pages）是电商网站的"支柱页面"（Pillar Pages）。
- **高意图**：搜索"best lightweight backpacks"的用户比搜索"how to pack a backpack"的用户更接近购买。
- **高流量**：分类词通常比单一产品词（PDP）有更高的搜索量。
- **内部链接枢纽**：分类页将权重传递给所有子产品，是网站架构的核心。

---

## 二、3 层架构优化框架

### Layer 1: 基础元数据 (Meta Data)

这是用户在搜索结果页面 (SERP) 看到的第一印象，直接决定点击率 (CTR)。

#### 1.1 关键词映射 (Keyword Mapping)
- **主关键词**：1 个（如 "lightweight backpacks"），商业/交易意图，搜索量最大。
- **次关键词**：2-3 个（如 "ultralight hiking backpacks", "best daypacks"）。
- **长尾词**：3-5 个（如 "lightweight backpacks under 2 lbs"）。

#### 1.2 Meta Title 优化
- **长度**：≤ 60 字符。
- **结构**：[主关键词] + [次关键词/修饰词] | [品牌名]
- **示例**：`Lightweight & Ultralight Hiking Backpacks | Osprey`

#### 1.3 Meta Description 优化
- **长度**：≤ 155 字符。
- **结构**：包含主关键词 + 独特卖点 (USP) + 行动号召 (CTA)。
- **示例**：`Shop our collection of lightweight and ultralight hiking backpacks. Designed for comfort and durability on the trail. Free shipping on orders over $50. Shop now!`

---

### Layer 2: 页面内容 (Page Content)

这是 Google 理解页面主题和用户获取购买信息的关键。

#### 2.1 H1 标题
- 必须包含主关键词。
- 简洁明了，通常就是分类名称。
- **示例**：`<h1>Lightweight Hiking Backpacks</h1>`

#### 2.2 首屏描述 (Above-the-fold)
- **位置**：H1 标题下方，产品网格上方。
- **长度**：2-3 句话（约 50-100 字）。
- **目的**：快速确认用户找对了地方，自然融入主关键词，强调购买理由。
- **示例**：`Discover our range of lightweight hiking backpacks engineered for multi-day treks and fast-packing. Featuring breathable suspension systems and durable ripstop fabrics, these packs keep you moving fast without weighing you down.`

#### 2.3 底部购买指南 (Below-the-fold)
- **位置**：产品网格下方（避免将产品推到首屏以下）。
- **长度**：300-600 字。
- **结构**：使用 H2/H3 标题组织内容。
- **内容方向**：
  - **What to look for**：如何选择合适的尺寸/容量。
  - **Key features**：解释核心技术（如防水材料、背负系统）。
  - **Use cases**：适合哪些场景（如周末徒步、长途旅行）。
- **目的**：建立主题权威，自然融入长尾关键词，解答用户购买前的疑问。

---

### Layer 3: 内部链接与结构化数据

这是提升页面权重和在 SERP 中占据更多空间的高级策略。

#### 3.1 内部链接 (Internal Linking)
- **面包屑导航 (Breadcrumbs)**：`Home > Gear > Backpacks > Lightweight Backpacks`。
- **相关分类链接**：在底部指南中，横向链接到平级或相关的分类（如 "Looking for something smaller? Check out our [Daypacks] collection."）。
- **博客/指南链接**：链接到相关的教育性内容（如 "Read our guide on [How to Pack a Backpack for a 3-Day Trip]."）。

#### 3.2 常见问题 (FAQ) 与 Schema
- **来源**：从 Google 的 "People Also Ask" (PAA) 中提取 4-6 个相关问题。
- **回答**：提供直接、简洁的答案（1-2 句话）。
- **Schema**：必须使用 JSON-LD 格式部署 `FAQPage` Schema，这能让你的页面在搜索结果中占据更多垂直空间。

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is considered a lightweight hiking backpack?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "A lightweight hiking backpack typically weighs between 2 to 4 pounds (0.9 to 1.8 kg) when empty, while ultralight packs weigh under 2 pounds."
    }
  }]
}
```

---

## 三、常见错误与避坑指南

1. **关键词蚕食 (Keyword Cannibalization)**：确保每个分类页都有独特的主关键词。不要让 `/collections/backpacks` 和 `/collections/hiking-backpacks` 竞争同一个词。
2. **内容隐藏**：不要使用"阅读更多" (Read More) 折叠底部指南内容，Google 可能会降低隐藏内容的权重。
3. **过度优化**：不要在首屏描述中堆砌关键词，保持自然流畅的阅读体验。
4. **忽视移动端**：确保底部指南在移动端排版良好，字体大小易读。
