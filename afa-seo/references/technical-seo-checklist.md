# 技术 SEO 审计清单与修复指南

> **用途**：本文件为 SEO 增长模块的内部参考文件，用于执行技术 SEO 审计、排查收录异常和排名下降。

---

## 一、爬取与索引 (Crawlability & Indexability)

### 1.1 Robots.txt 检查
- **目标**：确保搜索引擎可以访问重要页面，同时屏蔽低价值页面。
- **Shopify 特有检查**：
  - 确保 `/collections/*+*`（带过滤器的分类页）被屏蔽，防止无限爬取。
  - 确保 `/search`（内部搜索结果页）被屏蔽。
  - 确保 `/cart` 和 `/checkout` 被屏蔽。
- **修复建议**：在 Shopify 中，通过编辑 `robots.txt.liquid` 模板来修改默认规则。

### 1.2 XML Sitemap 检查
- **目标**：为搜索引擎提供网站结构的清晰地图。
- **检查项**：
  - 是否包含所有核心产品页、分类页和博客文章？
  - 是否排除了 404、301 或带有 `noindex` 标签的页面？
  - 是否在 Google Search Console (GSC) 中成功提交且无错误？
- **修复建议**：Shopify 自动生成 `sitemap.xml`，但如果使用了无头架构 (Headless) 或自定义应用，需确保 Sitemap 动态更新。

### 1.3 规范化标签 (Canonical Tags)
- **目标**：解决重复内容问题，整合页面权重。
- **检查项**：
  - 每个页面是否都有自引用的规范标签？
  - 带有参数的 URL（如 `?variant=123` 或 `?sort_by=price`）是否指向主 URL？
  - 跨域重复内容（如在 Medium 上发布的博客）是否指向官网原文？
- **修复建议**：在 Shopify 的 `theme.liquid` 的 `<head>` 部分确保包含 `<link rel="canonical" href="{{ canonical_url }}">`。

---

## 二、网站性能与 Core Web Vitals

### 2.1 LCP (Largest Contentful Paint)
- **目标**：< 2.5 秒。
- **常见问题**：首屏大图（Hero Image）未优化、服务器响应慢。
- **修复建议**：
  - 对首屏图片使用 `fetchpriority="high"`。
  - 避免在首屏使用轮播图 (Carousel) 或视频背景。
  - 使用 WebP 或 AVIF 格式，并确保图片尺寸适合设备。

### 2.2 INP (Interaction to Next Paint)
- **目标**：< 200 毫秒。
- **常见问题**：主线程被繁重的 JavaScript 阻塞（常见于 Shopify 的第三方应用）。
- **修复建议**：
  - 延迟加载非关键的第三方脚本（如客服聊天、热图工具）。
  - 优化或移除未使用的 Shopify App。

### 2.3 CLS (Cumulative Layout Shift)
- **目标**：< 0.1。
- **常见问题**：图片或广告未指定宽高、动态注入的内容（如促销横幅）推开现有内容。
- **修复建议**：
  - 为所有 `<img>` 和 `<video>` 标签添加 `width` 和 `height` 属性。
  - 为动态加载的内容（如评论小部件）预留 CSS 最小高度。

---

## 三、结构化数据 (Schema Markup)

### 3.1 电商核心 Schema
- **Product Schema**：必须包含 `name`, `image`, `description`, `sku`/`gtin`, `brand`, `offers` (price, priceCurrency, availability), `aggregateRating`。
- **BreadcrumbList Schema**：帮助 Google 理解网站层级，并在 SERP 中显示面包屑。
- **FAQPage Schema**：在分类页和产品页部署，增加在 SERP 中占据的空间。

### 3.2 验证与监控
- 使用 Google 的 [Rich Results Test](https://search.google.com/test/rich-results) 工具验证。
- 在 GSC 的 "Enhancements" 报告中监控结构化数据错误。

---

## 四、移动端优先索引 (Mobile-First Indexing)

- **目标**：确保移动端体验与桌面端一致或更好。
- **检查项**：
  - 移动端是否包含桌面端的所有核心内容（不要在移动端隐藏重要的 SEO 文本）？
  - 移动端的结构化数据是否与桌面端一致？
  - 触摸目标（按钮、链接）是否足够大且间距合理？
  - 避免使用侵入式的移动端弹窗（Intrusive Interstitials）。

---

## 五、国际化 SEO (International SEO)

### 5.1 Hreflang 标签
- **目标**：向 Google 表明页面的语言和地区定位。
- **检查项**：
  - 是否包含自引用的 hreflang？
  - 是否提供了 `x-default` 作为后备页面？
  - 语言和地区代码是否正确（如 `en-US`, `en-GB`）？
- **修复建议**：在 Shopify 中，如果使用 Shopify Markets，系统会自动处理大部分 hreflang，但需检查自定义域名或子目录的配置是否正确。
