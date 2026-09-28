# 诊断报告模板

> 本文件包含全局诊断输出诊断报告时使用的完整模板。
> 用于支持全面体检、专项深诊、急诊、复诊与数据缺口整理等全链路诊断场景，并统一诊断模板的结构与输出纪律。

---

## 模板一：全面体检报告

```markdown
# AFA DTC 全链路诊断报告

**品牌**：{brand_name}
**诊断日期**：{date}
**诊断模式**：全面体检 (Full Health Check)
**品牌阶段**：{stage}（0→1 / 1→10 / 10→100）
**数据基础**：{data_sources_description}
  例：「基于你提供的 Shopify 后台数据（30天）+ GA4 数据 + Meta Ads 后台数据」

---

## 核心发现（按严重度排序）

### 发现 1（严重）：{critical_finding_title}

**所属维度**：{dimension}
**数据对比**：
  - 你的数据：{your_data}
  - 行业基准：{benchmark}（仅作参考对照）
  - 差距：{gap}

**根因分析**：
  推理链：{evidence_1} → {evidence_2} → {conclusion}

**影响评估**：
  {定性描述影响，如「这是目前最大的利润出血点」}
  推算依据：{展示具体计算过程}
  假设声明：{列出所有假设}

---

### 发现 2（中等）：{finding_title}

[同上结构]

---

### 发现 3（关注）：{finding_title}

[同上结构]

---

## 行动方案（ICE 排序 + 成本标签）

### 本周必须做（ICE >7.0）

| # | 行动项 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 1 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {brief_calculation} | {owner_or_direction} |
| 2 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {brief_calculation} | {owner_or_direction} |

### 本月应该做（ICE 4.0-7.0）

| # | 行动项 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 3 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {brief_calculation} | {owner_or_direction} |

### 有空可以做（ICE 2.0-4.0）

| # | 行动项 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 4 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {brief_calculation} | {owner_or_direction} |

---

## 假设声明

以上分析基于以下假设，请核实：
- {assumption_1}
- {assumption_2}
- {assumption_3}

如果实际情况与假设不同，结论会相应调整。

---

## 数据补充建议

如果你手边能补充以下信息，我可以把判断收得更准：
- [ ] {missing_data_1}（例如：{source_name} 中与你当前问题直接相关的那部分数据）
- [ ] {missing_data_2}（例如：{source_name} 中与你当前问题直接相关的那部分数据）

---

## 下一步

建议执行顺序：先做 ①，完成后做 ②，③ 可以并行。
如需继续推进，下一步建议优先从第一个方案开始。

**建议复诊时间**：{next_checkup_date}
```

---

## 模板二：专项深诊报告

```markdown
# AFA DTC 专项诊断报告

**品牌**：{brand_name}
**诊断日期**：{date}
**聚焦维度**：{dimension_name}
**诊断深度**：深度钻探 (Deep Dive)
**数据基础**：{data_sources_description}

---

## 诊断背景

**触发原因**：{trigger_reason}
**速诊发现**：{quick_diagnosis_finding}
**本次目标**：深入分析 {dimension_name}，定位根因并出具行动方案

---

## 常见原因框架

{root_problem} 的常见原因包括：
A. {possible_cause_a}
B. {possible_cause_b}
C. {possible_cause_c}
D. {possible_cause_d}

---

## 数据验证

基于你提供的数据，逐一验证：

| 假设 | 验证数据 | 结果 | 状态 |
|:---|:---|:---|:---:|
| A. {cause_a} | {your_data} vs {benchmark} | {conclusion} | 排除/确认/待验证 |
| B. {cause_b} | {your_data} vs {benchmark} | {conclusion} | 排除/确认/待验证 |
| C. {cause_c} | {your_data} vs {benchmark} | {conclusion} | 排除/确认/待验证 |

---

## 根因定位

### 根因 1：{root_cause_title}

**推理链**：
  {evidence_1} + {evidence_2} → {conclusion}

**影响路径**：
  {root_cause} → {intermediate_effect} → {final_impact}

**推算依据**：
  {展示具体计算过程和假设}

---

## 行动方案（带成本标签）

| 优先级 | 行动项 | ICE | 成本标签 | 推算依据 | 建议承接方向 |
|:---:|:---|:---:|:---|:---|:---:|
| 1 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {calculation} | {direction} |
| 2 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {calculation} | {direction} |

---

## 假设声明

以上分析基于以下假设：
- {assumption_1}
- {assumption_2}

**建议复诊**：{next_checkup}
```

---

## 模板三：急诊报告

