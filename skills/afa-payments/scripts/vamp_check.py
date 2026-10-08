#!/usr/bin/env python3
"""
AFA DTC — Visa VAMP 争议率自查

对齐事实出处：afa-payments/references/core-frameworks.md「Visa VAMP 事实卡」
  VAMP 比率 = (TC40 欺诈报告 + TC15 争议) / TC05 结算笔数   （仅计 CNP 交易）
  2026-04-01 起商户阈值 = 1.50%（原 2.20%）
  仅当月度事件数（TC40+TC15）≥ 1,500 才进入监控
  超标（Excessive 档）罚金约 $8/笔（估算，最终以收单行/卡组织口径为准）

设计：纯 Python 标准库；argparse；--json 与人读双输出。
调用协议：优先执行本脚本；不可用时回退 VAMP 事实卡的文字口径。
免责：本脚本仅供内部自查，不构成支付合规裁决；具体口径与申诉以收单行/支付服务商与卡组织最新政策为准。

用法示例：
  python vamp_check.py --tc40 40 --tc15 120 --tc05 12000
  python vamp_check.py --tc40 40 --tc15 120 --tc05 12000 --json
"""
import argparse, json, sys

WARN_LO, WARN_HI = 0.65, 0.90  # 建议内部预警带（%）


def compute(a):
    if a.tc05 <= 0:
        return {"error": "TC05（结算笔数）必须 > 0"}
    events = a.tc40 + a.tc15
    ratio = events / a.tc05 * 100.0
    in_monitoring = events >= a.monitor_floor
    over = ratio > a.threshold
    if ratio <= WARN_LO:
        status = "安全"
    elif ratio <= WARN_HI:
        status = "预警带内（0.65%-0.9%：早于监管线，排查根因）"
    elif ratio <= a.threshold:
        status = "接近监管阈值（0.9%-1.5%：立即降险）"
    else:
        status = "超标"
    est_fine = round(events * a.fine, 2) if (over and in_monitoring) else 0.0
    return {
        "inputs": {"TC40": a.tc40, "TC15": a.tc15, "TC05": a.tc05,
                   "threshold_pct": a.threshold, "monitor_floor": a.monitor_floor, "fine_per_event": a.fine},
        "events": events, "vamp_ratio_pct": round(ratio, 4),
        "in_monitoring": in_monitoring, "over_threshold": over, "status": status,
        "internal_warning_band_pct": [WARN_LO, WARN_HI],
        "estimated_monthly_fine": est_fine,
        "note": ("事件数 < 监控门槛，暂不入监控，但比率仍应控制" if not in_monitoring
                 else "已达监控门槛：比率必须压在阈值内"),
    }


def human(r):
    if r.get("error"):
        return "错误：" + r["error"]
    lines = [
        "=== Visa VAMP 自查 ===",
        f"事件数 (TC40+TC15) = {r['events']}   TC05 = {r['inputs']['TC05']}",
        f"VAMP 比率 = {r['vamp_ratio_pct']}%   阈值 = {r['inputs']['threshold_pct']}%",
        f"状态：{r['status']}",
        f"是否入监控（月事件≥{r['inputs']['monitor_floor']}）：{'是' if r['in_monitoring'] else '否'}",
        f"内部建议预警带：{r['internal_warning_band_pct'][0]}%–{r['internal_warning_band_pct'][1]}%（早于阈值行动）",
    ]
    if r["estimated_monthly_fine"] > 0:
        lines.append(f"  ⚠ 估算月度罚金 ≈ ${r['estimated_monthly_fine']:,.2f}（$"
                     f"{r['inputs']['fine_per_event']}/笔，粗估，以收单行口径为准）")
    lines.append("  " + r["note"])
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Visa VAMP 争议率自查（仅 CNP）")
    p.add_argument("--tc40", type=float, required=True, help="TC40 欺诈报告数（月）")
    p.add_argument("--tc15", type=float, required=True, help="TC15 争议数（月）")
    p.add_argument("--tc05", type=float, required=True, help="TC05 结算笔数（月，CNP）")
    p.add_argument("--threshold", type=float, default=1.50, help="商户阈值 %%（2026-04-01 起 1.50）")
    p.add_argument("--monitor-floor", type=float, default=1500, help="进入监控的月度事件门槛")
    p.add_argument("--fine", type=float, default=8, help="Excessive 档每笔罚金（估算）")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    a = p.parse_args()
    r = compute(a)
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else human(r))
    return 0 if "error" not in r else 1


if __name__ == "__main__":
    sys.exit(main())
