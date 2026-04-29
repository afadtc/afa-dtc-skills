# 工作模式与模板

> 本文件为全局数据中枢的内部参考文件，用于沉淀本模块的工作模式、执行模板与交付骨架。
> **层级声明**：本文件默认作为 **internal-only** 的内部起草模板库使用，不得整段直接粘贴给用户。
> 如需整理为用户可见交付物，必须删除内部路由标签、模块代号和系统字段，只保留自然语言、业务角色与行动建议。
> **渲染规则**：本文件中的 KPI、渠道占比、NSM 目标、异常等级、ICE/优先级、时间窗口和任何推算结果，默认只可作为参考结构、保守起点或待验证判断；不得写成统一健康线或品牌当前既成事实。

---

## 一、数据体检工作流

### 1.1 工作流一：首次数据体检（Full Health Check）

**触发条件**：用户首次使用数据体检流程，或说“帮我做一次全面数据体检”

```
Step 1: 数据收集
  ├── 引导用户提供核心数据（使用数据收集模板）
  ├── 最低必要信息：优先收集月营收、月订单数、广告花费、主要渠道
  ├── 缺失数据标注为"—"，不做任何估算，列入数据缺口清单
  └── 将收集到的数据存入 brand-brain/metrics.md

Step 2: NSM 设定
  ├── 如果尚未设定 NSM → 启动 NSM 设定引导流程
  └── 如果已有 NSM → 跳过

Step 3: 基准线生成
  ├── 基于用户提供的数据计算指标画像（CVR、AOV、CAC、ROAS 等）
  ├── 如有历史数据，以历史最优值为参考线
  ├── 如无历史数据，引导用户设定阶段性目标或保守参考区间，不把行业均值写成品牌真实基线
  └── 将基准线存入 brand-brain/metrics.md

Step 4: 三层看板生成
  ├── 生成高管摘要层（核心指标 + 状态，数量按信息密度决定）
  ├── 生成渠道管理层（各渠道表现矩阵）
  └── 生成客户洞察层（如有足够数据）

Step 5: 异常扫描
  ├── 对所有指标进行三层异常检测
  ├── 对检测到的异常执行 IDA 三步诊断
  └── 生成异常预警列表

Step 6: 输出报告
  ├── 使用"首次体检报告"模板
  ├── 包含：整体健康度评分 + 三层看板 + 异常列表 + 行动建议
  └── 更新 brand-brain/learnings.jsonl
```

### 1.2 工作流二：周期性复检（Periodic Check-up）

**触发条件**：用户说"帮我看看这周/这个月的数据"

```
Step 1: 数据更新
  ├── 询问用户最新数据
  ├── 与 brand-brain/metrics.md 中的历史数据对比
  └── 更新 metrics.md

Step 2: 变化追踪
  ├── 计算所有指标的周环比/月环比变化
  ├── 标记显著变化（按波动背景与业务影响判断）
  └── 追踪上次体检发现的异常是否已改善

Step 3: 异常扫描
  ├── 执行三层异常检测
  ├── 对新发现的异常执行 IDA 诊断
  └── 对持续存在的异常升级严重度

Step 4: NSM 追踪
  ├── 更新 NSM 及其输入指标的最新值
  ├── 计算 NSM 健康度评分
  └── 评估是否在目标轨道上

Step 5: 输出报告
  ├── 使用"复检报告"模板
  ├── 重点展示：变化趋势 + 新异常 + NSM 进展
  └── 更新 learnings.jsonl
```

### 1.3 工作流三：专项数据分析（Deep Dive）

**触发条件**：用户说"帮我分析一下 Facebook 广告数据"、"看看转化漏斗"

