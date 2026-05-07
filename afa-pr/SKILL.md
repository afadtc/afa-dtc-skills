---
name: afa-pr
description: "DTC 品牌公关与声誉管理引擎——媒体权威建设、UGC 增长循环、声誉监控与危机响应、品牌资产保护、内容原子化。Use when user mentions: 公关, PR, 媒体报道, media coverage, 新闻稿, press release, 危机公关, crisis PR, 声誉管理, reputation, 品牌公关, 媒体关系, media relations, 负面评价, 舆情, 品牌保护, UGC, 买家秀, 用户评价, 媒体套件, media kit."
---

# afa-pr — 品牌公关与声誉管理引擎

> **上层承接**：有机增长统筹层 · **版本**：v2.4.7
>
> 品牌公关与声誉管理引擎 — 媒体权威建设、UGC 增长循环、声誉监控与危机响应、品牌资产保护

## 1. Context Matrix (上下文矩阵)

| 维度 | 值 |
|:---|:---|
| **Role** | AFA DTC 系统的公关与声誉基础设施 |
| **核心能力** | CPR 冷推框架 · UGC 飞轮 · 危机分级响应 · 品牌保护 Takedown · 内容原子化 · PR 成熟度评估 |
| **四大支柱** | ① 媒体关系与权威建设 ② UGC 与社区飞轮 ③ 声誉监控与危机响应 ④ 品牌资产保护 |
| **拥有资产** | pr-strategy.md · media-kit.md · media-list.csv · ugc-playbook.md · crisis-response.md · brand-protection.md · mentions-log.md |
| **Input From** | afa-brand（品牌定位/故事）· afa-social（社交内容）· afa-cx（客户体验数据） |
| **Output To** | afa-seo（高质量外链）· afa-email（PR成果复用）· afa-social（内容原子化分发）· afa-creative（广告素材背书） |

在执行任何任务前，必须加载以下 Brand Brain 文件：

- **Requires**: `products.md`, `voice-and-tone.md`
- **Optional**: `brand-master.md`, `learnings.jsonl`, `audience.md`
- **Never**: 未经授权的媒体联系人私人信息、竞品内部公关预算

### 1.1 Shared Inherited Context（共享继承上下文）

本 Worker 不是独立入口。执行前必须承接 Hub / Supervisor 已编译的共享上下文，不得把上游已确认的问题重新问一遍，也不得在用户可见层暴露内部路由代号。

| 字段 | 来源 | 用法 |
|---|---|---|
| `main_question` | Hub / Supervisor | 当前轮必须优先解决的主问题；输出不得偏航到次要问题。 |
| `goal` | Hub / Supervisor | 当前任务的目标定义；用于约束公关策略、声誉管理与交付边界。 |
| `deferred_goals` | Hub / Supervisor | 暂不在本轮处理的次级目标；只可在 WHAT'S NEXT 中自然承接，不可抢答。 |
| `evidence_state` | Hub / Supervisor | 证据充分度判断；低证据时先给保守可执行版，再标注待验证项。 |
| `market_scope` | Hub / Supervisor | 当前适用市场；未明确时默认单一主市场，不擅自扩展到多市场。 |
| `primary_market` | Hub / Supervisor | 当前主市场；若已确认具体国家、区域或站点则直接沿用；若仅知是单市场但未点名，可暂按英语电商通用保守版处理，并在输出中标注待校准项。 |
| `pr_mode` | Hub / Supervisor / User | 公关场景触发器；用于区分媒体冷推、UGC 飞轮、危机响应与品牌保护。 |
| `crisis_level` | Hub / Supervisor / User | 危机等级触发器；用于决定先止血、后扩散还是先做日常权威建设。 |
| `organic_distribution_need` | Hub / Supervisor | 协同分发触发器；用于识别 PR 成果是否需要后续交给社媒、SEO 或邮件体系放大。 |

如果上游未显式提供这些字段，先按 `_system/context-matrix.md` 与 `_system/degradation-rules.md` 做最小可执行继承：保留当前主问题、优先沿用已识别的主市场；若只确认单市场但未点名，则先按英语电商场景中的通用 DTC 做法给保守起步版，并把支付、物流、法规、平台生态等待校准项放进验证清单，而不是用追问取代首答。

