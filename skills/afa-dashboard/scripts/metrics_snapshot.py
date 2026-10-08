#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""经营数据快照（用户自基准画像生成器）

方法论出处：afa-dashboard/references/benchmark-database.md「基准线生成器」——
诊断不用行业平均数，用你自己的数据建基准。本脚本把订单 CSV 变成可直接喂给
诊断/仪表盘工作流的自基准画像。

输入：订单导出 CSV（Shopify orders 导出可直接用；任意含下列三类列的 CSV 均可）
  日期列:  created_at / Created at / date / order_date
  客户列:  customer_id / Email / email / customer
  金额列:  total / Total / total_price / amount
用法：
  python metrics_snapshot.py orders.csv [--json] [--months 6]
输出：GMV/订单/AOV 月度趋势、新客vs复购结构、30/60/90 天复购率、
      复购间隔中位数、月度 cohort 复购三角（人读 + --json 机器格式）。
纯标准库，无第三方依赖。
口径说明：①检测到订单号列（Name/Order ID/#/订单号）时自动按订单号聚合——Shopify 多行订单
  （子行 Total 为空）金额取行合计、日期取最早行、客户取首个非空；若同号多行日期不一致则
  判定该列非订单号并放弃聚合。②斜杠日期按美式 %m/%d/%Y 优先解释，欧式日期请先转 ISO。
