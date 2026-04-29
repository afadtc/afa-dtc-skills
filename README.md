# AFA DTC Skills

面向独立站与 DTC 品牌的全链路增长顾问 Skill 系统。30 个模块，三层架构，覆盖从市场洞察到规模化扩张的完整链路。

**最新版本：v2.4.6**

**作者**：1亿美刀站长阿发 · [小红书](https://xhslink.com/m/34JAVccyOdD) · [抖音](https://v.douyin.com/nSkhVHdGCrg/)

**所有内容开放，可以整套装，也可以只拿一部分。**

---

## 系统架构

AFA DTC Skills 不是一堆散装工具——它是一个三层架构的 AI 顾问系统：

```
L0  Hub          afa ─── 系统入口 · 一级路由 · 工作流编排
                  │
                  ├── afa-diagnose ─── 全局诊断引擎（直接向 Hub 汇报）
                  ├── afa-dashboard ── 全局数据中枢（直接向 Hub 汇报）
                  │
L1  Supervisors   ├── afa-foundation ─── 品牌与产品基建中枢
                  │     └─ explore / compete / brand / product / launch
                  │
                  ├── afa-paid ───────── 付费获客中枢
                  │     └─ creative / fb / gg / tt
                  │
                  ├── afa-organic ────── 有机增长中枢
                  │     └─ seo / social / influencer / pr / geo
                  │
                  ├── afa-monetize ───── 变现与留存中枢
                  │     └─ convert / cx / retain / aov / email / sms
                  │
L2  Workers       └── afa-scale ──────── 运营与扩张中枢
                        └─ ops / expand
```

### 三层是什么意思？

| 层级 | 角色 | 做什么 |
|:---|:---|:---|
| **L0 Hub** | `afa` | 系统入口。接收用户请求，判断意图，路由到对的 Supervisor 或全局引擎。编排跨组工作流。 |
| **L1 Supervisor** | 5 个中枢 + 2 个全局引擎 | 二级路由。把 Hub 分配来的任务再派发给具体 Worker，协调多 Worker 串联，回收结果。 |
| **L2 Worker** | 22 个执行引擎 | 干活的。每个 Worker 专注一个领域，有自己的方法论、参考库和工作模式。 |

**关键规则**：Hub 不直接调用 Worker，Worker 不直接跨组调用其他 Worker。严格分层，越界请求走回交链路。

---

## 工具箱

### 🔀 Hub（系统入口）

| 模块 | 做什么 |
|:---|:---|
| `afa` | 主入口，一级路由器。接收任何 DTC 问题，自动路由到对的模块 |

### 🔍 全局引擎（直接向 Hub 汇报）

| 模块 | 做什么 |
|:---|:---|
| `afa-diagnose` | 全链路诊断与归因。Stage 0 问题具体化引擎、"主治医师"——三阶段诊断法、8 大维度、四维溢价路由，输出行动处方 |
| `afa-dashboard` | 数据仪表盘与体检。三层看板，北极星指标追踪，异常预警 |

### 🏗️ afa-foundation — 品牌与产品基建中枢

| Worker | 做什么 |
|:---|:---|
| `afa-explore` | 用户洞察与市场探索。VOC 挖掘、市场机会评估、角度生成 |
| `afa-compete` | 竞争情报。竞争格局扫描、深度拆解、对标学习 |
| `afa-brand` | 品牌定位与识别。定位画布、声音架构、品牌故事、视觉识别、品牌健康审计、品牌规范文档生成 |
| `afa-product` | 产品策略。产品发现与验证、四维溢价评估、定价建模、产品组合优化、产品上市检查清单 |
| `afa-launch` | 产品上市与冷启动。完整启动规划、PMF 评估、预算规划 |

### 💰 afa-paid — 付费获客中枢

| Worker | 做什么 |
|:---|:---|
| `afa-creative` | 创意生产与测试。视觉套件、脚本文案、Prompt Engineering、广告测试矩阵、平台适配 |
| `afa-fb` | Meta 广告优化。账户结构、受众策略、创意文案、预算扩量、追踪归因 |
| `afa-gg` | Google Ads 优化。搜索广告、PMax、Shopping Feed、预算扩量 |
| `afa-tt` | TikTok 广告优化。账户设置、创意策略、TikTok Shop、联盟营销、扩量与预算 |

### 🌱 afa-organic — 有机增长中枢

| Worker | 做什么 |
|:---|:---|
| `afa-seo` | SEO 与有机搜索增长。全面审计、关键词研究、页面优化、内容策略、链接建设、国际 SEO |
| `afa-social` | 社交内容与 UGC。全盘策略、UGC 项目、爆款脚本、有机转付费管道、大促内容日历、社区飞轮 |
| `afa-influencer` | 网红与联盟营销。创作者筛选、触达合作、联盟计划、品牌大使 |
| `afa-pr` | 品牌公关与声誉管理。CPR 冷推、UGC 飞轮、危机响应、品牌保护、媒体套件生成 |
| `afa-geo` | AI 搜索可见度与本地化搜索。GEO/AEO 审计、引用机会挖掘 |

### 💎 afa-monetize — 变现与留存中枢

| Worker | 做什么 |
|:---|:---|
| `afa-convert` | 全链路转化率优化。审计、落地页优化、CRO 飞轮、结账优化 |
| `afa-cx` | 客户体验与服务智能。旅程映射、工单分析、自助服务内容建设、情感分析、CX 自动化、退货体验优化 |
| `afa-retain` | 用户留存与 LTV 增长。留存体检、生命周期管理、忠诚度、订阅防流失、召回体系 |
| `afa-aov` | 客单价提升与利润优化。门槛设计、捆绑包、促销利润模拟、全链路 Upsell、订阅 AOV 优化 |
| `afa-email` | 邮件营销。自动化流设计、Campaign 文案、可交付性诊断、邮件日历规划 |
| `afa-sms` | SMS 营销。自动化流架构、对话式 SMS、跨渠道协同、频率治理 |

### 🚀 afa-scale — 运营与扩张中枢

| Worker | 做什么 |
|:---|:---|
| `afa-ops` | 运营与供应链优化。单位经济审计、库存管理、履约优化、团队架构、自动化蓝图、供应链风险评估、财务运营优化 |
| `afa-expand` | 渠道扩张与多元化。渠道评估、Marketplace 入驻、批发、国际化、线下零售、渠道健康审计 |

---

## 工具路径图

### 路由逻辑

#### 一级路由（Hub → Supervisor / 全局引擎）

| 用户意图 | 路由到 |
|:---|:---|
| 数据不好看、指标异常、为什么下降了、诊断 | afa-diagnose |
| 看数据、数据体检、指标画像、仪表盘 | afa-dashboard |
| 选品、竞品、品牌定位、产品策略、新品上市 | afa-foundation |
| 广告、投放、ROAS、素材、Meta/Google/TikTok Ads | afa-paid |
| SEO、内容营销、社交媒体、网红、公关、AI 搜索 | afa-organic |
| 转化率、留存、复购、邮件、SMS、客单价、客户体验 | afa-monetize |
| 供应链、运营、渠道扩展、跨国、亚马逊、批发 | afa-scale |

#### 二级路由（Supervisor → Worker）

**afa-foundation →**

| 意图信号 | Worker |
|:---|:---|
| 选品、市场机会 | afa-explore |
| 竞品分析 | afa-compete |
| 品牌定位、品牌故事 | afa-brand |
| 产品策略、定价 | afa-product |
| 新品上市、冷启动 | afa-launch |

**afa-paid →**

| 意图信号 | Worker |
|:---|:---|
| 广告素材、创意、脚本 | afa-creative |
| Facebook/Meta/Instagram 广告 | afa-fb |
| Google 广告、Shopping、PMax | afa-gg |
| TikTok 广告、TikTok Shop | afa-tt |

**afa-organic →**

| 意图信号 | Worker |
|:---|:---|
| SEO、关键词、搜索排名 | afa-seo |
| 社交媒体、UGC、社群 | afa-social |
| 网红合作、KOL | afa-influencer |
| 公关、媒体报道 | afa-pr |
| AI 搜索优化、GEO | afa-geo |

**afa-monetize →**

| 意图信号 | Worker |
|:---|:---|
| 转化率低、落地页 | afa-convert |
| 客户体验、售后 | afa-cx |
| 复购率低、留存 | afa-retain |
| 客单价低、追加销售 | afa-aov |
| 邮件营销 | afa-email |
| 短信营销 | afa-sms |

**afa-scale →**

| 意图信号 | Worker |
|:---|:---|
| 供应链、物流、库存、运营效率 | afa-ops |
| 拓展新渠道、亚马逊、批发 | afa-expand |

### 预设工作流

AFA DTC Skills 内置 11 个预设工作流，覆盖从零起步到规模化的全阶段：

| # | 工作流 | 适用场景 | 执行链路 |
|:--|:---|:---|:---|
| 1 | **从零起步** | 什么都还没有 | explore → compete → brand → product → launch |
| 2 | **增长瓶颈突破** | 数据不好看，不知道卡在哪 | diagnose → 按 ICE 优先级执行 → dashboard 验证 |
| 3 | **广告体系搭建** | 要开始投广告了 | brand 确认 → creative → fb/gg/tt → convert 配合 |
| 4 | **留存体系搭建** | 复购太低，LTV 上不去 | retain → email → sms → aov |
| 5 | **内容营销体系** | 想做有机增长 | seo → geo → social → creative 配合 |
| 6 | **品牌升级** | 品牌老了，要重新定位 | compete → brand → creative + convert 配合 |
| 7 | **大促备战** | BFCM / 大促前准备 | product + creative → fb+gg+tt → convert+email+sms（三组并行） |
| 8 | **渠道扩展** | 想拓展新渠道 | expand 评估 → 按结果路由到对应 Supervisor |
| 9 | **紧急止血** | 现金流告急 | 按资产有无分支到 monetize/foundation/paid（多组联动） |
| 10 | **Level 0 引导** | 完全没方向 | 方向梳理 → explore → 进入从零起步 |
| 11 | **溢价能力构建** | 想提高利润率 | product 四维评估 → 按 Tier 路由到不同模块 |

### 常见路径

```
不知道做什么 → afa（Hub 自动路由）→ 对的模块

数据出问题 → afa-diagnose（诊断）→ 定位原因 → 对应 Worker 执行

从零开始 → afa-foundation → explore → compete → brand → product → launch

要投广告 → afa-paid → creative（素材）→ fb / gg / tt（投放）

做内容 → afa-organic → seo + social + influencer + pr

提高复购 → afa-monetize → retain + email + sms + aov

扩规模 → afa-scale → ops（运营）+ expand（渠道）
```

### 跨组协同

模块之间会自动协同。比如：

- 广告体系搭建时，`afa-paid` 会先拉 `afa-brand` 确认品牌定位，投放后拉 `afa-convert` 优化落地页
- 大促备战时，`foundation`、`paid`、`monetize` 三个 Supervisor 并行协同
- 任何模块遇到超出职责的请求，通过回交链路上报，Hub 重新路由——不会自作主张

---

## 数据流转

### Brand Brain — 模块间的数据总线

上游模块写入的文件自动成为下游模块的输入：

```
afa-explore → competitors.md（初步竞品）
    ↓
afa-compete → 更新 competitors.md（深化竞品分析）
    ↓
afa-brand → brand-master.md + voice-and-tone.md
    ↓
afa-product → products.md
    ↓
afa-launch → 上市计划（消费以上所有文件）
```

### Monetize 组协同规则

- email + sms 不同时触发同一事件（邮件先发 → 无响应 → SMS 跟进）
- `convert` 负责"第一次购买"，`retain` 负责"第二次及以后"
- `aov` 策略通过 `convert`（产品页）、`email`（交叉销售）、`cx`（购后追加）三个触点落地
- 每个 Worker 执行后关键指标变化回传 `learnings.jsonl`

---

## 设计原则

### 十一大铁律

1. **连续提问不超过 3 个** — 避免审讯感，快速进入执行
2. **绝不展示模块菜单，自动路由** — 用户说需求，系统自己判断该谁干
3. **废话清零，100% 可执行** — 每一条输出必须是能直接做的事
4. **不全量喂数据，按需调用** — 只拉当前步骤需要的信息
5. **不重建已有的东西** — Brand Brain 里有的直接复用
6. **不给泛泛建议** — 必须具体到数字、步骤、工具
7. **不把工作流当单个模块用** — 工作流是串联编排，不是单点调用
8. **不忘更新 Brand Brain** — 每次交互结束必须写回
9. **诚实兜底，绝不硬编** — 数据不够就说不够，不编造
10. **创作者声明红线** — 除 Hub 开头「关于」章节外，任何地方不出现推广信息，不在模块输出末尾添加个人推广
11. **不充当法律/合规/财务顾问** — 涉及法律税务问题明确告知用户咨询专业人士

### Brand Brain 记忆系统

- `brand-brain/` 目录结构持久化品牌数据（品牌定位、竞品、产品、受众等）
- 每次交互结束更新 `learnings.jsonl`，记录关键发现与指标变化
- 文件所有权：每个文件有明确的 Worker 负责写入，避免冲突覆盖

### 上下文交接协议

Hub → Supervisor → Worker 全链路传递 5 个核心字段：

| 字段 | 说明 |
|:---|:---|
| `main_question` | 用户的核心问题 |
| `deferred_goals` | 暂缓的次要目标 |
| `evidence_state` | 当前已有的数据/证据 |
| `market_scope` | 目标市场范围 |
| `primary_market` | 主要市场 |

不得静默丢失任何字段——交接时必须完整传递。

### 越界回交机制

```
Worker 发现越界请求 → 标记 out_of_scope → 上报 Supervisor → Supervisor 上报 Hub → Hub 重路由
```

绝不自作主张处理职责外请求。

### 三级降级策略

| 级别 | 触发条件 | 执行策略 |
|:---|:---|:---|
| Level 1 | 部分数据缺失 | 基于已有数据推进 + 标注假设 |
| Level 2 | 极少数据 | 保守方案 + 标注待验证项 |
| Level 3 | 零数据 | 行业基准参考 + 明确告知数据缺失 |

### 危机模式

| 模式 | 触发信号 | 策略 |
|:---|:---|:---|
| `cash_crisis` | 现金流告急、亏损加速 | 止血优先，暂缓所有长期项目 |
| `pr_crisis` | 负面舆情爆发、品牌事故 | 声誉修复优先，暂停营销推送 |

### 成本标签

每条建议必须带成本标签：

- **预算**：执行这件事要花多少钱
- **时间**：从开始到见效要多久
- **技能要求**：需要什么人来做（创始人自己 / VA / 专业服务商）

### 供应链 & 季节性感知

- 自动检测商业模式：dropshipping / wholesale / manufacturing / DTC self-fulfilled
- 自动检测季节阶段：旺季备战 / 旺季中 / 淡季恢复 / 平稳期
- 不把淡季正常波动误判为业务衰退

---

## 工作模式明细

| 模块 | 工作模式 |
|:---|:---|
| afa | 从零起步 / 增长瓶颈突破 / 广告体系搭建 / 留存体系搭建 / 内容营销体系 / 品牌升级 / 大促备战 / 渠道扩展 / 紧急止血 / Level 0 引导 / 溢价能力构建 |
| afa-diagnose | 全面体检 / 专项深诊 / 急诊 / 复诊 / 危机诊断 |
| afa-dashboard | 首次体检 / 周期复检 / 专项分析 / 实时响应 |
| afa-foundation | 从零起步 / 品牌升级 / 溢价能力构建 |
| afa-paid | 广告体系搭建 / 大促广告备战 / 素材迭代 |
| afa-organic | 内容营销体系搭建 / 影响力构建 / 溢价支撑 |
| afa-monetize | 留存体系搭建 / 大促变现备战 / 转化漏斗修复 / 溢价变现 |
| afa-scale | 渠道扩展 / 运营体系搭建 / Dropshipping→DTC 过渡 |
| afa-explore | VOC 挖掘 / 角度生成 / 竞争与市场评估 / 诊断 |
| afa-compete | 竞争格局扫描 / 深度竞品拆解 / 对标学习与差异化借鉴 / 竞品监控与季节性策略 |
| afa-brand | 品牌定位构建 / 品牌声音构建 / 品牌故事构建 / 视觉识别构建 / 品牌健康审计 / 品牌规范文档生成 |
| afa-product | 产品发现与验证 / 溢价与定价 / 诊断 / 产品组合与供应链 / 产品上市检查清单 |
| afa-launch | 完整启动规划 / 启动诊断 / PMF 评估 / 创意测试方案 / 预算规划 |
| afa-creative | 品牌视觉套件 / 创意概念与脚本 / Prompt Engineering / 广告测试矩阵 / 平台适配 |
| afa-fb | 账户结构与设置 / 受众策略 / 创意与文案 / 预算与扩量 / 追踪与归因 / 账户健康与合规 |
| afa-gg | 搜索广告策略 / PMax 深度优化 / 产品 Feed 优化 / 预算与扩量 / 追踪与设置 |
| afa-tt | 账户设置与结构 / 创意策略 / TikTok Shop 策略 / 联盟营销 / 扩量与预算 |
| afa-seo | SEO 全站审计 / 关键词研究与主题规划 / 页面级内容优化 / 流量诊断与恢复 / 内容策略规划 / 国际 SEO 规划 |
| afa-social | 全盘社交内容策略 / UGC 项目启动与管理 / 爆款脚本工程 / 有机转付费管道 / 大促内容日历 / 社区飞轮构建 |
| afa-influencer | 创作者发现与筛选 / 冷拓展与邀约 / 创作者内容简报 / 联盟计划设计 / 渠道诊断与优化 / 社区飞轮与品牌倡导者培育 |
| afa-pr | 媒体冷推策划 / UGC 飞轮构建 / 危机预警与响应 / 品牌资产保护 / 媒体套件生成 |
| afa-geo | AI 可见度审计 / 内容结构重塑 / 跨市场搜索信号输入 |
| afa-convert | 全链路转化审计 / 落地页架构设计 / PDP 深度优化 / CRO 增长飞轮 / 结账流程优化 / 微转化漏斗分析 |
| afa-cx | 旅程映射 / 工单智能分析 / 自助服务内容建设 / 情感分析 / CX 自动化 / 退货体验优化 |
| afa-retain | 留存体检 / 生命周期管理 / 忠诚度计划设计 / 订阅防流失 / 召回体系 |
| afa-aov | 门槛设计 / 捆绑包构建 / 促销利润模拟 / 全链路 Upsell / 订阅 AOV 优化 |
| afa-email | 自动化流构建 / Campaign 文案撰写 / 可交付性修复 / 邮件日历规划 |
| afa-sms | Flow 架构设计 / Campaign 文案撰写 / 渠道诊断 / SMS×Email 协同规划 |
| afa-ops | 单位经济审计 / 库存健康检查 / 履约优化 / 团队架构规划 / 自动化蓝图 / 供应链风险评估 / 财务运营优化 |
| afa-expand | 渠道评估 / Marketplace 入驻 / 批发计划 / 国际化规划 / 线下零售 / 渠道健康审计 |

---

## 模块全览

| # | 模块 | 层级 | 上级 | 工作模式 | 参考库文件 |
|:--|:---|:---|:---|:---|:---|
| 1 | afa | Hub | — | 11 预设工作流 | 5 |
| 2 | afa-diagnose | 全局引擎 | Hub | 5 种诊断模式 | 9 |
| 3 | afa-dashboard | 全局引擎 | Hub | 4 大工作流 | 9 |
| 4 | afa-foundation | Supervisor | Hub | 3 工作流 | — |
| 5 | afa-paid | Supervisor | Hub | 3 工作流 | — |
| 6 | afa-organic | Supervisor | Hub | 3 工作流 | — |
| 7 | afa-monetize | Supervisor | Hub | 4 工作流 | — |
| 8 | afa-scale | Supervisor | Hub | 3 工作流 | — |
| 9 | afa-explore | Worker | foundation | 4 种模式 | 11 |
| 10 | afa-compete | Worker | foundation | 4 种模式 | 11 |
| 11 | afa-brand | Worker | foundation | 6 种模式 | 12 |
| 12 | afa-product | Worker | foundation | 5 种模式 | 11 |
| 13 | afa-launch | Worker | foundation | 5 种模式 | 11 |
| 14 | afa-creative | Worker | paid | 5 种模式 | 16 |
| 15 | afa-fb | Worker | paid | 6 种模式 | 11 |
| 16 | afa-gg | Worker | paid | 5 种模式 | 12 |
| 17 | afa-tt | Worker | paid | 5 种模式 | 10 |
| 18 | afa-seo | Worker | organic | 6 种模式 | 13 |
| 19 | afa-social | Worker | organic | 6 种模式 | 11 |
| 20 | afa-influencer | Worker | organic | 6 种模式 | 11 |
| 21 | afa-pr | Worker | organic | 5 种模式 | 9 |
| 22 | afa-geo | Worker | organic | 3 种模式 | 9 |
| 23 | afa-convert | Worker | monetize | 6 种模式 | 10 |
| 24 | afa-cx | Worker | monetize | 6 种模式 | 11 |
| 25 | afa-retain | Worker | monetize | 5 种模式 | 11 |
| 26 | afa-aov | Worker | monetize | 5 种模式 | 12 |
| 27 | afa-email | Worker | monetize | 4 种模式 | 10 |
| 28 | afa-sms | Worker | monetize | 4 种模式 | 10 |
| 29 | afa-ops | Worker | scale | 7 种模式 | 10 |
| 30 | afa-expand | Worker | scale | 6 种模式 | 12 |

---

## 知识库

知识库由 200+ 个方法论、框架、案例库文件组成，每个 Worker 的 `references/` 目录都可以独立使用。

<details>
<summary>afa-foundation 组知识库（56 个文件）</summary>

**afa-explore（11 个）：**
voc-mining-playbook.md / spherical-scaling-system.md / awareness-mapping-guide.md / scamper-innovation-model.md / market-sizing-framework.md / advanced-models.md / advanced-strategies.md / core-paradigms.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-compete（11 个）：**
competitive-landscape-mapping.md / multi-dimensional-analysis.md / ad-intelligence.md / price-intelligence.md / seo-gap-analysis.md / benchmarking-playbook.md / core-frameworks.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-brand（12 个）：**
positioning-frameworks.md / voice-architecture-guide.md / voice-building-sop.md / storytelling-playbook.md / visual-identity-system.md / brand-audit-toolkit.md / competitive-brand-analysis.md / archetype-deep-dive.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-product（11 个）：**
product-discovery-framework.md / cogs-and-pricing-model.md / product-portfolio-matrix.md / sourcing-and-supply-chain.md / differentiation-playbook.md / product-launch-checklist.md / core-frameworks.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-launch（11 个）：**
launch-timeline-template.md / cross-channel-launch-playbook.md / core-frameworks.md / diagnostic-decision-trees.md / pmf-assessment-template.md / mvp-testing-playbook.md / creative-brief-template.md / budget-calculator.md / failure-postmortem-template.md / work-modes-and-templates.md / anti-patterns.md

</details>

<details>
<summary>afa-paid 组知识库（49 个文件）</summary>

**afa-creative（16 个）：**
brand-kit-template.md / typography-guide.md / reali-tea-scripting.md / product-visual-system.md / copywriting-frameworks.md / prompt-engineering.md / ad-testing-matrix.md / platform-specs.md / content-policy.md / visual-intelligence.md / seasonal-creative-calendar.md / core-frameworks.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-fb（11 个）：**
core-frameworks.md / audience-strategy.md / creative-templates.md / planning-and-budget.md / scaling-sop.md / tracking-setup.md / account-health.md / benchmark-data.md / diagnostic-rules.md / work-modes-and-kpi.md / anti-patterns.md

**afa-gg（12 个）：**
search-ads-playbook.md / pmax-playbook.md / feed-optimization.md / planning-and-budget.md / tracking-and-feed.md / shopify-google-setup.md / core-frameworks.md / benchmark-data.md / diagnostic-rules.md / work-modes-and-kpi.md / report-templates.md / anti-patterns.md

**afa-tt（10 个）：**
account-setup-sop.md / creative-templates.md / tiktok-shop-playbook.md / affiliate-playbook.md / scaling-sop.md / core-frameworks.md / benchmark-data.md / diagnostic-rules.md / work-modes-and-templates.md / anti-patterns.md

</details>

<details>
<summary>afa-organic 组知识库（53 个文件）</summary>

**afa-seo（13 个）：**
technical-seo-checklist.md / keyword-research-engine.md / pdp-seo-optimizer.md / collection-page-seo.md / content-engine-playbook.md / link-acquisition-playbook.md / international-seo-guide.md / geo-aeo-playbook.md / core-frameworks.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-social（11 个）：**
core-frameworks.md / content-archetypes-library.md / platform-playbooks.md / content-calendar-template.md / ugc-management-system.md / organic-to-paid-pipeline.md / community-flywheel.md / social-commerce-kpis.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-influencer（11 个）：**
core-frameworks.md / influencer-vetting-framework.md / outreach-playbook.md / compensation-models.md / affiliate-program-guide.md / compliance-and-risk.md / benchmark-data.md / community-flywheel.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-pr（9 个）：**
core-frameworks.md / cpr-pitching-playbook.md / ugc-community-flywheel.md / crisis-monitoring-response.md / brand-protection-toolkit.md / media-kit-templates.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-geo（9 个）：**
core-frameworks.md / ai-visibility-audit.md / geo-optimization-playbook.md / geographic-arbitrage-guide.md / landed-cost-calculator.md / trade-compliance-toolkit.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

</details>

<details>
<summary>afa-monetize 组知识库（64 个文件）</summary>

**afa-convert（10 个）：**
core-frameworks.md / audit-checklist.md / landing-page-playbook.md / personalization-playbook.md / ab-testing-playbook.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / report-templates.md / anti-patterns.md

**afa-cx（11 个）：**
core-frameworks.md / journey-mapping-framework.md / ticket-intelligence-system.md / self-service-content-engine.md / sentiment-analysis-playbook.md / cx-automation-toolkit.md / return-and-retention.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-retain（11 个）：**
core-frameworks.md / cohort-analysis-guide.md / rfm-ltv-framework.md / loyalty-program-playbook.md / subscription-management.md / win-back-workflows.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / report-templates.md / anti-patterns.md

**afa-aov（12 个）：**
core-frameworks.md / threshold-engineering.md / bundle-strategy.md / promotion-strategy.md / upsell-cross-sell.md / dynamic-pricing.md / cart-abandonment-recovery.md / aov-kpi-dashboard.md / benchmark-data.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-email（10 个）：**
core-frameworks.md / core-flows-playbook.md / campaign-archetypes.md / copywriting-formulas.md / deliverability-checklist.md / email-design-guidelines.md / segmentation-guide.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-sms（10 个）：**
core-frameworks.md / core-flows-playbook.md / copywriting-formulas.md / conversational-sms-guide.md / compliance-checklist.md / omnichannel-orchestration.md / campaign-calendar.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

</details>

<details>
<summary>afa-scale 组知识库（22 个文件）</summary>

**afa-ops（10 个）：**
core-frameworks.md / unit-economics-calculator.md / inventory-management-handbook.md / fulfillment-optimization-guide.md / customer-service-playbook.md / team-building-roadmap.md / automation-blueprint-collection.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

**afa-expand（12 个）：**
core-frameworks.md / channel-economics-toolkit.md / marketplace-entry-playbook.md / wholesale-pricing-calculator.md / international-compliance-guide.md / pop-up-execution-playbook.md / new-digital-channels-guide.md / tariff-arbitrage-strategies.md / landed-cost-calculator.md / diagnostic-system.md / work-modes-and-templates.md / anti-patterns.md

</details>

<details>
<summary>系统核心（Hub + 全局引擎，23 个文件）</summary>

**afa Hub（5 个 references + 14 个 _system）：**
References: brand-brain-template.md / diagnostic-rules.md / routing-checklist.md / benchmark-data.md / case-library.md
_system: brand-memory-protocol.md / context-matrix.md / cost-tag-spec.md / degradation-rules.md / edge-cases.md / interaction-protocol.md / iron-rules.md / localization-rules.md / output-format.md / preamble.md / reasoning-rules.md / reference-authoring-rules.md / skill-directory.md / scripts/memory_manager.py

**afa-diagnose（9 个）：**
core-frameworks.md / diagnostic-frameworks.md / industry-benchmarks.md / diagnostic-system.md / diagnostic-cases.md / priority-scoring.md / work-modes-and-templates.md / diagnostic-templates.md / anti-patterns.md

**afa-dashboard（9 个）：**
core-frameworks.md / benchmark-database.md / nsm-playbook.md / diagnostic-system.md / anomaly-diagnosis-rules.md / anti-patterns.md / work-modes-and-templates.md / report-templates.md / data-driven-decision-loop.md

</details>

---

## 如何安装

### npx 一键安装（推荐）

```shell
npx skills add afadtc/afa-dtc-skills
```

### 手动安装

```shell
git clone https://github.com/afadtc/afa-dtc-skills.git
```

将模块目录复制到 `~/.claude/skills/` 或项目的 `.claude/skills/` 目录下即可。

---

## 如何更新

重新运行安装命令即可，安装和更新用同一条命令：

```shell
npx skills add afadtc/afa-dtc-skills
```

---

## 目录结构

```
afa-dtc-skills/
├── afa/                        # Hub — 系统入口与工作流编排
│   ├── SKILL.md
│   ├── _system/                # 系统级规则（路由、交接、铁律等）
│   └── references/             # 路由清单、诊断规则、案例库等
│
├── afa-diagnose/               # 全局诊断引擎
├── afa-dashboard/              # 全局数据中枢
│
├── afa-foundation/             # Supervisor: 品牌与产品基建
│   └── Workers:
│       ├── afa-explore/        #   市场探索
│       ├── afa-compete/        #   竞争情报
│       ├── afa-brand/          #   品牌定位
│       ├── afa-product/        #   产品策略
│       └── afa-launch/         #   产品上市
│
├── afa-paid/                   # Supervisor: 付费获客
│   └── Workers:
│       ├── afa-creative/       #   创意生产
│       ├── afa-fb/             #   Meta 广告
│       ├── afa-gg/             #   Google Ads
│       └── afa-tt/             #   TikTok 广告
│
├── afa-organic/                # Supervisor: 有机增长
│   └── Workers:
│       ├── afa-seo/            #   SEO
│       ├── afa-social/         #   社交内容
│       ├── afa-influencer/     #   网红营销
│       ├── afa-pr/             #   品牌公关
│       └── afa-geo/            #   AI 搜索可见度
│
├── afa-monetize/               # Supervisor: 变现与留存
│   └── Workers:
│       ├── afa-convert/        #   转化率优化
│       ├── afa-cx/             #   客户体验
│       ├── afa-retain/         #   用户留存
│       ├── afa-aov/            #   客单价提升
│       ├── afa-email/          #   邮件营销
│       └── afa-sms/            #   SMS 营销
│
├── afa-scale/                  # Supervisor: 运营与扩张
│   └── Workers:
│       ├── afa-ops/            #   运营优化
│       └── afa-expand/         #   渠道扩张
│
├── LICENSE
└── README.md
```

每个 Worker 模块包含：
- `SKILL.md` — 模块定义、工作模式、执行规则
- `references/` — 方法论框架、案例库、模板、基准数据

---

## 许可证

本项目采用 [CC BY-NC 4.0](LICENSE) 许可证。

- **个人使用、学习、研究、非商业项目**：不需要署名，不需要申请
- **公开发布衍生作品**（文章、工具、课程等）：请注明来源
- **商业用途**：需要单独授权，请联系作者
