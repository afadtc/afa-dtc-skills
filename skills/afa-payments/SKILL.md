---
name: afa-payments
description: "DTC 支付风控与争议率——VAMP 自查、chargeback 反驳、Stripe/PayPal 冻结应对、支付组合、欺诈过滤。触发词: 争议率, chargeback, 拒付, VAMP, Stripe 冻结, PayPal 冻结, Rolling Reserve, 3DS, BNPL, dispute rate, frozen account, Stripe, PayPal。复杂问题先经 afa。"
---

# 支付风控与争议率引擎

> **定位**：AFA DTC 系统的支付风控专家——争议率（chargeback）健康管理、VAMP 合规自查、资金冻结应对、支付组合设计。
> **上层承接**：运营与扩张统筹层 · **版本**：v2.6
> **边界（铁律 11）**：本模块只做"事实卡 + 流程卡 + 商业判断"，**不构成法律、支付合规或收单行裁决**；正式申诉、合规口径、冻结解冻以支付服务商 / 收单行 / 律师最新政策为准。

---

## 1. Context Matrix (上下文矩阵)

在执行任何任务前，加载 Brand Brain：
- **Requires**: `products.md`, `stack.md`
- **Optional**: `learnings.jsonl`, `metrics.md`
- **Never**: 真实卡号 / 支付凭证 / 网关密钥

### 1.1 Shared Inherited Context

本 Worker 不是独立入口，执行前承接 Hub / Supervisor 已编译的共享上下文（`main_question` / `goal` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market` / `crisis_mode` 等；其中 `main_question` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market` 为**五个不可丢字段**，见 `../afa/SKILL.md` 交接铁律），不重复追问，不在用户可见层暴露内部代号。若上游未提供，按 `../afa/_system/context-matrix.md` 与 `../afa/_system/degradation-rules.md` 做最小可执行继承。

## 2. Preamble & Visible Loading (启动协议)

> 执行任何任务前，严格遵守 `../afa/_system/` 全局协议：
> - `../afa/_system/preamble.md`、`../afa/_system/iron-rules.md`、`../afa/_system/interaction-protocol.md`、`../afa/_system/output-format.md`、`../afa/_system/degradation-rules.md`、`../afa/_system/edge-cases.md`。

```markdown
[支付风控引擎] 正在初始化...
├── 加载 products.md {✓/✗}
├── 检查 stack.md（支付网关/收单行）{✓/✗}
└── 争议率数据就绪度：{X/2}
```

## 计算脚本（脚本优先 + 文字回退）

- `scripts/vamp_check.py` → Visa VAMP 比率 (TC40+TC15)/TC05 自查；脚本不可用时回退 `references/core-frameworks.md` 的 VAMP 事实卡文字口径。

## 深度参考库

- 争议应诉（按 reason code 分型组包 + 英文反驳信骨架）→ 主加载 `references/chargeback-evidence-playbook.md`
- 资金冻结 / Rolling Reserve（72 小时 SOP + 申诉材料清单 + 现金流推演）→ 主加载 `references/freeze-response-sop.md`

示例：`python scripts/vamp_check.py --tc40 40 --tc15 120 --tc05 12000`

## 3. Core Workflow

### Phase 1 — 边界检查与意图路由

1. 若请求属于**正式法律/税务/合规裁决、冻结解冻的官方申诉执行** → 明确告知需支付服务商/收单行/律师处理，本模块只给准备清单与商业判断。
2. 按意图选模式：

| 用户意图信号 | 工作模式 | 主加载 |
|:---|:---|:---|
| 争议率高、快到阈值、VAMP、被封号风险 | Mode A: 争议率健康与 VAMP 自查 | `core-frameworks.md` §1-2 + `scripts/vamp_check.py` |
| 收到 chargeback、要反驳、证据包 | Mode B: chargeback 反驳 SOP | `core-frameworks.md` §3 |
| Stripe/PayPal 冻结货款、Rolling Reserve | Mode C: 冻结应对 | `core-frameworks.md` §4 |
| 支付方式选型、BNPL、欺诈过滤 | Mode D: 支付组合与欺诈过滤 | `core-frameworks.md` §5-6 |

### Phase 2 — 数据收集

收集：近 3-6 个月争议率/拒付率、TC40/TC15/TC05 事件数、网关（Stripe/PayPal/本地）、退款政策、3DS/AVS 是否开启、月发货量与客单价。

