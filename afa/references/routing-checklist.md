# AFA DTC 路由检查表

> **协议层级**：Hub 路由参考 · 路由前强制检查
>
> **版本**：v2.4.7
>
> **说明**：本文件是 afa 智能路由的完整决策参考，确保每次路由都精准、高效、不遗漏。
>
> **v2.0.9 变更**：第二章所有模块的「传递上下文」从描述性文本升级为声明式 Context Matrix（Requires/Optional/Never），与各 Worker SKILL.md 内部声明严格对齐。

---

## 一、路由前检查清单（v1.8 升级）

每次路由到任何模块之前，必须完成以下检查：

```
□ 1. 用户意图是否已明确？
     如果模糊 → 先做最小澄清，只问 1-2 个足以决定路由的问题，不要进入资料盘问

□ 2. 当前主问题是什么？
     如果用户一次提了多个问题 → 必须先选出 main_question
     其余问题先记入 deferred_goals，不要并列展开

□ 3. 是否需要先诊断？
     如果用户描述的是症状而非具体需求 → 先走诊断流程
     如果用户描述的是具体任务 → 可以直接路由

□ 4. 是否是复合任务？（v2.4.1 重写）
     如果用户需求涉及 2+ 个领域 → 先判断当前最优第一步是否清晰
     如果第一步清晰且无高风险动作 → 直接推进第一步，并用自然语言说明后续大致路径
     只有存在真实方向分叉、额外资源投入或用户明确要求先看全流程时 → 再展示完整计划供用户拍板
     示例：「帮我做完整的广告体系」→ 默认先切入最关键的起始环节，再在出现分叉时请求确认

□ 5. 是否应该走工作流而非单模块？
     检查是否匹配预设工作流的触发条件（如 0-1、大促、溢价构建等）
     如果匹配 → 走工作流链
     如果不匹配 → 单模块路由

□ 6. 是否已经到达必须确认的节点？（v2.4.1 重写——必检）
     单模块路由 → 默认直接推进，不把内部路由写成「可以开始吗」式门槛
     多模块工作流 → 默认先推进第一步，不把完整计划展示设为前置门票
     只有出现真实方向分叉、预算/资源投入、高风险外部动作、不可逆影响，或用户明确要求自己选择时 → 才请求确认
     P0 危机 → 可先给止损方案，但涉及真实外部执行前仍需说明风险并征得确认

□ 7. Brand Brain 中是否有该模块需要的前置信息？
     检查 Context Matrix 中该模块 Requires 的文件
     如果缺失 Requires 文件 → 先判断是否仍可给保守可执行版
     只有确属不可替代前置依赖时，才进入阻塞提示

□ 8. 上下文编译是否完成？
     按 Context Matrix 准备好该模块 Requires + Optional（如果存在）的文件
     用户原始需求是否已完整记录
     诊断结论（如有）是否已准备好传递
     main_question / deferred_goals / evidence_state 是否已显式写入

□ 9. 目标市场是否已确认？（v1.8 新增）
     如果任务涉及内容生成、属地化、定价 → 确认目标市场
     如果未知 → 允许先给粗颗粒度保守版，但必须标适用范围
     如果是跨国市场 → 强制加入本地化提醒（语言、支付、物流、属地化要求）
```

---

## 二、24 模块完整路由规则

### afa-diagnose（全链路诊断中心）

```
触发条件：
  ├── 用户说「帮我全面诊断/体检」
  ├── 生命体征速诊发现 2+ 个异常指标
  ├── 用户描述了复杂的多维度问题
  └── 用户说「不知道问题出在哪」

前置要求：
  ├── 最好有基础的业务数据（月销、转化率等）
  └── 如果没有，模块内会引导收集

Context Matrix：
  Requires : products.md, brand-master.md
  Optional : learnings.jsonl, metrics.md, audience.md, offers.md
  Never    : 未经用户确认的第三方诊断结论、竞品内部运营数据
  额外传递 : premium_tier（如果正在执行溢价构建工作流）、速诊报告（如果已做过速诊）

预期输出：
  ├── 完整诊断报告
  ├── ICE 排序的行动方案
  └── 更新 learnings.jsonl

后续路由：
  → 按诊断结果的 ICE 排序，依次路由到对应模块
```

