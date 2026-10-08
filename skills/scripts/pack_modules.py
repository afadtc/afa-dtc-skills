#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""打纯模块包（Release 附件）——31 个模块目录直接位于 zip 顶层。

纯模块包是发给「任何 Agent 类工具」使用者的发布物：解压后把全部模块目录整体
复制进所用软件的技能目录即可使用（WorkBuddy / 豆包工作 / 千问办公 / Codex /
Cursor / Claude Code …），与 v2.4.7 发布物同形。因此包内只放模块目录，不放
scripts/ evals/ examples/ 与仓库级文件（README / CHANGELOG / LICENSE / .github），
也不带 .DS_Store / __MACOSX / __pycache__ 等脏条目。

用法：
  python scripts/pack_modules.py <模块根目录> <输出zip>
  python scripts/pack_modules.py skills dist/AFA_DTC_v2.7.7.zip
退出码：0=成功；1=模块数不符或根目录无效。
产物应随后交给 scripts/release_check.py 复检（第四道门禁）。纯标准库。

可复现构建：设置环境变量 SOURCE_DATE_EPOCH（Unix 秒，发布工作流取标签所指提交的时间）后，
条目时间戳、权限位与顺序全部固定，同一提交在任何机器上打出的 zip 字节一致，sha256 可与
Release 页面展示的值直接比对；未设置时条目时间取当前时刻。
"""
import os, sys, time, zipfile

EXPECTED_SKILLS = 31  # 与 scripts/repo_lint.py / scripts/release_check.py 期望一致
DIRTY_DIRS = {".git", "__MACOSX", "__pycache__", ".pytest_cache"}
DIRTY_FILES = {".DS_Store", "Thumbs.db"}
DIRTY_SUFFIXES = (".pyc", ".pyo")


def module_dirs(root):
    """模块目录 = 直接含 SKILL.md 的一级子目录（名称以 afa 开头），排序保证产物稳定。"""
    return sorted(d for d in os.listdir(root)
                  if d.startswith("afa") and os.path.isfile(os.path.join(root, d, "SKILL.md")))


def iter_files(root, mod):
    base = os.path.join(root, mod)
    for dp, dns, fns in os.walk(base):
        dns[:] = sorted(d for d in dns if d not in DIRTY_DIRS)
        for fn in sorted(fns):
            if fn in DIRTY_FILES or fn.endswith(DIRTY_SUFFIXES):
                continue
            full = os.path.join(dp, fn)
            yield full, os.path.relpath(full, root).replace(os.sep, "/")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    root, out = sys.argv[1], sys.argv[2]
    if not os.path.isfile(os.path.join(root, "afa", "SKILL.md")):
        sys.exit(f"[错误] {root!r} 下没有 afa/SKILL.md——请传模块根目录（仓库布局下为 skills/）")
    mods = module_dirs(root)
    if len(mods) != EXPECTED_SKILLS:
        sys.exit(f"[错误] 模块数 {len(mods)} ≠ 预期 {EXPECTED_SKILLS}：{mods}")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    stamp = time.gmtime(max(int(epoch), 315532800)) if epoch else time.localtime()  # zip 最早 1980-01-01
    date_time = stamp[:6]
    n = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for mod in mods:
            for full, arc in iter_files(root, mod):
                if os.path.getsize(full) == 0:
                    sys.exit(f"[错误] 零字节文件：{arc}")
                zi = zipfile.ZipInfo(arc, date_time=date_time)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.create_system = 3                 # Unix 语义，权限位固定为 rw-r--r--
                zi.external_attr = 0o100644 << 16
                with open(full, "rb") as fh:
                    z.writestr(zi, fh.read())
                n += 1
    print(f"[OK] {out}：{len(mods)} 个模块目录，{n} 个文件，{os.path.getsize(out):,} 字节"
          + (f"，时间戳固定于 SOURCE_DATE_EPOCH={epoch}" if epoch else ""))


if __name__ == "__main__":
    main()
