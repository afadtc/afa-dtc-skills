# 报告模板

> 本文件为转化率优化模块的内部参考文件，用于输出审计报告、优化方案和实验计划模板。
> **层级声明**：本文件作为 **internal-only** 的内部起草模板库使用，不得整段直接粘贴给用户。
> 如需整理为用户可见交付物，必须删除内部路由标签、模块代号和系统字段，只保留自然语言、业务角色与行动建议。
> **渲染规则**：本文件中的 KPI、样本量、窗口期、提升幅度、优先级权重与预估结果，只可作为参考区间、保守起点或待验证假设；不得写成统一健康线、既成事实或对品牌结果的确定性承诺。

---

## 模板 1：全链路 CRO 审计报告

```markdown
# CRO 审计报告

**品牌**：{brand_name}
**网站**：{url}
**审计日期**：{date}
**平台**：{platform}
**月均访客**：{monthly_visitors}
**当前转化率**：{current_cr}
**AOV**：${aov}
**月均营收**：${monthly_revenue}

---

## 执行摘要

**CRO 状态概览**

{score_emoji} {score_description}

**关键发现**：
1. {finding_1} → 推算依据：{reasoning_1}
2. {finding_2} → 推算依据：{reasoning_2}
3. {finding_3} → 推算依据：{reasoning_3}

**数据基础**：[说明本报告基于哪些数据源]

---

## 模块评分总览

| 模块 | 参考权重口径 | 状态 | 关键发现 |
|:---|:---|:---:|:---|
| 产品详情页 | 通常属于高权重模块 | {emoji} | {finding} |
| 结账流程 | 通常属于高权重模块 | {emoji} | {finding} |
| 购物车体验 | 结合品牌漏斗断点校准 | {emoji} | {finding} |
| 产品发现 | 结合入口流量与类目结构校准 | {emoji} | {finding} |
| 首页与导航 | 结合站型与导航复杂度校准 | {emoji} | {finding} |
| 移动端体验 | 若移动端占比高，权重通常上升 | {emoji} | {finding} |
| 信任与社证 | 若高客单或新客占比高，权重通常上升 | {emoji} | {finding} |
| 追加销售 | 在基础转化稳定后提高关注度 | {emoji} | {finding} |
| 购后体验 | 结合复购与退款问题校准 | {emoji} | {finding} |
| 网站速度 | 若性能波动明显，应前置处理 | {emoji} | {finding} |
| 无障碍 | 结合合规与体验要求校准 | {emoji} | {finding} |
| 页面 SEO | 结合自然流量角色校准 | {emoji} | {finding} |

---

## 详细发现（按营收影响排序）

### 🔴 严重 — 优先修复

#### 发现 #{n}：{title}
- **建议承接方向**：{owner_or_direction}
- **严重度**：🔴 严重
- **月度营收影响**：${impact}
- **问题描述**：{description}
- **数据支撑**：{data_evidence}
- **修复方案**：
  {detailed_fix}
- **平台实施**：
  - Shopify：{shopify_fix}
  - WooCommerce：{woo_fix}
  - 通用：{general_fix}
- **推算依据**：{reasoning_chain}
- **假设声明**：{assumptions}

---

### 🟠 高 — 近期优先修复
{repeat_format}

### 🟡 中 — 中期排期修复
{repeat_format}

### 🔵 低 — 有空时处理
{repeat_format}

---

## 行动计划

### 优先行动（当前周期）

| # | 行动 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 1 | {action} | {score} | [{budget}] [{time}] | {reasoning} | {owner_or_direction} |

### 短期行动（本月）

| # | 行动 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 1 | {action} | {score} | [{budget}] [{time}] | {reasoning} | {owner_or_direction} |

### 中期行动（本季度）

| # | 行动 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 1 | {action} | {score} | [{budget}] [{time}] | {reasoning} | {owner_or_direction} |

### 假设声明
以上行动方案基于以下假设：
- [假设 1]
- [假设 2]

---

## A/B 测试建议

| 优先级 | 测试假设 | 主要指标 | 推算依据 | 所需样本 |
|:---:|:---|:---|:---|:---:|
| 1 | {hypothesis} | {metric} | {reasoning} | {sample} |

---

## 下一步建议

1. **优先处理**：{immediate_action}
2. **当前周期推进**：{this_week_action}
3. **后续排期推进**：{this_month_action}
4. **持续观察与迭代**：{ongoing_action}

---

## 附录

### A. 行业基准对比
{benchmark_comparison}

### B. 竞品对比（如提供）
{competitor_comparison}

### C. 技术审计详情
{technical_details}
```

---

## 模板 2：落地页架构文档

