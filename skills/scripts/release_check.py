#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布物检查（第四道门禁）——检查发布 zip 的解压本体。

前三道门禁（repo_lint / build_inject --check / run_evals）检查工作树；
本脚本检查最终交付的 zip：解压后做结构/一致性/卫生断言，再用三道门禁复检本体
（带工具目录的布局用解压体自带脚本；纯模块包用本脚本同目录的脚本），可选与
上一版 zip 对比输出文件级变更清单。

设计动因（发版实战中的两类真实事故）：
  1) 打包丢失类——工作树正确，但排除规则/打包过程吃掉文件（.github/ 曾被通配符误伤）；
  2) 自报成功类——补丁脚本自报 OK 但产物内容错误（区段重建曾复现旧损伤）。
两类事故工作树侧门禁天然无感，只有「检查解压本体」能兜住。
边界：本脚本不做语义判断——内容对错由评审与 evals 负责。

用法：
  python scripts/release_check.py dist.zip
  python scripts/release_check.py dist.zip --against prev.zip   # 附文件级变更清单
  python scripts/release_check.py dist.zip --json
退出码：0=PASS；1=存在 FAIL。--against 变更清单仅呈现，不参与判定。
纯标准库，无第三方依赖。
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile, zipfile

EXPECTED_SKILLS = 31  # 与 scripts/repo_lint.py 期望一致
LEARNINGS = "examples/brand-brain-sample/learnings.jsonl"  # 必须存在，且逐行合法 JSONL
# 三种合法布局：①平铺（模块目录与 scripts/evals/examples 同在 zip 根）；②插件市场布局（根为
# .claude-plugin/ + README/CHANGELOG/LICENSE/.github，模块与 scripts/evals/examples 整体位于 skills/）；
# ③纯模块包（Release 附件：31 个模块目录直接在 zip 根，不含任何工具目录与仓库级文件，由
# scripts/pack_modules.py 生成，解压后可整体拷入任何 Agent 工具的技能目录）。
# 自动检测：skills/afa/SKILL.md → ②；afa/SKILL.md 且无 scripts/ → ③；否则 ①。
# ROOT_MUST 按 zip 根检查、MOD_MUST 按模块根检查（③ 两者均不适用，改为「纯净性」断言）。
ROOT_MUST = ["README.md", "CHANGELOG.md", "LICENSE", ".github/workflows/lint.yml"]
PURE_FORBIDDEN = ["scripts", "evals", "examples", ".github", ".claude-plugin",
                  "README.md", "CHANGELOG.md", "LICENSE"]  # ③ 顶层不得出现的条目
MOD_MUST = ["examples", "examples/quickstart-and-sessions.md",
            "examples/brand-brain-sample/brand-master.md",
            "examples/brand-brain-sample/products.md", LEARNINGS,
            "scripts/repo_lint.py", "scripts/build_inject.py", "scripts/release_check.py",
            "evals/run_evals.py", "evals/README.md"]
MUST_EXIST = ROOT_MUST + MOD_MUST  # 向后兼容的合并视图（仅供阅读）
# 精确匹配：目录名/文件名按路径分量比对，后缀按 endswith，避免 substring 误伤
DIRTY_DIRS = {".git", "__MACOSX", "__pycache__"}
DIRTY_FILES = {".DS_Store", "Thumbs.db"}
DIRTY_SUFFIXES = (".pyc", ".pyo")
L_TYPES = {"pitfall", "pattern", "preference", "error", "correction", "promoted"}
L_SOURCES = {"observed", "user-stated", "error-recovery"}
R = []

def add(group, name, ok, detail=""):
    R.append({"group": group, "name": name, "ok": bool(ok), "detail": str(detail)})

def is_dirty(name):
    parts = [p for p in name.split("/") if p]
    if not parts:
        return False
    if any(p in DIRTY_DIRS for p in parts[:-1]) or parts[-1] in DIRTY_DIRS:
        return True
    return parts[-1] in DIRTY_FILES or parts[-1].endswith(DIRTY_SUFFIXES)

def top_prefix(names):
    """GitHub 源码包场景：zip 内所有条目共用一个顶层目录 → 返回该目录名，否则返回 ''。"""
    tops = {n.split("/", 1)[0] for n in names
            if n.strip("/") and not n.startswith("__MACOSX/")}
    if len(tops) != 1:
        return ""
    top = tops.pop()
    return top if any(n.startswith(top + "/") for n in names) else ""

