# AFA DTC 上下文编译协议

> **协议层级**：全局强制 · afa Hub 路由时必须遵守
>
> **版本**：v2.4.6
>
> **来源说明**：本文件为当前生效的全局协议，供 Hub、Supervisor 与 Worker 统一遵守。
>
> **v2.0.8 变更**：回传格式中 `status` 升级为四状态码枚举（DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT），新增 `handoff_summary` 字段

当 afa 将任务路由到某个专业模块时，必须为该模块编译精准的上下文包。这是整个系统质量的关键——给太多上下文会稀释焦点，给太少会导致泛化输出。

---

## 一、上下文编译规则

```
规则 1：只传该模块需要的
  按 Context Matrix 严格执行，不多传一个文件

规则 2：传完整的需要的
  不要摘要化或截断，传完整文件内容

规则 3：标注新鲜度
  每个传递的文件标注最后更新日期

规则 4：传递用户原话
  用户的原始需求描述必须完整传递，不要替用户总结

规则 5：传递诊断结论
  如果经过了诊断流程，将诊断结论和证据链一并传递

规则 6：显式传递主问题
  Hub 必须明确写出本轮要先解决的 main_question，避免 Worker 平铺多个目标

规则 7：把次问题放入 deferred_goals
  与主问题同时出现但不应抢占首答主体的目标，必须进入 deferred_goals

规则 8：显式标注证据状态
  传递 evidence_state（sufficient / partial / minimal），帮助 Worker 判断输出强度与保守程度

规则 9：显式标注市场范围
  传递 market_scope（single_market / multi_market / unknown）和 primary_market，避免把跨市场问题混成单一结论；若仅知单市场但未点名具体国家，允许把 `primary_market` 暂记为 `unknown`，由下游在输出中使用保守占位说明
```

---

## 二、上下文交接格式

```yaml
# 上下文交接 → afa-{module}
business: "{品牌描述}"
goal: "{用户本次的具体目标}"
main_question: "{本轮必须优先回答的主问题}"
deferred_goals:
  - "{先记录、后展开的次问题 1}"
  - "{先记录、后展开的次问题 2}"
evidence_state: sufficient / partial / minimal
market_scope: single_market / multi_market / unknown
primary_market: "{主市场；若未知写 unknown}"
stage: "{Level 0 / 0→1 / 1→10 / 10→100 / 衰退期}"
health_status: "{健康 / 亚健康 / 危机}"  # v1.9 新增
crisis_mode: none/cash_crisis/pr_crisis  # v1.9 新增，危机类型枚举，子 Skill 据此切换对应止血模式
seasonal_mode: none/pre_season/peak_season/off_season  # v1.9.3 新增，季节阶段枚举，子 Skill 据此调整策略和 KPI 基准
supply_chain_mode: dropshipping/wholesale/manufacturing/dtc  # v1.9.5 新增，供应链模式枚举，子 Skill 据此调整建议优先级排序
premium_tier: "Tier 1-4"  # v1.9.8 新增，四维溢价阶梯的当前主攻层级（非用户会员等级），子 Skill 据此对齐策略
urgency_level: CRITICAL/HIGH/MEDIUM/LOW  # v2.2.8 补全，紧急程度枚举，由诊断引擎或 Hub 根据用户情境判定，子 Skill 据此调整策略优先级和时间框架
user_request: "{用户的原始需求描述}"
diagnosis:
  root_cause: "{诊断出的根因，如有}"
  evidence: "{证据链，如有}"
  priority: "{ICE 评分，如有}"
brand_brain:
  # 仅包含该模块需要的文件
  voice_and_tone: "{完整内容 或 '尚未创建'}"
  products: "{完整内容 或 '尚未创建'}"
  store: "{完整内容 或 '尚未创建'}"  # 店铺基础信息（store_url、平台、支付方式、配送区域、退换货政策）
  # ... 按 Context Matrix 决定传哪些
relevant_learnings:
  - "{与本次任务相关的历史教训 1}"
  - "{与本次任务相关的历史教训 2}"
expected_output:
  files: ["{预期输出文件列表}"]
  update_assets: true/false
return_to: afa
```

