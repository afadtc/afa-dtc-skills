# 基准数据治理规范（Benchmark Governance）

> 本文件为 `_system` 层的全局规范，是全库**基准数字（benchmark）**的唯一治理真源。凡 references 中出现的行业/平台基准数值，其来源标注、新鲜度与使用边界，统一以本文件为准；各基准文件只继承、不平行重定义。

---

## 一、三字段规则（每张基准表必带）

每一张基准表 / 每一组基准数字，必须标注三字段：

| 字段 | 含义 | 缺失时的降级 |
|---|---|---|
| **来源（Source）** | 数据出处（机构 + 报告名 / 链接） | 写不出 → 标"内部经验估算" |
| **采集窗口（Window）** | 数据对应的时间区间（如 2025-Q1、2024-2025） | 写不出 → 标编制月份 |
| **适用地区（Region）** | 数据适用的市场（如 US DTC、全球、EU） | 写不出 → 标"通用参考，需按目标市场校准" |

**降级写法**（三字段任一写不出时统一用）：

> 内部经验估算，编制于 YYYY-MM；非官方数据，使用时结合品牌自有历史校准。

## 二、硬数字仅限"路由分诊"

沿用基准分层规则（`../references/diagnostic-rules.md`、`../references/benchmark-data.md`、`../../afa-diagnose/references/industry-benchmarks.md` 三方互注）：

- **硬编码阈值**（健康 / 警告 / 危险三档等）**只允许**出现在 Hub 路由分诊场景——用于快速判断问题属于哪个领域；
- **进入深度诊断后一律改用用户自基准**（基于品牌自身历史数据与目标），不得把跨品牌基准当成统一健康线。

## 三、分层新鲜度（单人可维护）

不同类型的基准，过期策略不同——避免"所有数字都要每月刷"的不可维护负担：

| 类型 | 新鲜度要求 | 说明 |
|---|---|---|
| **平台功能类**（广告平台费率、算法、产品能力） | `last_verified` ≤ 6 个月 | 变化快，过期即需复核 |
| **法规 / 合规类**（TCPA、de minimis、VAMP、ADA、订阅法） | **事件驱动更新** | 不设固定周期；相关判例 / 生效日一变即更新 |
| **方法论类**（公式、框架、评分维度） | **不设过期** | 稳定，单人可长期维护 |

> **集中复核提醒（v2.6 引入）**：GEO / agentic commerce / 支付风控三块新增内容中的平台功能类事实（Meta Andromeda、TikTok GMV Max 默认化、Google AI Max、agentic commerce / ACP·UCP·Instant Checkout 等）多标注 `last_verified: 2026-07`，按上表「平台功能类 ≤ 6 个月」将于 **2027-01** 前后集中到期——建议把 2027-01 作为一次集中复核窗口统一校验这批事实，避免半年后逐条遗漏。

## 四、长期基准数据源订阅清单

解决"数字从哪来"的根本问题——以下为可长期对表的权威源（写基准时优先引用并标注采集窗口）：

| 来源 | 覆盖（引用示例） | 用于模块 |
|---|---|---|
| [Triple Whale Benchmarks](https://www.triplewhale.com/blog/ecommerce-benchmarks) | 2 万+ DTC 商家实时聚合；2025 中位 ROAS 2.04 | fb / gg / tt / paid / dashboard |
| [Klaviyo Benchmarks](https://www.klaviyo.com/products/email-marketing/benchmarks) | 18.3 万客户；flows 以 5.3% 发送量贡献 41% 邮件收入，RPR ≈ campaign ×18 | email / sms / retain |
| [Varos](https://www.varos.com/) | 分品类月更（补剂类 Meta CPA $45.62 vs 大盘 $30-35，2025-04） | fb / tt / diagnose |
| [分流量来源 CVR](https://eightx.co/blog/average-ecommerce-conversion-rate-by-traffic-source-2026) | email 4.2% / referral 4.2% / organic 2.8% / paid social 1.1% | convert / dashboard |
| Recharge State of Subscription（年度） | 订阅留存 / 流失 | retain |
| Gorgias / Zendesk CX 年报 | FRT / CSAT / 偏转率 | cx |

> 引用上表数字时，务必带上其采集窗口与适用地区；跨期或跨市场使用前先按本规范第一、二条校准。

## 五、继承关系

| 主题 | 上位真源 |
|---|---|
| 基准三字段、硬数字边界、分层新鲜度 | 本文件 |
| references 头部 / 语言 / 抬头规范 | `reference-authoring-rules.md` |
| frontstage / backstage 裁决 | `iron-rules.md` |

> 核实于 2026-07。数据源清单与关键数字随平台 / 机构更新，按第三条分层新鲜度维护。
