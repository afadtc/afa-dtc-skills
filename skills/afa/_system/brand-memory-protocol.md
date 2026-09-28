# AFA DTC Brand Brain 协议

> **协议层级**：全局强制 · 所有模块必须遵守
>
> **版本**：v2.4.7
>
> **来源说明**：本文件为当前生效的全局协议，供 Hub、Supervisor 与 Worker 统一遵守。


Brand Brain 是 AFA DTC 的记忆系统。它让每个模块都能记住用户是谁、卖什么、什么有效、什么无效。

---

## 一、目录结构

```
./brand-brain/
  brand-master.md         ← 品牌 DNA（由 afa-brand 创建，afa 初始化基础版）
  voice-and-tone.md       ← 品牌调性（由 afa-brand 创建）
  positioning.md          ← 品牌定位画布（由 afa-brand 创建）
  brand-story.md          ← 品牌故事（由 afa-brand 创建）
  visual-identity.md      ← 视觉识别规范（由 afa-brand 创建）
  brand-guidelines.md     ← 品牌规范文档（由 afa-brand 创建）
  brand-audit.md          ← 品牌健康审计报告（由 afa-brand 创建）
  products.md             ← 产品矩阵（由 afa-product 创建，afa 初始化基础版）
  audience.md             ← 用户画像（由 afa-brand 创建）
  competitors.md          ← 竞品情报（由 afa-compete 创建）
  keywords.md             ← 关键词库（由 afa-seo 创建）
  creative-kit.md         ← 创意素材库（由 afa-creative 创建）
  offers.md               ← 报价策略（由 afa-product 创建）
  objections.md           ← 常见异议（由 afa-convert 创建）
  guardrails.md           ← 品牌红线（由 afa-brand 创建）
  metrics.md              ← KPI 基准与北极星指标（由 afa-dashboard 创建）
  store.md                ← 店铺基础信息（由 afa-brand 创建）
  stack.md                ← 工具栈（由 afa 创建和维护）
  assets.md               ← 资产登记（追加写入，所有模块共享）
  learnings.jsonl         ← 结构化记忆（JSONL 格式，追加写入，所有模块共享）
```

---

## 二、文件所有权规则

Brand Brain 的 20 个文件按写入行为分为三类，每类有不同的管理规则：

| 类型 | 文件 | 规则 |
|:---|:---|:---|
| **Profile 文件（可覆写，15 个）** | brand-master.md, voice-and-tone.md, positioning.md, brand-story.md, visual-identity.md, brand-guidelines.md, brand-audit.md, products.md, audience.md, competitors.md, keywords.md, creative-kit.md, offers.md, metrics.md, store.md | 每个文件有唯一的所有者模块（见第一章标注）。所有者可以创建和更新（更新需用户确认）。其他模块只能读取，不能修改。 |
| **Append-only 文件（只追加，2 个）** | assets.md, learnings.jsonl | 所有模块都可以追加写入。任何模块不得删除、截断或覆盖已有内容。learnings.jsonl 每行一个 JSON 对象。 |
| **Config 文件（一次性，3 个）** | stack.md, guardrails.md, objections.md | 初始创建后很少变动。任何变动必须显式请求用户确认，并说明变动原因。未经用户确认，禁止修改。 |

```
三分类速查：
  Profile    → 所有者可更新（需确认）→ 品牌定位、产品、受众、店铺等核心档案
  Append     → 所有模块可追加（禁覆盖）→ 结构化记忆、资产登记
  Config     → 初始创建后冻结（变动需确认+说明原因）→ 工具栈、品牌红线、异议库
```

---

## 三、子目录扩展协议（v1.7 新增）