```
Step 1: 确定分析范围
  ├── 用户想分析哪个维度？
  │   ├── 付费广告（Facebook / Google / TikTok）
  │   ├── 转化漏斗
  │   ├── 留存与复购
  │   ├── Email / SMS
  │   ├── SEO / 自然流量
  │   └── 客户分层（RFM）
  └── 确定时间范围

Step 2: 数据收集
  ├── 针对该维度收集详细数据
  └── 引导用户提供渠道特定的指标

Step 3: 深度分析
  ├── 使用该维度对应的诊断框架
  ├── 与用户历史数据、目标值或盈亏平衡线对比
  ├── 执行维度下钻分析
  └── 识别最大的机会和问题

Step 4: 输出报告
  ├── 使用"专项分析报告"模板
  ├── 包含：详细数据对比 + 问题定位 + 行动建议
  └── 如果发现严重问题 → 建议升级为全链路深度诊断
```

### 1.4 工作流四：实时异常响应（Alert Response）

**触发条件**：用户说"我的 ROAS 突然暴跌"、"转化率掉了"

```
Step 1: 快速确认
  ├── 确认异常指标和当前值
  ├── 确认异常开始时间
  └── 确认影响范围

Step 2: IDA 三步诊断
  ├── 异常确认与量化
  ├── 跨指标关联分析
  └── 维度下钻归因

Step 3: 快速输出
  ├── 使用“异常预警”输出格式
  ├── 给出初步归因和建议行动
  └── 如果问题复杂 → 建议升级为专项深度诊断

Step 4: 后续追踪
  ├── 将异常记录到 learnings.jsonl
  └── 在下次复检时追踪是否已解决
```

### 1.5 内部协作映射（仅供系统使用，不直接进入用户交付物）

```md
- 当专项分析发现问题已超出常规数据体检范围时：建议内部承接到 `afa-diagnose` 做深度诊断。
- 当异常响应确认问题复杂、跨维度或持续存在时：建议内部承接到 `afa-diagnose` 做专项深诊。
- learnings.jsonl 记录时如需保留系统标签，使用统一格式：`- [日期] [afa-dashboard] 具体发现（含量化数据）`。
```

---

## 二、数据驱动决策循环

> 数据的终极目标是驱动更好的商业决策。数据体检流程不仅帮你看数据，还帮你用数据。

### 2.1 五步决策循环

```
┌──────────────────────────────────────────────────┐
│                                                  │
│    ① 设定目标 ──→ ② 获取数据 ──→ ③ 分析洞察    │
│         ↑                              │         │
│         │                              ↓         │
│    ⑤ 衡量学习 ←── ④ 采取行动                    │
│                                                  │
└──────────────────────────────────────────────────┘
```

**① 设定目标**：
- 基于 NSM 罗盘，明确当前最重要的增长目标
- 将目标分解为可衡量的输入指标
- 设定时间框架和目标值

**② 获取数据**：
- 通过三层仪表盘全面监控数据
- 确保数据追踪准确（GA4 + 平台数据 + 第三方工具）
- 定期更新 brand-brain/metrics.md

**③ 分析洞察**：
- 利用 IDA 框架发现数据背后的"为什么"
- 提出可验证的假设
- 例："我们认为优化移动端结账流程有机会提升转化率，但具体幅度需要验证"

**④ 采取行动**：
- 基于假设，设计具体的实验
- 转交给对应的专项方向继续执行（如转化优化、付费投放等）
- 设定实验的成功标准和时间框架

**⑤ 衡量学习**：
- 评估实验结果，验证或推翻假设
- 将学到的知识记录到 learnings.jsonl（必须使用 Hub 统一四分类格式：有效的做法 / 无效的做法 / 用户洞察 / 行业变化；如需保留系统标签，参见上方 internal-only 区块）
- 用于指导下一轮的目标设定

### 2.2 假设驱动分析模板

```markdown
## 假设 #{number}

**观察**：{observation}
**假设**：如果我们 {action}，那么 {metric} 将会 {expected_change}
**依据**：{evidence_or_reasoning}
**实验设计**：{experiment_description}
**成功标准**：{success_criteria}
**时间框架**：{timeframe}
**后续跟进方向**：{follow_up_direction}

### 实验结果（待填写）
**实际结果**：{actual_result}
**结论**：假设 ✅ 验证 / ❌ 推翻
**学习**：{key_learning}
**下一步**：{next_action}
```

