# 支付风控核心框架（事实卡 + 流程卡）

> 本文件为 `afa-payments` 的内部参考。**非法律/支付合规裁决**；正式口径与申诉以支付服务商 / 收单行 / 卡组织最新政策为准。数据核实于 2026-07（税率/阈值随政策变动）。

---

## 1. 争议率健康与内部预警线

对广告驱动、CNP（无卡）为主的 DTC，争议率是**封号/冻结的悬顶之剑**。别等踩到卡组织阈值才行动：

- **设内部预警带 0.65%–0.9%**（早于监管阈值），触带即排查根因；
- 争议率 = 争议笔数 / 结算笔数；分子分母都要盯（促销期分母大、争议滞后）；
- 高争议根因八成在**物流（未收到）/ 客服（未解决）/ 产品（货不对板）**——先回溯根因，再谈申诉。

## 2. Visa VAMP 事实卡（由 afa-ops 迁入）

| 项 | 事实 |
|---|---|
| 阈值 | **2026-04-01 起，商户"欺诈 + 争议"合并阈值从 2.20% 降至 1.50%**（降约 32%） |
| 计算口径 | **(TC40 欺诈报告 + TC15 争议) ÷ TC05 结算笔数**，**仅计 CNP 交易**；月 **≥ 1,500 事件**才进入监控 |
| 罚金 | 商户 Excessive 档 **$8/笔**；收单行 0.5% / 0.7% 两档；12 个月内**首犯 3 个月宽限期** |

> 量化自查用 `../scripts/vamp_check.py`（脚本优先；不可用时按上表口径手算）。
> **来源**：[Chargebacks911：Visa VAMP 2026](https://chargebacks911.com/visa-acquirer-monitoring-program/)；[Visa 官方 Fact Sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)；[Basis Theory：VAMP 2026 更新](https://blog.basistheory.com/visa-acquirer-monitoring-program-2026-updates)；[MRC 合规指引](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2026/stricter-vamp-ratio-thresholds-are-now-in-effect-heres-how-to-stay-compliant)。

## 3. chargeback 反驳证据包 SOP（Representment）

收到 chargeback 后，按理由码组织**证据包**（不同理由码要的证据不同）：

1. **订单与授权**：订单号、金额、时间、授权码、**AVS / 3DS 结果**；
2. **履约证明**：物流单号 + **签收回执**（"未收到"类争议的核心）；
3. **沟通记录**：客服往来、退款/换货记录（证明已尝试解决）；
4. **政策披露**：结账页可见的退款/发货政策截图（证明用户知情）；
5. **产品一致性**：商品页与实物一致的证据（"货不对板"类）。

> 时限很紧（常 7-21 天，随收单行）；建议**建模板 + 留痕自动化**，别临时翻记录。反驳成功率因理由码而异，不承诺必胜。

## 4. Stripe / PayPal 冻结与 Rolling Reserve 应对

**预防姿势 >> 事后申诉**：

- **预防**：稳定发货节奏、低争议率、清晰政策、避免品类/金额突变（网关风控最怕"异常尖峰"）；分散网关，别把 100% 流水压一个账户。
- **Rolling Reserve**（滚动准备金）：网关按比例扣留一段时间的货款作缓冲——**当作现金流成本预先建模**，别指望它不发生（见 `../../afa-ops/references/unit-economics-calculator.md` 现金流口径）。
- **冻结时的申诉路径**：按服务商要求提交营业执照、履约证明、供应链凭证、争议处理记录；**保持沟通、别多账户腾挪**（易被判规避）。
- **现金流预案**：假设一段货款被冻结 30-120 天，备足周转，避免断链。

> 具体解冻以服务商裁决为准，本模块只给准备清单与现金流预案，不做保证。

## 5. 支付组合与 BNPL

- **组合设计**：卡 + PayPal + 本地支付（按目标市场）+ **BNPL**（Klarna/Afterpay/Affirm）——BNPL 常能**提升转化与客单价**（影响 AOV，见 `../../afa-aov/references/core-frameworks.md`），但有手续费与结算差异，计入落地成本。
- **退款政策与争议率联动**：过严的退款政策会把"退款"逼成"争议"——适度宽松的退款反而降 chargeback。

## 6. 欺诈过滤

- **3DS**（尤其欧盟 SCA 强制）：把欺诈责任转移给发卡行，同时可能损失少量转化——按市场与风险权衡；
- **AVS**（地址验证）、CVV、速度规则、黑名单、设备指纹；
- 用网关自带风控 + 第三方（如 Signifyd/Riskified 类）过滤高风险单，平衡"拦欺诈"与"误杀真单"。

---

## 归属与路由

- 争议率数字问题先由本模块接；诊断出根因是**物流** → 回交 `afa-ops`，**客服情绪** → 回交 `afa-cx`（通过 `completion.out_of_scope`）。
- **订阅扣款失败（通道侧）**：杠杆＝卡账户自动更新（Account Updater）+ 智能重试窗口 + 备付卡；挽留/催缴序列归留存引擎 Dunning 节（`../../afa-retain/references/subscription-management.md`），本模块只管通道配置面。
- **结账页支付方式的转化率视角**归转化引擎（`../../afa-convert/references/core-frameworks.md` 原则 5）；本模块管通道成本与风控面。