```markdown
# 落地页架构文档

**品牌**：{brand_name}
**产品**：{product_name}
**目标**：{conversion_goal}
**流量来源**：{traffic_source}
**目标客群**：{target_audience}

---

## 页面策略

**核心价值主张**：{value_proposition}
**主要异议**：{top_objections}
**差异化定位**：{differentiation}

---

## 12 模块内容规划

### 模块 1：英雄区

**主标题**：{headline}
**副标题**：{subheadline}
**英雄图/视频**：{hero_visual_description}
**CTA**：{cta_text}
**信任微标**：
  - {trust_badge_1}
  - {trust_badge_2}
  - {trust_badge_3}

### 模块 2：痛点共鸣

**痛点 1**：{pain_point_1}
**痛点 2**：{pain_point_2}
**痛点 3**：{pain_point_3}

{repeat_for_all_12_modules}

---

## 文案初稿

{full_copy_for_each_module}

---

## 设计建议

**配色**：{color_scheme}
**字体**：{typography}
**布局**：{layout_notes}
**移动端适配**：{mobile_notes}

---

## A/B 测试计划

| 优先级 | 测试元素 | 变体 A | 变体 B | 主要指标 |
|:---:|:---|:---|:---|:---|
| 1 | {element} | {variant_a} | {variant_b} | {metric} |
```

---

## 模板 3：A/B 测试计划

```markdown
# A/B 测试计划

**测试名称**：{test_name}
**测试页面**：{page_url}
**测试日期**：{start_date} - {end_date}
**负责人**：{owner}

---

## 假设

**如果**我们 {change}，
**那么** {metric} 将会 {direction} {expected_lift}%，
**因为** {reasoning}。

---

## 测试设计

**测试类型**：A/B / A/B/C / 多变量
**流量分配**：{split}（如 50/50）
**最小样本量**：按当前流量、基准转化率与可接受误差计算的 {sample_size}
**最短运行时间**：{min_duration}（需结合流量稳定性与业务周期校准）
**统计显著性要求**：采用与当前测试设计相匹配的判定方法，并明确所用口径

### 变体 A（对照组）
{description_of_control}

### 变体 B（测试组）
{description_of_treatment}

---

## 指标

**主要指标**：{primary_metric}
**次要指标**：
  - {secondary_metric_1}
  - {secondary_metric_2}

**护栏指标**（不应恶化的指标）：
  - {guardrail_metric_1}
  - {guardrail_metric_2}

---

## 结果记录

**胜出变体**：{winner}
**主要指标提升**：{lift}%（p = {p_value}）
**次要指标变化**：{secondary_changes}
**定性洞察**：{qualitative_insights}

---

## 结论与下一步

**结论**：{conclusion}
**可推广的洞察**：{generalizable_insight}
**下一步测试**：{next_test}
**更新 learnings.jsonl**：{learning_to_record}
```

---

## 模板 4：PDP 优化方案

```markdown
# PDP 优化方案

**产品**：{product_name}
**产品页 URL**：{pdp_url}
**当前加购率**：{current_atc_rate}
**目标加购率**：{target_atc_rate}

---

## 当前状态评估

### 首屏黄金区
- 产品图片：{current_images_assessment}
- 产品信息：{current_info_assessment}
- CTA：{current_cta_assessment}
- 信任信号：{current_trust_assessment}

### 各段评估
{assessment_for_each_section}

---

## 优化方案

### 段 1：首屏黄金区优化
{detailed_optimization_plan}

### 段 2-9 优化
{repeat_for_each_section}

---

## 实施优先级

| # | 优化项 | 预期提升 | 难度 | 时间 |
|:---:|:---|:---:|:---:|:---:|
| 1 | {item} | {lift}% | 低/中/高 | {time} |

---

## A/B 测试建议

{test_suggestions}
```

---

## 模板 5：月度 CRO 复盘报告

```markdown
# 月度 CRO 复盘报告

**月份**：{month}
**品牌**：{brand_name}

---

## 关键指标趋势

| 指标 | 上月 | 本月 | 变化 | 目标 | 状态 |
|:---|:---:|:---:|:---:|:---:|:---:|
| 转化率 | {prev}% | {curr}% | {change} | {target}% | {status} |
| AOV | ${prev} | ${curr} | {change} | ${target} | {status} |
| 加购率 | {prev}% | {curr}% | {change} | {target}% | {status} |
| 购物车放弃率 | {prev}% | {curr}% | {change} | {target}% | {status} |
| 营收 | ${prev} | ${curr} | {change} | ${target} | {status} |

---

## 本月实验总结

| 实验 | 假设 | 结果 | 提升 | 状态 |
|:---|:---|:---|:---:|:---:|
| {test_name} | {hypothesis} | {result} | {lift}% | ✅/❌ |

---

## 关键洞察

1. {insight_1}
2. {insight_2}
3. {insight_3}

---

## 下月计划

| 优先级 | 行动 | 推算依据 | 负责人 |
|:---:|:---|:---|:---:|
| 1 | {action} | {impact} | {owner} |

---

## 更新 learnings.jsonl

{new_learnings_to_record}
```

---

*此模板库提供 CRO 工作中常见的内部起草模板。其数值、阈值和结构仅用于帮助形成专业判断与行动顺序，正式用户交付前必须结合真实数据、阶段和证据强度重新渲染。*