---

## 二-B、全局枚举变量定义

以下变量在上下文交接中被引用，必须有明确的枚举值定义：

```
evidence_state (证据状态)：
  sufficient → 证据充足，可给较强判断和更完整展开
  partial    → 证据部分成立，应给保守版并标注待验证项
  minimal    → 证据极少，只能给低强度、低扰动、可回退建议

market_scope (市场范围)：
  single_market → 已锁定为单市场视角；若国家未点名，可先给单市场保守版，但不得伪装成已确认具体国家
  multi_market  → 涉及多个市场，必须拆开或显式标范围
  unknown       → 尚未确认市场范围，默认给粗颗粒度保守结论

urgency_level (紧急程度)：
  CRITICAL  → 影响核心转化链路或导致严重亏损（需立即修复）
  HIGH      → 显著影响关键指标（1-3天内修复）
  MEDIUM    → 常规优化项（随迭代周期修复）
  LOW       → 长期建设项

supply_chain_mode (供应链模式)：
  dropshipping   → 一件代发（低库存风险，长物流时间）
  wholesale      → 批发囤货（中等库存风险，标准物流）
  manufacturing  → 自有工厂/深度定制（高库存风险，可控物流）
  dtc            → 直接面向消费者（系统默认值）

seasonal_mode (季节阶段)：
  none           → 无季节性影响（系统默认值）
  pre_season     → 旺季前备战期（提前 4-6 周，重点备货、素材储备、受众蓄水）
  peak_season    → 旺季执行期（包含 BFCM、圣诞等大促，重点放量和转化）
  off_season     → 淡季调整期（重点降本、测试、素材迭代、品牌建设）

crisis_mode (危机类型)：
  none           → 无危机（系统默认值）
  cash_crisis    → 现金流危机（营收断崖、ROAS 崩盘、库存积压，切换止血模式）
  pr_crisis      → 公关危机（负面舆情、媒体曝光、产品召回，切换声誉修复模式）

stage (品牌阶段)：
  Level 0    → 无产品/无网站/纯概念
  0→1       → 从零到一，验证 PMF
  1→10      → 初始增长，建立可复制模式
  10→100    → 规模化扩张
  衰退期     → 业务下滑，需要止血或转型

health_status (健康状态)：
  健康       → 核心指标正常或上升
  亚健康   → 部分指标下滑但未达危机线
  危机       → 核心指标严重下滑或现金流断裂
```

---

## 三、模块完成回传格式

以下 completion 结构是 **Worker / 全局引擎 / Supervisor 共用的系统真源**。任何模块都不得自造另一套回传语法；允许的差异只体现在字段是否适用，而不体现在字段名或语义上。

> 本节所有字段、`afa-*` 代号与 YAML 结构**仅供系统内部回传与路由使用**。它们不得直接出现在用户报告、WHAT'S NEXT、页脚、推荐区块、行动表格或任何用户可复制成品中；用户可见层一律改用 `display_name` 或自然语言渲染。

字段分层：

- **核心必填字段**：`from`、`status`、`main_question_answered`、`deferred_goals`、`evidence_state_used`、`market_scope_used`、`primary_market_used`、`files_written`、`suggested_next`
- **条件字段**：`concerns`、`blocked_reason`、`unblock_condition`、`needs`、`out_of_scope`、`handoff_summary`；仅在对应状态或对应场景下填写
- **Supervisor 扩展字段**：`workers_executed`、`assets_added`、`learnings`；Worker 与全局引擎无需伪造这些汇总字段

