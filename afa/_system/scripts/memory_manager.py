#!/usr/bin/env python3
"""
AFA DTC Memory Manager — 增强加载脚本
版本：v2.4.6
对齐协议：brand-memory-protocol.md §9.5「增强实现」

功能：
  1. Worker 过滤（按 --worker 参数筛选，hub/diagnose 加载全部）
  2. 失效检测（跳过 type=promoted；跳过 related_files 中文件已不存在的记录）
  3. 30 天衰减（每过 30 天 confidence 减 1，低于 3 分自动丢弃）
  4. 按 key 去重（保留 ts 最新的一条；检测多版本冲突）
  5. 截断输出（按 confidence 降序，最多输出 Top 5）

用法：
  python memory_manager.py --worker hub
  python memory_manager.py --worker afa-email
  python memory_manager.py --worker afa-email --file ./brand-brain/learnings.jsonl
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from collections import defaultdict


# ── 常量 ──────────────────────────────────────────────────
DEFAULT_JSONL_PATH = "./brand-brain/learnings.jsonl"
MAX_OUTPUT = 5
DECAY_INTERVAL_DAYS = 30
MIN_CONFIDENCE = 3
FULL_ACCESS_WORKERS = {"hub", "afa-diagnose", "afa-dashboard"}


def parse_args():
    parser = argparse.ArgumentParser(description="AFA DTC Memory Manager")
    parser.add_argument(
        "--worker",
        required=True,
        help="当前 Worker 名称（如 afa-email）。hub/afa-diagnose/afa-dashboard 加载全部记录。",
    )
    parser.add_argument(
        "--file",
        default=DEFAULT_JSONL_PATH,
        help=f"learnings.jsonl 文件路径（默认：{DEFAULT_JSONL_PATH}）",
    )
    return parser.parse_args()


def load_records(filepath):
    """逐行读取 JSONL 文件，跳过空行和格式错误的行。"""
    records = []
    if not os.path.isfile(filepath):
        print(f"[memory_manager] 文件不存在：{filepath}", file=sys.stderr)
        return records

    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                records.append(record)
            except json.JSONDecodeError:
                print(
                    f"[memory_manager] 第 {line_num} 行 JSON 解析失败，已跳过",
                    file=sys.stderr,
                )
    return records


def step1_worker_filter(records, worker):
    """Step 1 — Worker 过滤：只加载匹配当前模块（或 global）的记录。"""
    if worker in FULL_ACCESS_WORKERS:
        return records
    return [
        r for r in records if r.get("worker") == worker or r.get("worker") == "global"
    ]


def step2_invalidation(records, brand_brain_dir):
    """Step 2 — 失效检测：跳过 promoted 记录；跳过 related_files 中文件已不存在的记录。

    Args:
        records: 过滤后的记忆记录列表。
        brand_brain_dir: brand-brain 目录的路径（从 --file 参数推导）。
            related_files 中存储的是裸文件名（如 "brand-guidelines.md"），
            需要与 brand_brain_dir 拼接后才能正确检查文件是否存在。
    """
    valid = []
    for r in records:
        # 跳过已晋升的记录
        if r.get("type") == "promoted":
            continue

        # 检查关联文件是否存在
        # related_files 存储裸文件名（见 brand-memory-protocol.md §9.1），
        # 需要拼接 brand-brain 目录路径进行检查
        related = r.get("related_files", [])
        if related:
            all_exist = all(
                os.path.exists(os.path.join(brand_brain_dir, f)) for f in related
            )
            if not all_exist:
                continue

        valid.append(r)
    return valid


def step3_decay(records):
    """Step 3 — 30 天衰减：每过 30 天 confidence 减 1，低于 MIN_CONFIDENCE 自动丢弃。"""
    now = datetime.now(timezone.utc)
    surviving = []

    for r in records:
        ts_str = r.get("ts", "")
        confidence = r.get("confidence", 5)

        try:
            ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            # 无法解析时间戳时，保留记录但不衰减
            surviving.append(r)
            continue

        days_elapsed = (now - ts).days
        decay_amount = days_elapsed // DECAY_INTERVAL_DAYS
        effective_confidence = confidence - decay_amount

        if effective_confidence < MIN_CONFIDENCE:
            continue

        # 将衰减后的 confidence 写入记录（不修改原文件，仅用于排序）
        r["_effective_confidence"] = effective_confidence
        surviving.append(r)

    return surviving


def step4_dedup(records):
    """Step 4 — 按 key 去重：保留 ts 最新的一条；检测多版本冲突。"""
    grouped = defaultdict(list)
    for r in records:
        key = r.get("key", "")
        grouped[key].append(r)

    deduped = []
    conflicts = []

    for key, group in grouped.items():
        if len(group) == 1:
            deduped.append(group[0])
        else:
            # 按 ts 降序排列，保留最新的
            group.sort(key=lambda x: x.get("ts", ""), reverse=True)
            latest = group[0]

            # 检测内容冲突（insight 不同视为冲突）
            insights = set(r.get("insight", "") for r in group)
            if len(insights) > 1:
                latest["_conflict"] = "[MULTIPLE_VERSIONS]"
                conflicts.append(key)

            deduped.append(latest)

    return deduped, conflicts


def step5_truncate(records, max_output=MAX_OUTPUT):
    """Step 5 — 截断：按 effective_confidence 降序排列，最多输出 Top N。"""
    records.sort(
        key=lambda x: x.get("_effective_confidence", x.get("confidence", 0)),
        reverse=True,
    )
    return records[:max_output]


def clean_internal_fields(records):
    """清除内部计算字段，输出干净的记录。"""
    for r in records:
        r.pop("_effective_confidence", None)
    return records


def main():
    args = parse_args()
    worker = args.worker
    filepath = args.file

    # 加载
    records = load_records(filepath)
    if not records:
        print(json.dumps({"memories": [], "conflicts": [], "total_loaded": 0}))
        return

    total_raw = len(records)

    # 从 --file 参数推导 brand-brain 目录路径
    # 例如 --file ./brand-brain/learnings.jsonl → brand_brain_dir = ./brand-brain
    brand_brain_dir = os.path.dirname(os.path.abspath(filepath))

    # Step 1: Worker 过滤
    records = step1_worker_filter(records, worker)

    # Step 2: 失效检测
    records = step2_invalidation(records, brand_brain_dir)

    # Step 3: 30 天衰减
    records = step3_decay(records)

    # Step 4: 去重
    records, conflicts = step4_dedup(records)

    # 记录截断前的有效记录数（经过过滤、衰减、去重后的真实数量）
    after_filter = len(records)

    # Step 5: 截断
    records = step5_truncate(records)

    # 清理内部字段
    records = clean_internal_fields(records)

    # 输出结构化 JSON
    output = {
        "memories": records,
        "conflicts": conflicts,
        "total_loaded": total_raw,
        "after_filter": after_filter,
        "final_count": len(records),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