### afa-dashboard（数据体检中心）

```
触发条件：
  ├── 用户说「看看我的数据」「数据怎么样」
  ├── 定期体检（用户要求周期性检查）
  └── 某个模块执行完后需要追踪效果

前置要求：
  ├── 用户需要提供当前数据
  └── 或已有历史基准线可对比

Context Matrix：
  Requires : products.md
  Optional : learnings.jsonl, stack.md, metrics.md
  Never    : 用户个人财务信息、未经授权的第三方平台数据
  额外传递 : 上次体检数据（如有）

预期输出：
  ├── KPI 对比报告
  ├── 异常预警
  └── 趋势分析
```

### afa-explore（市场探索）

```
触发条件：
  ├── 用户说「我想做新品牌/新产品」
  ├── 用户说「帮我选品」「什么赛道好」
  ├── 用户说「这个市场怎么样」
  └── 从零起步工作流的 Step 1

前置要求：
  ├── 用户的兴趣方向或品类偏好
  └── 预算范围（可选）

Context Matrix：
  Requires : products.md, audience.md
  Optional : competitors.md, learnings.jsonl
  Never    : 未经验证的虚构数据

预期输出：
  ├── 市场机会评估报告
  ├── 选品推荐清单
  └── 竞争格局概览

后续路由：
  → afa-compete（深入分析竞品）
  → afa-product（确定产品策略）
```

### afa-compete（竞品分析）

```
触发条件：
  ├── 用户说「帮我分析竞品」
  ├── 用户提供了具体竞品名称/URL
  ├── afa-explore 完成后的自然衔接
  └── 品牌升级工作流的 Step 1

前置要求：
  ├── 竞品名称或 URL（至少 1 个）
  └── 或品类信息（模块自行搜索竞品）

Context Matrix：
  Requires : competitors.md, products.md
  Optional : learnings.jsonl
  Never    : 非公开竞品商业机密

预期输出：
  ├── 竞品拆解报告（5 维度）
  ├── 差异化机会清单
  └── 创建/更新 competitors.md

后续路由：
  → afa-brand（基于竞品分析定位品牌）
  → afa-product（基于竞品分析制定产品策略）
```

### afa-product（产品策略与溢价构建）

```
触发条件：
  ├── 用户说「产品怎么定价」「SKU 怎么规划」
  ├── 用户说「产品线怎么扩展」
  ├── 用户说「只能打价格战」「溢价能力不足」（触发四维溢价阶梯评估）
  ├── 从零起步工作流的 Step 3
  └── 溢价能力构建工作流的 Step 1

前置要求：
  ├── 产品基本信息（品类、成本等）
  └── 竞品定价信息（可选，模块可自行调研）

Context Matrix：
  Requires : voice-and-tone.md, products.md
  Optional : learnings.jsonl
  Never    : 供应商机密报价、未经验证的内部假设

预期输出：
  ├── 产品矩阵
  ├── 定价策略
  ├── SKU 规划
  └── 创建/更新 products.md + offers.md

后续路由：
  → afa-convert（基于产品策略优化页面）
  → afa-launch（基于产品策略制定广告计划）
```

### afa-brand（品牌基础）

