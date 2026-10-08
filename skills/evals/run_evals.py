#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AFA DTC 路由评测 harness（纯标准库，无第三方依赖）。

对 evals/cases/*.jsonl 逐条做四类可机判断言：
  1) routing_correct    —— expect_route 模块存在，且 user_input（或 trigger_hint）命中该模块 description 的触发词
  2) five_fields_present —— 目标 SKILL.md 剥离内核块后的正文含五个不可丢字段名（main_question/deferred_goals/evidence_state/market_scope/primary_market）
  3) no_codename_leak    —— expected_visible 用户可见样例不含 afa- 代号（display_name 纪律）
  4) cost_tagged         —— 用例声明 cost_tag ∈ {low, medium, high}（路由建议须带成本/工作量标签）

用法：python evals/run_evals.py [root]   （默认 root=.）
存在任一结构性失败即以非零退出，供 CI 红灯。
"""
import os, re, sys, json, glob

FIELDS = ["main_question", "deferred_goals", "evidence_state", "market_scope", "primary_market"]
# 内核注入块会让「SKILL.md 全文含五字段名」恒真 → 断言空转。
# 剥离 KERNEL:AUTO 区段后只看模块自身正文，才是真检查。
KERNEL_RE = re.compile(r"<!--\s*KERNEL:AUTO:START.*?<!--\s*KERNEL:AUTO:END\s*-->", re.S)
_cache = {}

def strip_kernel(text):
    return KERNEL_RE.sub("", text)

def load_module(root, mod):
    if mod in _cache:
        return _cache[mod]
    p = os.path.join(root, mod, "SKILL.md")
    if not os.path.isfile(p):
        _cache[mod] = None
        return None
    s = open(p, encoding="utf-8").read()
    m = re.search(r'^description:\s*"(.*)"', s, re.M)
    desc = m.group(1) if m else ""
    t = re.search(r'触发词[:：]\s*(.*?)(?:。|$)', desc)
    words = [w.strip() for w in re.split(r'[,，、]', t.group(1))] if t else []
    words = [w for w in words if w]
    info = {"path": p, "text": s, "body": strip_kernel(s), "triggers": words}
    _cache[mod] = info
    return info

def check_case(root, c):
    out = []
    mod = c.get("expect_route", "")
    info = load_module(root, mod)
    # 1) routing_correct
    if info is None:
        out.append(("routing_correct", False, f"模块 {mod!r} 不存在"))
    else:
        hay = c.get("user_input", "") + " " + " ".join(c.get("trigger_hint", []))
        hits = [w for w in info["triggers"] if w and w in hay]
        out.append(("routing_correct", bool(hits),
                    f"命中触发词 {hits[:3]}" if hits else f"未命中 {mod} 触发词（触发词库 {len(info['triggers'])} 个）"))
    # 2) five_fields_present —— 在剥离内核注入块后的模块正文里查，避免恒真空转
    if info:
        miss = [f for f in FIELDS if f not in info["body"]]
        out.append(("five_fields_present", not miss,
                    "五字段齐全（模块正文，已剥离内核块）" if not miss
                    else f"模块正文缺 {miss}（内核块已剥离，不计入）"))
    else:
        out.append(("five_fields_present", False, "模块不存在"))
    # 3) no_codename_leak
    vis = c.get("expected_visible", "")
    leak = sorted(set(re.findall(r'afa-[a-z]+', vis)))
    out.append(("no_codename_leak", not leak, "无代号泄漏" if not leak else f"泄漏 {leak}"))
    # 4) cost_tagged
    ct = c.get("cost_tag")
    out.append(("cost_tagged", ct in ("low", "medium", "high"), f"cost_tag={ct}"))
    return out

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    files = sorted(glob.glob(os.path.join(root, "evals", "cases", "*.jsonl")))
    if not files:
        sys.exit("[错误] 未找到 evals/cases/*.jsonl")
    total = passed = 0
    fails = []
    per_line = {}
    for f in files:
        base = os.path.basename(f)
        for ln, line in enumerate(open(f, encoding="utf-8"), 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            try:
                c = json.loads(line)
            except json.JSONDecodeError as e:
                fails.append((base, f"L{ln}", [("json_valid", False, str(e))]))
                total += 1
                continue
            total += 1
            rs = check_case(root, c)
            ok = all(r[1] for r in rs)
            passed += ok
            bl = c.get("business_line", base)
            per_line.setdefault(bl, [0, 0])
            per_line[bl][0] += 1
            per_line[bl][1] += ok
            if not ok:
                fails.append((base, c.get("id", f"L{ln}"), [r for r in rs if not r[1]]))
    print(f"=== AFA 路由评测 ===")
    print(f"用例总数 {total} | 通过 {passed} | 失败 {total - passed}")
    for bl in sorted(per_line):
        n, p = per_line[bl]
        print(f"  [{bl}] {p}/{n}")
    if fails:
        print("--- 失败明细 ---")
        for fn, cid, fr in fails:
            print(f"  ✗ {fn}#{cid}: " + "; ".join(f"{a}=false({d})" for a, _, d in fr))
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
