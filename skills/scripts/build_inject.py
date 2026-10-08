#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AFA DTC 协议内核注入器
从 afa/_system/kernel.md 的 INJECT 区块，注入每个 SKILL.md 的「## 系统协议（内核版）」固定小节。
幂等：KERNEL:AUTO 标记存在则替换，不存在则在文件末尾追加。
目的：单模块安装也能自含协议内核（不依赖 _system 完整版）。

用法:
  python scripts/build_inject.py .          # 注入/更新全部 SKILL.md
  python scripts/build_inject.py . --check  # 只检查是否需要重注入（CI 用），有差异退出码 1
"""
import os, re, sys, glob

HEADER = "## 系统协议（内核版）"
START = "<!-- KERNEL:AUTO:START — 由 scripts/build_inject.py 从 _system/kernel.md 生成，勿手改 -->"
END = "<!-- KERNEL:AUTO:END -->"


def get_block(root):
    k = open(os.path.join(root, "afa", "_system", "kernel.md"), encoding="utf-8").read()
    m = re.search(r"<!-- INJECT:START -->\n(.*?)\n<!-- INJECT:END -->", k, re.S)
    if not m:
        sys.exit("[错误] kernel.md 缺少 INJECT 区块")
    return m.group(1).strip()


def build_section(block):
    return f"{HEADER}\n{START}\n{block}\n{END}"


def main():
    root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
    check = "--check" in sys.argv
    sec = build_section(get_block(root))
    pat = re.compile(re.escape(HEADER) + r"\n" + re.escape(START) + r".*?" + re.escape(END), re.S)
    total = changed = 0
    broken = []
    for p in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
        total += 1
        s = open(p, encoding="utf-8").read()
        m = pat.search(s)
        if m:
            # 区段完好：整段替换（多重区段视为损伤，见下）
            if s.count(START) > 1 or s.count(END) > 1 or s.count(HEADER) > 1:
                broken.append((p, "区段重复（HEADER/START/END 出现多次）"))
                continue
            new = s[:m.start()] + sec + s[m.end():]
        elif HEADER in s or START in s or END in s:
            # 有残迹但拼不成完整区段：HEADER 或标记损坏/缺失。
            # 旧行为在此静默无操作，--check 还报绿（假绿）——现在必须红。
            broken.append((p, "区段损坏：HEADER/KERNEL:AUTO 标记不成对或被改动"))
            continue
        else:
            new = s.rstrip() + "\n\n" + sec + "\n"  # 首次注入
        if new != s:
            changed += 1
            if not check:
                open(p, "w", encoding="utf-8").write(new)
    print(f"SKILL.md 总数 {total} | {'待更新' if check else '已注入/更新'} {changed}"
          + (f" | 损坏 {len(broken)}" if broken else ""))
    if total == 0:  # 护栏：一个 SKILL.md 都没扫到，说明 root 传错/打包丢失，不得判绿
        sys.exit(f"[错误] 未扫描到任何 SKILL.md（root={root!r}）——路径错误或产物缺失，拒绝报绿")
    if broken:
        for p, why in broken:
            print(f"[错误] {p}：{why}", file=sys.stderr)
        sys.exit(f"[错误] {len(broken)} 个 SKILL.md 的内核区段损坏，需人工修复后重跑（不会静默跳过）")
    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