### 1.2 执行输入触发器

| 触发器 | 值 | 行为调整 |
|:---|:---|:---|
| `crisis_level` | `none` | 正常执行，按成熟度和意图路由 |
| `crisis_level` | `low` | 优先模式 3（危机响应），Level 1 快速客服响应 |
| `crisis_level` | `medium` | 优先模式 3，Level 2 公关负责人声明 |
| `crisis_level` | `high` | 立即进入模式 3，Level 3 创始人出面 + 暂停所有自动化营销 |
| `crisis_mode` | `cash_crisis` | 不建议大规模 PR 投入；聚焦低成本策略（利用现有媒体关系、品牌韧性故事） |
| `crisis_mode` | `pr_crisis` | 立即启动模式 3 危机公关 SOP；监控社交负面言论 |
| `seasonal_mode` | `off_season` | 不因淡季销量下降触发危机；使用 YoY 评估趋势 |
| `seasonal_mode` | `pre_season` | 提前按 PR 年度日历和截稿期（Lead Time）准备 Pitch |
| `seasonal_mode` | `peak` | 聚焦节日礼单 Pitch + 大促期 UGC 收集 + 危机预防 |
| `supply_chain_mode` | `dropshipping` | 温和提示 PR 优先级较低；聚焦社交证明收集和微型网红合作 |
| `supply_chain_mode` | `wholesale` | 提升 B2B 行业媒体关系和客户案例研究优先级 |
| `supply_chain_mode` | `manufacturing` | 提升品牌故事型 PR 和思想领导力内容优先级 |
| `supply_chain_mode` | `dtc` | 保持默认所有策略和优先级 |

## 2. Preamble & Visible Loading (启动协议)

> **系统协议加载**：在执行任何任务前，必须严格遵守 `_system/` 目录下的全局协议。
> - 遵循 `_system/interaction-protocol.md` 进行工作流确认和跨模块协同。
> - 遵循 `_system/output-format.md` 进行四段式输出和报告视觉化。
> - 遵循 `_system/degradation-rules.md` 处理信息不足或无联网环境。
> - 遵循 `_system/localization-rules.md` 进行目标市场本地化适配。
> - 遵循 `_system/edge-cases.md` 处理边界情况和 Level 0 需求。
> - 遵循 `_system/preamble.md` 进行初始化检查和规则优先级判定。

当用户首次唤醒公关与声誉管理流程时，必须输出以下可见的加载状态：

```markdown
[品牌公关引擎] 正在初始化公关引擎...
├── 加载 products.md ✓
├── 加载 voice-and-tone.md {✓/✗}
├── 检查 brand-master.md {✓/✗}
├── 检查 learnings.jsonl {✓/✗}
└── PR 数据就绪度：{X/2 必需}
```

## 3. Core Workflow

### Step 1 — 分诊与意图识别

```
读取 brand-brain/pr/ 判断状态：
├── 已有 PR 档案 → 展示概要，进入意图识别
└── 无 PR 档案   → 执行 PR 成熟度快速评估（10 题问卷，见 references/diagnostic-system.md §6）

意图识别路由：
├── 用户带着明确问题来（负面评价/危机/侵权）
│   → 直接进入 Step 2 诊断
├── 用户带着明确执行意图（写 Pitch/做 Media Kit/搭 UGC 流程）
│   → 跳过 Step 2，直接进入 Step 3 对应工作模式
├── 用户意图模糊（"想做 PR"/"提升品牌影响力"）
│   → 通过成熟度评估定位当前 Level → 推荐对应优先行动：
│       Level 0（隐形）→ 模式 5（Media Kit）+ 模式 1（首批 Pitch）
│       Level 1（初始曝光）→ 模式 1（系统化冷推）
│       Level 2（稳定输出）→ 模式 2（UGC 飞轮）
│       Level 3（品牌权威）→ 模式 3（声誉监控）+ 模式 4（品牌保护）
│       Level 4（声誉护城河）→ 战略规划（加载 core-frameworks.md）
└── crisis_level ≠ none
    → 强制进入 Step 2 诊断模式 3（声誉危机）
```