```
部分专业模块需要存储超出核心 20 个文件范围的专属数据。
这些模块可以在 brand-brain/ 下创建以自己名称命名的子目录。

授权的子目录：
  brand-brain/expand/    ← afa-expand 拥有（渠道评估、扩张策略等）
  brand-brain/geo/       ← afa-geo 拥有（AI 搜索可见度、落地成本等）
  brand-brain/pr/        ← afa-pr 拥有（公关策略、媒体套件等）
  brand-brain/seo/       ← afa-seo 拥有（技术审计、内容日历等）
  brand-brain/email/     ← afa-email 拥有（邮件序列、模板库等）

子目录规则：
  1. 子目录中的文件由对应模块独占管理
  2. 其他模块可以读取子目录内容，但不能修改
  3. 子目录文件不影响核心 20 个文件的命名和所有权
  4. 模块的核心读取列表（Context Matrix）仅引用根目录文件
  5. 子目录是模块的"私有工作空间"，不纳入全局路由
```

---

## 四、读取协议（Context Matrix）

每个模块声明它需要读取的 Brand Brain 文件。不读取不需要的文件。

```
模块                 读取的文件（以各模块 SKILL.md 的 Requires + Optional 为准）
──────────────────────────────────────────────────────────────
afa                  ALL（管家需要全局视图）
afa-diagnose         ALL（诊断需要全局数据）
afa-ops              ALL（运营需要全局视图）
afa-aov              products + offers + learnings + brand-master + audience
afa-brand            products + voice-and-tone + positioning + brand-story + visual-identity + learnings
afa-compete          competitors + products + learnings
afa-convert          products + objections + guardrails + audience + learnings
afa-creative         voice-and-tone + products + creative-kit + brand-master + learnings + audience + store
afa-cx               products + objections + learnings + voice-and-tone + audience
afa-dashboard        products + learnings + stack + metrics
afa-email            voice-and-tone + products + audience + learnings
afa-expand           brand-master + products + competitors + stack + learnings
afa-explore          products + audience + competitors + learnings
afa-fb               products + audience + learnings + creative-kit + offers + store
afa-geo              products + brand-master + learnings + audience
afa-gg               products + audience + learnings + offers + brand-master + store
afa-influencer       products + voice-and-tone + audience + learnings + brand-master
afa-launch           voice-and-tone + products + learnings
afa-pr               products + voice-and-tone + brand-master + learnings + audience
afa-product          voice-and-tone + products + learnings
afa-retain           products + audience + learnings + offers + brand-master
afa-seo              products + brand-master + learnings + audience + store
afa-sms              products + voice-and-tone + audience + learnings + offers
afa-social           products + voice-and-tone + audience + learnings + creative-kit
afa-tt               products + audience + learnings + creative-kit + offers + store
```

---

## 五、写入协议

### 创建新文件

1. 通过模块工作流生成内容
2. 写入 `./brand-brain/{filename}.md`
3. 告知用户：「已创建 {filename}，内容如下：...」

### 更新已有文件

1. 先读取现有文件
2. 展示将要变更的内容差异
3. 等待用户确认：「要更新这个文件吗？」
4. 确认后才写入
5. 告知用户：「已更新 {filename}，主要变更：...」

### 追加写入（assets.md / learnings.jsonl）

```
assets.md：
  1. 读取现有文件了解当前内容
  2. 在对应章节底部追加新条目
  3. 告知用户：「已添加 {n} 条新记录到 assets.md」

learnings.jsonl：
  1. 在文件末尾追加一行新的 JSON 对象（格式见第九章）
  2. 每行必须是完整的单行 JSON，禁止跨行
  3. 静默写入，无需告知用户（除非用户主动声明场景）
```

---

## 六、缺失文件处理（v1.8 重构——数据缺口清单）

