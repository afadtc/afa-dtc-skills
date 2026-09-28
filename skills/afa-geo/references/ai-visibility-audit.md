# AI 搜索可见度审计 SOP (AI Visibility Audit SOP)

在 2026 年，如果你的品牌在 AI 搜索引擎中不可见，你就等于把高意向的转化流量拱手让给了竞争对手。本 SOP 提供了一套标准化的审计流程，用于评估和监控品牌在生成式引擎中的表现。

## 1. 审计准备阶段 (Preparation)

### 1.1 构建核心查询词库 (Query Matrix)
不要只测试品牌词。AI 搜索的查询通常更长、更具对话性。构建包含 15-20 个词的矩阵：
*   **品牌词 (Brand)**："What is [Brand Name]?", "[Brand Name] reviews"
*   **品类定义词 (Category Definition)**："What is the best [Category] for [Specific Use Case]?"
*   **痛点解决词 (Problem-Solving)**："How to fix [Problem] without [Common Side Effect]?"
*   **竞品对比词 (Comparison)**："[Your Brand] vs [Top Competitor]", "Best alternatives to [Top Competitor]"

### 1.2 确定目标 AI 平台
必须在以下三大核心平台进行测试，因为它们的底层逻辑和市场份额各不相同：
1.  **Google AI Overviews (AIO)**：占据最大的搜索入口，影响最广泛的自然流量。
2.  **ChatGPT (Browsing Mode)**：用户基数最大，对话式搜索的代表。
3.  **Perplexity.ai**：纯粹的答案引擎，对数据和权威引用的要求最高。

## 2. 执行审计测试 (Execution)

### 2.1 手动测试与记录 (Manual Testing)
对于每个查询词，在三个平台上分别输入，并记录以下数据：

| 审计维度 | 评估标准与记录方式 |
| :--- | :--- |
| **触发状态 (Trigger)** | AI 是否生成了回答？(Yes/No) |
| **品牌提及 (Mention)** | 你的品牌是否在回答的正文或参考链接中被提及？(Yes/No) |
| **排名位置 (Position)** | 如果被提及，是作为首选推荐，还是列在最后？(1st, Top 3, Other) |
| **情感倾向 (Sentiment)** | AI 对品牌的描述是正面的（推荐）、中立的（仅列出），还是负面的（指出缺点）？ |
| **竞品表现 (Competitors)** | 哪些竞争对手被高频引用？记录他们的名字。 |
| **引用来源 (Source URL)** | AI 引用了哪个具体的 URL？是你的官网，还是第三方平台（如 Reddit, 评测网站）？ |

### 2.2 竞争对手逆向工程 (Competitor Reverse Engineering)
如果竞品被频繁引用而你没有，深入分析竞品被引用的那个页面：
1.  **结构分析**：他们是否使用了 40-60 词的定义块？是否有对比表格？
2.  **权威分析**：页面上是否有专家引言？是否有带来源的统计数据？
3.  **技术分析**：使用工具（如 Schema Validator）检查他们是否部署了 `FAQPage` 或 `Product` Schema。

## 3. 技术拦截排查 (Technical Blockers Check)

很多时候，品牌在 AI 搜索中隐形，仅仅是因为技术设置错误。

### 3.1 `robots.txt` 检查
访问 `https://yourdomain.com/robots.txt`，检查是否错误地拦截了以下关键爬虫：
```text
# 必须确保以下爬虫没有被 Disallow: /
User-agent: GPTBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: ClaudeBot
User-agent: Google-Extended
```
*注意：如果你发现 `User-agent: *` 下面有 `Disallow: /`，这意味着你屏蔽了所有爬虫，这是一个灾难性的错误。*

### 3.2 渲染与可提取性检查 (Rendering Check)
AI 爬虫在处理重度依赖客户端渲染（Client-Side Rendering, CSR）的 JavaScript 页面时经常遇到困难。
*   **测试方法**：在浏览器中禁用 JavaScript，然后重新加载你的核心页面。
*   **评估**：如果页面变成空白，或者核心内容（如产品描述、价格、FAQ）消失，说明 AI 爬虫也无法提取这些内容。必须切换到服务端渲染（SSR）或静态站点生成（SSG）。

## 4. 审计报告与优化路线图 (Reporting & Roadmap)

基于审计结果，生成结构化的报告，并制定分阶段的优化路线图。

### 4.1 优先级划分矩阵
*   **高优先级 (Quick Wins)**：修复技术拦截（修改 robots.txt）；为已经有一定流量的核心页面添加 FAQ Schema 和定义块。
*   **中优先级 (Content Upgrade)**：重写表现不佳的博客文章，添加统计数据、专家引言和对比表格；更新所有页面的“最后修改日期”。
*   **低优先级/长期 (Authority Building)**：启动第三方平台播种计划（Reddit 参与、联系评测媒体、建立维基百科页面）。

### 4.2 持续监控机制 (Continuous Monitoring)
AI 搜索引擎的算法和索引更新非常频繁。
*   **频率**：建议每月进行一次完整的可见度审计。
*   **工具辅助**：对于拥有大量 SKU 的品牌，建议使用自动化工具（如 Otterly AI 或 Peec AI）来大规模追踪“AI 语音份额 (Share of AI Voice)”，而不是纯手动测试。

## 5. 进阶：AI 情感分析与声誉修复 (Sentiment Analysis & Reputation Repair)