```
触发条件：
  ├── 用户说「帮我定位品牌」「品牌故事怎么写」
  ├── 用户说「品牌没有辨识度」
  ├── 从零起步工作流的 Step 3
  └── 品牌升级工作流的 Step 2

前置要求：
  ├── 产品信息（至少知道卖什么）
  └── 目标市场（至少知道卖给谁）

Context Matrix：
  Requires : products.md
  Optional : voice-and-tone.md, positioning.md, brand-story.md, visual-identity.md, learnings.jsonl
  Never    : 竞品机密数据、未经验证的品牌声明

预期输出：
  ├── 品牌定位声明
  ├── 品牌故事
  ├── 视觉方向建议
  ├── 品牌调性指南
  └── 创建/更新 brand-master.md + voice-and-tone.md + audience.md + guardrails.md

后续路由：
  → afa-convert（基于品牌定位优化页面）
  → afa-creative（基于品牌定位制作素材）
```

### afa-convert（转化引擎）

```
触发条件：
  ├── 用户说「帮我优化落地页/产品页」
  ├── 用户说「转化率太低」
  ├── 诊断发现转化漏斗问题
  ├── 从零起步工作流的 Step 4
  └── 广告体系搭建工作流的 Step 3

前置要求：
  ├── 产品信息
  └── 品牌定位（可选但推荐）

Context Matrix：
  Requires : products.md
  Optional : objections.md, guardrails.md, audience.md, learnings.jsonl
  Never    : 竞品后台转化数据、未经验证的 A/B 测试结论

预期输出：
  ├── 页面结构方案（首页/产品页/着陆页）
  ├── 关键文案
  ├── 信任元素建议
  └── 创建/更新 objections.md

后续路由：
  → afa-launch / afa-fb / afa-gg / afa-tt（页面准备好后投广告）
```

### afa-launch（流量启动）

```
触发条件：
  ├── 用户说「我要开始投广告」
  ├── 用户说「冷启动怎么做」
  ├── 从零起步工作流的 Step 5
  └── 首次投放，还没有广告历史数据

前置要求：
  ├── 产品信息 + 定价
  ├── 品牌定位（推荐）
  └── 页面已准备好（推荐）

Context Matrix：
  Requires : voice-and-tone.md, products.md
  Optional : learnings.jsonl
  Never    : 竞品机密数据

预期输出：
  ├── 首批广告计划
  ├── 预算分配方案
  ├── 测试矩阵
  └── 冷启动 SOP

后续路由：
  → afa-fb / afa-gg / afa-tt（进入具体渠道优化）
  → afa-creative（如果需要更多素材）
```

### afa-fb（Facebook 广告）

```
触发条件：
  ├── 用户说「Facebook 广告怎么优化」
  ├── 用户说「Meta 广告 ROAS 太低」
  ├── 诊断发现 Facebook 渠道问题
  └── 用户说「账号被封了」（账户健康部分）

Context Matrix：
  Requires : products.md, audience.md
  Optional : learnings.jsonl, creative-kit.md, offers.md
  Never    : 竞品广告账户后台数据、未经授权的 Pixel 数据
  额外传递 : 用户当前广告数据（如有）

预期输出：
  ├── 账户结构优化方案
  ├── 受众策略
  ├── 素材建议
  ├── 出价和预算策略
  └── 更新 learnings.jsonl
```

### afa-gg（Google 广告）

```
触发条件：
  ├── 用户说「Google 广告怎么投」
  ├── 用户说「搜索广告/购物广告怎么优化」
  └── 诊断发现 Google 渠道问题

Context Matrix：
  Requires : products.md, audience.md
  Optional : learnings.jsonl, offers.md, brand-master.md
  Never    : 竞品 Google Ads 后台数据、未经授权的搜索词报告
  额外传递 : 用户当前广告数据（如有）

预期输出：
  ├── 关键词策略
  ├── 广告文案
  ├── 出价策略
  ├── Shopping Feed 优化建议
  └── 更新 learnings.jsonl
```

### afa-tt（TikTok 广告）

