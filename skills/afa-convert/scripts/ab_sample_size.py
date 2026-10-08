#!/usr/bin/env python3
"""
AFA DTC — A/B 测试样本量计算器（两比例检验）

方法论出处：afa-convert/references/ab-testing-playbook.md「样本量计算」（本脚本采用两比例 z 检验精确计算；文档速查表为近似参考值，大效应量下差异可达 15-18%，以脚本结果为准）
  输入：基线转化率、最小可检测效应（MDE）、显著性 α（默认 0.05，双侧）、功效（默认 0.80）
  公式（pooled，两比例 z 检验，每组样本量）：
    p1 = 基线；p2 = 处理后转化率（由 MDE 推得）
    pbar = (p1 + p2) / 2
    n/组 = [ z_(α/2)·√(2·pbar·(1-pbar)) + z_β·√(p1(1-p1)+p2(1-p2)) ]² / (p2 - p1)²
  z 分位数用标准库 statistics.NormalDist().inv_cdf（无需第三方依赖）。

设计：纯 Python 标准库；argparse；--json 与人读双输出。
调用协议：优先执行本脚本；不可用时回退 ab-testing-playbook.md 的查表/文字框架。

用法示例：
  python ab_sample_size.py --baseline 2.5 --mde 10 --mde-type relative --daily-visitors 2000
  python ab_sample_size.py --baseline 2.5 --mde 0.5 --mde-type absolute --power 0.9 --json
"""
import argparse, json, math, sys
from statistics import NormalDist


def _n_per_group(p1, p2, abs_lift, alpha, power):
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2.0)   # 双侧
    z_beta = NormalDist().inv_cdf(power)
    pbar = (p1 + p2) / 2.0
    num = (z_alpha * math.sqrt(2 * pbar * (1 - pbar)) +
           z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (abs_lift ** 2))


def compute(a):
    # 分母/组数护栏：variants < 2 时没有对照可比，sample_total 会退化为 0 或负数。
    if a.variants < 2:
        return {"error": "--variants 必须 >= 2（至少 1 个对照 + 1 个处理组）；当前 %d" % a.variants}
    if not (0 < a.alpha < 1):
        return {"error": "--alpha 需在 (0,1) 区间内（默认 0.05）"}
    if not (0 < a.power < 1):
        return {"error": "--power 需在 (0,1) 区间内（默认 0.80）"}
    p1 = a.baseline / 100.0
    if a.mde_type == "relative":
        p2 = p1 * (1 + a.mde / 100.0)
        abs_lift = p2 - p1
    else:  # absolute percentage points
        abs_lift = a.mde / 100.0
        p2 = p1 + abs_lift
    if not (0 < p1 < 1) or not (0 < p2 < 1) or abs_lift == 0:
        return {"error": "基线或 MDE 取值非法：需 0<基线<100，且推得的处理组转化率在 (0,100) 内、与基线不等"}
    n_per = _n_per_group(p1, p2, abs_lift, a.alpha, a.power)
    total = n_per * a.variants
    out = {
        "inputs": {"baseline_pct": a.baseline, "mde": a.mde, "mde_type": a.mde_type,
                   "alpha": a.alpha, "power": a.power, "variants": a.variants},
        "p1_pct": round(p1 * 100, 4), "p2_pct": round(p2 * 100, 4),
        "absolute_lift_pp": round(abs_lift * 100, 4),
        "sample_per_variant": n_per, "sample_total": total,
    }
    # 多变体：k-1 次「处理 vs 对照」比较会抬高族系错误率（FWER），需做多重比较校正
    if a.variants > 2:
        comparisons = a.variants - 1
        alpha_adj = a.alpha / comparisons
        n_per_adj = _n_per_group(p1, p2, abs_lift, alpha_adj, a.power)
        out["multiple_comparisons"] = {
            "comparisons": comparisons,
            "bonferroni_alpha": round(alpha_adj, 6),
            "sample_per_variant_bonferroni": n_per_adj,
            "sample_total_bonferroni": n_per_adj * a.variants,
            "note": ("%d 个变体 = %d 次与对照的比较：不校正时假阳性概率会从 %g 膨胀到约 %.3g。"
                     "若要按 α=%g 的族系错误率读结论，请改用 Bonferroni 校正后的样本量"
                     "（每组 %d，合计 %d）；或改为一次只测一个变体。"
                     % (a.variants, comparisons, a.alpha,
                        1 - (1 - a.alpha) ** comparisons, a.alpha,
                        n_per_adj, n_per_adj * a.variants)),
        }
    if a.daily_visitors > 0:
        out["days_needed"] = math.ceil(total / a.daily_visitors)
        out["daily_visitors"] = a.daily_visitors
    if 0 < a.baseline < 0.5:
        out["warning"] = ("基线 {:.4g} 疑似按小数传入：--baseline 以百分数为单位"
                          "（如 3.7% 应传 3.7，而非 0.037）；当前按 {:.4g}% 解释，样本量可能被放大。"
                          ).format(a.baseline, a.baseline)
    return out


def human(r):
    if "error" in r:
        return "错误：" + r["error"]
    lines = [
        "=== A/B 样本量 ===",
        f"基线 {r['p1_pct']}%  →  目标 {r['p2_pct']}%  （绝对提升 {r['absolute_lift_pp']} pp）",
        f"每个变体所需样本量：{r['sample_per_variant']:,}",
        f"合计（{r['inputs']['variants']} 个变体）：{r['sample_total']:,}",
    ]
    if "multiple_comparisons" in r:
        mc = r["multiple_comparisons"]
        lines += [
            "",
            f"— 多重比较校正（Bonferroni） —",
            f"比较次数：{mc['comparisons']}  校正后 α：{mc['bonferroni_alpha']}",
            f"校正后每个变体：{mc['sample_per_variant_bonferroni']:,}  合计：{mc['sample_total_bonferroni']:,}",
            "  " + mc["note"],
        ]
    if "days_needed" in r:
        lines.append(f"按 {r['daily_visitors']:,}/天访客估算：约 {r['days_needed']} 天")
    if "warning" in r:
        lines.append("⚠ 警告：" + r["warning"])
    lines.append("注：样本量不足时不得提前结束实验（见 ab-testing-playbook.md）。")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="A/B 测试样本量（两比例 z 检验）")
    p.add_argument("--baseline", type=float, required=True, help="基线转化率 %%")
    p.add_argument("--mde", type=float, required=True, help="最小可检测效应（相对 %% 或绝对 pp，见 --mde-type）")
    p.add_argument("--mde-type", choices=["relative", "absolute"], default="relative", help="MDE 口径")
    p.add_argument("--alpha", type=float, default=0.05, help="显著性水平（双侧，默认 0.05）")
    p.add_argument("--power", type=float, default=0.80, help="统计功效（默认 0.80）")
    p.add_argument("--variants", type=int, default=2, help="变体数（含对照，默认 2）")
    p.add_argument("--daily-visitors", type=float, default=0, help="每天进入实验的访客数（用于估算天数）")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    a = p.parse_args()
    r = compute(a)
    if "warning" in r:
        print("⚠ 警告：" + r["warning"], file=sys.stderr)
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else human(r))
    return 0 if "error" not in r else 1


if __name__ == "__main__":
    sys.exit(main())
