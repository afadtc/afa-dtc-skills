# AFA DTC 初始化检查清单

> **协议层级**：全局强制 · afa Hub 每次启动时执行
>
> **版本**：v2.4.6
>
> **来源说明**：本文件为当前生效的全局协议，供 Hub、Supervisor 与 Worker 统一遵守。
>
> **v2.1.0 变更**：启动检查序列新增 learnings.jsonl 结构化记忆加载步骤；老朋友回来流程新增记忆加载与向后兼容逻辑

---

## 启动检查序列

每次 afa 被调用时，按以下顺序执行检查：

```
✓ 检查 ./brand-brain/ 目录是否存在
✓ 如果存在，读取所有文件并构建品牌状态
✓ 加载结构化记忆（见下方「记忆加载」章节）
✓ 判断运行模式（首次接触 vs 老朋友回来）
✓ 检查运行环境能力（是否支持联网、文件读写、脚本执行等）
✓ 解析用户输入（如果有）
✓ 执行意图识别
✓ 判断紧急度
✓ 匹配业务阶段
✓ 检测 Level 0 状态（无产品/无网站/纯概念）→ 命中则温馨提示，但不拦截；如用户无明确问题则建议工作流 10
✓ 检测衰退/危机期信号 → 命中则温和提醒，建议工作流 9；用户坚持则正常执行
✓ 当用户提到销量/营收/ROAS 下降时，主动询问季节性 → 确认淡季则标记 seasonal_mode = off_season（如为旺季前备战期则标记 pre_season，旺季执行期则标记 peak_season），不误判为衰退/危机
✓ 检测供应链模式（v1.9.5 新增）：根据 Brand Brain 中的履约方式、配送时效、产品来源等信息判定 supply_chain_mode = dropshipping / wholesale / manufacturing / dtc（四选一），传递给子 Skill 用于调整建议优先级
```

## 记忆加载（v2.1 新增）

```
加载 learnings.jsonl 时的执行逻辑：

  Step 1 — 检测环境能力
  ├── 检查是否支持执行 Python 脚本
  └── 检查 ./brand-brain/learnings.jsonl 是否存在

  Step 2 — 向后兼容检查
  ├── 如果只存在旧版 learnings.md（无 learnings.jsonl）：
  │   ├── 读取 learnings.md，将每条记录转换为 JSONL 格式
  │   ├── 追加到 learnings.jsonl（转换时 confidence 统一设为 5）
  │   ├── 将 learnings.md 重命名为 learnings.md.bak
  │   └── 后续只使用 learnings.jsonl
  └── 如果 learnings.jsonl 已存在 → 直接进入 Step 3

  Step 3 — 选择加载策略
  ├── 如果环境支持 Python → 尝试增强加载：
  │   ├── 执行 python afa/_system/scripts/memory_manager.py --worker hub
  │   │   （脚本自动完成过滤、去重、30天衰减、失效检测，输出 Top 5）
  │   └── 如果脚本执行失败（文件不存在、运行报错等）→ 自动回退到基线加载
  └── 如果不支持 Python（或增强加载失败）→ 基线加载：
      ├── 读取 learnings.jsonl 全部内容
      ├── 跳过 type = promoted 的记录
      ├── 跳过 related_files 中文件已不存在的记录
      ├── 按 key 去重，保留 ts 最新的一条
      ├── 按 confidence 降序排列
      └── 提取最相关的 5 条记录

  Step 4 — 应用记忆
  ├── 如果当前任务与某条记忆直接相关 → 主动应用
  ├── 如果某条 pitfall/correction 与当前方案冲突 → 主动规避
  ├── 如果发现 [MULTIPLE_VERSIONS] → 主动向用户确认
  └── 将加载的记忆作为上下文传递给后续 Worker
```

## 首次接触流程

```
✓ 展示欢迎文案
✓ 问 2 个定位问题
✓ 初始化 Brand Brain 基础档案
✓ 路由到对应工作流或模块
```

## 老朋友回来流程

```
✓ 展示品牌状态扫描
✓ 检查数据新鲜度
✓ 加载结构化记忆（按上方「记忆加载」章节执行）
✓ 识别缺口和异常
✓ 路由到模块 或 建议最高优先级行动
✓ 如果识别为多步工作流，默认先推进当前最优第一步；只有出现真实方向分叉、资源投入差异或用户明确要求先看全流程时，再说明完整路径
✓ 每个模块完成后更新 Brand Brain
```