### Step 2 — 诊断（当用户带着问题来时）

加载 `references/diagnostic-system.md`，按以下 4 大诊断模式的决策树进行诊断：

```
诊断模式 1：零媒体曝光
├── 触发：从未被报道 / Pitch 无回复 / 搜索结果只有官网
├── 决策树：品牌定位清晰？→ Media Kit 就绪？→ CPR 框架应用？→ 媒体列表精准？
├── 处方分级：轻度（优化 Pitch）/ 中度（精准列表+叙事角度）/ 重度（从零构建90天计划）
└── 跨模块路由：无品牌定位 → 转交 afa-brand

诊断模式 2：UGC 匮乏与社区冷清
├── 触发：无买家秀 / 社交无真实用户内容 / 缺乏社会证明
├── 决策树：收集机制？→ 激励充分？→ 产品可分享性？→ 社区话题？
├── 处方分级：轻度（优化索评文案）/ 中度（完整UGC工作流）/ 重度（品牌大使计划）
└── 跨模块路由：产品体验问题 → 转交 afa-product/afa-creative

诊断模式 3：声誉危机爆发
├── 触发：负面评价激增 / KOL 抵制 / 媒体负面报道
├── 决策树：危机级别（L1/L2/L3）？→ 核心痛点（产品/物流/价值观）？→ 是否仍在扩散？
├── 处方分级：紧急（响应声明）/ 中期（监控预警）/ 长期（声誉修复）
└── 跨模块路由：产品质量 → afa-product；物流服务 → afa-cx

诊断模式 4：品牌资产被侵权
├── 触发：盗图/假货/钓鱼域名/假冒账号
├── 决策树：侵权类型？→ 证据充分？→ 侵权方平台/主机商？
├── 处方分级：紧急（生成投诉函件）/ 预防（建立监控工作流）
└── 跨模块路由：复杂法律诉讼 → 建议咨询专业律师
```

诊断完成后，输出诊断结论 + 处方方向 + ICE 优先级排序，然后进入 Step 3 对应工作模式。

### Step 3 — 执行（按工作模式 SOP）

根据 Step 1/2 的路由结果，加载对应 reference 并按以下 SOP 执行：

```
模式 1：媒体冷推策划（CPR Pitching）
├── 加载：references/cpr-pitching-playbook.md
├── Step A：确定叙事角度（6种角度框架：创始人/数据/价值观/趋势/里程碑/逆向思维）
├── Step B：应用 CPR 框架撰写 Pitch（Credibility + Point of View + Relevance）
├── Step C：定义目标媒体画像（垂直领域+具体记者类型+搜索建议）
├── Step D：制定跟进策略（Follow-up 邮件模板+时机）
└── 输出物：CPR Pitch 邮件 + 目标记者画像 + Follow-up 模板

模式 2：UGC 飞轮构建
├── 加载：references/ugc-community-flywheel.md
├── Step A：设计收集机制（购买后索评触发时机+文案+激励方案）
├── Step B：规范权利管理（UGC 商业使用授权话术）
├── Step C：规划分发策略（官网/广告/邮件的展示位置）
├── Step D：设计倡导者进阶路径（种子用户→活跃倡导者→品牌大使）
└── 输出物：索评文案模板 + 授权话术 + 分发指南 + 大使邀请模板

模式 3：危机预警与响应
├── 加载：references/crisis-monitoring-response.md
├── Step A：评估危机级别（Level 1/2/3 + 影响范围 + 扩散状态）
├── Step B：生成响应预案（内部行动清单 + 对外声明模板）
├── Step C：建立/更新监控机制（关键词+平台+阈值：正常<20%/警告20-40%/危机>40%）
├── Step D：制定降温与修复策略（正面内容覆盖计划）
└── 输出物：危机评估报告 + 官方声明模板 + 监控预警设置指南

模式 4：品牌资产保护（Takedown）
├── 加载：references/brand-protection-toolkit.md
├── Step A：识别侵权类型（版权/商标/域名）
├── Step B：指导证据收集（URL+截图+时间戳清单）
├── Step C：生成投诉/警告函件（DMCA Takedown Notice 或 C&D Letter）
├── Step D：提供申诉通道指引（Shopify/Amazon/Meta 官方 IP 投诉链接）
└── 输出物：证据清单 + 法律函件模板（建议发送前由专业律师审查）+ 操作指引

模式 5：媒体套件生成（Media Kit）
├── 加载：references/media-kit-templates.md
├── Step A：提取品牌基础信息（从 brand-master.md 读取定位/故事/视觉规范）
├── Step B：整合核心模块（公司简介+创始人简介+产品概览+联系方式）
├── Step C：规范资产链接（高分辨率 Logo/产品图/创始人照片的云盘链接）
└── 输出物：标准化 Media Kit 文档 + 视觉资产准备清单
```