```
如果模块需要的文件不存在：
  → 不报错，不崩溃
  → 输出「数据缺口清单」，明确告知用户缺什么、去哪里拿：

  「为了执行此任务，我需要以下数据：

  ✅ 已有：
  • 品牌基础信息（来自 Brand Brain）
  • 产品信息（来自 Brand Brain）

  ❌ 缺少：
  • {数据项 A} → 可从 {具体来源，如 GA4 > 报告 > 流量获取} 获取
  • {数据项 B} → 可从 {具体来源，如 Shopify > 分析 > 报告} 获取

  请提供以上数据后我们继续。
  如果暂时拿不到精确数据，给个大概范围也行。」

绝对禁止：
  ✗ 主动推送长篇工具设置教程
  ✗ 在用户没问的情况下教用户怎么配置 GA4
  ✗ 用缺少数据为借口拒绝给任何建议

正确做法：
  ✓ 告知缺什么、去哪里拿（具体到菜单路径）
  ✓ 用户问了怎么获取时，再给简洁的操作步骤
  ✓ 即使数据不完整，也基于已有数据给出初步建议
  ✓ 标注哪些结论基于估算，哪些基于实际数据
```

---

## 七、上下文新鲜度规则

```
文件年龄            处理方式
──────────────────────────────────────────────────────
< 7 天              直接使用，数据新鲜
7-30 天             使用，但标注日期：
                   「此数据来自 {date}，如有变化请告知」
30-90 天            仅使用摘要，标注：
                   「此数据已 {n} 天未更新，建议刷新后再做重要决策」
> 90 天             不主动使用，提醒用户：
                   「你的 {file} 已超过 3 个月未更新，
                   建议先刷新再继续」
```

---

## 八、冲突检测与处理规则（v2.0.9 新增）

当用户在当前会话中提供的信息与 Brand Brain 中已有记录存在逻辑矛盾时，系统必须主动检测并处理，而不是静默覆盖。

### 8.1 触发条件

```
以下任一情形触发冲突检测：
  ├── 用户描述的产品信息与 products.md 中的记录不一致
  │   （如价格、SKU、产品线变动）
  ├── 用户提到的品牌定位/调性与 brand-master.md 或 voice-and-tone.md 矛盾
  │   （如“我们现在走高端路线”但记录显示平价定位）
  ├── 用户描述的目标受众与 audience.md 中的画像明显不同
  ├── 用户提供的竞品信息与 competitors.md 中的记录冲突
  ├── 用户说的工具栈与 stack.md 中的记录不一致
  │   （如“我们已经换成 Klaviyo 了”但记录显示 Mailchimp）
  └── 用户提到的品牌红线与 guardrails.md 中的规则矛盾
```

### 8.2 处理流程

```
检测到冲突时，按以下流程处理：

  Step 1：暂停当前工作流
  Step 2：向用户指出矛盾点，使用以下标准话术：

  「注意到一个信息差异：
  ── 你刚才说的：{user_statement}
  ── Brand Brain 中的记录：{existing_record}（来自 {file}，{date} 更新）

  请确认：
  a) 以新信息为准，更新 Brand Brain
  b) 保持原有记录，忽略本次差异
  c) 两者都不对，我来说明实际情况」

  Step 3：根据用户选择执行：
  ├── 选 a → 更新对应的 Brand Brain 文件，记录变更原因到 learnings.jsonl
  ├── 选 b → 不修改文件，继续当前工作流
  └── 选 c → 让用户补充说明，然后重新判断
```

### 8.3 铁律

```
冲突检测铁律：
  ✘ 绝对禁止静默覆盖 Brand Brain 中的已有记录
  ✘ 绝对禁止在未告知用户的情况下使用矛盾信息继续工作
  ✔ 必须在发现冲突后立即暂停并询问用户
  ✔ 必须同时展示新旧两份信息，让用户做出知情决策
  ✔ Config 文件的冲突检测优先级最高（因为它们很少变动，变动通常意味着重大变化）
```

---

## 九、结构化记忆系统

> 本章节定义 `learnings.jsonl` 的结构化记忆格式，以及与全场景静默捕获协议的衔接方式。

### 9.1 数据结构定义

每条记忆必须是一个合法的单行 JSON 对象，包含以下 8 个严格的元数据字段：

```json
{
  "ts": "2026-04-08T10:00:00Z",
  "worker": "afa-seo",
  "type": "pitfall",
  "key": "avoid-emoji-in-email-subject",
  "insight": "用户不喜欢在邮件标题使用 emoji，目标客户群体偏专业，emoji 降低可信度",
  "confidence": 8,
  "source": "observed",
  "related_files": ["brand-guidelines.md"]
}
```