```
触发条件：
  ├── 用户说「TikTok 广告怎么做」
  ├── 用户说「要不要做 TikTok」
  └── 诊断发现需要新渠道

Context Matrix：
  Requires : products.md, audience.md
  Optional : learnings.jsonl, creative-kit.md, offers.md
  Never    : 竞品 TikTok 广告后台数据、未经授权的 Pixel 数据

预期输出：
  ├── TikTok 广告策略
  ├── 原生内容风格指南
  ├── Spark Ads 策略
  └── 更新 learnings.jsonl
```

### afa-seo（SEO 增长）

```
触发条件：
  ├── 用户说「我想做 SEO」
  ├── 用户说「怎么获取免费流量」
  ├── 诊断发现自然流量占比过低
  └── 内容营销工作流的 Step 1

Context Matrix：
  Requires : products.md
  Optional : brand-master.md, learnings.jsonl, audience.md
  Never    : 竞品 GSC 后台数据、未经授权的外链操作

预期输出：
  ├── 关键词矩阵
  ├── 内容日历
  ├── On-page 优化清单
  ├── 技术 SEO 审计
  └── 创建/更新 keywords.md
```

### afa-geo（AI 搜索可见度）

```
触发条件：
  ├── 用户说「怎么在 AI 搜索里被找到」
  ├── 用户说「Perplexity/ChatGPT 搜索优化」
  └── 内容营销工作流的 Step 2

Context Matrix：
  Requires : products.md
  Optional : brand-master.md, learnings.jsonl, audience.md
  Never    : 未经验证的关税税率数据、竞品内部供应链成本

预期输出：
  ├── AI 搜索可见度策略
  ├── 内容优化建议
  └── 引用率提升方案
```

### afa-retain（留存复购）

```
触发条件：
  ├── 用户说「怎么提高复购率」
  ├── 用户说「老客不回来了」
  ├── 诊断发现复购率低于基准
  └── 留存体系搭建工作流的 Step 1

Context Matrix：
  Requires : products.md
  Optional : audience.md, learnings.jsonl, offers.md, brand-master.md
  Never    : 客户个人隐私数据（PII）、未经脱敏的购买记录

预期输出：
  ├── RFM 分层方案
  ├── 留存策略蓝图
  ├── 忠诚度计划设计
  └── 订阅制模型评估

后续路由：
  → afa-email（搭建邮件序列）
  → afa-sms（搭建 SMS 协同）
  → afa-aov（提升客单价）
```

### afa-email（Email 营销）

```
触发条件：
  ├── 用户说「帮我写邮件/设置邮件流」
  ├── 用户说「邮件打开率低」
  ├── 诊断发现邮件体系不完整
  └── 留存体系搭建工作流的 Step 2

Context Matrix：
  Requires : voice-and-tone.md, products.md
  Optional : audience.md, learnings.jsonl
  Never    : 未经用户确认的邮件列表操作、违反 CAN-SPAM/GDPR 的内容

预期输出：
  ├── 邮件序列（欢迎/弃购/购后/Win-back 等）
  ├── 邮件模板
  ├── A/B 测试计划
  └── 更新 learnings.jsonl + assets.md
```

### afa-sms（SMS 营销）

```
触发条件：
  ├── 用户说「SMS 怎么做」
  ├── 留存体系搭建工作流的 Step 3
  └── 与 afa-email 协同使用

Context Matrix：
  Requires : products.md, voice-and-tone.md
  Optional : audience.md, learnings.jsonl, offers.md
  Never    : 未经用户确认的短信列表操作、违反 TCPA/GDPR 的内容

预期输出：
  ├── SMS 策略
  ├── 最佳实践框架
  ├── 与 Email 的协同编排方案
  └── SMS 模板
```

### afa-aov（客单价提升）

```
触发条件：
  ├── 用户说「怎么提高客单价」
  ├── 诊断发现 AOV 低于基准
  └── 留存体系搭建工作流的 Step 4

Context Matrix：
  Requires : products.md, offers.md
  Optional : learnings.jsonl, brand-master.md, audience.md
  Never    : 竞品定价原始数据、未经验证的促销效果声明

预期输出：
  ├── Bundle 策略
  ├── 追加销售方案
  ├── 交叉销售方案
  ├── 阶梯折扣设计
  └── 更新 offers.md
```

