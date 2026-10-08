#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""落地成本对比计算器（多关税情景）

方法论出处：afa-expand/references/landed-cost-calculator.md（本脚本负责算术层；
适用性/合规判断仍按该文件的边界声明交由专业方确认）。

用法示例（单价口径，美元）：
  python landed_cost.py --fob 6.5 --qty 1000 --freight 1800 --insurance 60 \\
      --tariff-rates 0,7.5,25 --vat-rate 0 --dest-fees 350 --sell-price 29.9
说明：--tariff-rates 支持逗号分隔多情景对比（%）；--vat-rate 为目的国进口增值税（%），
按 (货值+运保+关税) 计征的通用口径估算，具体计征基数以目的国规则为准。
输出：每情景的单件落地成本、落地毛利率、以及"关税每+1pp 吃掉多少毛利"敏感度。
"""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fob", type=float, required=True, help="单件 FOB 采购价")
    ap.add_argument("--qty", type=int, required=True)
    ap.add_argument("--freight", type=float, default=0, help="整批头程运费")
    ap.add_argument("--insurance", type=float, default=0, help="整批保险")
    ap.add_argument("--tariff-rates", default="0", help="关税率%%，逗号分隔多情景")
    ap.add_argument("--vat-rate", type=float, default=0, help="进口增值税%%（可抵扣地区可填 0 做现金流外口径）")
    ap.add_argument("--dest-fees", type=float, default=0, help="整批目的港/清关/派送杂费")
    ap.add_argument("--sell-price", type=float, default=None, help="单件售价（选填，算落地毛利率）")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.qty <= 0: import sys; sys.exit("错误：--qty 必须为正整数")
    goods = a.fob * a.qty
    cif = goods + a.freight + a.insurance          # 通用估算口径：以 CIF 计征关税
    rows = []
    for r in [float(x) for x in a.tariff_rates.split(",")]:
        duty = cif * r / 100
        vat = (cif + duty) * a.vat_rate / 100
        total = cif + duty + vat + a.dest_fees
        unit = total / a.qty
        row = {"tariff_%": r, "duty": round(duty, 2), "vat": round(vat, 2),
               "landed_total": round(total, 2), "landed_unit": round(unit, 4)}
        if a.sell_price:
            row["landed_margin_%"] = round((a.sell_price - unit) / a.sell_price * 100, 1)
        rows.append(row)
    sens = round(cif / 100 * (1 + a.vat_rate / 100) / a.qty, 4)  # 关税每+1pp 单件增量（含 VAT 联动）
    out = {"qty": a.qty, "goods_value": goods, "cif_base": round(cif, 2),
           "scenarios": rows, "duty_sensitivity_unit_per_pp": sens,
           "note": "估算口径：关税按 CIF 计征、VAT 按(CIF+关税)计征；正式税率/归类/申报以持牌专业方与官方口径为准。"}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    print(f"=== 落地成本对比（{a.qty} 件，CIF 基数 ${out['cif_base']:,}）===")
    hdr = "关税率   关税$      VAT$      整批落地$     单件落地$" + ("   落地毛利率" if a.sell_price else "")
    print(hdr)
    for x in rows:
        line = f"{x['tariff_%']:>5.1f}%  {x['duty']:>9,.0f}  {x['vat']:>8,.0f}  {x['landed_total']:>11,.0f}   ${x['landed_unit']:>8.2f}"
        if a.sell_price: line += f"      {x['landed_margin_%']:>5.1f}%"
        print(line)
    if a.sell_price:
        print(f"\n敏感度：关税每 +1pp，单件成本 +${sens}（≈ 吃掉 {round(sens/a.sell_price*100,2)}pp 毛利）")
    print("\n" + out["note"])

if __name__ == "__main__":
    main()