```markdown
# AFA DTC 急诊报告

**品牌**：{brand_name}
**诊断日期**：{date}
**紧急问题**：{emergency_description}
**数据基础**：{data_sources_description}

---

## 快速诊断

**常见原因**（按发生频率排序）：
1. {most_common_cause}
2. {second_cause}
3. {third_cause}

**基于你提供的数据判断**：
  推理链：{evidence_1} + {evidence_2} → 判断最可能原因是 {conclusion}

  注意：{data_limitation_note}
  例：「以上判断基于你描述的症状，如果能提供 {specific_data}，诊断会更精准」

---

## 立即行动

### 第一步（现在就做）：
{immediate_action_1}
成本：[{预算标签}] [{时间标签}] [{技能标签}]

### 第二步（今天内完成）：
{immediate_action_2}
成本：[{预算标签}] [{时间标签}] [{技能标签}]

### 第三步（本周内完成）：
{immediate_action_3}
成本：[{预算标签}] [{时间标签}] [{技能标签}]

---

## 注意事项

- {warning_1}
- {warning_2}

---

## 后续跟进

问题稳定后，建议做一次 {dimension} 的专项深诊，确保根因已彻底解决。
```

---

## 模板四：复诊报告

```markdown
# AFA DTC 复诊报告

**品牌**：{brand_name}
**复诊日期**：{date}
**上次诊断日期**：{last_diagnosis_date}
**间隔**：{interval}
**数据基础**：{data_sources_description}

---

## 指标变化追踪

| 指标 | 上次 | 本次 | 变化 | 趋势 |
|:---|:---:|:---:|:---:|:---:|
| {metric_1} | {old_value} | {new_value} | {change} | 改善/恶化/持平 |
| {metric_2} | {old_value} | {new_value} | {change} | 改善/恶化/持平 |

---

## 上次行动项执行情况

| # | 行动项 | 状态 | 效果 |
|:---:|:---|:---:|:---|
| 1 | {action_1} | 已完成/进行中/未执行 | {effect} |
| 2 | {action_2} | 已完成/进行中/未执行 | {progress} |

---

## 新发现

{new_findings}

---

## 下一阶段行动方案（带成本标签）

| 优先级 | 行动项 | ICE | 成本标签 | 建议承接方向 |
|:---:|:---|:---:|:---|:---:|
| 1 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {direction} |
| 2 | {action} | {score} | [{预算}] [{时间}] [{技能}] | {direction} |

**下次复诊时间**：{next_checkup_date}
```

---

## 模板五：learnings.jsonl 更新条目

```markdown
## {date} — AFA 全局诊断 — {diagnosis_topic}

### 诊断模式
{mode}（全面体检 / 专项深诊 / 急诊 / 复诊）

### 数据基础
{data_sources_description}

### 核心发现
1. {finding_1}
2. {finding_2}
3. {finding_3}

### 关键数据对比
| 指标 | 实际值 | 基准值（参考） | 状态 |
|:---|:---:|:---:|:---:|
| {metric} | {actual} | {benchmark} | {status} |

### 行动项
- [ ] {action_1} → {direction_1}（ICE: {score}）[{成本标签}]
- [ ] {action_2} → {direction_2}（ICE: {score}）[{成本标签}]

### 下次复诊关注
- {focus_1}
- {focus_2}
```

---

## 模板六：数据缺口清单

```markdown
## 诊断数据补充清单

以下信息如果能补充，会让诊断更精准；如果你暂时没有，我也会先基于当前信息给出起步判断，并明确标注假设与最关键补证点。

### 优先补充（最能提高判断准确度）

1. **{data_category_1}**
   - {specific_data_item} — 可从 {source} 中与你当前问题最直接相关的页面或报表查看
   - {specific_data_item} — 可从 {source} 中与你当前问题最直接相关的页面或报表查看

2. **{data_category_2}**
   - {specific_data_item} — 可从 {source} 中与你当前问题最直接相关的页面或报表查看

### 可选补充（有助于进一步收束结论）

3. **{data_category_3}**
   - {specific_data_item} — 可从 {source} 中与你当前问题最直接相关的页面或报表查看

4. **{data_category_4}**
   - {specific_data_item} — 可从 {source} 中与你当前问题最直接相关的页面或报表查看

---

如果你愿意，我可以按这份清单带你一起确认最关键的 1-2 项；如果你暂时拿不到数据，我们也可以先继续。
```

> **执行铁律**：
> - 不主动推送长篇工具设置教程。用户问了再教。
> - 不标注为行业参考（非用户实际数据）当作用户实际数据使用。
> - 用户没给数据时不等待卡住；先基于现有信息给出保守判断，显式标注假设与最关键补证点，不编造。

---

*本模板库确保全局诊断的每次输出都格式统一、专业、可执行，并统一遵守推导透明、数据基础声明、成本标签与数据补充提示的输出纪律。*
