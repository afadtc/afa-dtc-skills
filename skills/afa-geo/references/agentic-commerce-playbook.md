# Agentic Commerce 操盘手册（AI 渠道从"被引用"到"被购买"）

> 本文件为 AI 渠道引擎的旗舰参考：把 GEO/AEO（被 AI 引用）升级到 **agentic commerce**（在 AI 里被直接购买）。所有平台事实带来源脚注，核实于 2026-07。

---

## 〇、为什么现在必须做（实证）

AI 渠道不再是"前瞻"，是正在发生的流量迁移：**Shopify Q1 2026 披露——店铺的 AI 流量同比约 8 倍、AI 搜索订单近 13 倍、AI 渠道新客率约为其他渠道的 2 倍**；麦肯锡预估 agentic 渠道 2030 年全球 $3-5 万亿。

> **来源**：[Shopify Spring '26 商家版](https://www.shopify.com/news/spring-26-edition-merchant)；[Fast Company：agentic commerce 竞赛](https://www.fastcompany.com/91533534/shop-til-you-bot-google-openai-and-the-race-to-build-agentic-commerce)。

## 一、两大协议（谁在 AI 里帮用户下单）

### 1.1 OpenAI ACP（Agentic Commerce Protocol，与 Stripe 共建）
- ChatGPT **Instant Checkout** 自 2025-09 上线，每天约 **5,000 万条购物查询**。
- **商家排序因子（官方口径）**：库存、价格、质量、**是否一级卖家（first-party）**、**是否开通 Instant Checkout**。
> **来源**：[OpenAI：Buy it in ChatGPT](https://openai.com/index/buy-it-in-chatgpt/)。

### 1.2 Shopify + Google UCP（Universal Commerce Protocol）
- 2026-01 发布，Amazon / Meta / Microsoft / Stripe / Target / Etsy 站台。
- **Shopify Catalog**：把商品标准化为 AI 可读数据层，**符合条件默认收录**；**Universal Cart** 让 AI agent 跨商家组单。
> **来源**：[Shopify：agentic commerce 解读](https://www.shopify.com/blog/how-agentic-commerce-works)；[shopify.dev/docs/agents](https://shopify.dev/docs/agents)。

## 二、双协议对照决策树（用哪个）

```text
用户主要在哪个 agent 里购买？
├── ChatGPT / OpenAI 生态 → 优先接 ACP：开通 Instant Checkout、把 feed 喂给 ChatGPT 购物
├── Google / Shopify 生态 → 优先走 UCP：确认 Shopify Catalog 收录状态、开 Universal Cart
└── 两者都重要（多数成长期品牌）→ 双协议并行，先补齐"库存/价格/质量"三项通用排序因子，再按渠道占比分配接入优先级
```

## 三、接入检查清单

- [ ] **Catalog 收录状态**：Shopify 商家确认商品是否已进入 Catalog（默认收录≠一定合规，需检查字段完整性）。
- [ ] **结构化 feed**：标题/属性/库存/价格/合规字段齐全，AI 可读。
- [ ] **Instant Checkout 开通**（ACP 排序因子之一）。
- [ ] **一级卖家信号**：官网自营优先于第三方转售。
- [ ] **排序三要素**：库存充足、价格有竞争力、质量/评价过硬——这是两协议的通用地基。

## 四、llms.txt 实施

`llms.txt` 是放在站点根目录、给 AI 爬虫的"内容地图"（类似 robots.txt 之于搜索引擎），指明哪些页面/文档最值得被 AI 读取与引用。

- **放哪**：网站根目录 `/llms.txt`（可配套 `/llms-full.txt` 提供全文）。
- **写什么**：品牌简介 + 最权威页面（产品、FAQ、政策、可摘录统计）的链接与一句话说明，用 Markdown。
- **作用**：提高第一方内容被 AI 正确引用的概率，减少 AI 抓错/编造。
> **来源**：[Elementera：llms.txt 实施指南](https://www.elementera.com/blog/what-is-llms-txt-how-implement-for-ai-bots-2026-guide)。

## 五、测试对象（2026，务必逐个测）

| 对象 | 说明 |
|---|---|
| ChatGPT（含 Instant Checkout） | 每天约 5,000 万购物查询，ACP 主场 |
| Perplexity | AI 搜索引用高权重 |
| Google AI Overviews / AI Mode | 头部链接与 AI 引用重合度已从约 70% 跌破 20% |
| **Amazon Alexa for Shopping** | 原 **Rufus**，**2026-05-13 更名**，约 **2.5 亿用户**、互动同比 +210%；COSMO 语义层（use-case > 关键词堆砌） |
| Gemini 购物 | Google 生态的购物助手 |

> **来源**：[Search Engine Land：LLM 优化 2026](https://searchengineland.com/llm-optimization-tracking-visibility-ai-discovery-463860)；[Amalytix：Alexa for Shopping 指南](https://www.amalytix.com/en/knowledge/ai/amazon-rufus-guide-2026/)；[LLMrefs：GEO 2026](https://llmrefs.com/generative-engine-optimization)。

## 六、指标升级：从 Share of Voice 到 LLM Visibility Score

- 旧口径"份额/曝光"不够——升级为 **LLM Visibility Score**：在一组目标购物问题里，品牌被 AI **提及/引用/推荐结账**的综合可见度。
- 优化优先级（据 Yext 分析 680 万条 AI 引用）：**44% 引用来自品牌第一方官网、42% 来自 listings**、8% 评论/社交、6% 新闻论坛——**"listings + 第一方内容"是第一梯队**，优先把这两块做扎实，再做社媒/PR 补充。

> **来源**：[Search Engine Land / Yext：AI 引用来源分布](https://searchengineland.com/llm-optimization-tracking-visibility-ai-discovery-463860)。

## 七、与其他模块的衔接

- 落地成本/关税影响定价与"价格"排序因子 → 见 `landed-cost-calculator.md` 与 `../../afa-expand/references/tariff-new-normal-playbook.md`。
- Amazon COSMO 语义优化与本手册的 GEO 内容块模板跨模块复用 → 见 `../../afa-expand/references/marketplace-entry-playbook.md`。