AI 引擎不仅会决定是否提及你的品牌，还会决定**如何**描述你的品牌。如果 AI 认为你的产品“质量差”或“客服糟糕”，这比不被提及更具破坏性。

### 5.1 情感倾向评估 (Sentiment Evaluation)
在审计时，必须仔细阅读 AI 生成的关于你品牌的描述段落，并进行分类：
*   **强正面 (Strong Positive)**：AI 主动推荐，并列出具体的优点（如“如果你追求极致的耐用性，[Brand] 是最佳选择”）。
*   **中立/事实性 (Neutral/Factual)**：AI 仅仅列出品牌名称或客观描述功能，没有明显的倾向性。
*   **混合/有保留 (Mixed/Caveated)**：AI 提出了优点，但也明确指出了缺点（如“[Brand] 功能强大，但许多用户反映其价格过高且退货困难”）。
*   **负面 (Negative)**：AI 建议用户避免购买，或将其作为反面教材。

### 5.2 负面情感的根源追踪 (Root Cause Tracing)
AI 不会凭空捏造负面评价（除非是幻觉）。如果 AI 对品牌有负面评价，通常是因为它抓取到了网络上的负面共识。
*   **操作**：向 AI 提问：“你为什么认为 [Brand] 的退货政策不好？请提供你的信息来源。”
*   **常见根源**：Trustpilot 上的大量 1 星评价、Reddit 上的负面吐槽贴、BBB（商业改进局）的投诉记录。

### 5.3 AI 声誉修复策略 (AI Reputation Repair Strategy)
一旦发现负面情感，必须立即启动修复计划。这比传统的 SEO 声誉管理更具挑战性，因为你无法直接修改 AI 的模型权重。

1.  **源头阻断 (Source Mitigation)**：
    *   如果负面评价来自 Trustpilot，立即启动客户关怀计划，联系留下差评的用户解决问题，并请求他们修改评价。
    *   如果负面评价来自 Reddit，不要试图删除帖子（通常不可能），而是由官方账号在帖子下进行诚恳、透明的回复，说明改进措施。
2.  **正面信息轰炸 (Positive Information Flooding)**：
    *   AI 引擎倾向于相信“最新”和“最权威”的信息。
    *   发布大量带有最新日期的高质量内容，详细阐述品牌在受批评领域的改进（例如：“2026 年全新升级的无忧退货政策”）。
    *   积极获取权威媒体的正面评测，并确保这些评测被发布在权重极高的网站上。
3.  **利用“数据”对抗“观点” (Data vs. Opinions)**：
    *   如果 AI 引用了某些用户的负面“观点”，品牌应该用硬核的“数据”来进行反击。
    *   例如，在官网和 PR 稿件中大量发布：“根据 2026 年针对 10,000 名用户的调查，我们的产品满意度达到 98%。” AI 引擎在抓取时，往往会赋予具体的统计数据更高的权重。

## 6. 审计工具的自动化集成 (Automating the Audit)

对于拥有数十个产品线和数百个核心查询词的成熟 DTC 品牌，手动审计是不现实的。必须利用自动化工具建立监控仪表盘。

### 6.1 推荐的自动化工作流
1.  **关键词导入**：将核心查询词库导入 Peec AI 或 Otterly AI。
2.  **频率设置**：设置为每周自动抓取一次 ChatGPT, Perplexity 和 Google AI Overviews 的结果。
3.  **警报机制 (Alerting)**：
    *   设置阈值警报：如果品牌在核心查询词中的“AI 语音份额”单周下降超过 10%，立即发送 Slack/邮件通知。
    *   设置竞品警报：如果主要竞争对手突然在某个高流量查询词中获得了强正面推荐，立即触发警报。
4.  **数据可视化**：将 AI 可见度数据与 Google Analytics 4 (GA4) 中的 AI 引荐流量数据结合，在 Looker Studio 中建立统一的“AI 搜索表现仪表盘”。

## 7. 审计交付物：执行摘要模板 (Executive Summary Template)

审计报告的开头必须包含一个面向高管的执行摘要，用最简练的语言说明现状和行动建议。

> **[品牌名称] AI 搜索可见度审计 - 2026年 Q2 执行摘要**
>
> **现状诊断**：
> 目前，[品牌名称] 在 AI 搜索领域的整体表现处于**危险**水平。在 20 个核心查询词中，我们的 AI 语音份额仅为 4%，而主要竞品 [Competitor A] 达到了 38%。我们在 Perplexity 中几乎完全隐形，主要原因是官网内容缺乏数据支撑和专家引言。
>
> **关键发现**：
> 1. 我们的 `robots.txt` 错误地拦截了 `PerplexityBot`，导致该平台无法抓取我们的最新产品页。
> 2. 竞品广泛使用了对比表格和 FAQ Schema，而我们仍在使用传统的长篇散文格式。
> 3. ChatGPT 在回答中提及了我们“发货缓慢”的负面评价，经查实，该信息来源于 Trustpilot 上 6 个月前的旧评论。
>
> **核心行动建议 (未来 30 天)**：
> 1. **立即修复**：更新 `robots.txt`，解除对所有主流 AI 爬虫的拦截。
> 2. **内容重构**：重写 Top 5 流量博客文章，加入 40-60 词的定义块、对比表格和至少 3 项带来源的统计数据。
> 3. **声誉修复**：在官网发布最新的“次日达物流升级公告”，并启动 Trustpilot 正面评价收集活动，以覆盖旧的负面信息。
