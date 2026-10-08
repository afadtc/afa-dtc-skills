#!/usr/bin/env python3
"""
AFA DTC — 促销盈亏平衡 + 捆绑混合毛利计算器

对齐公式出处：
  afa-aov/references/promotion-strategy.md §3.1（折扣架构：折扣侵蚀毛利，需要多少增量才回本）
  afa-aov/references/bundle-strategy.md（混合毛利率 = (捆绑售价 - 全部单品 COGS) / 捆绑售价）
  afa-aov/references/anti-patterns.md（混合毛利红线 50% / 建议目标线 60%）

  discount 模式：给定当前毛利率 m%% 与折扣 d%%
    折后毛利率（**相对折后售价**，与 promotion-strategy.md §3.1 案例一致）
        = (m - d) / (100 - d) x 100
      例：m=60、d=20 → (60-20)/(100-20) = 50%（$100 原价、$40 COGS、折后售价 $80、利润 $40 → 40/80）
      注意：不要用 "m - d"——那是「折后毛利额占**原价**的比例」（本例 40%），不是毛利率；
            两者混用会把折后毛利率低估约 10 个点，进而误判是否跌破红线。
    折后毛利额占原价比例 = m - d（辅助对账值）
    若 d >= m → 折后毛利 <= 0，任何销量都亏
    盈亏平衡所需销量增幅 = m / (m - d) - 1 = d / (m - d)

  bundle 模式：混合毛利率 = (捆绑售价 - Σ单品COGS) / 捆绑售价
    三档判定（手册本来就是两条线，不是一条）：
      < floor（默认 50 = 红线）        → FAIL，红色警告，必须提价/换品/砍包
      floor <= x < target（默认 60）   → WARN，未达建议目标线但未破红线（各套装型底线区间 55-65%，
                                         见 benchmark-data.md §捆绑包类型）
      >= target                        → PASS

设计：纯 Python 标准库；argparse 子命令；--json 与人读双输出。
调用协议：优先执行本脚本；不可用时回退 promotion-strategy.md / bundle-strategy.md 文字框架。

用法示例：
  python promo_breakeven.py discount --margin 60 --discount 20
  python promo_breakeven.py bundle --bundle-price 130 --costs 30,15,8 --target 60 --json
"""
import argparse, json, sys

_warns = []


def _pct(name, v):
    """百分数入参守卫：0<v<=1 几乎必然是把小数当百分数传了（没有 0.6% 毛利率的品牌）。
    自动按 x100 归一，并留下 warning 字段，避免静默算错。"""
    if v is not None and 0 < v <= 1:
        _warns.append("%s=%.4g 疑似按小数传入（本脚本以百分数为单位，60%% 应传 60 而非 0.6）；"
                      "已按 %.4g%% 解释" % (name, v, v * 100))
        return v * 100.0
    return v


def discount(a):
    m = _pct("--margin", a.margin)
    d = _pct("--discount", a.discount)
    if not (0 < m <= 100) or not (0 <= d < 100):
        return {"mode": "discount", "error": "取值非法：需 0<毛利率<=100、0<=折扣<100（均为百分数）"}
    if d >= m:
        return {"mode": "discount", "margin_pct": m, "discount_pct": d,
                "profitable": False,
                "note": "折扣 %g%% >= 毛利率 %g%%：折后毛利 <= 0，任何销量都无法回本" % (d, m),
                "required_volume_uplift_pct": None}
    post_margin = (m - d) / (100.0 - d) * 100.0   # 相对折后售价（手册口径）
    gross_on_list = m - d                          # 折后毛利额占原价的比例（辅助值）
    uplift = (m / (m - d) - 1) * 100.0
    return {"mode": "discount", "margin_pct": m, "discount_pct": d,
            "post_discount_margin_pct": round(post_margin, 2),
            "post_discount_margin_basis": "相对折后售价（promotion-strategy.md §3.1 口径）",
            "gross_profit_pct_of_list_price": round(gross_on_list, 2),
            "profitable": True,
            "required_volume_uplift_pct": round(uplift, 2),
            "note": "要维持毛利总额，销量至少需增长 %.1f%%" % uplift}