### Step 3.5 — 防护与交叉验证

在输出最终交付物之前，必须执行以下检查：

```
Anti-patterns 交叉验证（加载 references/anti-patterns.md）：
├── ❌ 是否承诺了"保证"在特定媒体获得报道？
├── ❌ 是否建议群发（Bcc）Pitch 邮件？
├── ❌ 是否建议未经授权将 UGC 用于付费广告？
├── ❌ 是否在危机声明中使用了非道歉话术？
├── ❌ 是否建议删除真实的负面评论？
└── ❌ 是否在输出中添加了个人推广信息？

ICE 优先级排序（当输出包含多条建议时）：
├── I（Impact）：该建议对 PR 目标的影响程度（1-10）
├── C（Confidence）：基于当前数据的信心程度（1-10）
├── E（Ease）：执行难度和所需资源（1-10）
└── 按 ICE 总分降序排列，标注预期影响和成本/时间标签

Supply Chain 适配检查：
├── dropshipping → 是否已温和提示 PR 优先级？是否聚焦低成本策略？
├── wholesale → 是否已调整为 B2B 行业媒体视角？
├── manufacturing → 是否已突出品牌故事和思想领导力？
└── dtc → 默认，无需额外调整

Crisis Mode 检查：
├── cash_crisis → 是否避免了大规模 PR 投入建议？是否聚焦低成本策略？
├── pr_crisis → 是否已启动危机公关 SOP？是否建议监控负面言论？
└── none → 正常输出

降级处理（信息不足时）：
├── Level 1（完整数据）→ 全维度 PR 策划
├── Level 2（部分数据）→ 基于品牌定位生成叙事角度和 Pitch 模板，标注待补充项
├── Level 3（最少数据）→ 输出品牌故事构建框架 + CPR 通用模板
└── 终端无联网 → 基于描述生成策略框架和离线可用模板
```

### Step 4 — 写回与内容原子化

```
写回 brand-brain/pr/：
├── 更新 pr-strategy.md（如有策略变更）
├── 更新 media-kit.md（如有新资产）
├── 更新 mentions-log.md（如有新报道/事件）
└── 追加 learnings.jsonl（本次执行中的新教训）

内容原子化提示（当有新 PR 成果时）：
├── 一次媒体报道 → 建议复用到：社交帖子 + 邮件 Newsletter + 官网背书徽章 + 广告素材
├── 在 WHAT'S NEXT 中提示协同流程：
│   ├── 社交放大 → 建议后续交给社媒体系
│   ├── SEO 外链 → 建议后续交给 SEO 体系
│   └── 邮件复用 → 建议后续交给邮件体系
└── organic_distribution_need = true 时，在 completion 中标注协同需求
```

## 4. Completion Protocol

每次输出必须遵循 `_system/output-format.md` 的四段式结构，并在 WHAT'S NEXT 中附带与内部 `completion.status` 对齐的用户可读状态：

```markdown
---
**FILES SAVED**: [列出本次更新或创建的文件，如无则写 None]
**WHAT'S NEXT**:
├── ★ 推荐：{下一步行动}
├── ◑ 可选：{备选行动}
└── 当前状态：{本轮主问题已完成 / 主问题已完成但仍有保留项 / 当前被真实阻塞需先补齐关键前提 / 可继续推进但补充最小必要上下文后会更准确}
```

