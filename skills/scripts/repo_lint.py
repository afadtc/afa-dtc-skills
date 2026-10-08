#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AFA DTC 仓库质量门禁（入库版）
用法: python scripts/repo_lint.py <仓库根目录> [--json]
检查: ①死引用 ②frontmatter 规范 ③历史版本串 ④内部代号泄漏(启发式) ⑤模块计数对账

退出码约定（供 CI 使用）：
  ERROR 类（deadref / version / frontmatter / codename）任一存在 → 退出码 1（CI 红灯）。
  WARN 类（size / count）仅提示，不影响退出码（size 为官方建议、count 随版本变动）。
每次发版更新 CUR_VER 与 EXPECTED_SKILLS。
"""
import os, re, sys, json, argparse
from collections import Counter

# 注意：本库采用「双轨版本」——正文（SKILL.md/references/_system）统一停在 CUR_VER 基线，
# 发布号（v2.7.x）只出现在 CHANGELOG.md 与 README.md。改 CUR_VER 时必须同步全库正文版本头，
# 否则本检查会把所有正文判为「历史版本串」。日常发补丁**不需要**动 CUR_VER。
CUR_VER = "v2.6"
EXPECTED_SKILLS = 31               # 新增 Worker（如 payments/messaging）时同步更新
ALLOW_VER_FILES = ("CHANGELOG.md", "README.md")
RUNTIME_HINTS = ("brand-brain", "./deliverables/", "todo-")
# WARN 类不触发非零退出码；其余类型为 ERROR。
WARN_TYPES = {"size", "count"}


def load_md(root):
    md = {}
    for dp, _, fs in os.walk(root):
        if os.sep + ".git" in dp:
            continue
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(dp, f)
                try:
                    md[p] = open(p, encoding="utf-8").read()
                except Exception as e:
                    print(f"[读取失败] {p}: {e}")
    return md


def check_frontmatter(root, md, issues):
    total_desc = 0
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d, "SKILL.md")
        if p not in md:
            continue
        m = re.match(r"^---\s*\n(.*?)\n---", md[p], re.S)
        if not m:
            issues.append(("frontmatter", d, "无 frontmatter")); continue
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+?)\s*$", fm, re.M)
        ds = re.search(r"^description:\s*(.+)$", fm, re.M)
        name = nm.group(1).strip().strip('"') if nm else ""
        desc = ds.group(1).strip().strip('"') if ds else ""
        total_desc += len(desc)
        if name != d: issues.append(("frontmatter", d, f"name({name})≠目录名"))
        if not desc: issues.append(("frontmatter", d, "缺 description"))
        elif len(desc) > 1024: issues.append(("frontmatter", d, f"description {len(desc)}>1024"))
        if len(name) > 64: issues.append(("frontmatter", d, f"name 长度 {len(name)}>64"))
        body = md[p][m.end():].count("\n")
        if body > 500: issues.append(("size", d, f"SKILL.md 正文 {body} 行 >500(官方建议)"))
    if total_desc > 5600:  # 英文触发词为刻意的范围扩展（4500→5600）；单条 ≤1024 硬限与词元级查重不变
        issues.append(("size", "全局", f"description 合计 {total_desc} 字符 >5600 目标"))


def check_deadrefs(root, md, issues):
    # SKILL.md/kernel/CHANGELOG 及运行时文件（含旧版 learnings.md 迁移引用）白名单
    wl = {"SKILL.md", "todo.md", "kernel.md", "CHANGELOG.md", "learnings.md"}
    bbt = md.get(os.path.join(root, "afa", "references", "brand-brain-template.md"), "")
    wl |= set(re.findall(r"([\w\-]+\.md)", bbt))          # Brand Brain 运行时文件
    seen = set()
    for p, txt in md.items():
        skill = os.path.relpath(p, root).split(os.sep)[0]
        for line in txt.splitlines():
            for ref in re.findall(r"[\w\-./]*[\w\-]+\.md\b", line):
                base = os.path.basename(ref)
                if base in wl or "*" in ref or "{" in ref: continue
                if ref.startswith("./") or any(h in line for h in RUNTIME_HINTS): continue
                if "/" in ref:
                    cands = [os.path.normpath(os.path.join(os.path.dirname(p), ref)),
                             os.path.join(root, ref.lstrip("/"))]
                else:
                    cands = [os.path.join(os.path.dirname(p), ref),
                             os.path.join(root, skill, "references", ref),
                             os.path.join(root, skill, ref),
                             os.path.join(root, "afa", "_system", ref),
                             os.path.join(root, "afa", "references", ref)]
                if not any(os.path.isfile(c) for c in cands):
                    key = (os.path.relpath(p, root), ref)
                    if key not in seen:
                        seen.add(key)
                        issues.append(("deadref", key[0], f"→ {ref}"))


def check_versions(root, md, issues):
    for p, txt in md.items():
        rp = os.path.relpath(p, root)
        if os.path.basename(p) in ALLOW_VER_FILES: continue
        for v in set(re.findall(r"v\d+\.\d+(?:\.\d+)?", txt)):
            if v != CUR_VER:
                issues.append(("version", rp, f"历史版本串 {v}"))


def check_codename_leak(root, md, issues):
    """启发式: references/ 下模板/话术文件里出现 afa- 代号且不在'仅供系统使用'区块附近。"""
    for p, txt in md.items():
        if f"{os.sep}references{os.sep}" not in p: continue
        lines = txt.splitlines()
        guard = [i for i, l in enumerate(lines) if "仅供系统使用" in l or "internal" in l.lower()]
        for i, l in enumerate(lines):
            if re.search(r"[「\"'']afa-[a-z]+", l):     # 引号包裹的话术里出现代号=高危
                if not any(abs(i - g) <= 30 for g in guard):
                    issues.append(("codename", os.path.relpath(p, root), f"L{i+1} 疑似话术含内部代号"))



# 引用锚点形态：`target.md` 后 60 字内出现 §N / §N.N（或反向：§N.N 前 60 字内出现 `target.md`）
_ANCHOR_FWD = re.compile(r"`([\w\-./]+\.md)`[^\n]{0,60}?§\s*(\d+(?:\.\d+)*)")
_ANCHOR_BWD = re.compile(r"§\s*(\d+(?:\.\d+)*)[^\n]{0,20}?（?见\s*`([\w\-./]+\.md)`")
_HEADING_NUM = re.compile(r"^#{2,6}\s+(?:§\s*)?(\d+(?:\.\d+)*)[\s、.．:：\u4e00-\u9fff]")


def _heading_nums(txt):
    """收集文件里所有形如 '## 3.2 xxx' / '### 3.2.1 xxx' 的编号小节。"""
    nums = set()
    for l in txt.splitlines():
        m = _HEADING_NUM.match(l)
        if m:
            nums.add(m.group(1))
    return nums


def check_anchors(root, md, issues):
    """§锚点存在性：`x.md` §N.N 形式的引用，目标文件必须真有该编号小节（封死"死锚点"整类）。"""
    idx = {os.path.normpath(p): _heading_nums(t) for p, t in md.items()}
    for p, txt in md.items():
        base = os.path.dirname(p)
        hits = [(m.group(1), m.group(2)) for m in _ANCHOR_FWD.finditer(txt)]
        hits += [(m.group(2), m.group(1)) for m in _ANCHOR_BWD.finditer(txt)]
        for tgt_name, num in hits:
            tgt = os.path.normpath(os.path.join(base, tgt_name))
            if tgt not in idx:
                continue  # 文件不存在 → 交给 deadref 报，不重复
            nums = idx[tgt]
            if not nums:
                continue  # 目标文件不用编号小节制，跳过（避免误报）
            # 命中：完全相等，或它是某个更深编号的前缀（§3 命中 3.1）
            if num in nums or any(x.startswith(num + ".") for x in nums):
                continue
            issues.append(("anchor", os.path.relpath(p, root), f"→ {tgt_name} §{num} 不存在（该文件有 §{sorted(nums)[:6]}…）"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    md = load_md(a.root)
    issues = []
    check_frontmatter(a.root, md, issues)
    check_deadrefs(a.root, md, issues)
    check_versions(a.root, md, issues)
    check_codename_leak(a.root, md, issues)
    check_anchors(a.root, md, issues)
    skills = sum(1 for d in os.listdir(a.root) if os.path.isfile(os.path.join(a.root, d, "SKILL.md")))
    if skills != EXPECTED_SKILLS:
        issues.append(("count", "全局", f"skill 目录 {skills}≠预期 {EXPECTED_SKILLS}（新增模块请同步 EXPECTED_SKILLS）"))

    errors = [i for i in issues if i[0] not in WARN_TYPES]
    warns = [i for i in issues if i[0] in WARN_TYPES]

    if a.json:
        print(json.dumps({"files": len(md), "skills": skills,
                          "errors": len(errors), "warnings": len(warns),
                          "issues": [{"type": t, "where": w, "detail": d} for t, w, d in issues]},
                         ensure_ascii=False, indent=1))
    else:
        print(f"扫描 {len(md)} 个 md 文件 / {skills} 个 skill 目录")
        if errors:
            print("== ERROR（阻断 CI）==")
            for t, w, d in errors[:120]:
                print(f"  [{t}] {w}  {d}")
            if len(errors) > 120: print(f"  ...共 {len(errors)} 条 error")
        if warns:
            print("== WARN（仅提示，不阻断）==")
            for t, w, d in warns:
                print(f"  [{t}] {w}  {d}")
        print("分类统计:", dict(Counter(t for t, _, _ in issues)) if issues else "全部通过 ✅")
        print(f"结论: errors={len(errors)}  warnings={len(warns)}  →  CI {'FAIL' if errors else 'PASS'}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