```yaml
completion:
  from: afa-{module}
  status: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
  # ── 四状态码说明（详见 interaction-protocol.md 第八章）──
  # DONE               → 主问题已被回答，且本轮任务完整完成
  # DONE_WITH_CONCERNS → 主问题已被回答，但仍有保留事项（附 concerns 字段）
  # BLOCKED            → 任务被真实阻塞，且阻塞会直接影响首答成立（附 blocked_reason + unblock_condition）
  # NEEDS_CONTEXT      → 仍可继续推进，但需要最小必要上下文以提高准确度（附 needs 字段）
  main_question_answered: true/false
  deferred_goals:
    - "{本轮未展开、需后续处理的次问题}"
  evidence_state_used: sufficient / partial / minimal
  market_scope_used: single_market / multi_market / unknown
  primary_market_used: "{本次结论主要适用的市场；若单市场已明确到具体国家/区域则写具体市场；若只知单市场但未点名，可写 english_ecommerce_generic 这类保守占位，不得凭空猜具体国家}"
  concerns:            # 仅 DONE_WITH_CONCERNS 时填写
    - "{保留事项 1}"
    - "{保留事项 2}"
  blocked_reason: ""   # 仅 BLOCKED 时填写
  unblock_condition: "" # 仅 BLOCKED 时填写
  needs:               # 仅 NEEDS_CONTEXT 时填写
    - what: "{需要什么}"
      where: "{去哪里获取，具体到菜单路径}"
  workers_executed: [afa-{worker1}, afa-{worker2}, ...]  # 仅 Supervisor 填写实际执行的 Worker 列表
  files_written:
    - path: "./brand-brain/{file}.md"
      type: "{profile / asset / campaign}"
  assets_added:        # 可选，仅在 Supervisor 创建了新资产时填写
    - name: "{资产名称}"
      type: "{资产类型}"
      campaign: "{关联活动}"
  learnings:           # Supervisor 可填；Worker / 全局引擎按实际需要填写，不强制伪造
    - "{本次执行中发现的新教训}"
  suggested_next:
    - skill: "afa-{next}"
      reason: "{为什么建议接下来做这个}"
  out_of_scope:        # 可选，仅在职责越界需回交上层时填写
    reason: "{为什么当前请求超出本模块职责}"
    suggested_route: "afa-{next}"
  handoff_summary:     # 可选，仅在跨模块协同场景下填写
    completed: "{本模块完成了什么}"
    key_findings: "{下游模块需要知道的核心信息}"
    data_handover: "{传递的文件或数据点}"
    suggested_focus: "{下游模块应该重点关注什么}"
```

### 三-A、状态码使用顺序

为避免 Worker / 全局引擎把低信息场景误写成硬阻塞，统一按以下顺序判定：

1. **只要还能给保守可执行版，优先不用 `BLOCKED`。**
2. **仅当缺口会直接阻断主问题首答成立时，才允许 `BLOCKED`。**
3. **如果主问题已回答，但仍有保留或待验证项，优先用 `DONE_WITH_CONCERNS`，而不是 `NEEDS_CONTEXT`。**
4. **如果只是需要最小补充信息来提高精度，但不影响先给一版保守方案，优先用 `DONE_WITH_CONCERNS` 或 `NEEDS_CONTEXT`，不得直接写成阻塞。**
5. **如果请求真实越界，应通过 `out_of_scope` 结构化回交上层；不得只在正文口头说“超出范围”而不回传路由信息。**

### 三-B、市场字段一致性约束

- `market_scope_used` 表示本次答案的适用范围，而不是用户输入的原样复述。
- `primary_market_used` 表示**本次结论主要适用的市场**，不是机械复写输入字段。
- 若 `market_scope_used = single_market` 且已确认具体国家/区域，则 `primary_market_used` 应填写对应具体市场。
- 若仅知“这是单市场问题”但具体国家未点名，则 `primary_market_used` 可填写 `english_ecommerce_generic` 等保守占位，明确它是为了支撑通用 DTC 起步版，而不是声称已确认具体国家。
- 在上述占位场景下，正文必须同步标注支付、物流、法规、平台生态等部分需待确认主市场后再校准。
- 若当前信息不足以锁定主市场，则应显式维持粗颗粒度结论，并在 `deferred_goals`、`concerns` 或 `needs` 中说明剩余市场待后续展开。
