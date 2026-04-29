# 多语言/多地区 SEO 与 hreflang 部署指南

> **用途**：afa-seo 在品牌出海、拓展新国家市场时的标准操作程序 (SOP)。

---

## 一、核心理念：为什么需要国际化 SEO？

当品牌向全球扩张时，Google 需要知道将哪个版本的页面展示给哪个国家/语言的用户。
- **避免重复内容惩罚**：美国英语版和英国英语版的内容可能高度相似，如果没有正确的信号，Google 可能会将其视为重复内容。
- **提升本地相关性**：向英国用户展示以英镑计价、包含本地配送信息的页面，能显著提升转化率。
- **精准的流量分配**：确保每个市场的流量都导向为其专门优化的页面。

---

## 二、URL 结构战略选择

选择合适的 URL 结构是国际化 SEO 的基础。

### 2.1 ccTLD (国家/地区代码顶级域名)
- **格式**：`brand.co.uk`, `brand.de`, `brand.fr`
- **优点**：最强的本地化信号，用户信任度高。
- **缺点**：成本高，每个域名都需要独立建立权威度（DR）。
- **适用场景**：在目标市场有实体运营、预算充足的大型品牌。

### 2.2 子目录 (Subdirectories)
- **格式**：`brand.com/uk/`, `brand.com/de/`, `brand.com/fr/`
- **优点**：继承主域名的权威度，维护成本低。
- **缺点**：本地化信号较弱。
- **适用场景**：大多数 DTC 品牌的首选方案（Shopify Markets 默认使用此结构）。

### 2.3 子域名 (Subdomains)
- **格式**：`uk.brand.com`, `de.brand.com`, `fr.brand.com`
- **优点**：易于分离不同市场的服务器和技术栈。
- **缺点**：权威度继承不如子目录，维护复杂。
- **适用场景**：不同市场使用完全不同的电商平台时。

---

## 三、Hreflang 精确部署

Hreflang 标签是告诉 Google 页面语言和地区定位的最重要技术信号。

### 3.1 部署规则
- **双向链接**：如果页面 A 链接到页面 B，页面 B 必须链接回页面 A。
- **自引用**：每个页面必须包含指向自身的 hreflang 标签。
- **x-default**：必须提供一个默认页面（通常是主站或英语版），供未指定语言/地区的用户访问。
- **代码规范**：必须使用 ISO 639-1 语言代码和 ISO 3166-1 Alpha 2 地区代码（如 `en-GB`, `fr-CA`）。

### 3.2 示例代码 (HTML Head)
```html
<link rel="alternate" hreflang="en-US" href="https://brand.com/us/product" />
<link rel="alternate" hreflang="en-GB" href="https://brand.com/uk/product" />
<link rel="alternate" hreflang="fr-FR" href="https://brand.com/fr/product" />
<link rel="alternate" hreflang="x-default" href="https://brand.com/product" />
```

### 3.3 Shopify 实施建议
- 如果使用 Shopify Markets，系统会自动在 `<head>` 中生成正确的 hreflang 标签。
- 确保不要在 `theme.liquid` 中手动硬编码 hreflang，以免与系统生成的标签冲突。

---

## 四、内容本地化（超越翻译）

仅仅翻译文字是不够的，必须进行深度的本地化。

### 4.1 货币与度量衡
- 确保价格以当地货币显示（如 £, €, $）。
- 转换度量衡（如将 lbs 转换为 kg，inches 转换为 cm）。

### 4.2 关键词本地化
- 不同地区对同一事物的称呼可能不同。
- **示例**：美国叫 "sneakers"，英国叫 "trainers"；美国叫 "sweater"，英国叫 "jumper"。
- 必须针对每个市场进行独立的关键词研究。

### 4.3 文化与信任信号
- 提供本地的客户服务联系方式（如本地电话号码）。
- 展示本地用户熟悉的支付方式（如欧洲的 Klarna, 荷兰的 iDEAL）。
- 明确说明本地的配送时间和退换货政策。

---

## 五、本地信号建设 (Local Signal Building)

### 5.1 Google Business Profile
- 如果在目标市场有实体店或办公室，必须创建并优化 Google Business Profile。
- 确保 NAP (Name, Address, Phone) 信息在所有本地目录中保持一致。

### 5.2 本地外链获取
- 积极获取目标市场本地网站（如 `.co.uk`, `.de` 域名）的反向链接。
- 参与本地的行业活动、赞助本地组织，或向本地媒体发布新闻稿。
- 本地外链是提升该地区搜索排名的关键驱动力。
