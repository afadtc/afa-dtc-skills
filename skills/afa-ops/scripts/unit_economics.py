#!/usr/bin/env python3
"""
AFA DTC — 真实单位成本与贡献利润计算器（六层成本，含关税参数）

对齐公式出处：afa-ops/references/unit-economics-calculator.md
  L1 采购 = FOB + (模具费 + 样品费) / 数量
  L2 入境 = FOB×关税率 + (头程运费 + 保险 + 报关费) / 数量        ← 含关税参数
  L3 仓储 = 单件仓储 + 单件入库
  L4 履约 = 拣选 + 打包 + 包装材料 + 尾程快递（合计单件）
  L5 交易 = ASP×(支付费率 + 平台费率) + 固定手续费
  L6 逆向 = 退货率 × (退货处理成本 + 前四层物理成本)
  真实单位成本 = L1+L2+L3+L4+L5+L6
  贡献利润   = ASP - 真实单位成本 - CPA
  贡献利润率 = 贡献利润 / ASP

设计：纯 Python 标准库；argparse；--json 与人读双输出。
调用协议：优先执行本脚本；不可用时回退 unit-economics-calculator.md 的文字框架。

用法示例：
  python unit_economics.py --qty 1000 --fob 6 --tooling 2000 --tariff-rate 30 \\
      --freight 1500 --customs 300 --fulfillment 4.5 --asp 39 \\
      --payment-rate 2.9 --fixed-fee 0.30 --return-rate 5 --return-cost 6 --cpa 12
  python unit_economics.py --qty 1000 --fob 6 --tariff-rate 30 --asp 39 --json
"""
import argparse, json, sys


def compute(a):
    # 分母护栏：ASP=0 会让贡献利润率退化成 0%（看起来"打平"，实为无意义）；qty<=0 会除零。
    if a.asp <= 0:
        return {"error": "--asp 必须 > 0：ASP 为 0 时贡献利润率没有定义（分母为零），"
                         "不能按 0% 呈现。请填入真实平均售价。"}
    if a.qty <= 0:
        return {"error": "--qty 必须 > 0：批量数量用于摊销模具/样品/头程，为 0 时无法计算。"}
    qty = a.qty
    L1 = a.fob + (a.tooling + a.sample) / qty
    tariff = a.fob * a.tariff_rate / 100.0  # 简化口径：按 FOB 计征；CIF 精确口径用 afa-expand/scripts/landed_cost.py
    L2 = tariff + (a.freight + a.insurance + a.customs) / qty
    L3 = a.storage + a.receiving
    L4 = a.fulfillment
    physical = L1 + L2 + L3 + L4
    L5 = a.asp * (a.payment_rate + a.platform_rate) / 100.0 + a.fixed_fee
    L6 = a.return_rate / 100.0 * (a.return_cost + physical)
    true_cost = physical + L5 + L6
    contribution = a.asp - true_cost - a.cpa
    cm = contribution / a.asp * 100.0
    breakeven_cpa = a.asp - true_cost
    return {
        "inputs": {"qty": qty, "fob": a.fob, "tariff_rate_pct": a.tariff_rate, "asp": a.asp, "cpa": a.cpa},
        "layers": {
            "L1_采购": round(L1, 4), "L2_入境": round(L2, 4), "L2_关税分量": round(tariff, 4),
            "L3_仓储": round(L3, 4), "L4_履约": round(L4, 4), "L5_交易": round(L5, 4), "L6_逆向": round(L6, 4),
        },
        "true_unit_cost": round(true_cost, 4),
        "contribution": round(contribution, 4),
        "contribution_margin_pct": round(cm, 2),
        "breakeven_cpa": round(breakeven_cpa, 4),
        "flags": [f for f in [
            "贡献利润为负：当前 ASP/CPA 下每单亏损" if contribution < 0 else None,
            "关税率为 0：de minimis 取消后请务必填入真实有效税率" if a.tariff_rate == 0 else None,
        ] if f],
    }


def human(r):
    if "error" in r:
        return "错误：" + r["error"]
    lines = ["=== 真实单位成本（六层） ==="]
    for k, v in r["layers"].items():
        lines.append(f"  {k:<12} {v:>10.4f}")
    lines += [
        f"  {'真实单位成本':<12} {r['true_unit_cost']:>10.4f}",
        "",
        f"ASP={r['inputs']['asp']}  CPA={r['inputs']['cpa']}",
        f"贡献利润        {r['contribution']:>10.4f}",
        f"贡献利润率      {r['contribution_margin_pct']:>9.2f}%",
        f"盈亏平衡 CPA    {r['breakeven_cpa']:>10.4f}  （CPA 高于此值即亏损）",
    ]
    for f in r["flags"]:
        lines.append(f"  ⚠ {f}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="真实单位成本与贡献利润（六层成本，含关税）")
    p.add_argument("--qty", type=float, default=1000, help="批量数量（用于模具/样品/头程摊销）")
    p.add_argument("--fob", type=float, default=0, help="单件 FOB/出厂价")
    p.add_argument("--tooling", type=float, default=0, help="模具费合计")
    p.add_argument("--sample", type=float, default=0, help="样品费合计")
    p.add_argument("--tariff-rate", type=float, default=0, help="关税率 %%（对 FOB 值征收）")
    p.add_argument("--freight", type=float, default=0, help="头程运费合计")
    p.add_argument("--insurance", type=float, default=0, help="货运保险合计")
    p.add_argument("--customs", type=float, default=0, help="报关/杂费合计")
    p.add_argument("--storage", type=float, default=0, help="单件仓储成本")
    p.add_argument("--receiving", type=float, default=0, help="单件入库成本")
    p.add_argument("--fulfillment", type=float, default=0, help="单件履约（拣选+打包+材料+尾程）")
    p.add_argument("--asp", type=float, default=0, help="平均售价")
    p.add_argument("--payment-rate", type=float, default=2.9, help="支付费率 %%")
    p.add_argument("--platform-rate", type=float, default=0, help="平台费率 %%")
    p.add_argument("--fixed-fee", type=float, default=0.30, help="每笔固定手续费")
    p.add_argument("--return-rate", type=float, default=0, help="退货率 %%")
    p.add_argument("--return-cost", type=float, default=0, help="单次退货处理成本（不含 COGS）")
    p.add_argument("--cpa", type=float, default=0, help="单次获客成本")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    a = p.parse_args()
    r = compute(a)
    out = json.dumps(r, ensure_ascii=False, indent=2) if a.json else human(r)
    if "error" in r:
        print(out, file=sys.stderr)
        return 2
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
