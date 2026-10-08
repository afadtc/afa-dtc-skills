# Chargeback 反驳证据包手册（按 Reason Code 分型）

> 本文件为支付风控模块的内部参考文件。如需整理为用户可见交付物，必须删除内部路由标签、模块代号和系统字段，只保留自然语言、业务角色与行动建议。
>
> **边界声明**：本文件提供运营层面的证据组织与流程参考，不构成法律意见或支付网络规则的正式解读；具体争议处理以你的支付服务商（PSP）后台指引与卡组织最新规则为准，重大金额或涉诉争议请咨询专业律师。Reason code 体系与响应窗口以官方当期口径为准（本文编制于 2026-07）。

---

## 1. 先判型再举证：四大家族速查

争议不是一种病。**用错证据包是反驳失败的第一大原因**——先按 reason code 分型：

| 家族 | 典型代码（Visa） | 客户主张 | 反驳核心 |
|---|---|---|---|
| 欺诈类 | 10.4（CNP 欺诈） | "不是我买的" | 证明"就是他本人、他收到了、他用了" |
| 未收到货 | 13.1 | "没收到" | 证明妥投（签收/GPS/照片） |
| 与描述不符 | 13.3 | "货不对板/有瑕疵" | 证明页面描述与实物一致 + 客户未走退货流程 |
| 取消/退款未达 | 13.6 / 13.7 | "取消了还扣款/说退没退" | 证明政策展示 + 取消/退款时间线 |
| 重复/金额错误 | 12.5 / 12.6 | "扣了两次/金额不对" | 交易日志与授权记录对账 |

Mastercard 对应族（4837 欺诈 / 4853 货不对板 / 4855 未收到）逻辑同构，证据包通用。

## 2. 各家族证据包清单（提交前逐项打钩）

**通用底座（任何家族都要）**：订单详情（时间/金额/商品）□ 账单描述符与店铺名一致性说明 □ 客户沟通记录全导出 □ 退货/退款政策的结账页展示截图 □

**欺诈类（10.4）追加**：AVS/CVV 校验结果 □ 3DS 认证记录（有=近乎必胜）□ 设备/IP 与历史订单匹配 □ 同客户历史成功订单 □ 收货人与持卡人关系说明 □ 数字商品则附使用/登录日志 □

**未收到货（13.1）追加**：带签收的物流全链路 □ 妥投照片/GPS（末端承运商可提供时）□ 地址由客户本人填写的证明 □ 妥投后与客户的沟通记录 □

**与描述不符（13.3）追加**：下单当日产品页存档（文字+图片）□ 出库质检/称重记录 □ 客户拒绝退货流程或超期的记录 □ 批次质检报告（如有）□

**取消/退款类（13.6/13.7）追加**：订阅条款与取消入口展示证明 □ 取消/退款请求时间戳 vs 扣款时间戳对照 □ 已退款凭证（ARN 号）□

## 3. 响应时间线（错过窗口=自动败诉）

```
争议发起 → PSP 通知你（当天）
  ├── D+0-2：判型 + 决定应诉/接受（小额欺诈类常见"接受更省"，见 §5）
  ├── D+3-7：按清单组包提交（Stripe/PayPal 后台上传）
  └── 硬窗口：多数网络给商户约 20-30 天应诉期，以 PSP 后台倒计时为准——永远以后台显示为唯一时钟
裁决：通常 30-75 天返回；二次仲裁成本高，非大额不建议
```

## 4. 反驳信骨架（英文交付物，两个高频家族）

**A · 欺诈类（10.4）**

```
Dispute Rebuttal — Order #{ORDER}
Summary: Cardholder claims unauthorized use. Evidence shows the order was placed,
received and used by the cardholder.
1. Payment passed AVS (full match) and CVV; 3DS authentication completed on {DATE}.
2. Shipping address matches cardholder's verified billing address; delivered with
   signature on {DATE} (tracking {TRK}).
3. Customer contacted support on {DATE} regarding this order, confirming possession.
4. Same card/device placed {N} prior undisputed orders since {DATE}.
Requested outcome: reversal of chargeback {CASE_ID}. Exhibits A-E attached.
```

**B · 未收到货（13.1）**

```
Dispute Rebuttal — Order #{ORDER}
Summary: Cardholder claims non-receipt. Carrier records confirm delivery.
1. {CARRIER} tracking {TRK} shows "Delivered" on {DATE} at the address provided
   by the customer at checkout (Exhibit A: full tracking; Exhibit B: POD photo/GPS).
2. No delivery-issue contact was received within {N} days after delivery.
3. Our published policy requires reporting non-receipt within {N} days (Exhibit C).
Requested outcome: reversal of chargeback {CASE_ID}.
```

## 5. 应诉还是接受：一条利润算术

应诉成本 = 组包工时 + 部分 PSP 的争议费（无论输赢）。**经验判断口径（内部经验估算，编制于 2026-07）**：金额 < 组包成本的 2 倍且证据不含 3DS/签收硬证时，接受争议、把精力花在预防，往往期望值更高；金额较大或证据链含硬证（3DS、签收、使用日志）时应诉胜率显著上升。每月复盘一次"应诉胜率 × 家族"，把输面大的家族转入预防。

## 6. 预防联动（比反驳便宜十倍）

- 争议率健康线与 VAMP 自查：优先运行 `../scripts/vamp_check.py`（脚本不可用时回退 `core-frameworks.md` VAMP 事实卡）。
- 高频预防杠杆：账单描述符可识别（品牌名而非公司缩写）；发货即推送带追踪的通知；欺诈筛查开启 AVS/CVV 严格模式 + 高风险单人工复核；订阅类在扣款前发提醒；"先退款后扯皮"策略用于低金额高情绪工单（退款 < 争议费时直接退）。
- 争议数据回写：每笔争议的家族/结果/根因记入 learnings，供诊断与 CX 模块联动消灭上游原因。