### 9.2 字段规范

| 字段 | 类型 | 必填 | 说明 |
|:---|:---|:---|:---|
| `ts` | string | ✔ | ISO 8601 时间戳，如 `2026-04-08T10:00:00Z` |
| `worker` | string | ✔ | 产生该教训的 Worker 名称，全局通用则为 `global` |
| `type` | enum | ✔ | 枚举值：`pitfall` / `pattern` / `preference` / `error` / `correction` / `promoted` |
| `key` | string | ✔ | 简短的唯一标识符，如 `avoid-emoji-in-email-subject`。同一个 key 可以有多条记录（以 ts 最新的为准） |
| `insight` | string | ✔ | 一句话描述教训内容，必须包含可操作的行动指导 |
| `confidence` | number | ✔ | 1-10 分。用户主动声明 = 10，用户纠正 = 9，错误捕获 = 7，观察发现 = 5 |
| `source` | enum | ✔ | 枚举值：`observed`（系统观察）/ `user-stated`（用户明确表达）/ `error-recovery`（错误恢复） |
| `related_files` | array | ✖ | 关联的 Brand Brain 文件路径。如果关联文件已不存在，该条记忆自动失效 |

### 9.3 type 枚举值说明

| type | 说明 | 典型场景 |
|:---|:---|:---|
| `pitfall` | 经验证无效或有害的做法 | 某类文案转化差、某种定价导致流失 |
| `pattern` | 经验证有效的可复用模式 | 某类标题打开率高、某种素材 ROAS 好 |
| `preference` | 用户的特定偏好或规则 | 用户不喜欢红色 CTA、偏好简洁风格 |
| `error` | 系统执行失败的教训 | 某平台 API 变更导致失败、某策略触发平台审核 |
| `correction` | 用户纠正系统的错误做法 | 用户说「不对」「其实应该是」 |
| `promoted` | 已晋升固化到 Brand Profile 的记忆 | 读取时自动跳过（见 9.6 晋升机制） |

### 9.4 文件示例

```jsonl
{"ts":"2026-03-15T09:00:00Z","worker":"afa-email","type":"pattern","key":"numeric-subject-lines","insight":"带数字的邮件标题打开率更高，数字提供具体预期，62% vs 41%，后续优先使用数字式结构","confidence":7,"source":"observed","related_files":["brand-guidelines.md"]}
{"ts":"2026-03-15T09:30:00Z","worker":"afa-email","type":"pitfall","key":"avoid-emoji-in-email-subject","insight":"邮件标题使用 emoji 导致打开率下降 8%，目标客户偏专业，避免使用","confidence":8,"source":"observed","related_files":[]}
{"ts":"2026-03-20T14:00:00Z","worker":"afa-fb","type":"pattern","key":"vertical-video-roas","insight":"竖版视频素材 ROAS 比横版高 2.3 倍，后续优先使用竖版","confidence":6,"source":"observed","related_files":[]}
{"ts":"2026-03-22T11:00:00Z","worker":"afa-convert","type":"preference","key":"trust-badge-refund-policy","insight":"用户对 30 天无理由退货的信任标识反应最强，所有产品页优先展示","confidence":9,"source":"user-stated","related_files":["products.md"]}
{"ts":"2026-04-01T08:00:00Z","worker":"afa-fb","type":"error","key":"meta-health-product-review","insight":"Meta 更新广告政策，健康类产品需要额外平台审查，提前预留 48 小时审核时间","confidence":7,"source":"error-recovery","related_files":[]}
```

### 9.5 读取与生命周期管理

