# AFA DTC 路由评测（evals）

首版路由回归评测集。目的：在每次改动 description / 路由结构 / 内核后，用**可机判**的方式确认「问题被送到对的模块、且交接纪律没破」，而不是靠人肉回归。

## 怎么跑

```bash
python evals/run_evals.py .
```

纯 Python 标准库，无第三方依赖。存在任一结构性失败即非零退出（已接入 CI，见 `../.github/workflows/lint.yml`）。

## 四类断言（每条用例都会被检查）

| 断言 | 含义 | 判定方式 |
|:---|:---|:---|
| `routing_correct` | 该 query 应落到的模块存在，且 query 命中该模块 description 的触发词 | 解析目标 `SKILL.md` frontmatter 的「触发词:」列表，与 `user_input` / `trigger_hint` 做子串匹配 |
| `five_fields_present` | 目标模块承接了五个不可丢字段 | 在目标 `SKILL.md` 剥离内核注入块后的模块正文中查 `main_question` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market` |
| `no_codename_leak` | 用户可见样例不暴露内部代号 | 对 `expected_visible` 扫描 `afa-[a-z]+` |
| `cost_tagged` | 路由建议带成本 / 工作量标签 | `cost_tag ∈ {low, medium, high}` |

> 说明：这是**静态可机判**层，覆盖「路由是否可达 + 交接纪律是否在位 + 前台是否泄漏代号 + 是否带成本标签」。真正的语义路由质量（LLM 是否真的选对分支）属于人工 / LLM-as-judge 层，用例里的 `expected_visible` 同时充当该层的黄金样例，便于后续接入。

## 用例格式（JSONL，一行一例）

```json
{"id":"paid-01","business_line":"paid","user_input":"Facebook广告 CBO 跑不动，想调 Advantage+","expect_route":"afa-fb","expected_visible":"我先看账户结构，再决定 CBO 和 Advantage+ 的取舍。","cost_tag":"medium"}
```

字段：

- `id` — 用例编号
- `business_line` — 所属业务线（用于分组统计）
- `user_input` — 模拟用户输入
- `expect_route` — 期望最终归属模块（目录名）
- `expected_visible` — 期望的用户可见话术样例（必须无 `afa-` 代号）
- `cost_tag` — `low` / `medium` / `high`
- `trigger_hint`（可选）— 当 `user_input` 措辞不含显式触发词时，补充命中依据

## 用例文件

按路由分组，位于 `cases/`：

- `cases/routing_hub.jsonl` — 综合 / 未定位 → Hub 入口
- `cases/foundation.jsonl` — 品牌与产品基建线
- `cases/paid.jsonl` — 付费获客线
- `cases/organic.jsonl` — 有机增长线
- `cases/monetize.jsonl` — 变现与留存线
- `cases/scale.jsonl` — 运营与扩张线
- `cases/diagnose.jsonl` — 诊断与数据线
- `cases/english.jsonl` — 英文问句路由覆盖（跨业务线抽样）

## 怎么加用例

1. 在对应 `cases/*.jsonl` 追加一行；
2. 确保 `user_input` 含目标模块 description 的某个触发词（否则加 `trigger_hint`）；
3. `expected_visible` 用自然语言、**不写内部代号**；
4. 跑 `python evals/run_evals.py .` 应全绿。