---

## 三、数据收集引导

### 3.1 极简数据收集模板

```
为了给你做数据体检，我需要一些基础数据。
不用一次全给，先给你有的，没有的我会标注为“—”，不会估算。

🔴 最低必要信息：
1. 月营收大概多少？（例：$50K）
2. 月广告花费大概多少？（例：$15K）
3. 你的品类是什么？（例：美妆/服饰/食品/保健品）

🟡 如果有更好（让体检更精准）：
4. 月订单数
5. 转化率
6. 各渠道的 ROAS
7. 复购率
8. Email 列表大小

🟢 锦上添花：
9. 各渠道详细数据（CTR、CPM、CPC）
10. 客户 LTV 数据
11. 退货率

🟡 成本数据（用于精确计算净利润率）：
12. 产品成本（COGS）：每个 SKU 的采购/生产成本
13. 物流成本：平均每单运费（包括包装）
14. 支付处理费：按实际支付服务商费率填写
15. 平台费用：Shopify 月费 + 应用订阅费

如果不确定具体数字，可以用以下估算方式：
  ├── COGS 可参考历史财务或供应链报价估算
  ├── 物流成本可参考近期订单结构与目的地分布估算
  └── 支付处理费可参考支付服务商账单估算
```

### 3.2 数据在哪里找

```
Shopify 后台：
  ├── Analytics → Reports → Sales over time（营收）
  ├── Analytics → Reports → Online store conversion rate（转化率）
  ├── Analytics → Reports → Returning customer rate（复购率）
  └── Analytics → Reports → Average order value（AOV）

Google Analytics 4：
  ├── Reports → Monetization → Ecommerce purchases（营收、转化）
  ├── Reports → Acquisition → Traffic acquisition（流量来源）
  └── Reports → Engagement → Pages and screens（页面表现）

Facebook Ads Manager：
  ├── Campaigns → Columns → Customize（自定义列）
  ├── 关键列：ROAS, CTR, CPM, CPC, Frequency, Reach
  └── 时间范围：选择你要分析的周期

Google Ads：
  ├── Campaigns → 选择时间范围
  ├── 关键列：Cost, Conversions, Conv. Value, ROAS, CPC
  └── Search Terms Report（搜索词报告）

Klaviyo：
  ├── Analytics → Dashboard（整体表现）
  ├── Analytics → Flows（自动化序列表现）
  └── Analytics → Campaigns（活动表现）
```

### 3.3 自动化数据接入 SOP

```
如果你觉得手动提供数据太麻烦，可以用以下方式快速导出：

Shopify 数据导出：
  ├── 方法 1：Shopify 后台 → Analytics → Reports → 选择报表 → Export
  ├── 方法 2：安装 Lifetimely / Triple Whale 等插件，自动生成报表
  └── 方法 3：截图 Shopify 后台数据页面，我来帮你提取数字

GA4 数据导出：
  ├── 方法 1：GA4 → Reports → 右上角 Share → Download file
  ├── 方法 2：GA4 → Explore → 自定义报表 → Export
  └── 方法 3：截图 GA4 概览页面，我来帮你解读

广告平台数据导出：
  ├── Meta Ads Manager → 选择时间范围 → Reports → Export
  ├── Google Ads → Reports → Predefined reports → Download
  └── TikTok Ads Manager → 报表 → 导出

推荐的一站式数据工具（按预算）：
  ├── 免费：Google Sheets + Shopify 原生报表（手动更新）
  ├── $29-99/月：Lifetimely（LTV 分析）/ BeProfit（利润追踪）
  ├── $100-300/月：Triple Whale（全渠道归因）/ Polar Analytics（自动看板）
  └── $300+/月：Northbeam（高级归因）/ Daasity（企业级 BI）
```