```
基线实现（纯 Prompt 驱动，全平台 100% 兼容）：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
读取 learnings.jsonl 时，必须按以下顺序执行过滤：

  Step 1 ─ Worker 过滤
  ├── 只加载 worker 字段匹配当前模块（或为 global）的记录
  ├── Hub 初始化时 → 加载所有 worker 的记录
  └── 诊断模块 → 加载所有记录（诊断需要全局视图）

  Step 2 ─ 失效检测
  ├── 如果 related_files 中的文件在文件系统中已不存在 → 跳过该条记录
  └── 如果 type 为 promoted → 跳过该条记录（已固化到 Profile）

  Step 3 ─ 去重与多版本提醒
  ├── 按 key 去重，保留 ts 最新的一条
  └── 如果同一个 key 有多条记录且内容冲突，标记为 [MULTIPLE_VERSIONS]
     └── 主动向用户确认哪一个是当前正确的规则

  Step 3.5 ─ 简化衰减（与增强实现的 30 天衰减对齐）
  ├── 检查每条记录的 ts 字段，计算距今天数
  ├── 每过 30 天，confidence 视为减 1（不修改原文件，仅用于本次排序）
  └── 衰减后 confidence 低于 3 的记录 → 丢弃

  Step 4 ─ 截断
  ├── 按衰减后的 confidence 降序排列
  └── 最多只提取最相关的 5 条记录
```

```
增强实现（Python 辅助脚本，支持脚本执行的平台优先使用）：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
在支持执行 Python 的环境中（如 Manus、MuleRun、Claude Code），
优先执行：
  python afa/_system/scripts/memory_manager.py --worker <current_worker>

该脚本将自动完成：
  ├── Worker 过滤
  ├── 失效检测（文件存在性检查）
  ├── 30 天衰减（每过 30 天 confidence 减 1，低于 3 分自动丢弃）
  ├── 按 key 去重
  └── 输出最相关的 5 条记忆

如果脚本不可用（文件不存在、运行报错、权限不足等），必须自动回退到基线实现，不得中断记忆加载流程。
```

### 9.6 记忆晋升机制（Promotion）

```
触发条件：
  当 Agent 在反思时发现某条 learnings.jsonl 中的记录
  被反复命中（例如，连续 3 次会话都用到了同一个 Pattern）

执行流程：
  Step 1：主动向用户提出建议：
    「我注意到我们多次使用了 [{insight 摘要}]。
    为了提高效率，建议将其固化为 Brand Brain 的全局规则
    （写入 {target_file}）。是否同意？」

  Step 2：如果用户同意：
    ├── 将该规则写入对应的 Profile 文件（如 brand-guidelines.md）
    ├── 在 learnings.jsonl 中追加一条该 key 的记录，type = promoted
    └── 后续读取时自动跳过所有 type = promoted 的记录

  Step 3：如果用户拒绝：
    └── 不做任何操作，该记忆保留在 learnings.jsonl 中

晋升铁律：
  ✘ 绝对禁止未经用户确认就自动晋升
  ✔ 晋升建议必须明确说明将写入哪个文件
  ✔ 晋升后的 promoted 记录永远不删除，作为审计轨迹
```

### 9.7 向后兼容

```
如果已存在旧版 learnings.md：
  ├── 首次启动时读取 learnings.md，将每条记录转换为 JSONL 格式
  ├── 追加到 learnings.jsonl（转换时 confidence 统一设为 5）
  ├── 将 learnings.md 重命名为 learnings.md.bak（保留备份）
  └── 后续只使用 learnings.jsonl
```

---

## 十、Assets 格式

```markdown
# 资产登记

> 由 AFA DTC 系统自动维护。新条目追加在活跃资产表底部。

## 活跃资产

| 资产名称 | 类型 | 创建日期 | 关联活动 | 状态 | 备注 |
|---------|------|---------|---------|------|------|
| welcome-sequence | 邮件序列(6封) | 2026-03-15 | 品牌上线 | 已上线 | 打开率 42% |
| hero-banner-v2 | 图片 | 2026-03-18 | 品牌上线 | 已上线 | 1200x630 深色版 |

## 已退役资产

| 资产名称 | 类型 | 退役日期 | 原因 |
|---------|------|---------|------|
```