def bundle(a):
    raw = [x.strip() for x in a.costs.split(",") if x.strip() != ""]
    if not raw:
        return {"mode": "bundle",
                "error": "--costs 为空：请传入逗号分隔的单品 COGS，如 --costs 30,15,8"}
    costs = []
    for x in raw:
        try:
            costs.append(float(x))
        except ValueError:
            return {"mode": "bundle",
                    "error": "--costs 含非数字项 %r：应为逗号分隔的数字，如 --costs 30,15,8" % x}
    if any(c < 0 for c in costs):
        return {"mode": "bundle", "error": "--costs 不得含负数"}
    total_cogs = sum(costs)
    if a.bundle_price <= 0:
        return {"mode": "bundle", "error": "捆绑售价必须 > 0"}
    target = _pct("--target", a.target)
    floor = _pct("--floor", a.floor)
    if floor > target:
        return {"mode": "bundle", "error": "红线 --floor 不得高于目标线 --target"}
    blended = (a.bundle_price - total_cogs) / a.bundle_price * 100.0
    if blended < floor:
        status = "FAIL"
        note = ("跌破毛利红线 %g%%：必须发出红色警告——提价、替换低毛利单品或砍掉该捆绑包"
                "（红线口径见 anti-patterns.md）" % floor)
    elif blended < target:
        status = "WARN"
        note = ("未达建议目标线 %g%%，但仍在红线 %g%% 之上：可放行，但需说明这部分利润让渡换到了什么"
                "（AOV 提升 / 清库存 / 拉新）。各套装型的底线区间 55-65%% 见 benchmark-data.md"
                % (target, floor))
    else:
        status = "PASS"
        note = "达标（>= 目标线 %g%%）" % target
    return {"mode": "bundle", "bundle_price": a.bundle_price,
            "total_cogs": round(total_cogs, 4), "item_count": len(costs),
            "blended_margin_pct": round(blended, 2),
            "floor_pct": floor, "target_pct": target,
            "status": status,
            "pass": status == "PASS",
            "note": note}


def human(r):
    if r.get("error"):
        return "错误：" + r["error"]
    if r["mode"] == "discount":
        lines = ["=== 促销盈亏平衡（折扣） ===",
                 "当前毛利率 %g%%  折扣 %g%%" % (r["margin_pct"], r["discount_pct"])]
        if not r["profitable"]:
            lines.append("  [!] " + r["note"])
        else:
            lines += ["折后毛利率 %g%%（相对折后售价 = 手册口径）" % r["post_discount_margin_pct"],
                      "  参考：折后毛利额占原价 %g%%（另一口径，勿与上一行混用）"
                      % r["gross_profit_pct_of_list_price"],
                      "盈亏平衡所需销量增幅：%g%%" % r["required_volume_uplift_pct"],
                      "  " + r["note"]]
    else:
        icon = {"PASS": "[OK]", "WARN": "[WARN]", "FAIL": "[FAIL]"}[r["status"]]
        lines = ["=== 捆绑混合毛利 ===",
                 "捆绑售价 %g  单品 COGS 合计 %g（%d 件）"
                 % (r["bundle_price"], r["total_cogs"], r["item_count"]),
                 "混合毛利率 %g%%  （红线 %g%% / 目标线 %g%%）"
                 % (r["blended_margin_pct"], r["floor_pct"], r["target_pct"]),
                 "  %s %s" % (icon, r["note"])]
    for w in _warns:
        lines.append("  [!] " + w)
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="促销盈亏平衡 + 捆绑混合毛利（口径对齐 afa-aov/references/）")
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("discount", help="折扣盈亏平衡：折后毛利率 + 需要多少销量增幅才回本")
    d.add_argument("--margin", type=float, required=True, help="当前毛利率（百分数，如 60）")
    d.add_argument("--discount", type=float, required=True, help="折扣（百分数，如 20）")
    d.add_argument("--json", action="store_true")
    b = sub.add_parser("bundle", help="捆绑混合毛利率（三档 PASS / WARN / FAIL）")
    b.add_argument("--bundle-price", type=float, required=True, help="捆绑包售价")
    b.add_argument("--costs", type=str, required=True, help="各单品 COGS，逗号分隔，如 30,15,8")
    b.add_argument("--target", "--min-margin", dest="target", type=float, default=60,
                   help="建议目标线（百分数，默认 60；未达仅 WARN，不算 FAIL）")
    b.add_argument("--floor", type=float, default=50,
                   help="毛利红线（百分数，默认 50；跌破即 FAIL 红色警告）")
    b.add_argument("--json", action="store_true")
    a = p.parse_args()
    r = discount(a) if a.cmd == "discount" else bundle(a)
    if _warns and not r.get("error"):
        r["warnings"] = list(_warns)
    out = json.dumps(r, ensure_ascii=False, indent=2) if getattr(a, "json", False) else human(r)
    if r.get("error"):
        print(out, file=sys.stderr)
        return 2          # 入参非法 → 非零退出码，供调用方判活
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