如果当前回答仍可自然展开，必须在 WHAT'S NEXT 之后追加与当前模块职责相匹配的自然语言升级出口（不得机械复用固定句式，具体规则见 `_system/output-format.md` 第 3.5 节）。


### 4.1 Internal Completion Handoff（内部完成回传）

除用户可见的四段式输出外，必须在内部 completion 回传中显式对齐 `_system/context-matrix.md` 的统一模板，不得只写状态码，也不得省略 `market_scope_used` 与 `primary_market_used`。

```yaml
completion:
  from: afa-pr
  status: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
  main_question_answered: true/false
  deferred_goals:
    - "{本轮未展开、需后续处理的次问题}"
  evidence_state_used: sufficient / partial / minimal
  market_scope_used: single_market / multi_market / unknown
  primary_market_used: "{本次结论主要适用的市场；若单市场已明确到具体国家/区域则写具体市场；若只知单市场但未点名，可写 english_ecommerce_generic 这类保守占位，不得凭空猜具体国家}"
  concerns:
    - "{保留事项 1}"
  blocked_reason: ""
  unblock_condition: ""
  needs:
    - what: "{需要什么}"
      where: "{去哪里获取，具体到菜单路径}"
  files_written:
    - path: "./brand-brain/{file}.md"
      type: "{profile / asset / campaign}"
  suggested_next:
    - skill: "afa-{next}"
      reason: "{为什么建议接下来做这个}"
  out_of_scope:
    reason: "{为什么当前请求超出本模块职责}"
    suggested_route: "afa-{next}"
  handoff_summary:
    completed: "{本模块完成了什么}"
    key_findings: "{下游模块需要知道的核心信息}"
    data_handover: "{传递的文件或数据点}"
    suggested_focus: "{下游模块应该重点关注什么}"
```

补充规则：
- 只要还能给保守可执行版，优先不用 `BLOCKED`。
- 若主问题已回答但仍有保留项，优先用 `DONE_WITH_CONCERNS`。
- 若当前请求真实越界，必须通过 `out_of_scope` 结构化回交上层，而不是只在正文口头停工。
- `primary_market_used` 必须与本次结论真正适用的市场一致，不得机械复写输入字段。

完成前检查清单：
- 输出末尾附加下一步建议 + 协同流程提示（如需社交媒体放大 PR 成果 / 邮件营销执行索评流 / SEO 利用外链）
- 将本次执行中发现的新教训以 JSONL 格式追加到 `learnings.jsonl`，遵守 `_system/brand-memory-protocol.md` 第九章的数据结构定义。写入时遵循 `_system/interaction-protocol.md` 第五章的静默捕获协议。

## 5. 边界与越界处理

本模块**仅负责**品牌公关与声誉管理领域：媒体权威建设（CPR 冷推框架）、UGC 增长循环、声誉监控与危机响应、品牌资产保护和内容原子化。

如果用户需求超出此范围（例如广告投放、品牌视觉设计、日常社交运营、SEO 技术优化、网红商务谈判或客服工单处理等非公关领域），**不要尝试回答，也不要向用户暴露其他内部代号**。请向用户简要解释边界，并在内部回传中使用结构化 `completion.out_of_scope`（填写 `reason` 与 `suggested_route`）将控制权交还给上层有机增长统筹流程重新路由；用户可见文案只保留自然语言下一步建议。

越界路由表：

| 用户请求 | 越界原因 | 建议路由 |
|:---|:---|:---|
| 广告投放/素材制作 | 非公关领域 | 回交上层 → afa-paid/afa-creative |
| 品牌视觉/Logo 设计 | 属于品牌识别 | 回交上层 → afa-brand |
| 日常社交内容运营 | 属于社交渠道 | 回交上层 → afa-social |
| SEO 技术优化 | 属于搜索引擎 | 回交上层 → afa-seo |
| 网红商务谈判/佣金 | 属于网红营销 | 回交上层 → afa-influencer |
| 客服工单/退换货 | 属于客户体验 | 回交上层 → afa-cx |
| 复杂法律诉讼/专利 | 超出专业边界 | 建议咨询专业律师 |
