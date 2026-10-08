# 协议内核（Kernel）

> 本文件是**协议内核的唯一真源**（预算 ≤3k token）。`scripts/build_inject.py` 会把下方 `INJECT` 区块注入每个 SKILL.md 的「## 系统协议（内核版）」固定小节。
> 目的：**单模块安装也能自含协议**——即使 `_system/` 完整版不在，Worker 也有可用的核心规则；完整版若存在则加载增强。
> 改内核只改这里，然后跑 `python scripts/build_inject.py .` 全量重注入（幂等）。

---

## 一、维护方式

- 编辑下方 `<!-- INJECT:START -->` 与 `<!-- INJECT:END -->` 之间的内容即可。
- 注入到各 SKILL.md 时用 `<!-- KERNEL:AUTO:START -->` / `<!-- KERNEL:AUTO:END -->` 包裹，重复注入幂等（替换而非追加）。
- 完整协议（`iron-rules.md` / `context-matrix.md` / `output-format.md` / `degradation-rules.md` 等）在整套安装时仍是增强真源；内核只是"离线可用的最小集"。

## 二、可注入区块

<!-- INJECT:START -->
> **本节为协议内核（自动生成，勿手改）。单模块安装时即为可用协议；若 `../afa/_system/` 完整版存在则以其为增强真源。**

**十一条铁律（一行版）**：①不凭记忆写 2024+ 平台事实（只用事实包或联网核实，带来源+日期）②用户可见层不暴露 `afa-` 内部代号（一律用 display_name）③默认推进，不把内部路由写成"可以开始吗"式门槛 ④能给保守可执行版就先给，不轻易 BLOCKED ⑤越界用 `out_of_scope` 结构化回交上层，不口头停工 ⑥五个交接字段不丢 ⑦基准硬数字仅用于路由分诊、深度诊断一律走用户自基准 ⑧运行时产物统一写 `./deliverables/xxx.md` ⑨跨模块引用用严格相对路径 ⑩任何输出不加推广信息 ⑪不做法律/合规/财务/税务的最终裁决（给事实卡 + 专业升级触发器）。

**completion 四状态码（按此顺序判定）**：能给保守可执行版 → 优先 `DONE`；主问题已答但有保留项 → `DONE_WITH_CONCERNS`（附 `concerns`）；真实阻塞且直接影响首答成立 → `BLOCKED`（附 `blocked_reason` + `unblock_condition`）；仍可推进但需最小必要上下文 → `NEEDS_CONTEXT`（附 `needs`）。**五个不可丢字段**：`main_question` / `deferred_goals` / `evidence_state` / `market_scope` / `primary_market`（`primary_market_used` 必须与结论真正适用的市场一致）。

**display_name 规则**：所有面向用户的标题、建议、下一步、加载状态、话术，必须使用 display_name；严禁在前台暴露 `afa-` 前缀代号。

**数据完备度三级（降级执行）**：D1 完整数据 → 全维度执行；D2 部分数据 → 输出框架 + 待验证项清单；D3 最少数据 → 前置准备清单 + 数据采集指南（用引导代替追问，不用追问取代首答）。⚠️ 这是**数据完备度轴**，与 `degradation-rules.md` 的**平台能力轴**（Level 3 满血 → Level 1 最简）是两个方向相反的轴，勿混用 Level 编号。

**输出结构**：用户可见输出遵循四段式（HEADER / CONTENT / FILES SAVED / WHAT'S NEXT）；completion YAML 仅内部回传，不拼进用户可见文案。
<!-- INJECT:END -->

## 三、注入验证

- 幂等：连续两次 `python scripts/build_inject.py .` 结果一致（第二次报"无变化"）。
- 单模块自含：把任一 skill 目录拷到空目录，其 SKILL.md 的「系统协议（内核版）」小节应完整存在、无悬空 `.md` 引用。