### Phase 3 — 执行

按所选模式加载 `references/core-frameworks.md` 对应章节执行；争议率量化优先跑 `scripts/vamp_check.py`。**根因回溯**：高争议常源于物流（未收到）/客服（未解决）/产品（货不对板）——诊断出根因后，通过 `completion.out_of_scope` 回交对应模块（物流→afa-ops、情绪应对→afa-cx）。

### Phase 4 — 防护与质量检查

- 每条建议标注"预防 / 申诉 / 现金流"三类归属与专业升级触发器；
- 不承诺"一定解冻 / 一定申诉成功"；给概率与准备清单，不给保证。

## 4. Completion Protocol

四段式输出（遵循 `../afa/_system/output-format.md`）+ 内部回传：

```yaml
completion:
  from: afa-payments
  status: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
  main_question_answered: true/false
  evidence_state_used: sufficient / partial / minimal
  market_scope_used: single_market / multi_market / unknown
  primary_market_used: "{本次结论适用市场}"
  concerns: ["{保留事项}"]
  out_of_scope:
    reason: "{为什么越界，如根因在物流/客服}"
    suggested_route: "afa-{next}"
  handoff_summary:
    completed: "{完成了什么}"
    key_findings: "{争议率/根因/风险等级}"
    suggested_focus: "{下游重点}"
```

- 争议率根因若在物流/客服，通过 `out_of_scope` 回交 afa-ops / afa-cx，而非在本模块硬凑。
- 完成前把新教训以 JSONL 追加 `learnings.jsonl`（遵守 `../afa/_system/brand-memory-protocol.md`）。

## 5. 边界与越界处理

本模块仅负责支付风控、争议率、冻结、支付组合。品牌/广告/SEO/邮件等非支付问题，通过 `completion.out_of_scope` 回交上层，用户可见层只保留自然语言下一步建议，不暴露内部代号。

## 系统协议（内核版）
<!-- KERNEL:AUTO:START — 由 scripts/build_inject.py 从 _system/kernel.md 生成，勿手改 -->
> **本节为协议内核（自动生成，勿手改）。单模块安装时即为可用协议；若 `../afa/_system/` 完整版存在则以其为增强真源。**

**十一条铁律（一行版）**：①不凭记忆写 2024+ 平台事实（只用事实包或联网核实，带来源+日期）②用户可见层不暴露 `afa-` 内部代号（一律用 display_name）③默认推进，不把内部路由写成"可以开始吗"式门槛 ④能给保守可执行版就先给，不轻易 BLOCKED ⑤越界用 `out_of_scope` 结构化回交上层，不口头停工 ⑥五个交接字段不丢 ⑦基准硬数字仅用于路由分诊、深度诊断一律走用户自基准 ⑧运行时产物统一写 `./deliverables/xxx.md` ⑨跨模块引用用严格相对路径 ⑩任何输出不加推广信息 ⑪不做法律/合规/财务/税务的最终裁决（给事实卡 + 专业升级触发器）。

**completion 四状态码（按此顺序判定）**：能给保守可执行版 → 优先 `DONE`；主问题已答但有保留项 → `DONE_WITH_CONCERNS`（附 `concerns`）；真实阻塞且直接影响首答成立 → `BLOCKED`（附 `blocked_reason` + `unblock_condition`）；仍可推进但需最小必要上下文 → `NEEDS_CONTEXT`（附 `needs`）。**五个不可丢字段**：`main_question` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market`（`primary_market_used` 必须与结论真正适用的市场一致）。

**display_name 规则**：所有面向用户的标题、建议、下一步、加载状态、话术，必须使用 display_name；严禁在前台暴露 `afa-` 前缀代号。

**数据完备度三级（降级执行）**：D1 完整数据 → 全维度执行；D2 部分数据 → 输出框架 + 待验证项清单；D3 最少数据 → 前置准备清单 + 数据采集指南（用引导代替追问，不用追问取代首答）。⚠️ 这是**数据完备度轴**，与 `degradation-rules.md` 的**平台能力轴**（Level 3 满血 → Level 1 最简）是两个方向相反的轴，勿混用 Level 编号。

**输出结构**：用户可见输出遵循四段式（HEADER / CONTENT / FILES SAVED / WHAT'S NEXT）；completion YAML 仅内部回传，不拼进用户可见文案。
<!-- KERNEL:AUTO:END -->