③金额不支持欧式千分位（如 1.234,56），请先转标准格式。
"""
import csv, sys, json, argparse, statistics
from datetime import datetime, timedelta
from collections import defaultdict

DATE_KEYS = ["created_at", "created at", "date", "order_date", "day", "创建时间", "日期"]
CUST_KEYS = ["customer_id", "email", "customer email", "customer", "客户", "邮箱"]
AMT_KEYS  = ["total", "total_price", "amount", "总额", "金额", "subtotal"]
ORDER_KEYS = ["order id", "order_id", "order number", "name", "order", "#", "订单号"]

def pick(fieldnames, keys):
    low = {f.lower().strip(): f for f in fieldnames}
    for k in keys:
        if k in low: return low[k]
    for f in fieldnames:                      # 次优：包含式匹配
        for k in keys:
            if k in f.lower(): return f
    return None

def parse_date(s):
    s = (s or "").strip()[:19].replace("T", " ")
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y"):
        try: return datetime.strptime(s[:len(fmt)+2].strip(), fmt)
        except ValueError: pass
    return None

def parse_amt(s):
    try: return float(str(s).replace("$", "").replace(",", "").strip() or 0)
    except ValueError: return 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--months", type=int, default=6, help="趋势窗口（月），默认 6")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.csv_path, encoding="utf-8-sig")))
    if not rows: sys.exit("CSV 为空")
    fn = rows[0].keys()
    dcol, ccol, acol = pick(fn, DATE_KEYS), pick(fn, CUST_KEYS), pick(fn, AMT_KEYS)
    if not (dcol and ccol and acol):
        sys.exit(f"列识别失败：日期={dcol} 客户={ccol} 金额={acol}；请重命名列后重试")

    ocol = pick(fn, ORDER_KEYS)
    raw = []
    for r in rows:
        d = parse_date(r.get(dcol, ""))
        if d: raw.append((d, str(r.get(ccol, "")).strip().lower(), parse_amt(r.get(acol, 0)),
                          str(r.get(ocol, "")).strip() if ocol else ""))
    orders = None
    if ocol:                                   # 订单号聚合（Shopify 多行订单去重）
        g = defaultdict(list)
        for rec in raw: g[rec[3] or ("_r%d" % len(g))].append(rec)
        multi = [v for v in g.values() if len(v) > 1]
        if not (multi and any(len({x[0].date() for x in v}) > 1 for v in multi)):
            orders = [(min(x[0] for x in v), next((x[1] for x in v if x[1]), ""),
                       sum(x[2] for x in v)) for v in g.values()]
    if orders is None:
        if ocol: print('提示：订单号列存在同号跨天行，已放弃聚合、按逐行计单（结果可能高估订单数）', file=sys.stderr)
        orders = [(d, c, amt) for d, c, amt, _ in raw]
    orders.sort()
    if not orders: sys.exit("没有可解析的订单行")

    by_cust = defaultdict(list)
    for d, c, amt in orders:
        if c: by_cust[c].append(d)

    # 月度趋势
    monthly = defaultdict(lambda: [0, 0.0])
    for d, c, amt in orders:
        m = d.strftime("%Y-%m"); monthly[m][0] += 1; monthly[m][1] += amt
    months = sorted(monthly)[-a.months:]

    # 新客 vs 复购（按客户首单月判定）
    first = {c: min(ds) for c, ds in by_cust.items()}
    struct = defaultdict(lambda: [0, 0])
    for d, c, amt in orders:
        if not c: continue
        struct[d.strftime("%Y-%m")][0 if first[c].strftime("%Y-%m") == d.strftime("%Y-%m") else 1] += 1

    # 30/60/90 天复购率 + 间隔中位数（对观察期足够的客户）
    now = orders[-1][0]; rep = {30: [0, 0], 60: [0, 0], 90: [0, 0]}; gaps = []
    for c, ds in by_cust.items():
        ds = sorted(ds)
        if len(ds) >= 2: gaps.append((ds[1] - ds[0]).days)
        for w in rep:
            if (now - ds[0]).days >= w:            # 观察期充分才计入分母
                rep[w][1] += 1
                if any((d2 - ds[0]).days <= w for d2 in ds[1:]): rep[w][0] += 1

    # cohort 三角（首单月 × 之后各月是否回购）
    cohort = defaultdict(lambda: defaultdict(set)); size = defaultdict(set)
    for c, ds in by_cust.items():
        fm = min(ds).strftime("%Y-%m"); size[fm].add(c)
        for d in ds:
            off = (d.year - min(ds).year) * 12 + d.month - min(ds).month
            if off > 0: cohort[fm][off].add(c)

    out = {
        "orders_total": len(orders), "gmv_total": round(sum(o[2] for o in orders), 2),
        "aov_overall": round(sum(o[2] for o in orders) / len(orders), 2),
        "monthly": [{"month": m, "orders": monthly[m][0], "gmv": round(monthly[m][1], 2),
                     "aov": round(monthly[m][1] / monthly[m][0], 2),
                     "new_orders": struct[m][0], "repeat_orders": struct[m][1]} for m in months],
        "repurchase_rate": {f"{w}d": (round(n / d * 100, 1) if d else None) for w, (n, d) in rep.items()},
        "repurchase_gap_median_days": statistics.median(gaps) if gaps else None,
        "cohort": {m: {f"M+{o}": round(len(cohort[m][o]) / len(size[m]) * 100, 1)
                        for o in sorted(cohort[m])[:6]} for m in sorted(size)[-a.months:]},
        "note": "以上即该品牌的自基准画像；诊断与仪表盘比较请用本画像而非行业平均。",
    }
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    print("=== 经营数据快照（自基准画像）===")
    print(f"总订单 {out['orders_total']} | GMV ${out['gmv_total']:,} | 整体 AOV ${out['aov_overall']}")
    print("\n月份       订单   GMV        AOV     新客单  复购单")
    for m in out["monthly"]:
        print(f"{m['month']}   {m['orders']:>5}  ${m['gmv']:>9,.0f}  ${m['aov']:>6.2f}  {m['new_orders']:>5}  {m['repeat_orders']:>5}")
    rr = out["repurchase_rate"]
    fmt=lambda v: "—" if v is None else f"{v}%"
    print(f"\n复购率：30 天 {fmt(rr['30d'])} | 60 天 {fmt(rr['60d'])} | 90 天 {fmt(rr['90d'])}（观察期充分客户口径；—＝观察期不足）")
    g=out["repurchase_gap_median_days"]
    print(f"复购间隔中位数：{'—' if g is None else str(g)+' 天'}")
    print("\nCohort（首单月 → M+n 回购率%）：")
    for m, r in out["cohort"].items():
        print(f"  {m}: " + "  ".join(f"{k}={v}%" for k, v in r.items()))
    print("\n" + out["note"])

if __name__ == "__main__":
    main()