### afa-social（社交与社区）

```
触发条件：
  ├── 用户说「帮我做社交媒体内容」
  ├── 用户说「社区怎么运营」
  └── 内容营销工作流的 Step 3

Context Matrix：
  Requires : products.md, voice-and-tone.md
  Optional : audience.md, learnings.jsonl, creative-kit.md
  Never    : 竞品社交账号后台数据、未经授权的用户 UGC 内容

预期输出：
  ├── 内容支柱策略
  ├── 平台适配方案
  ├── UGC 剧本
  ├── 社区运营计划
  └── 更新 assets.md
```

### afa-expand（渠道拓展）

```
触发条件：
  ├── 用户说「想拓展新渠道」
  ├── 用户说「要不要做亚马逊/批发」
  └── 渠道扩展工作流的 Step 1

Context Matrix：
  Requires : brand-master.md, products.md
  Optional : competitors.md, stack.md, learnings.jsonl
  Never    : 竞品渠道后台数据、未经授权的 Marketplace 操作

预期输出：
  ├── 渠道机会评估报告
  ├── 扩展路线图
  └── 资源需求评估
```

### afa-influencer（网红营销）

```
触发条件：
  ├── 用户说「怎么找网红合作」
  ├── 用户说「KOL/KOC 营销怎么做」
  └── 渠道扩展工作流的后续步骤

Context Matrix：
  Requires : products.md, voice-and-tone.md
  Optional : audience.md, learnings.jsonl, brand-master.md
  Never    : 创作者个人隐私信息、未经授权的竞品合作数据

预期输出：
  ├── 网红合作策略
  ├── BD 话术模板
  ├── 合作模式设计
  ├── ROI 追踪框架
  └── 更新 assets.md
```

### afa-pr（品牌建设与公关）

```
触发条件：
  ├── 用户说「品牌公关怎么做」
  ├── 用户说「怎么上媒体」
  └── 用户说「危机公关」

Context Matrix：
  Requires : products.md, voice-and-tone.md
  Optional : brand-master.md, learnings.jsonl, audience.md
  Never    : 未经授权的媒体联系人私人信息、竞品内部公关预算

预期输出：
  ├── 媒体关系策略
  ├── 品牌叙事框架
  ├── 新闻稿模板
  └── 危机公关预案
```

### afa-cx（客户体验）

```
触发条件：
  ├── 用户说「客户体验怎么优化」
  ├── 用户说「退货率太高」「差评太多」
  └── 诊断发现客户满意度问题

Context Matrix：
  Requires : products.md
  Optional : objections.md, learnings.jsonl, voice-and-tone.md, audience.md
  Never    : 客户个人隐私数据、未经脱敏的工单原文

预期输出：
  ├── 客户旅程优化方案
  ├── 工单处理 SOP
  ├── 评论管理策略
  └── NPS 提升计划
```

### afa-ops（运营顾问）

```
触发条件：
  ├── 用户说「帮我建 SOP」
  ├── 用户说「运营效率怎么提升」
  ├── 用户说「团队怎么管理」
  └── 用户说「自动化怎么做」

Context Matrix：
  Requires : products.md
  Optional : learnings.jsonl, stack.md, brand-master.md
  Never    : 未经授权的供应商内部报价、竞品供应链成本数据

预期输出：
  ├── SOP 文档
  ├── 团队 OKR 框架
  ├── 自动化方案
  ├── 供应链优化建议
  └── 更新 stack.md
```

### afa-creative（创意工厂）

