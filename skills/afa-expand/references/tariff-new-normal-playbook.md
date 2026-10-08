# 关税新常态操盘手册（de minimis 取消后）

> 本文件为 `afa-expand` 的深度参考文件，用于在**关税 / de minimis 新常态**下识别成本冲击、应对框架、待补资料与专业升级触发器。
>
> **重要边界**：本文件不构成法律、税务、海关、申报或贸易合规建议。凡涉及正式税率、HS 归类、原产地判定、清关操作、申报口径、退税或处罚处理，必须升级给报关行、关务/税务顾问或律师，并以官方最新信息为准。本文件只服务"商业判断与风险筛查层"。

---

## 一、如何使用本参考

本参考服务四类任务：①判断关税/清关变化对某条供应链或某个市场的成本冲击有多大；②在定价与选品前把关税计入真实落地成本；③在信息不全时输出待补资料清单；④明确哪些问题一出现就必须升级给报关行/关务顾问。它**不**替用户做 HS 归类、申报或税率裁决。

## 二、事实与时间线（截至 2026-07）

### 2.1 美国：de minimis 已对所有国家终止

- **2025-08-29 起，美国取消 $800 de minimis 免税待遇——对所有国家、所有价值、所有运输方式**：每一票商业货物都需正式报关、10 位 HTS 归类、全额缴税（此前中国大陆/香港更早，自 2025-05 起关闭）。
- 冲击实测：**新规生效 5 周内，经邮政入美的包裹量下降约 70.7%**。
- **2026-02-20，美国以行政令继续维持该暂停**，截至 2026 年年中无恢复迹象；**2026-02-28 起，承运商对邮政包裹须统一采用从价税（ad valorem）计征**（按原产地对应的 IEEPA 有效税率 × 货值）。
- 影响：过去靠"小包直发 + 免税"跑通的低价跨境模型基本失效，成本结构被重写。

> **来源**：[White House：继续暂停 de minimis（2026-02）](https://www.whitehouse.gov/presidential-actions/2026/02/continuing-the-suspension-of-duty-free-de-minimis-treatment-for-all-countries/)；[DCL：de minimis 终结实操](https://dclcorp.com/blog/fulfillment/end-of-the-de-minimis/)；[Practical Ecommerce：入美邮政量 -70.7%](https://www.practicalecommerce.com/ecommerce-after-de-minimis-tariff-exemption)；[EY：美国暂停低值免税](https://www.ey.com/en_gl/technical/tax-alerts/us-suspends-duty-free-de-minimis-treatment-for-low-value-shipments)。核实于 2026-07。

### 2.2 欧盟：€150 免税也在退场（分阶段）

- **2025-11-13，欧盟理事会表决通过逐步取消 €150 关税免税额**。
- **约 2026-07-01 起（过渡期）**：€150 免税取消，低值包裹改征**临时统一 €3/件**关税，过渡至 2028-07-01；另有 EU 层面**约 €2/HS 编码处理费**（不晚于 2026-11-01），两者叠加约 **€5/HS**。
- **2028-07-01**：随 EU Customs Data Hub 上线，€150 免税彻底移除，改按逐项 HS 归类正常征税。

> **来源**：[EU 委员会：2026 起取消 €150 免税阈值](https://taxation-customs.ec.europa.eu/news/e-commerce-150-eur-customs-duty-exemption-threshold-be-removed-2026-2025-11-13_en)；[EU 委员会：低值进口临时统一费（至 2028-07-01）](https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en)；[Portless：EU de minimis 变化](https://www.portless.com/blogs/the-eu-is-ending-de-minimis-exemptions-what-your-brand-needs-to-know)。核实于 2026-07。

## 三、应对框架（商业判断层，不做申报裁决）

| 方向 | 做法 | 适用信号 |
|---|---|---|
| **本土备货** | 批量进口到目的国仓再本地发货，**按批发价而非零售价缴税**（税基更低），并摊薄单票清关成本 | 有稳定销量、可承担库存资金占用 |
| **DDP + 实时落地成本** | 采用 DDP（完税后交货）并把关税、清关费实时计入落地成本与定价，杜绝"到岸才发现亏损" | 直发为主、SKU 多、价格敏感 |
| **3PL / 报关行合作** | 与目的国 3PL、持牌报关行合作处理正式报关与 HTS 归类，把合规交给专业方 | 无自有关务能力 |
| **原产地多元化（中国 +1）** | 评估把部分产能迁往其他原产地，以对冲单一原产地的税率与政策风险 | 单一原产地依赖度高、税率冲击大 |

**定价与选品联动**：关税必须计入 `../../afa-ops/references/unit-economics-calculator.md` 的 L2 入境成本层再判断毛利；落地成本对比可用 `landed-cost-calculator.md`。低价、低毛利、强价格敏感的 SKU 在新常态下最先被淘汰。

## 四、待补资料清单（信息不全时先要这些）

- 各主力 SKU 的 HS 编码（初判）、原产国、FOB/批发价、货值构成；
- 目的国现行有效税率区间与适用依据（**以官方/报关行口径为准，税率随政策变动**）；
- 现有履约方式（小包直发 / 海外仓 / DDP）、月发货量与均单值；
- 现金流对"本土备货"资金占用的承受度。

## 五、专业升级触发器

出现以下情形，必须升级给报关行 / 关务或税务顾问 / 律师，本模块不越权裁决：

- 需要确定**正式税率、HS 归类、原产地认定或申报口径**；
- **海关扣货、查验、补件、处罚或退运**；
- 涉及**反倾销 / 301 等附加关税**的适用判断；
- 需要出具可执行的清关、退税或合规方案。