---

## 四、输出报告模板

### 4.1 首次体检报告模板

```markdown
# AFA DTC 数据体检报告

**品牌**：{brand_name}
**体检日期**：{date}
**基准来源**：{benchmark_source}（用户目标 / 历史最优 / 上月环比 / 盈亏平衡线）
**品类**：{category}

---

## 北极星指标

**{nsm_name}**：{nsm_value}
**健康度**：{health_score}（按当前评分口径展示） {status_emoji}
**目标**：{target_value}（差距：{gap}）

| 输入指标 | 当前值 | 目标值 | 状态 |
|:---|:---:|:---:|:---:|
| {input_1} | {value} | {target} | {emoji} |
| {input_2} | {value} | {target} | {emoji} |
| {input_3} | {value} | {target} | {emoji} |
| {input_4} | {value} | {target} | {emoji} |

---

## 高管摘要

| 指标 | 当前值 | 基准 | 差距 | 状态 |
|:---|:---:|:---:|:---:|:---:|
| 月营收 | ${value} | {prev_or_target} | {trend} | {emoji} |
| 新客收入占比 | {pct}% | {prev_or_target} | {gap} | {emoji} |
| 净利润率 | {pct}% | {prev_or_target} | {gap} | {emoji} |
| LTV:CAC | {ratio} | {prev_or_target} | {gap} | {emoji} |
| 复购率 | {pct}% | {prev_or_target} | {gap} | {emoji} |
| 异常数量 | {count} | 0 | - | {emoji} |

---

## 渠道表现

[渠道矩阵表格]

---

## ⚠️ 异常预警

[异常列表，按严重度排序]

---

## 建议行动

[基于数据发现的行动建议，含建议承接方向或负责人]

---

## 下次体检

建议 {timeframe} 后进行复检，届时重点关注：
1. {focus_1}
2. {focus_2}
```

### 4.2 复检报告模板

```markdown
# AFA DTC 数据复检报告

**品牌**：{brand_name}
**复检日期**：{date}
**上次体检**：{last_date}
**间隔**：{interval}

---

## 指标变化追踪

| 指标 | 上次 | 本次 | 变化 | 趋势 |
|:---|:---:|:---:|:---:|:---:|
| {metric} | {old} | {new} | {change} | {emoji} |

↑ 改善  ↓ 恶化  → 持平

---

## NSM 进展

{nsm_name}：{old_value} → {new_value}（{change}）
目标进度：{progress}（按当前阶段口径展示）

---

## ⚠️ 异常更新

### 已解决的异常
- {resolved_anomaly}

### 持续存在的异常
- {persistent_anomaly}（已持续 {duration}）

### 新发现的异常
- {new_anomaly}

---

## 建议行动

[更新后的行动建议]
```

---

## 五、Brand Brain 数据文件规范

### 5.1 metrics.md 文件结构

```markdown
# {Brand Name} 核心指标档案

## 北极星指标
- NSM：{nsm_name}
- 当前值：{value}
- 目标值：{target}
- 设定日期：{date}

## 输入指标
| 指标 | 当前值 | 目标值 |
|:---|:---:|:---:|
| {input_1} | {value} | {target} |
| {input_2} | {value} | {target} |
| {input_3} | {value} | {target} |
| {input_4} | {value} | {target} |

## 基准线
- 品类：{category}
- 基准来源：{用户目标 / 历史最优 / 上月环比}
- 用户目标（如有）：
  | 指标 | 目标值 | 设定日期 |
  |:---|:---:|:---|

## 历史数据
| 月份 | 营收 | 订单数 | 转化率 | AOV | ROAS | 复购率 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| {month} | ${value} | {value} | {pct}% | ${value} | {value}x | {pct}% |

## 异常记录
| 日期 | 异常指标 | 描述 | 状态 |
|:---|:---|:---|:---:|
| {date} | {metric} | {description} | ✅/⏳/❌ |
```