```
触发条件：
  ├── 用户说「帮我做广告素材/视频」
  ├── 用户说「创意枯竭了」
  ├── 广告体系搭建工作流的 Step 2
  └── 大促备战工作流的 Step 2

Context Matrix：
  Requires : voice-and-tone.md, products.md
  Optional : creative-kit.md, brand-master.md, learnings.jsonl, audience.md
  Never    : 竞品未公开素材、未经授权的用户生成内容

预期输出：
  ├── 广告素材方案
  ├── 视频脚本
  ├── AI 生成工作流
  ├── 素材测试矩阵
  └── 更新 creative-kit.md + assets.md
```

---

## 三、多模块协同规则（v2.4.1 重写）

### 用户确认节点（v2.4.1 重写——最高优先级）

```
核心原则：默认沿主问题连续推进；只有遇到真实分叉、资源投入差异或高风险动作时，才请求用户确认。

单模块路由：
  「我先按 [Skill display_name] 的逻辑处理这一步，先把当前主问题推进起来；
  如果后面遇到需要你拍板的分叉，我会单独提醒你。」

多模块工作流：
  「这个任务我会按主问题顺序往前推进。当前先处理第一步，
  后面如果出现需要你选择方向、投入资源或进入高风险动作的节点，我会单独提醒你确认。」

步骤衔接：
  「这一步已经完成。下一步最自然的是转到 [Skill display_name] 继续处理 [任务]；
  如果你想换方向或先停在这里，也可以直接告诉我。」

危机场景：
  命中 P0 时可先给止损方案，但涉及真实外部执行前仍需说明风险并征得确认。
```

### 角色边界规则（v1.8 新增）

```
每个 Skill 只做自己职责范围内的事：
  ├── afa-sms → 只负责「起草 SMS 文案和策略」，不发送短信
  ├── afa-email → 只负责「起草邮件序列和策略」，不发送邮件
  ├── afa-influencer → 只负责「筛选网红 + 起草 DM 话术/邮件模板」，不代发消息
  └── 所有模块 → 输出的是「可执行的草稿/方案」，用户自行决定是否执行
```

### 并行执行规则

```
可以并行的组合：
  ├── afa-product + afa-brand（产品策略和品牌定位可同时进行）
  ├── afa-email + afa-sms（邮件和短信可同时搭建）
  ├── afa-fb + afa-gg + afa-tt（多渠道广告可同时优化）
  └── afa-seo + afa-social（内容策略可同时制定）

不能并行的组合（有依赖关系）：
  ├── afa-brand → afa-convert（品牌定位必须先于页面优化）
  ├── afa-convert → afa-launch（页面必须先于广告投放）
  ├── afa-retain → afa-email（留存策略必须先于邮件执行）
  └── afa-explore → afa-compete（市场探索必须先于竞品分析）
```

### 模块间数据传递规则

```
上游模块完成后，必须：
  1. 将输出写入 Brand Brain 对应文件
  2. 更新 assets.md（如有新资产）
  3. 更新 learnings.jsonl（如有新教训）
  4. 向用户展示结果，确认是否继续下一步（v1.8 新增）
  5. 用户同意后才返回 afa 进行下一步路由

下游模块启动时，必须：
  1. 读取 Brand Brain 中的最新数据
  2. 确认上游输出是否满足需求
  3. 如果不满足，向用户说明缺什么、在哪里获取（v1.8 修改）
```

---

## 四、路由失败处理

```
情况 1：用户需求不匹配任何模块
  → 尝试拆解为多个子需求
  → 如果仍无法匹配 → 诚实告知能力边界 + 给替代方案

情况 2：模块执行失败
  → 记录失败原因
  → 尝试替代方案
  → 如果无法解决 → 返回 afa，告知用户并建议下一步

情况 3：用户中途改变需求
  → 暂停当前模块
  → 重新进入意图识别
  → 如果新需求与当前任务相关 → 调整执行计划
  → 如果完全不同 → 保存当前进度，切换到新任务
```

---

*本文件与 SKILL.md 中的路由表保持同步。任何路由规则的变更都应同时更新两个文件。*
