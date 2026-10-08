# AFA DTC Skills

做了十年独立站，操盘超 1 亿美金预算，我把我自己蒸馏成了 31 个独立站 AI 顾问。这是一套面向独立站与 DTC 品牌的全链路增长顾问 Skill 系统：**31 个模块、三层路由、会算数、能自检、记得住、拆开单装也能用**，覆盖从市场洞察、选品测品、品牌、广告投放、CRO、留存，到支付风控、运营与规模化扩张的完整链路。

**当前版本：v2.7.7**

**作者**：1亿美刀站长阿发

|   | 平台  | 链接                                            |
| --- | --- | --------------------------------------------- |
| 📹 | 视频号 | 微信搜索「1亿美刀站长阿发」                                |
| 💬 | 公众号 | 微信搜索「1亿美刀站长阿发」                                |
| 📕 | 小红书 | [1亿美刀站长阿发](https://xhslink.com/m/34JAVccyOdD) |
| 🎵 | 抖音  | [1亿美刀站长阿发](https://v.douyin.com/nSkhVHdGCrg/) |

**所有内容开放，可以整套装，也可以只拿一部分。** 每个模块自带协议内核，单独拷出任何一个都能独立工作。

---

## 如何安装

### 方式一：Claude 插件安装（claude.ai / Claude 桌面版 / Cowork，推荐）

本仓库自带 `.claude-plugin/marketplace.json`，可以直接作为 Claude 插件市场添加，31 个 Skill 打包成一个插件 `afa`，之后在 Claude 里一键更新。

1. 打开 Claude 左侧 **Customize → Plugins**
2. 点 **Add → Add marketplace → Add from a repository**，填 `afadtc/afa-dtc-skills`
3. 在市场里找到 **afa** 插件，点 **Add**

安装后，插件里的 31 个 Skill 会同时出现在 claude.ai 网页、Claude 桌面版、Cowork 和登录同一账号的 Claude Code 中。

### 方式二：Claude Code 命令行

```shell
claude plugin marketplace add afadtc/afa-dtc-skills
claude plugin install afa@afa-dtc-skills
```

### 方式三：npx 一键安装（Cursor / Codex / Cline 等其他 Agent）

```shell
npx skills add afadtc/afa-dtc-skills
```

### 方式四：手动安装

```shell
git clone https://github.com/afadtc/afa-dtc-skills.git
```

将 `skills/` 下的模块目录复制到 `~/.claude/skills/` 或项目的 `.claude/skills/` 目录下即可。每个模块自带协议内核，单独拷出任何一个都能独立工作。

## 如何更新

- **Claude 插件方式**：在 **Customize → Plugins** 里对 `afa` 插件执行一次更新即可
- **Claude Code 命令行**：`claude plugin marketplace update afa-dtc-skills`，然后 `claude plugin update afa@afa-dtc-skills`
- **npx 方式**：重新运行安装命令即可，安装和更新用同一条命令：`npx skills add afadtc/afa-dtc-skills`

## 装好后，第一句话说什么

不用记任何命令，直接说人话，系统自动路由：

| 你说 | 系统会做什么 |
|---|---|
| "我想做独立站，还什么都没有" | 从零起步工作流：市场验证 → 竞品 → 定位 → 产品 → 上市 |
| "我想做一件代发，先开个测试店快速测品" | 测试店快速测品工作流：赢品验证 → 48 小时上线 → Day-0 冷启动测试 → 赢家再品牌化 |
| "ROAS 从 3 掉到 1.8 了" | 全链路诊断：先拆漏斗定位病灶，再给带优先级的处方 |
| "黑五怎么准备" | 大促备战：产品策略 + 广告 + 落地页 + 邮件短信三线并行 |
| "帮我算这个 SKU 的真实利润" | 运行单位经济脚本，六层成本（含关税）逐层拆给你 |
| "Stripe 把我的货款冻结了" | 支付风控引擎：冻结应对 SOP + 申诉材料清单 + 现金流预案 |
| "ChatGPT 里搜我这个品类，怎么才能被推荐" | AI 搜索可见度审计 + Agentic Commerce（ACP/UCP）接入评估 |

完整会话示例见 [`skills/examples/quickstart-and-sessions.md`](skills/examples/quickstart-and-sessions.md)。

---

## 从 v2.4.7 到 v2.7.7：变了什么，解决了什么

GitHub 上一版是 v2.4.7。这中间经历了 18 个版本、多轮独立终审和一轮四线盲审，311 个文件里改了 208 个、新增 41 个。概括成六件事：

### 1. 知识对齐到 2026，且句句有出处

v2.4.7 的平台知识停在 2025 上半年。现在所有平台功能类事实都带来源与核实日期（铁律 1），并设了集中复核窗口：

- **Meta**：Andromeda 检索层带来的"人从操盘手变 AI 监督者"范式、Advantage+ 默认化、详细定向降级为建议、归因口径收紧；28 天点击归因窗口早已下线，20% 文字规则早已废止——这类过时规则已从可选项里移除。
- **TikTok**：GMV Max 2026-07 起默认化、Smart+ 三档、Affiliate 机器。
- **Google**：AI Max for Search/Shopping、DSA → AI Max 迁移时间表、PMax 混合策略。
- **AI 渠道**：ChatGPT 站内下单（OpenAI ACP + Stripe Instant Checkout）、Shopify Catalog + Google UCP、`llms.txt`、Alexa for Shopping / Gemini 购物——`afa-geo` 从"AI 搜索可见度"升级为"从被引用到被购买"。
- **消息合规**：Gmail/Yahoo/Microsoft 批量发件人门槛（Microsoft 2025-05-05 起执行）、Apple Intelligence 邮件摘要对首屏文案的影响、10DLC 前置、TCPA 2025-26 时间线、RCS。
- **关税新常态**：美国 $800 de minimis 2025-08-29 全面终止、EU €150 免税 2026-07 起分阶段取消——关税进入单位经济六层成本的 L2 层，`afa-scale` 的运营准备度加了第七维"关税与合规韧性"。
- **支付**：Visa VAMP 2026-04-01 起合并阈值 2.20% → 1.50%，口径、罚金、宽限期全部带源。

### 2. 新增三块能力

- **`afa-payments` 支付风控引擎**（新 Worker，挂 `afa-scale`）：争议率内部预警带、VAMP 自查脚本、按 reason code 分型的 chargeback 证据包、Stripe/PayPal 冻结"黄金 72 小时"SOP、Rolling Reserve 现金流可复算推演、支付组合与 BNPL。
- **`afa-sms` 升格为消息营销引擎**：新增 WhatsApp/RCS 分册（模板/会话双轨、24h 窗口、两套合规体系互斥警示），与邮件、SMS 三渠道瀑布抑制强制对齐。
- **测试店快速测品体系**（v2.7.7）：此前 dropshipping 在系统里只是各模块降级分支的一句话，现在有了端到端链路——赢品五标准 + 四排除、三层零广告费验证漏斗、AI 整页改写 SOP、信任基建包、测品 Offer 工程（含 50% 混合毛利校验算术）、四种广告形态分类学、静态图生产线、Day-0 冷启动结构与双档预算、产品级 Kill / Iterate / Scale 出口，以及赢家回接品牌化的完整闭环。这条"产品 → 定位"的测试路径与原有"定位 → 产品"的品牌路径互为镜像。

### 3. 会算数了：11 个纯 Python 脚本

v2.4.7 只有文字框架。现在 6 个业务计算脚本（单位经济含关税、A/B 样本量、促销盈亏平衡、VAMP 争议率自查、多关税情景落地成本、订单 CSV 一键生成经营自基准画像）+ 1 个记忆运维脚本 + 4 个工程/评测脚本，零第三方依赖，全部"脚本优先、文字回退"——没有代码执行环境也能用文字框架兜底。顺带抓出一个真 bug：旧的折后毛利公式写成 `m − d`，正确应为 `(m − d) / (1 − d)`，60% 毛利 / 15% 折扣下系统性低估约 10 个百分点，已修正。

### 4. 系统工程化：能自检、拆得开

- **协议内核注入**：`afa/_system/kernel.md` 是唯一真源，`scripts/build_inject.py` 幂等注入到 31 个 SKILL.md——十一条铁律、completion 四状态码、五个不可丢字段、display_name 规则、数据完备度三级、四段式输出。**单模块安装即自含协议**。
- **四道门禁**：死链/版本/代号/§锚点扫描（`repo_lint.py`）+ 内核同步校验 + 54 条路由评测（含英文问句）每次提交自动跑（GitHub Actions）；发版另有 `release_check.py` 对发布 zip 的解压本体复检。死链从 288 条清到 0，正文历史版本串清零，§锚点悬空从人工排查变成机器拦截。
- **描述三层重构**：Worker 收窄到区分性触发词，Supervisor 去重，Hub 持综合触发词，修正三重触发倒挂；补齐英文触发短语。
- **基准数据治理**：每张基准表必带"来源 + 采集窗口 + 适用地区"三字段，写不出来源的一律如实标"内部经验估算"；硬阈值只用于路由分诊，深度诊断一律用你自己的数据建基准线。
- **多轮独立终审**（v2.7.2 → v2.7.6）累计修复 300 余条问题：跨文件红线漂移（频次、扩量幅度、弃购 Email/SMS 先后、打开率分母、争议率口径……）按"对齐真源"或"分层互认 + 双向口径注"二择一收口；HHI 双量纲致触发器永不命中、ICE 0-10 与 0-100 双尺度并存等结构性矛盾清零。v2.7.7 另做四线盲审（真源一致性 / 协议与路由 / 内容逻辑与合规 / 工程卫生），采纳 71 项后发版。

### 5. 记得住：Brand Brain 记忆系统升级

`learnings.jsonl` 固化为八字段协议（时间戳、来源模块、类型、键、洞察、置信度、来源、关联文件），读取时按模块过滤、失效检测、按键去重、30 天衰减、Top5 截断；连续 3 次命中的教训触发"晋升"建议固化到品牌档案。每次对话都建立在上次的积累上。

### 6. 上手即有用：包内 README + 示例

10 分钟上手指南、三段黄金示例会话（从零起步 / ROAS 下滑诊断 / 黑五备战）、一份可直接复制的 brand-brain 示例目录（含 5 条真实样式的 learnings）。

逐版本明细见 [`CHANGELOG.md`](CHANGELOG.md)。

---

## 系统架构

```
L0  Hub          afa ─── 系统入口 · 一级路由 · 12 条预设工作流编排
                  │
                  ├── afa-diagnose ─── 全局诊断引擎（直接向 Hub 汇报）
                  ├── afa-dashboard ── 全局数据中枢（直接向 Hub 汇报，附经营快照脚本）
                  │
L1  Supervisors   ├── afa-foundation ─── 品牌与产品基建中枢
                  │     └─ explore / compete / brand / product / launch
                  │
                  ├── afa-paid ───────── 付费获客中枢
                  │     └─ creative / fb / gg / tt
                  │
                  ├── afa-organic ────── 有机增长中枢
                  │     └─ seo / social / influencer / pr / geo（AI 搜索 + Agentic Commerce）
                  │
                  ├── afa-monetize ───── 变现与留存中枢
                  │     └─ convert / cx / retain / aov / email / sms（+ WhatsApp/RCS 分册）
                  │
L2  Workers       └── afa-scale ──────── 运营与扩张中枢
                        └─ ops / expand / payments
```

### 三层是什么意思

| 层级 | 角色 | 做什么 |
| --- | --- | --- |
| **L0 Hub** | `afa` | 系统入口。接收用户请求，判断意图，路由到对的 Supervisor 或全局引擎。编排跨组工作流。 |
| **L1 Supervisor** | 5 个中枢 | 二级路由。把 Hub 分配来的任务再派发给具体 Worker，协调多 Worker 串联，回收结果。 |
| **L2 Worker** | 23 个执行引擎 + 2 个全局引擎 | 干活的。每个 Worker 专注一个领域，有自己的方法论、参考库、工作模式，部分带计算脚本。 |

**关键规则**：Hub 不直接调用 Worker，Worker 不直接跨组调用其他 Worker。严格分层，越界请求走回交链路（`out_of_scope`）重路由。31 = 1 Hub + 5 Supervisor + 25 Worker 层模块。

---

## 工具箱

### 🔀 Hub（系统入口）

| 模块 | 做什么 |
| --- | --- |
| `afa` | 主入口，一级路由器。接收任何 DTC 问题，自动路由到对的模块；编排 12 条预设工作流；检测品牌阶段、健康状态、供应链模式、季节阶段、危机模式 |

### 🔍 全局引擎（直接向 Hub 汇报）

| 模块 | 做什么 |
| --- | --- |
| `afa-diagnose` | 全链路诊断与归因。Stage 0 问题具体化引擎、三阶段诊断法（框架拆解 → 数据索取 → 终判，绝不跳步下结论）、8 大维度、四维溢价路由、ICE/RICE 优先级引擎 |
| `afa-dashboard` | 数据仪表盘与体检。三层看板、北极星指标罗盘、五级自定义基准（用户目标 → 历史最优 → 环比 → 盈亏平衡 → 无基准）、三层异常检测；`metrics_snapshot.py` 把订单 CSV 变成自基准画像 |

### 🏗️ afa-foundation — 品牌与产品基建中枢

| Worker | 做什么 |
| --- | --- |
| `afa-explore` | 用户洞察与市场探索。VOC 挖掘、球形扩展角度生成、意识五级映射、市场机会评估、趋势监控；**赢品验证（测试店模式）**：五标准 + 四排除、三层零广告费验证漏斗 |
| `afa-compete` | 竞争情报。竞争格局扫描、五维深度拆解、广告逆向工程、价格监控自动化、对标五重过滤法；**单店广告信号学**（测品逐品决策） |
| `afa-brand` | 品牌定位与识别。定位画布、12 原型、五维语调光谱、StoryBrand 故事、视觉识别系统、品牌健康审计、品牌规范文档生成 |
| `afa-product` | 产品策略。机会解决方案树、四维溢价阶梯、COGS 五桶与定价建模、寻源与供应链（PPI/DPI/PSI）、产品组合矩阵、上市检查清单 |
| `afa-launch` | 产品上市与冷启动。四阶段启动计划、MVP 消息测试三级裁决、PMF 四维评分、预算计算器；**测品快速通道**（48 小时上线清单 + 产品级 Kill/Iterate/Scale 出口） |

### 💰 afa-paid — 付费获客中枢

| Worker | 做什么 |
| --- | --- |
| `afa-creative` | 创意生产与测试。品牌视觉套件、4×3 广告测试矩阵、五层 Prompt 约束模型与反 AI 塑料感指南、Reali-TEA UGC 脚本、平台规格；**测品广告手册**（四种广告形态分类学 + 静态图生产线 + AI 工具编排） |
| `afa-fb` | Meta 广告优化。Andromeda 时代的信号整合账户结构、ASC 启动与扩展、20% 扩量纪律、CPM-CTR-CVR 诊断链、CAPI 追踪、账户健康；**Day-0 冷启动测试结构**（双档预算、增强全关、产品级出口） |
| `afa-gg` | Google Ads 优化。PMax + 标准购物五策略、AI Max for Search、RSA、Feed 五自定义标签、Merchant Center 封号预防与解封 SOP、GA4/增强型转化 |
| `afa-tt` | TikTok 广告优化。15 大 Hook 公式、7 大原生格式、TikTok Shop 与 GMV Max 策略、Affiliate 机器、Spark Ads、四阶段扩量 |

### 🌱 afa-organic — 有机增长中枢

| Worker | 做什么 |
| --- | --- |
| `afa-seo` | SEO 与有机搜索增长。主题集群、技术 SEO、关键词六圈扩展、PDP/分类页优化、程序化 SEO、数字公关外链、国际 SEO |
| `afa-social` | 社交内容与 UGC。四大内容支柱、15 个高转化内容原型、TikTok SEO 三信号层、UGC 管理与授权、有机转付费管道、社区飞轮 |
| `afa-influencer` | 网红与联盟营销。Seeding 财务可行性前置检查、3C 评估模型、4P 薪酬模型、联盟七步构建、FTC 披露与 IP 授权 |
| `afa-pr` | 品牌公关与声誉管理。CPR 冷推、内容原子化、UGC × PR 协同、声量监控与三级危机响应、品牌保护、媒体套件 |
| `afa-geo` | AI 搜索可见度与 Agentic Commerce。AI 可见度审计、SOAIV 指标、内容结构重塑、技术拦截排查；**ACP/UCP 双协议决策树、Instant Checkout、Shopify Catalog、`llms.txt`、LLM Visibility Score** |

### 💎 afa-monetize — 变现与留存中枢

| Worker | 做什么 |
| --- | --- |
| `afa-convert` | 全链路转化率优化。12 模块审计、落地页 12 模块、PDP 九段式、结账八大原则、个性化五级成熟度、A/B 样本量脚本；**AI 产品页整页改写 SOP + dropshipping 信任基建包** |
| `afa-cx` | 客户体验与服务智能。六阶段旅程映射、工单偏转优先级评分、三层自助服务、物流静默期防御、T-A-S-C 危机沟通、退货体验工程 |
| `afa-retain` | 用户留存与 LTV 增长。RFM + JTBD + LTV 整合 11 大客群、流失风险评分模型、六阶段生命周期、订阅双轮防流失、忠诚度与召回体系、群组分析 |
| `afa-aov` | 客单价提升与利润优化。众数 AOV 门槛工程、三大捆绑模型与混合毛利计算、全链路 Upsell、弃单挽回的 AOV 保护、促销盈亏平衡脚本；**测品 Offer 工程**（Offer 即护城河 + 50% 毛利校验） |
| `afa-email` | 邮件营销。五大核心 Flow 拓扑、AIDA/PAS/BAB 文案公式、Apple Intelligence 首屏重写、批量发件人合规清单、零方数据分层、BFCM 五阶段 |
| `afa-sms` | 消息营销（SMS + WhatsApp/RCS 分册）。HVUC 文案公式、Flow 优先级瀑布、对话式 SMS、10DLC/TCPA 合规、三渠道编排与抑制、WhatsApp 模板/会话双轨 |

### 🚀 afa-scale — 运营与扩张中枢

| Worker | 做什么 |
| --- | --- |
| `afa-ops` | 运营与供应链优化。真实 COGS 六层模型（含关税）、3PL 评估矩阵、库存 ABC×XYZ、供应链风险映射、团队四阶段、自动化蓝图、CCC；**dropshipping 供应商三分法与升级阶梯** |
| `afa-expand` | 渠道扩张与多元化。MEURO 五维渠道评估、HHI 渠道集中度、关税新常态手册、多关税情景落地成本脚本、Marketplace 入驻、批发定价、国际化合规、趋势时间差套利 |
| `afa-payments` | 支付风控。VAMP 争议率自查、chargeback 四大家族证据包与反驳信骨架、Stripe/PayPal 冻结黄金 72 小时 SOP、Rolling Reserve 现金流推演、支付组合与 BNPL、欺诈过滤 |

---

## 工具路径图

### 一级路由（Hub → Supervisor / 全局引擎）

| 用户意图 | 路由到 |
| --- | --- |
| 数据不好看、指标异常、为什么下降了、诊断 | afa-diagnose |
| 看数据、数据体检、指标画像、仪表盘 | afa-dashboard |
| 选品、竞品、品牌定位、产品策略、新品上市 | afa-foundation |
| 测品、测试店、一件代发快速跑品 | afa-foundation（启动测试店快速测品工作流，多中枢协同） |
| 广告、投放、ROAS、素材、Meta/Google/TikTok Ads | afa-paid |
| SEO、内容营销、社交媒体、网红、公关、AI 搜索 | afa-organic |
| 转化率、留存、复购、邮件、SMS、WhatsApp、客单价、客户体验 | afa-monetize |
| 供应链、运营、渠道扩展、跨国、亚马逊、批发、支付冻结、争议率 | afa-scale |

### 二级路由（Supervisor → Worker）

**afa-foundation →** 选品/市场机会/赢品验证 → explore ｜ 竞品分析 → compete ｜ 品牌定位/故事 → brand ｜ 产品策略/定价 → product ｜ 新品上市/冷启动/测品快速通道 → launch

**afa-paid →** 广告素材/创意/脚本 → creative ｜ Meta/Instagram 广告 → fb ｜ Google/Shopping/PMax → gg ｜ TikTok 广告/TikTok Shop → tt

**afa-organic →** SEO/关键词 → seo ｜ 社交媒体/UGC/社群 → social ｜ 网红/KOL → influencer ｜ 公关/媒体 → pr ｜ AI 搜索/GEO/ChatGPT 下单 → geo

**afa-monetize →** 转化率/落地页 → convert ｜ 客户体验/售后 → cx ｜ 复购/留存 → retain ｜ 客单价/追加销售 → aov ｜ 邮件 → email ｜ 短信/WhatsApp/RCS → sms

**afa-scale →** 供应链/物流/库存 → ops ｜ 新渠道/亚马逊/批发/跨国 → expand ｜ 争议率/chargeback/冻结/VAMP → payments

### 12 条预设工作流

| # | 工作流 | 适用场景 | 执行链路 |
| --- | --- | --- | --- |
| 1 | **从零起步** | 什么都还没有 | explore → compete → brand → product → launch |
| 2 | **增长瓶颈突破** | 数据不好看，不知道卡在哪 | diagnose → 按 ICE 优先级执行 → dashboard 验证 |
| 3 | **广告体系搭建** | 要开始投广告了 | brand 确认 → creative → fb/gg/tt → convert 配合 |
| 4 | **留存体系搭建** | 复购太低，LTV 上不去 | retain → email → sms → aov |
| 5 | **内容营销体系** | 想做有机增长 | seo → geo → social → creative 配合 |
| 6 | **品牌升级** | 品牌老了，要重新定位 | compete → brand → creative + convert 配合 |
| 7 | **大促备战** | BFCM / 大促前准备 | product + creative → fb+gg+tt → convert+email+sms（三组并行） |
| 8 | **渠道扩展** | 想拓展新渠道 | expand 评估 → 按结果路由到对应 Supervisor |
| 9 | **紧急止血** | 现金流告急 | 按资产有无分支到 monetize/foundation/paid（建议性，不强制） |
| 10 | **Level 0 引导** | 完全没方向 | 方向梳理 → explore → 进入从零起步 |
| 11 | **溢价能力构建** | 想提高利润率 | product 四维评估 → 按 Tier 路由到不同模块 |
| 12 | **测试店快速测品** | 一件代发，先跑出能卖的产品 | foundation（explore 赢品验证 + compete 配合 → launch 测品快速通道）→ monetize（convert 整页改写 → aov 测品 Offer）→ paid（creative 静态图 → fb Day-0 冷启动 → 判读）→ 赢家 → scale（Dropshipping→DTC 过渡）→ 接回品牌路径 |

工作流 1 与工作流 12 互为镜像：一个是"定位 → 产品"的品牌路径，一个是"产品 → 定位"的测试路径，终点相同。

### 跨组协同

- 广告体系搭建时，`afa-paid` 会先拉 `afa-brand` 确认品牌定位，投放后拉 `afa-convert` 优化落地页
- 大促备战时，`foundation`、`paid`、`monetize` 三个 Supervisor 并行协同
- 测品工作流中，判读规则只在 `afa-launch` 定义、只由 `afa-paid` 执行回传，页面与 Offer 由 `afa-monetize` 承接——每一跳都有承接定义，不存在断链
- 任何模块遇到超出职责的请求，通过回交链路上报，Hub 重新路由——不会自作主张

---

## 数据流转

### Brand Brain — 模块间的数据总线

上游模块写入的文件自动成为下游模块的输入：

```
afa-explore → 赛道机会评估 / 赢品验证（写入 products.md + audience.md 最小测品档案）
    ↓
afa-compete → competitors.md（竞品情报）
    ↓
afa-brand → brand-master.md + voice-and-tone.md
    ↓
afa-product → products.md
    ↓
afa-launch → 上市计划（消费以上所有文件；测品模式只要求最小测品档案）
```

Brand Brain 共 20 个文件、三类权限（可覆写的 Profile / 只追加的 assets 与 learnings / 冻结的 stack、guardrails、objections），新鲜度分级（<7 天直用、7-30 天标注、30-90 天摘要、>90 天提醒刷新），冲突检测禁止静默覆盖。

### learnings.jsonl 八字段

`ts` / `worker` / `type`（pitfall · pattern · preference · error · correction · promoted）/ `key` / `insight` / `confidence`（1-10）/ `source`（observed · user-stated · error-recovery）/ `related_files`。加载时按模块过滤 → 失效检测 → 按键去重 → 30 天衰减（每 30 天 −1 分，<3 丢弃）→ Top5；连续 3 次命中触发晋升建议。`afa/_system/scripts/memory_manager.py` 负责。

---

## 会算数：11 个纯 Python 脚本（零第三方依赖）

以下路径相对仓库的 `skills/` 目录。

| 脚本 | 做什么 |
| --- | --- |
| `afa-ops/scripts/unit_economics.py` | 真实单位成本六层模型（含关税 L2）→ 贡献利润、盈亏平衡 CPA |
| `afa-expand/scripts/landed_cost.py` | 多关税情景落地成本对比 + 关税每 +1pp 的单件敏感度 |
| `afa-aov/scripts/promo_breakeven.py` | 促销盈亏平衡销量增幅；bundle 模式校验混合毛利（PASS ≥60 / WARN 50-60 / FAIL <50） |
| `afa-convert/scripts/ab_sample_size.py` | 两比例 z 检验样本量与所需天数（小数误用防呆） |
| `afa-payments/scripts/vamp_check.py` | VAMP 争议率三级预警（预警带 0.65-0.9% / 接近 / 超标）+ 估算月罚金 |
| `afa-dashboard/scripts/metrics_snapshot.py` | 订单 CSV → GMV/AOV 趋势、新客复购结构、30/60/90 天复购、cohort 三角 |
| `afa/_system/scripts/memory_manager.py` | learnings.jsonl 加载：过滤 / 失效 / 去重 / 衰减 / 截断 |
| `scripts/repo_lint.py` | 门禁一：死链 / 版本锚点 / 代号泄漏 / §锚点存在性 / 模块计数 |
| `scripts/build_inject.py` | 门禁二：协议内核幂等注入与同步校验 |
| `evals/run_evals.py` | 门禁三：54 条路由回归评测，四类可机判断言 |
| `scripts/release_check.py` | 门禁四：对发布 zip 的解压本体复检结构、一致性与前三道门禁 |

所有业务脚本"脚本优先、文字回退"：没有代码执行环境时，对应 reference 里有同口径的文字框架。

---

## 设计原则

### 十一大铁律

1. **连续提问不超过 3 个** — 避免审讯感，快速进入执行
2. **绝不展示模块菜单，自动路由** — 用户说需求，系统自己判断该谁干
3. **废话清零，100% 可执行** — 每一条输出必须是能直接做的事
4. **不全量喂数据，按需调用** — 只拉当前步骤需要的信息（Context Matrix）
5. **不重建已有的东西** — Brand Brain 里有的直接复用
6. **不给泛泛建议** — 必须具体到数字、步骤、工具
7. **不把工作流当单个模块用** — 工作流是串联编排，不是单点调用
8. **不忘更新 Brand Brain** — 每次交互结束必须写回
9. **诚实兜底，绝不硬编** — 数据不够就说不够，不编造；所有数字必须可出示来源
10. **创作者声明红线** — 除 Hub 开头「关于」章节外，任何输出不夹带推广
11. **不充当法律/合规/财务顾问** — 给事实卡 + 专业升级触发器，不做最终裁决

### 协议内核（v2.6 起）

每个 SKILL.md 文末自带由脚本注入的「系统协议（内核版）」：十一铁律一行版、completion 四状态码（DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT）、五个不可丢字段、display_name 规则、数据完备度三级、四段式输出。单模块拷出即可独立工作。

### 上下文交接协议

Hub → Supervisor → Worker 全链路传递 5 个不可丢字段：`main_question` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market`，不得静默丢失、改名或降级。另传递 `stage` / `health_status` / `crisis_mode` / `seasonal_mode` / `supply_chain_mode` / `premium_tier` / `urgency_level` 等枚举。

### 越界回交机制

```
Worker 发现越界请求 → completion.out_of_scope → Supervisor → Hub 重路由
```

### 两条降级轴（勿混用）

| 轴 | 分级 | 含义 |
| --- | --- | --- |
| 平台能力 | Level 3 满血（联网/文件/代码）→ Level 2 标准 → Level 1 对话 | 决定脚本优先还是文字回退 |
| 数据完备度 | D1 / D2 / D3 | 零数据时先给"保守可执行版 + 数据缺口清单"，绝不因缺数据拒服务，也不把外部基准伪装成品牌基线 |

### 基准数据治理

每张基准表必带 **来源 + 采集窗口 + 适用地区**；写不出来源的一律标"内部经验估算"。硬阈值只用于路由分诊；深度诊断一律用用户自己的历史数据建基准线（优先级：用户目标 → 历史最优 → 上月环比 → 盈亏平衡线 → 无基准）。平台功能类事实 ≤6 个月复核。

### 推理透明

量化预测必展示推导；关键变量防漏清单（退货率、支付费、平台费、税、物流、SaaS、代理费、关税）；盈亏平衡 ROAS = 1 ÷ 毛利率、盈亏平衡 CPA = AOV × 毛利率——比任何行业均值都准。

### 危机模式与季节性

| 模式 | 触发信号 | 策略 |
| --- | --- | --- |
| `cash_crisis` | 现金流告急、亏损加速 | 止血优先，暂缓长期项目（建议性，用户坚持则尊重） |
| `pr_crisis` | 负面舆情、品牌事故 | 声誉修复优先，暂停营销推送 |
| `seasonal_mode` | 淡季 / 旺季备战 / 旺季 | 不把淡季波动误判为衰退；60/40 预算法则、永不 Go Dark |

### 成本标签（三轴）

每条建议标 💰 预算（零成本 / $0-500 / $500-2K / $2K-10K / $10K+）+ ⏱️ 时间 + 🔧 技能（自己能做 / 需学习 / 需外包）。**策略不分层**：绝不因卖家规模隐藏高价值策略，区别只在沟通风格和成本标签。

### 供应链模式感知

自动检测 dropshipping / wholesale / manufacturing / dtc，各模块"同建议池、不同排序"；用户明示一件代发或测试店即可判定，并在测品诉求下切换到测试店快速测品工作流。

---

## 工作模式明细

| 模块 | 工作模式 |
| --- | --- |
| afa | 12 条预设工作流（从零起步 / 增长瓶颈突破 / 广告体系搭建 / 留存体系搭建 / 内容营销体系 / 品牌升级 / 大促备战 / 渠道扩展 / 紧急止血 / Level 0 引导 / 溢价能力构建 / 测试店快速测品） |
| afa-diagnose | 全面体检 / 专项深诊 / 急诊 / 复诊 / 危机诊断 |
| afa-dashboard | 首次体检 / 周期复检 / 专项分析 / 实时异常响应 / NSM 模式 |
| afa-foundation | 从零起步 / 品牌升级 / 溢价能力构建 / 测试店快速测品 |
| afa-paid | 广告体系搭建 / 大促广告备战 / 素材迭代 / 测品冷启动 |
| afa-organic | 内容营销体系搭建 / 影响力构建 / 溢价支撑 |
| afa-monetize | 留存体系搭建 / 大促变现备战 / 转化漏斗修复 / 溢价变现 / 测品页面与 Offer |
| afa-scale | 渠道扩展 / 运营体系搭建 / Dropshipping→DTC 过渡（含运营准备度七维评估） |
| afa-explore | VOC 挖掘 / 角度生成 / 市场机会评估 / 诊断 / 趋势与信号监控 / 客户深度访谈 / 赢品验证（测试店） |
| afa-compete | 竞争格局扫描 / 深度竞品拆解 / 对标学习与差异化借鉴 / 竞品监控与季节性策略（含单店广告信号学） |
| afa-brand | 品牌定位构建 / 品牌声音构建 / 品牌故事构建 / 视觉识别构建 / 品牌健康审计 / 品牌规范文档生成 |
| afa-product | 产品发现与验证 / 溢价与定价 / 产品诊断 / 产品组合与供应链 / 产品上市检查清单 |
| afa-launch | 完整启动规划 / 启动诊断 / PMF 评估 / 创意测试方案 / 预算规划 / 测品快速通道 |
| afa-creative | 品牌视觉基建 / 广告测试矩阵 / 社媒资产包 / Reali-TEA 脚本 / 单点视觉突破 / 胜者迭代（含测品广告手册） |
| afa-fb | 账户架构 / 广告创建 / 广告诊断 / 受众策略 / 预算扩量 / 追踪归因 / 账户健康（含 Day-0 冷启动测试） |
| afa-gg | 账户架构 / 广告创建 / 诊断优化 / 扩量 / GEO / PMax / Feed / 追踪 |
| afa-tt | 账户架构 / 创意策略 / 诊断 / TikTok Shop 运营（GMV Max）/ 联盟 / 扩量 |
| afa-seo | SEO 全站审计 / 关键词研究与主题规划 / 页面级内容优化 / 流量诊断与恢复 / 内容策略规划 / 国际 SEO 规划 |
| afa-social | 全盘社交内容策略 / UGC 项目启动与管理 / 爆款脚本工程 / 有机转付费管道 / 大促内容日历 / 社区飞轮构建 |
| afa-influencer | 创作者发现与筛选 / 冷拓展与邀约 / 创作者内容简报 / 联盟计划设计 / 渠道诊断与优化 / 社区飞轮与品牌倡导者培育 |
| afa-pr | 媒体冷推策划 / UGC 飞轮构建 / 危机预警与响应 / 品牌资产保护 / 媒体套件生成 |
| afa-geo | AI 可见度审计 / 内容结构重塑 / 跨市场搜索信号输入 / Agentic Commerce 接入 |
| afa-convert | 全链路转化审计 / 落地页架构设计 / PDP 深度优化 / CRO 增长飞轮 / 结账流程优化 / 微转化漏斗分析（含 AI 整页改写 SOP） |
| afa-cx | 旅程映射 / 工单智能分析 / 自助服务内容建设 / 情感分析 / CX 自动化 / 退货体验优化 |
| afa-retain | 留存体检 / 生命周期架构 / 忠诚度计划设计 / 订阅防流失 / 召回体系 |
| afa-aov | 门槛设计 / 捆绑包构建 / 促销利润模拟 / 全链路 Upsell / 订阅 AOV 优化（含测品 Offer 工程） |
| afa-email | 自动化流构建 / Campaign 文案撰写 / 可交付性修复 / 邮件日历规划 |
| afa-sms | Flow 架构设计 / Campaign 文案撰写 / 渠道诊断 / SMS×Email 协同规划（+ WhatsApp/RCS 分册） |
| afa-ops | 单位经济审计 / 库存健康检查 / 履约优化 / 客服运营 / 团队架构规划 / 自动化蓝图 / 供应链风险评估 |
| afa-expand | 渠道评估（MEURO）/ Marketplace 入驻 / 批发计划 / 国际化规划 / 线下 Pop-up / 渠道健康审计 |
| afa-payments | 争议率健康与 VAMP 自查 / chargeback 反驳 SOP / 冻结应对 / 支付组合与欺诈过滤 |

---

## 模块全览

| # | 模块 | 层级 | 上级 | 参考库文件 | 脚本 |
| --- | --- | --- | --- | --- | --- |
| 1 | afa | Hub | — | 5 references + 15 _system | memory_manager.py |
| 2 | afa-diagnose | 全局引擎 | Hub | 9 | — |
| 3 | afa-dashboard | 全局引擎 | Hub | 9 | metrics_snapshot.py |
| 4 | afa-foundation | Supervisor | Hub | — | — |
| 5 | afa-paid | Supervisor | Hub | — | — |
| 6 | afa-organic | Supervisor | Hub | — | — |
| 7 | afa-monetize | Supervisor | Hub | — | — |
| 8 | afa-scale | Supervisor | Hub | — | — |
| 9 | afa-explore | Worker | foundation | 12 | — |
| 10 | afa-compete | Worker | foundation | 11 | — |
| 11 | afa-brand | Worker | foundation | 12 | — |
| 12 | afa-product | Worker | foundation | 11 | — |
| 13 | afa-launch | Worker | foundation | 11 | — |
| 14 | afa-creative | Worker | paid | 17 | — |
| 15 | afa-fb | Worker | paid | 12 | — |
| 16 | afa-gg | Worker | paid | 12 | — |
| 17 | afa-tt | Worker | paid | 10 | — |
| 18 | afa-seo | Worker | organic | 13 | — |
| 19 | afa-social | Worker | organic | 11 | — |
| 20 | afa-influencer | Worker | organic | 11 | — |
| 21 | afa-pr | Worker | organic | 9 | — |
| 22 | afa-geo | Worker | organic | 10 | — |
| 23 | afa-convert | Worker | monetize | 11 | ab_sample_size.py |
| 24 | afa-cx | Worker | monetize | 11 | — |
| 25 | afa-retain | Worker | monetize | 11 | — |
| 26 | afa-aov | Worker | monetize | 12 | promo_breakeven.py |
| 27 | afa-email | Worker | monetize | 10 | — |
| 28 | afa-sms | Worker | monetize | 11 | — |
| 29 | afa-ops | Worker | scale | 10 | unit_economics.py |
| 30 | afa-expand | Worker | scale | 13 | landed_cost.py |
| 31 | afa-payments | Worker | scale | 3 | vamp_check.py |

---

## 知识库

知识库由 277 个方法论、框架、案例库与模板文件组成，每个 Worker 的 `references/` 目录都可以独立使用。

**afa-foundation 组（57 个）**

- **afa-explore（12）**：voc-mining-playbook / spherical-scaling-system / awareness-mapping-guide / scamper-innovation-model / market-sizing-framework / advanced-models / advanced-strategies / core-paradigms / **winning-product-playbook** / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-compete（11）**：competitive-landscape-mapping / multi-dimensional-analysis / ad-intelligence / price-intelligence / seo-gap-analysis / benchmarking-playbook / core-frameworks / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-brand（12）**：positioning-frameworks / voice-architecture-guide / voice-building-sop / storytelling-playbook / visual-identity-system / brand-audit-toolkit / competitive-brand-analysis / archetype-deep-dive / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-product（11）**：product-discovery-framework / cogs-and-pricing-model / product-portfolio-matrix / sourcing-and-supply-chain / differentiation-playbook / product-launch-checklist / core-frameworks / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-launch（11）**：launch-timeline-template / cross-channel-launch-playbook / core-frameworks / diagnostic-decision-trees / pmf-assessment-template / mvp-testing-playbook / creative-brief-template / budget-calculator / failure-postmortem-template / work-modes-and-templates / anti-patterns

**afa-paid 组（51 个）**

- **afa-creative（17）**：brand-kit-template / typography-guide / reali-tea-scripting / product-visual-system / copywriting-frameworks / prompt-engineering / ad-testing-matrix / platform-specs / content-policy / visual-intelligence / seasonal-creative-calendar / **dropshipping-ads-playbook** / core-frameworks / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-fb（12）**：core-frameworks / audience-strategy / creative-templates / planning-and-budget / scaling-sop / tracking-setup / account-health / **day-zero-testing** / benchmark-data / diagnostic-rules / work-modes-and-kpi / anti-patterns
- **afa-gg（12）**：search-ads-playbook / pmax-playbook / feed-optimization / planning-and-budget / tracking-and-feed / shopify-google-setup / core-frameworks / benchmark-data / diagnostic-rules / work-modes-and-kpi / report-templates / anti-patterns
- **afa-tt（10）**：account-setup-sop / creative-templates / tiktok-shop-playbook / affiliate-playbook / scaling-sop / core-frameworks / benchmark-data / diagnostic-rules / work-modes-and-templates / anti-patterns

**afa-organic 组（54 个）**

- **afa-seo（13）**：technical-seo-checklist / keyword-research-engine / pdp-seo-optimizer / collection-page-seo / content-engine-playbook / link-acquisition-playbook / international-seo-guide / geo-aeo-playbook / core-frameworks / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-social（11）**：core-frameworks / content-archetypes-library / platform-playbooks / content-calendar-template / ugc-management-system / organic-to-paid-pipeline / community-flywheel / social-commerce-kpis / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-influencer（11）**：core-frameworks / influencer-vetting-framework / outreach-playbook / compensation-models / affiliate-program-guide / compliance-and-risk / benchmark-data / community-flywheel / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-pr（9）**：core-frameworks / cpr-pitching-playbook / ugc-community-flywheel / crisis-monitoring-response / brand-protection-toolkit / media-kit-templates / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-geo（10）**：core-frameworks / ai-visibility-audit / geo-optimization-playbook / **agentic-commerce-playbook** / geographic-arbitrage-guide / landed-cost-calculator / trade-compliance-toolkit / diagnostic-system / work-modes-and-templates / anti-patterns

**afa-monetize 组（66 个）**

- **afa-convert（11）**：core-frameworks / audit-checklist / landing-page-playbook / personalization-playbook / ab-testing-playbook / **ai-page-rewrite-sop** / benchmark-data / diagnostic-system / work-modes-and-templates / report-templates / anti-patterns
- **afa-cx（11）**：core-frameworks / journey-mapping-framework / ticket-intelligence-system / self-service-content-engine / sentiment-analysis-playbook / cx-automation-toolkit / return-and-retention / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-retain（11）**：core-frameworks / cohort-analysis-guide / rfm-ltv-framework / loyalty-program-playbook / subscription-management / win-back-workflows / benchmark-data / diagnostic-system / work-modes-and-templates / report-templates / anti-patterns
- **afa-aov（12）**：core-frameworks / threshold-engineering / bundle-strategy / promotion-strategy / upsell-cross-sell / dynamic-pricing / cart-abandonment-recovery / aov-kpi-dashboard / benchmark-data / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-email（10）**：core-frameworks / core-flows-playbook / campaign-archetypes / copywriting-formulas / deliverability-checklist / email-design-guidelines / segmentation-guide / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-sms（11）**：core-frameworks / core-flows-playbook / copywriting-formulas / conversational-sms-guide / compliance-checklist / omnichannel-orchestration / campaign-calendar / **whatsapp-rcs-playbook** / diagnostic-system / work-modes-and-templates / anti-patterns

**afa-scale 组（26 个）**

- **afa-ops（10）**：core-frameworks / unit-economics-calculator / inventory-management-handbook / fulfillment-optimization-guide / customer-service-playbook / team-building-roadmap / automation-blueprint-collection / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-expand（13）**：core-frameworks / channel-economics-toolkit / marketplace-entry-playbook / wholesale-pricing-calculator / international-compliance-guide / pop-up-execution-playbook / new-digital-channels-guide / **tariff-new-normal-playbook** / trend-timing-arbitrage / landed-cost-calculator / diagnostic-system / work-modes-and-templates / anti-patterns
- **afa-payments（3）**：core-frameworks / **chargeback-evidence-playbook** / **freeze-response-sop**

**系统核心（Hub + 全局引擎，38 个）**

- **afa Hub（5 references + 15 _system）**：references：brand-brain-template / diagnostic-rules / routing-checklist / benchmark-data / case-library ｜ _system：kernel / iron-rules / context-matrix / interaction-protocol / degradation-rules / edge-cases / preamble / output-format / reasoning-rules / localization-rules / cost-tag-spec / brand-memory-protocol / **benchmark-governance** / reference-authoring-rules / skill-directory
- **afa-diagnose（9）**：core-frameworks / diagnostic-frameworks / industry-benchmarks / diagnostic-system / diagnostic-cases / priority-scoring / work-modes-and-templates / diagnostic-templates / anti-patterns
- **afa-dashboard（9）**：core-frameworks / benchmark-database / nsm-playbook / diagnostic-system / anomaly-diagnosis-rules / data-driven-decision-loop / report-templates / work-modes-and-templates / anti-patterns

---

## 能自检：四道门禁

| 门禁 | 脚本（相对 `skills/`） | 查什么 | 何时跑 |
| --- | --- | --- | --- |
| 一 | `scripts/repo_lint.py skills` | 死链、历史版本串、代号泄漏、§锚点存在性、模块计数、description 预算 | 每次提交（GitHub Actions） |
| 二 | `scripts/build_inject.py skills --check` | 31 个 SKILL.md 的协议内核与 `kernel.md` 是否同步 | 每次提交 |
| 三 | `evals/run_evals.py skills` | 54 条路由用例：路由可达 / 五字段在位 / 无代号泄漏 / 带成本标签 | 每次提交 |
| 四 | `scripts/release_check.py <zip>` | 发布 zip 解压本体的结构（自动识别平铺 / 插件市场两种布局）、README/CHANGELOG 版本一致、learnings 协议、再复跑前三道 | 发版前 |

你的真实用例可以进入回归评测集：路由不准、内容过时，请开 [Issue](https://github.com/afadtc/afa-dtc-skills/issues) 附上原话与期望行为。

---

## 目录结构

```
afa-dtc-skills/
├── .claude-plugin/
│   ├── marketplace.json        # Claude 插件市场清单（发版时改 version，plugin.json 同步改）
│   └── plugin.json             # 插件 afa 的元数据
├── .github/workflows/lint.yml  # CI：三道门禁（根目录参数指向 skills）
│
├── skills/                     # 31 个模块 + 工具，模块间相对引用全部在此目录内闭合
│   ├── afa/                    # Hub — 系统入口与工作流编排
│   │   ├── SKILL.md
│   │   ├── _system/            # 协议内核、铁律、交接、降级、基准治理等（含 memory_manager.py）
│   │   └── references/         # 路由清单、诊断规则、案例库、Brand Brain 模板
│   ├── afa-diagnose/           # 全局诊断引擎
│   ├── afa-dashboard/          # 全局数据中枢（含 metrics_snapshot.py）
│   ├── afa-foundation/         # Supervisor: 品牌与产品基建
│   │   （Workers：afa-explore / afa-compete / afa-brand / afa-product / afa-launch）
│   ├── afa-paid/               # Supervisor: 付费获客
│   │   （Workers：afa-creative / afa-fb / afa-gg / afa-tt）
│   ├── afa-organic/            # Supervisor: 有机增长
│   │   （Workers：afa-seo / afa-social / afa-influencer / afa-pr / afa-geo）
│   ├── afa-monetize/           # Supervisor: 变现与留存
│   │   （Workers：afa-convert / afa-cx / afa-retain / afa-aov / afa-email / afa-sms）
│   ├── afa-scale/              # Supervisor: 运营与扩张
│   │   （Workers：afa-ops / afa-expand / afa-payments）
│   ├── examples/               # 10 分钟上手 + 三段示例会话 + brand-brain 示例
│   ├── evals/                  # 路由回归评测（54 条用例 + harness）
│   └── scripts/                # 门禁脚本：repo_lint / build_inject / release_check
│
├── CHANGELOG.md                # 全库唯一保留历史版本号的地方
├── LICENSE
└── README.md
```

31 个模块目录并列在 `skills/` 下（Supervisor 与其 Worker 的从属关系由路由定义，不是目录嵌套）。每个 Worker 模块包含 `SKILL.md`（模块定义、工作模式、执行规则、协议内核）、`references/`（方法论、案例、模板、基准数据），部分含 `scripts/`。

---

## 更新日志（摘要）

- **v2.7.7** — 测试店快速测品体系：4 个新 reference、Hub WF12、launch 模式 F、explore 模式 G、foundation/paid 工作流 D、monetize 工作流 E；五处口径收口；六类红线给出合规替代；两轮自查 + 四线盲审。
- **v2.7.2 – v2.7.6** — 六轮独立终审：208 条 A/B/C 级问题全量收口（记忆协议冲突、kernel 五字段、ICE/HHI 双量纲、Meta 28 天归因、HARO 关停、Microsoft 发件人新规等）；§锚点机检上线；`promo_breakeven` 折后毛利公式 bug 修正。
- **v2.7.1** — afa-messaging 并入 afa-sms（消息营销引擎，WhatsApp/RCS 分册）；模块 32 → 31；payments 边界四向闭合。
- **v2.7.0** — 产品化：包内 README、examples、afa-payments 补厚（chargeback 证据包、冻结 SOP）、WhatsApp Flows、`metrics_snapshot.py` 与 `landed_cost.py`。
- **v2.6 – v2.6.7** — 能力扩容 + 系统工程化：afa-geo Agentic Commerce、afa-payments 新 Worker、协议内核注入、description 三层重构、evals 首版、case-library 换血；七轮语义深检补丁。
- **v2.5** — 2024-2026 平台/法规时效补丁（Andromeda、GMV Max、AI Max、发件人新规、TCPA、关税新常态、VAMP）、首批计算脚本、CI 门禁、基准治理三字段。
- **v2.4.8** — 十六条文件级硬伤修复：PMF 评分统一、死链 288 → 2、历史版本串清零、`_system` 路径根治。
- **v2.4.7** — 模块执行管线重构、YAML frontmatter 路由元数据、内联诊断树、用户确认点、数据降级策略。
- **v2.4.6** — 初始公开版本。

逐条明细见 [`CHANGELOG.md`](CHANGELOG.md)。

---

## 许可证

本项目采用 [CC BY-NC 4.0](LICENSE) 许可证。

- **个人使用、学习、研究、非商业项目**：不需要署名，不需要申请
- **公开发布衍生作品**（文章、工具、课程等）：请注明来源
- **商业用途**：需要单独授权，请联系作者