def sha_map(zip_path):
    with zipfile.ZipFile(zip_path) as z:
        return {i.filename: hashlib.sha256(z.read(i.filename)).hexdigest()
                for i in z.infolist() if not i.is_dir()}

def check_learnings(base, rel):
    fp = os.path.join(base, rel)
    if not os.path.isfile(fp):
        add("C", f"learnings 存在（{rel}）", False, "文件缺失——不得因未撞见而判绿")
        return
    add("C", f"learnings 存在（{rel}）", True)
    bad, records = [], 0
    with open(fp, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            records += 1
            try:
                j = json.loads(line)  # 每行必须是合法单行 JSON
            except json.JSONDecodeError:
                bad.append(f"L{i}JSON")
                continue
            if not isinstance(j, dict):
                bad.append(f"L{i}非对象")
            elif j.get("type") not in L_TYPES or j.get("source") not in L_SOURCES:
                bad.append(f"L{i}枚举")
    add("C", f"learnings 协议合法（{rel}）", not bad and records > 0,
        bad[:3] if bad else "空文件（0 条记录）")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path", help="待检查的发布 zip")
    ap.add_argument("--against", help="上一版 zip，输出文件级变更清单")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    with zipfile.ZipFile(a.zip_path) as z:
        names = z.namelist()
    bad = sorted({n for n in names if is_dirty(n)})
    add("C", "zip 无 .git/__MACOSX/.DS_Store 条目", not bad, bad[:3])

    prefix = top_prefix(names)  # GitHub 源码包会多包一层顶层目录
    tmp = tempfile.mkdtemp(prefix="relcheck_")
    try:
        with zipfile.ZipFile(a.zip_path) as z:
            z.extractall(tmp)
        base = os.path.join(tmp, prefix) if prefix else tmp
        if prefix:
            print(f"[提示] zip 带顶层目录 {prefix!r}（GitHub 源码包形态），已自动剥离一层后检查。\n"
                  f"       发布 zip 应以 README.md/afa*/ 为顶层；若这是正式发布物，请重新打包。",
                  file=sys.stderr)
        add("A", "zip 顶层结构（无多余包裹目录）", not prefix,
            f"顶层目录 {prefix!r}——已自动剥离，但发布 zip 不应多包一层")

        rel_names = [n[len(prefix) + 1:] if prefix else n for n in names]
        zero = [p for p in rel_names if p and not p.endswith("/")
                and os.path.isfile(os.path.join(base, p)) and os.path.getsize(os.path.join(base, p)) == 0]
        add("C", "无零字节文件", not zero, zero[:3])

        # 布局检测：skills/afa/SKILL.md → ②插件市场布局（模块根 skills/）；
        # afa/SKILL.md 且无 scripts/ → ③纯模块包；否则 ①平铺布局
        S = "skills" if os.path.isfile(os.path.join(base, "skills", "afa", "SKILL.md")) else ""
        mbase = os.path.join(base, S) if S else base
        pure = (not S and os.path.isfile(os.path.join(base, "afa", "SKILL.md"))
                and not os.path.isdir(os.path.join(base, "scripts")))
        add("A", "布局识别", True,
            "skills/ 插件市场布局" if S else ("纯模块包（Release 附件）" if pure else "平铺布局"))

        mods = sorted(d for d in os.listdir(mbase)
                      if d.startswith("afa") and os.path.isdir(os.path.join(mbase, d)))
        add("A", f"模块数 == {EXPECTED_SKILLS}", len(mods) == EXPECTED_SKILLS, f"实得 {len(mods)}")
        no_skill = [m for m in mods if not os.path.isfile(os.path.join(mbase, m, "SKILL.md"))]
        add("A", "每模块含 SKILL.md", not no_skill, no_skill[:3])
        no_kernel = [m for m in mods
                     if os.path.isfile(os.path.join(mbase, m, "SKILL.md"))
                     and "KERNEL:AUTO" not in open(os.path.join(mbase, m, "SKILL.md"), encoding="utf-8").read()]
        add("A", "协议内核块全量注入", not no_kernel, no_kernel[:3])
        if pure:
            # ③ 的契约：顶层只有模块目录——使用者「整体拷入技能目录」时不会带进任何非技能条目
            extra = sorted(d for d in os.listdir(base) if d not in mods)
            add("A", "纯模块包顶层仅含模块目录", not extra, extra[:5])
            add("A", "纯模块包不含工具目录与仓库级文件",
                not any(os.path.exists(os.path.join(base, p)) for p in PURE_FORBIDDEN))
        else:
            for p in ROOT_MUST:
                add("A", f"存在 {p}", os.path.exists(os.path.join(base, p)))
            for p in MOD_MUST:
                add("A", f"存在 {(S + '/') if S else ''}{p}", os.path.exists(os.path.join(mbase, p)))

        def read(p):
            fp = os.path.join(base, p)
            return open(fp, encoding="utf-8").read() if os.path.isfile(fp) else ""
        if pure:
            add("B", "纯模块包不带 README/CHANGELOG（版本一致性由仓库侧门禁保证）", True)
        else:
            readme, chlog = read("README.md"), read("CHANGELOG.md")
            rv = re.search(r"当前版本：(v[\d.]+)", readme)
            cv = re.findall(r"^## (v[\d.]+)[^\n]*（当前发布版本）", chlog, re.M)
            add("B", "README 与 CHANGELOG 版本一致",
                bool(rv) and len(cv) == 1 and rv.group(1) == cv[0],
                f"README={rv.group(1) if rv else '?'} CHANGELOG={cv}")
            add("B", "「当前发布版本」标记唯一",
                chlog.count("（当前发布版本）") == 1, f"出现 {chlog.count('（当前发布版本）')} 次")
            check_learnings(mbase, LEARNINGS)  # 显式断言：不靠 os.walk 撞见，缺失即 FAIL

        if pure:
            # 纯模块包自身不带脚本与 evals：用本脚本同目录的 scripts/ 与同级 evals/ 复检解压本体。
            # evals 以符号链接临时挂到解压目录（run_evals 从 root/evals/cases 读用例），不进 zip。
            here = os.path.dirname(os.path.abspath(__file__))
            tool_root = os.path.dirname(here)
            try:
                os.symlink(os.path.join(tool_root, "evals"), os.path.join(base, "evals"))
            except OSError:  # Windows 无符号链接权限时退化为复制（仍在临时目录内，用完即清）
                shutil.copytree(os.path.join(tool_root, "evals"), os.path.join(base, "evals"))
            gates = [("repo_lint", [sys.executable, os.path.join(here, "repo_lint.py"), "."], "errors=0"),
                     ("kernel同步", [sys.executable, os.path.join(here, "build_inject.py"), ".", "--check"], "待更新 0"),
                     ("evals", [sys.executable, os.path.join(tool_root, "evals", "run_evals.py"), "."], "失败 0")]
        else:
            root_arg = S or "."
            gates = [("repo_lint", [sys.executable, os.path.join(S, "scripts", "repo_lint.py"), root_arg], "errors=0"),
                     ("kernel同步", [sys.executable, os.path.join(S, "scripts", "build_inject.py"), root_arg, "--check"], "待更新 0"),
                     ("evals", [sys.executable, os.path.join(S, "evals", "run_evals.py"), root_arg], "失败 0")]
        for name, cmd, token in gates:
            try:
                r = subprocess.run(cmd, cwd=base, capture_output=True, text=True, timeout=300)
                out = r.stdout + r.stderr
                ok = r.returncode == 0 and token in out
                tail = out.strip().splitlines()[-1] if out.strip() else "(无输出)"
                add("D", f"解压体门禁·{name}", ok, tail)
            except Exception as e:
                add("D", f"解压体门禁·{name}", False, repr(e))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)  # 用完即清，不留临时解压目录

    diff = None
    if a.against:
        new, old = sha_map(a.zip_path), sha_map(a.against)
        diff = {"added": sorted(set(new) - set(old)),
                "removed": sorted(set(old) - set(new)),
                "changed": sorted(k for k in set(new) & set(old) if new[k] != old[k])}

    fails = [r for r in R if not r["ok"]]
    if a.json:
        print(json.dumps({"pass": not fails, "checks": R, "diff": diff},
                         ensure_ascii=False, indent=1))
    else:
        for r in R:
            line = ("PASS " if r["ok"] else "FAIL ") + f"[{r['group']}] {r['name']}"
            if r["detail"] and not r["ok"]:
                line += f"  ({r['detail']})"
            print(line)
        if diff is not None:
            print(f"\n--- 相对 {os.path.basename(a.against)} 的变更（仅呈现，不参与判定）---")
            for k in ("added", "removed", "changed"):
                print(f"{k}（{len(diff[k])}）:")
                for p in diff[k][:25]:
                    print(f"  {p}")
                if len(diff[k]) > 25:
                    print(f"  … 共 {len(diff[k])} 条")
        print(f"\n=== release_check: {'PASS' if not fails else 'FAIL（%d 项）' % len(fails)} ===")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
