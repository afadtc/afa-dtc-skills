# CHANGELOG — AFA DTC Skills

> 本文件是全库唯一保留历史版本号的地方。正文（SKILL.md / references / _system）遵守「不保留历史版本号锚点」卫生规则；所有版本沿革集中于此。
> 版本锚点自 v2.4.8 起从正文迁移至此。本文件按版本号倒序排列，不逐版标注发布日期。

---

## v2.7.7 — 测试店快速测品体系（当前发布版本）

补齐 dropshipping 模式的端到端方法论：此前 `supply_chain_mode = dropshipping` 仅为各模块降级分支的优先级调序，无完整"选品→验证→上线→测试→放大/品牌化"链路，本版以「新 reference + 现有文件扩写」方式落地（模块数维持 31 不变）。

**新增 4 个 reference**
- `afa-explore/references/winning-product-playbook.md`：测试店范式与建店纪律（广义店先行、赢家再品牌化）、赢品五标准 + 四排除、竞对执行质量评估（房间改进法则）、三层零广告费验证漏斗（广告持续性 → 跨平台需求量 → AI 深研风险筛查，非合规裁决）、快速客户语言提取。
- `afa-convert/references/ai-page-rewrite-sop.md`：模板 JSON 八步 AI 整页改写工作流（先理解后改写、反幻觉护栏）、首屏细节武器库（单位本地化等）、dropshipping 信任基建包（物流查询页 / 动态时效组件 / 免费+付费保险双轨运费）、三条合规红线替代表（编造社证 / 假紧迫 / 无据功效数字）。
- `afa-creative/references/dropshipping-ads-playbook.md`：四种广告形态分类学（搬运不采用并给合规替代 / 静态图为测试默认 / 原生软文须明示广告身份 / VSL 为成熟期）、静态图生产线五步、产品图序列模板、AI 工具编排六原则、五条素材红线（含"竞对照片不可作编辑底图"）。
- `afa-fb/references/day-zero-testing.md`：零数据账户冷启动结构（1 CBO + 1 广告组 broad + 3-5 静态图、四大英语市场、次日 0 点排期、增强全关）、双档预算表（粗筛 $5-10/天/品只判死 vs 验证 $30-100/天可判生，按预算宽松度选档）、产品级出口（Kill / Iterate≤2 轮 / Scale）、与 ASC 体系的毕业衔接。

**五处口径收口（经 Max 裁决）**
- 铺货测试哲学（条件化改写）：`afa-product` core-frameworks「传统铺货测试已失效」改写为「低质铺货已失效 + 品牌级质感测试店为 dropshipping 合法变体」，与 explore 双向互注；
- 测品预算双档分层互认：`afa-fb` anti-patterns dropshipping 段 $5-10/组 旧口径升格为粗筛档，与验证档（$30-100/天）并列，仲裁依据统一挂 launch mvp-testing 样本量真源，档位选择须先对齐用户预算宽松度；
- Advantage+ 增强分层互认：core-frameworks「+22%」句补成熟账户口径注；冷启动测试期全关（0/6）保单变量归因，毕业条件复用 ASC 前置（30 天 ≥50 购买）；
- 广告密度信号消歧：`afa-compete` 四维密度表（品类广告主数，赛道决策）与新增 `afa-compete/references/ad-intelligence.md` §4 单店广告信号学（单店广告数 20-75 黄金带 + 轨迹信号 + 赢家版式收集法，逐品决策）互加防混用注，dropshipping 逐品决策以单店信号优先；
- 上市节奏分流：`afa-launch` 新增模式 F 测品快速通道（48 小时上线清单、D-2→D+7，判读复用三级裁决并补产品级出口），四阶段模板加分流注，路由树与特殊触发器同步。

**其余扩写与注册**：`afa-ops` anti-patterns Dropshipping 适配节补供应商三分法与升级阶梯（公开平台→混合代发平台→私人代理 10-20 单/天门槛→私标）及测试单/变体极简纪律；`afa-aov/references/bundle-strategy.md` 新增 §4 测品场景 Offer 工程（Offer 即护城河：数量阶梯默认中档 + $0 赠品展示 + 赠品选法 + 数字零成本赠品 + 捆绑毛利倒推目标 CPA）；explore/convert/creative/fb 四个 SKILL 注册新 reference 加载条件；Hub 新增 WF12 测试店快速测品（与 WF1 互为镜像，终点接 scale 工作流 C），WF1 加分流行；README 工作流计数 11→12，interaction-protocol todo 触发同步 WF1-WF12。

**红线纪律**：全部新增内容不吸收"AI 编造评论/评价图、搬运他人视频素材、竞对原图作底图、假人设原生广告、永久假倒计时、无据功效数字"六类做法，逐条给出合规替代并指回既有真源（购后催评流程 / Spark Ads 授权 / AI 重建版式 / 明示广告身份 / 真实档期 / 铁律 9）。经验阈值一律标注内部经验、仅作分诊起点。

**仓库布局与发布物**：GitHub 仓库沿用插件市场布局（`.claude-plugin/` + `skills/`），31 个模块与 scripts/evals/examples 整体位于 `skills/`，模块间相对引用不变；CI 三道门禁的根目录参数指向 `skills`；`release_check.py` 自动识别平铺与插件市场两种布局（根文件按 zip 根检查、模块与工具按模块根检查、门禁按布局拼装命令）；`.claude-plugin/marketplace.json` 与 `plugin.json` 版本同步 2.7.7、Skill 计数 30→31；GitHub 长版 README 与包内 README 合一，发布 zip 即仓库快照。

**终审修复 6 项（发版前语义自查所得）**：fb SKILL Phase 3 插行后未顺延致双"3."、creative SKILL Phase 3 同类双"4."（两处编号级联修正）；compete / launch 两个 SKILL 的共享继承上下文表补 `supply_chain_mode` 行、creative 执行输入表同步补行（消除"模块不接收字段却写适配"的 gg 类漏洞）；三级裁决 D+3 钩子率指标与静态图形态互斥——day-zero-testing 与 launch 模式 F 两处补口径注（视频=Hook 率、静态图=CTR 主判）；粗筛档 CTR 杀线（<0.8%）与全链路点击黑洞线（<0.5%）补分层口径注（只判死档从严，两线用途不同勿互替）。

**终审第二轮修复 7 项（交叉约束自查）**：Hub WF12 声称"主导 afa-foundation"但 Supervisor 层无对应工作流（路由在中枢层断链）→ `afa-foundation` 增工作流 D 测试店快速测品（对应 WF12，明示跳过 A 的 Step 3-4 的理由）、`afa-paid` 增工作流 D 测品冷启动（无品牌定位前置）、`afa-scale` 工作流 C 触发补"WF12 赢家转入"入口；全库 description 无一含 dropshipping/一件代发/测品/测试店 触发词（测品诉求无法命中路由）→ Hub description 补 4 个综合触发词，评测集新增 hub-06/07（中英各一，52→54）并同步 README 计数；launch 模式 F 与本模块严禁清单互注（Scale 出口≠正式规模化仍受 PMF≥75 门约束、测试期单渠道≠渠道押注）；day-zero-testing 补三处口径（验证档 $30 下限 vs 成熟期每活动 ≥$50、四国默认须让位于上游已确认的 `primary_market`、分诊表补基准治理三字段）；ad-intelligence §4.1 分诊表补三字段；aov 测品 Offer 默认选中补透明化约束；CHANGELOG 错字 SKill→SKILL。

**四线盲审修复（独立会话、引句实证制，A 线真源一致性 / B 线协议与路由 / C 线内容逻辑与合规 / D 线工程卫生；四线共报 A 级 22 / B 级 54 / C 级 59，去重后采纳 71 项、驳回 3 项、遗留提示 5 项，详见随版《v2.7.7 盲审报告与裁决》）**。按主题收口：
- **样本量与预算档自洽**：粗筛档加"累计展示 ≥1,000 后才判杀"样本守卫并改用 ABO、幸存者升档只取预算撑得起的前 1-2 个；验证档"3-5 天出结论"改为公式（到 10 转化所需天数 ≈ 10 × 目标 CPA ÷ 日预算，$30/天约 10 天）；launch §4.2 与 fb 最低预算两道闸门加测品双档例外；$30 下限与"每活动 ≥$50"分层注改写。
- **产品级出口对齐 mvp 真源**：模式 F 不再自称"不新造"，明示为新增规则；Kill 线改为"0 转化且花费达 1.5× 目标 CPA（创意基准）或 D+7 CPA >200%（启动前选 150% 者按 150%）"，Iterate 为"再测 1 轮、不允许第三轮"，Scale 须满足胜出者确认（≥10 转化、连续 3 天波动 <20%）并在达到扩量 SOP 前提后才交接；规则只在 launch 模式 F 定义，执行与回传只归 paid 工作流 D，day-zero 改为引用；补零转化出口。
- **地理默认改回全局单市场规则**：Day-0 以上游 `primary_market` 为准，未知时按英语通用保守版并确认履约覆盖；四国合投降为可选扩展项（用户确认 + 本地化规则 2 清单 + 季节性品剔除反季市场 + 按国拆读 + 回传 multi_market）。
- **WF12 链路补齐**：foundation 前置文件表加工作流 D 例外行（products.md 以最小测品档案为准、voice-and-tone.md 降可选，不改道）；explore 新增模式 G 赢品验证并产出最小测品档案；Hub WF12 改为多中枢协同写法（foundation 工作流 D → monetize 新增工作流 E「测品页面与 Offer」→ paid 工作流 D → scale 工作流 C），Hub 路由表加测品信号行、判定规则加"用户明示即单信号"；paid 路由表加工作流 D 行并豁免 voice-and-tone 前置、确认点移至预算档位；creative Phase 1 加测品豁免模式 1 前置；compete 特殊触发器加测品分支；scale 工作流 C 加 WF12 入口门槛与回接 foundation 工作流 A Step 3；工作流 A 加中途入口；explore/fb/convert/creative 四个 SKILL §1.1 补 `supply_chain_mode` 行；context-matrix / preamble 同步字段语义；routing-checklist 七个模块补 WF12 触发与后续路由；launch work-modes 补模式 6 索引；所有加载条件收窄为"dropshipping 且处于测品阶段"。
- **创意真源冲突**：静态图文字改为"AI 出底图留负空间 + 后期叠字、AI 图内 ≤3 词"（对齐 creative anti-patterns 与 typography-guide）；版式→标题→角度顺序与 mvp"先测说什么"分层注；评价拼图式/前后对比式版式加限定；Meta 侧合规替代改为创作者授权 + 合作广告（Spark Ads 仅 TikTok）；版式收集法指定 ad-intelligence §4.3 为唯一真源。
- **铁律 11 与红线**：L3 改名"AI 深研风险筛查"，产出风险事实卡 + 专业升级触发器，去掉"合规裁决/必遭律师函/衍生侵权/本身合规"等裁决式表述；社证一律加"仅限真实评价、零评价期省略"（day-zero 星级行、主页评价区、convert 适配节）；亲友账号改为本人创建并授权管理、删去"女性账号"建议；"售罄仍可下单"加供应商库存可核前提；付费运费档须对应真实服务且不夸大命名、删"履约成本≈0"；"付运费是第一大弃单源"改为"意外的额外费用（含运费）"。
- **Offer 算术与前提**：买 2 送 1 + 赠品结构要求单品加价 ≥5 倍（3 倍时混合毛利恰压 50% 线），默认档须过 promo_breakeven bundle 校验；实物赠品须同供应商合单，否则数字赠品；三档阶梯以"推荐档"替代零销量期的"最受欢迎"；参照价须可核；验证信号改看主动切换率；履约成本定义补国际运费/税费/赠品并指向 landed_cost 脚本。
- **口径与卫生**：竞对执行质量法则更名并补"跟品 ≠ 模仿"；单店信号分诊带端点去重（10-19 / 76-100）、"翻倍"改"成倍"、按单品计广告数前提、与品牌级 ">6 个月"分层注；compete 口径注扩到电商饱和度维度并与 expand"搜不到"解读互注；VOC 七源改六源（explore SKILL 旧计数同步）；采集窗口字段名统一；四个新 reference 头部补完整交付物句与中文示意声明；display_name 全部对齐 skill-directory；fb SKILL 第八章模式号 4→5（旧遗留）；convert SOP 补"备份原 JSON"步与"逐句照抄"红线行；evals README/脚本 docstring 五字段由 goal 改 deferred_goals（旧遗留）。
- **驳回留档**：Supervisor/Worker description 增测品触发词（与 v2.6 批次 16 方案 A 的触发词分层设计冲突，Hub 综合触发词已覆盖）；模式 F 下沉 references 以压 SKILL 行数（与模式 A-E 内联体例不一致，size 提示为既知项）；"亲友账号"整条删除（改为合规表述保留）。
- **遗留提示（非本版引入，未改）**：launch 模式 C"满分 10 分"与 PMF 模板百分制并存；scaling-sop EMQ >6.0 与 fb anti-patterns ≥8 并存；product/payments 等 reference 开头说明含模块代号；内核一行版与 iron-rules.md 的铁律编号两套体系。

## v2.7.6 — 终验尾单收口

对 v2.7.5 独立终验确认的 14 条未修项全量收口：基准声明「唯一」改「Hub 路由层」并注明看板快筛线归属；邮件/SMS 三行指标分母 发送数→送达数（与送达口径统一）；异常播报模板补推导与数据基础字段；TikTok 生态图串台的 Demand Gen 更正为 Collection；PMax 标题下限 11→10（与 5+5 自洽）；「S Process」讹名 6 处更正为 Simprosys；客服「平均响应时间」去 ART 缩写解双指标同名；fb/tt 工作模式小节重编号对齐 SKILL 路由表并补映射注记；gg 两份 KPI 章互认定真源（work-modes-and-kpi 为真源）；工程黑话（批次17/D1×2）清除；客服自动化 70% 与 60% 分层口径调和；平台创意规范补口径说明头；60/40 法则补命名定义。

## v2.7.5 — 七线终审全量修复

落实《AFA v2.7.4 七线全量终审·定谳报告》的**全部 208 条**（A 级 24 / B 级 96 实 / C 级 87 + 1 条驳回项不修）。四道门禁全绿；新增第五类机检（§锚点存在性）。

**A 级 24 条（发版阻断）**
- **记忆协议冲突簇**：`brand-brain-template` §七、`afa-diagnose` 模板五、`afa-dashboard` work-modes 三处的 learnings.jsonl 模板原为 markdown 日志格式，直接违反 brand-memory-protocol 第九章「每行单行 JSON」——全部重写为协议八字段 JSONL；dashboard 虚构的「Hub 统一四分类格式」映射回协议真实 `type` 枚举。
- **协议层结构性矛盾**：kernel 的五个不可丢字段 `goal` → `deferred_goals`（对齐 Hub 真源）并全量重注入 31 个 SKILL.md；kernel 的「三级降级」与 degradation-rules 同名反向（数据轴 1→3 vs 平台轴 3→1，Worker 读 Level 3 语义反转）→ 改称「数据完备度三级 D1/D2/D3」并明示双轴；`interaction-protocol` L587 未闭合围栏致 §8.6 后半结构损坏（标题被吞进代码块）→ 补闭合。
- **编辑损伤**：全局替换事故病句 4 处（「标注为行业参考（非用户实际数据）其他指标」等双重否定把反模式写反）；`afa-gg` anti-patterns 区段截断 + 孤悬箭头（该模块实际不接收 `supply_chain_mode`，故改题而非编造内容）；`afa-tt`「20 大 Hook 公式」实为 15 个（三处承诺统一为 15）；`afa-diagnose` 等待范式残留 → 保守首答；`afa-fb` 28 天点击归因窗口（iOS 14.5 后已下线）→ 移出可选项、改历史注记。
- **数字/量纲互斥**：HHI 双量纲（0-1 vs 0-10,000，致「HHI>6,000」触发器永不命中）→ 统一 ×10,000 口径 + 换算示例；全库案例 ICE 0-10 制 vs 真源 0-100 制（33 处案例分值全落「暂缓」档）→ ×10 对齐；`afa-gg` 示例 ICE 裸乘积 504 → 50.4；`afa-tt` 扩量 30% → 20%；`afa-launch` 预算 20%/30% 与 CPA 150%/200% 两组「铁律」互斥 → 分层互认（默认纪律线 + 绝对红线 / 默认关停线 + 高容忍档）；`afa-influencer` 第三张报价表旧分层 → 对齐 10K-100K/100K-500K；`afa-sms` 分工矩阵把弃购写成 SMS 先行（与全局瀑布及同文件 §3.3 正向相反）→ 改回 Email 先行；单渠道弃购流补「让位全局瀑布」豁免注记；`afa-convert` 落地页硬编码「每变体 1,000 访客」（与样本量真源差 3-78 倍、诱导欠功效实验）→ 改指速查表与 `afa-convert/scripts/ab_sample_size.py`。

**B 级 96 条（七大家族）**
- **死锚点 14**：§编号/章节名引用悬空全部改指真实位置（含 `afa-launch` 17 处旧结构编号、`afa-email` §2 缺号与五大反模式清单名实不符、`afa-brand`「Tier 4 溢价飞轮」空承诺改题）。
- **跨文件红线漂移 21**：按「对齐 / 分层互认」二择一逐组收口——无依据的纯漂移对齐真源（fb 频次四梯、fb 保守扩量 20-30%、social 完播/分享同文件自矛盾、influencer 联盟退货率、email 弃购优先级、sms 召回序列、scale 争议率 2% → payments 0.9%、免邮门槛均值→众数、打开率分母→送达数）；有依据的分层互认并双向加口径注（ASC 占比、冷启动配比、seo 见效周期两里程碑、influencer 双口径佣金、retain 召回率两分母、dashboard 加载速度/回收期）。
- **平台事实 11**：Microsoft 高发件人要求（原写「2026 年加入」）经核实为 2025-04 公告、**2025-05-05 起执行**（先入垃圾箱后 550 拒收）；Meta AEM **协议未退役**，实为 2025-06 移除配置界面与 8 事件上限（原判断有误，已按事实写）；Meta 20% 文字规则 2020 年即废止；HARO/Connectively 2024-12-09 关停、2025-04 由 Featured.com 重启品牌；Google PMax 优先级变更实为 2024-10 分批推出（非「2025 年底」）。**查不到原始来源的硬数（geo 6.5 倍/30-40%、expand $242B、seo 6,000 字符、brand NN/g 30%）一律定性化 + 标注「内部经验估算」，无一处补造来源。**
- **协议/字段一致性 12**：Worker 计数三处口径统一（31 目录 = 1 Hub + 5 Supervisor + 25 Worker，其中 25 = 23 执行 Worker + 2 全局引擎）；记忆矩阵 `afa-payments` 整行缺失补齐、`ALL` 改为实际 Requires；五个模块 Context Matrix 补 `store.md`（Brand Brain 文件）；供应链枚举二值 → 四值；Brand Brain 的 assets 双规范择一为真源；preamble 补记忆衰减步；成本标签三套词表对齐 `afa/_system/cost-tag-spec.md`；`seasonal_mode` 的 `peak`/`bfcm` 错值 → `peak_season`（原枚举定义本就含 BFCM，故不新增枚举值）。
- **工程脚本加固 12**：`release_check.py`（MUST_EXIST 补全、learnings 校验由「walk 撞见」改显式断言+JSONL 格式校验、临时目录清理、顶层目录自动剥离、DIRTY 精确匹配、句柄 with）；`build_inject.py`（HEADER 损坏不再静默报绿、total=0 护栏）；`run_evals.py`（**five_fields 断言原因内核注入而恒真、等于空转** → 剥离内核块后再校验模块正文，改造后立即抓出 `afa-payments` 正文缺 `deferred_goals`）。
- **代号卫生 15**：按「仅高风险位」口径——用户可见话术、交付物模板（`voice-building-sop` 的 `by /afa-brand` 会直接写进用户的 voice-and-tone.md）、无免责头的 reference 散文，全部改用 display_name；31 个 SKILL.md 的 H1 统一去代号；纯内部编排文本（路由表、completion YAML）维持并记录为设计。
- **错字/小损伤 11**：斋月（原「斑月」）、英镑、抄袭、蚕食效应（原「自唠化」，据 §2.5 语境判定非「自动化」）、宿醉期、≥（原「♥」）、三处 anti-patterns 孤悬围栏与 fb 段落错插等。

**C 级 87 条**：ICE 维度命名统一、业务脚本护栏与退出码、examples/README/evals 文档细节（补 foundation 直达用例，评测 51→52）、ASCII 树形图与方框宽度错位 5 处、`_system/` 简称补严格相对路径 17 处、`afa-cx` DPS 内部字段移出用户模板、退货抵税补辖区限定、UGC 分层对齐等。

**发现的真 bug（报告未列，修复中自查所得）**
- `afa-aov/scripts/promo_breakeven.py` 折后毛利率公式写作 `m − d`，正确应为 `(m − d) / (1 − d)`（相对折后售价）——旧公式在 60% 毛利 / 15% 折扣下算出 45%，真实值 52.94%，**系统性低估约 10 个百分点**，已修正并补口径说明。

**机检加固**：`repo_lint.py` 新增 **§锚点存在性检查**（形如「反引号包裹的目标文件名 + §N.N」的引用，其目标小节必须真实存在；覆盖全库 83 处引用，anchor 为 ERROR 级）——把「死锚点」这一整类从人工排查变成机器拦截。另消除两处 .py 版本锚点陷阱（门禁只扫 .md，抓不到脚本注释里的陈旧版本号）。

**驳回项**：D 线称 `afa-convert` L96「（内部：afa-payments）」是「指向不存在模块的死路由」——`afa-payments` 模块实存，仅代号卫生问题成立，已按代号卫生处理。

## v2.7.4 — 第四道门禁与英文路由覆盖

新增 `scripts/release_check.py` 第四道门禁：对发布 zip 解压本体做结构/一致性/卫生断言，再以解压体自带三道门禁复检本体，支持 `--against` 输出相对上一版的新增/删除/修改文件清单，把「只验本体」从验收纪律固化为机制（不做语义判断，边界见脚本 docstring）。31 个模块 description 于「触发词:」段内补英文触发短语（v2.4.7 的中英触发词在描述精简中被压缩，本轮按 1024 字符规范恢复英文覆盖，查重按词元级比对）；新增 `evals/cases/english.jsonl` 10 条英文路由用例，评测 41→51。README 同步脚本计数（10→11）、评测计数与第四道门禁说明。全局 description 预算目标 4500→5600 字符（英文触发词为刻意的范围扩展，单条 ≤1024 硬限与词元级查重不变），lint 恢复 3 条既知 size 提示。第四道门禁首跑即产出：发现 README 的 LICENSE 链接自 v2.7.0 起无对应文件（既有死链扫描仅覆盖反引号 .md 路径故历轮未检出），本版补齐 CC BY-NC 4.0 通知文件。

## v2.7.3 — 弃购流跨模块口径互认

经用户裁决（三选项采纳 A·互认注记）修复跨模块口径漂移 1 项：邮件弃购流将 SMS 收缩到高价值路径 vs 全渠道瀑布真源弃购示例全量适用，两侧互不知情——email 弃购流 §2.4 补「保守默认」分层口径注记并指回真源，真源示例旁补「分层由品牌定」注记并指回邮件实现。不改任何流程拓扑，两路径触达预算维持 3 次不变。

## v2.7.2 — 独立终审修复批次

六线独立评审对 v2.7.x 新内容的终审产出：修复 gg 描述4 区段编辑损伤（重建被误删的长度行与 Sitelink 小节头）；ICE 优先级双尺度统一为百分制（priority-scoring §4 与 diagnostic-templates 三处，消除 0-10/0-100 并存）；gg ICE 表头「Data Basis」对齐为 Confidence（两文件）；social SKILL 同步四支柱表述；influencer 互注句修正（SaaS 两表本一致）；pr SKILL 阈值行定性化同步；三渠道抑制条款正式收编入 omnichannel-orchestration（附则，使「唯一真源」表述属实）；monetize 市场注同步「中东/南欧」；landed_cost.py 补 qty 校验与 VAT 联动敏感度；metrics_snapshot.py 增订单号聚合（Shopify 多行订单去重）与日期/金额口径说明；freeze SOP 删未使用参数；expand SKILL 补计算脚本节；routing-checklist 二级标题计数 26→25；示例 learnings source 字段改协议枚举；README 铁律与成本标签措辞厘清；budget-calculator 速算表加示意值注。另：评审报「expand 诊断系统标题带代号」经核为误报（实际标题干净），驳回留档。

**终审保险轮（六线全量 344 文件独立评审，引句实证制）追加修复 13 项**：metrics_snapshot 聚合降级加警告、复购输出 None 改「—」占位；tt 创意储备两口径分层互注（日常底线 vs 扩量加严）；tt 扩量幅度 30%→20% 统一；fb/gg/tt 输出格式章子节号级联修正；seo/influencer 共 8 个 references 开头说明去内部代号（改角色名）；sms 弃购顺序两处对齐全局瀑布（Email 先行、未打开再 SMS，保留 SMS 主导品牌例外）；email 购后流抑制表述与 §6 优先级瀑布对齐；aov 警戒线/目标线互注；payments 两处脚本相对路径补 `../`；vamp_check 预警分级由两级改三级（启用 0.65-0.9 预警带）；diagnostic-rules 退货率口径与 reasoning-rules 品类化同步；routing-checklist 补「三、执行与协同规则」二级标题；README 脚本构成说明。

**复验轮追加修复 11 项**：launch PMF 分档对齐四档真源；ops 团队/业务两套阶段模型互注；gg work-modes 小节全文去号；tt 四文件标题去内部代号；email×sms 欢迎折扣码双渠道协同闭环（两侧分支注）；pr 两处「动态口径」悬空引用改实为定性分级指向；geo/creative 两处开头说明去代号；ops ART 撞缩写更名（Avg. Resolution Time）；unit_economics 关税 FOB 简化口径注（CIF 精确口径指向 landed_cost）；示例 learnings 第 4 条 type 配对修正（correction→pattern）。popup 预算表列 3 总计经逐项复算修正为 $19,500-$82,000（原 18,500 为笔误）。

**终查轮（六线全覆盖 + organic 补跑）经用户批准修复 7 项**：launch SKILL 正文 PMF 同步四档真源；popup 预算表列 2 总计修正为 19,500；retain 积分返现 5% 改为参考护栏并互注 loyalty-playbook；creative 系 3 处开头说明去内部代号（backtick 路径保留）；new-digital 订阅时长基准与退订率换算对齐（>12 个月）；influencer 创作者分层三文件统一为 10K-100K/100K-500K；social-commerce-kpis 补基准治理声明。

## v2.7.1 — 架构合并：afa-messaging 并入 afa-sms

依据实际依赖关系定谳：messaging 的瀑布抑制真源与 email/sms 主线全部指向 sms 模块，本质是分册而非独立部门；合规隔离改由文件边界实现。变更：删除 afa-messaging 模块；afa-sms 升格「消息营销引擎」（description 增 WhatsApp/RCS 触发词，SKILL 增富媒体分册节，新增 `afa-sms/references/whatsapp-rcs-playbook.md` 含两套合规体系互斥警示与 RCS 章节）；Hub 覆盖列 / monetize 管辖与路由 / routing-checklist / skill-directory 四处反注册；全库计数 32→31（1 Hub + 5 中枢 + 25 执行模块）；evals 用例改指向 afa-sms；lint EXPECTED_SKILLS=31。另：payments 边界四向闭合——修复 scale 路由表遗留的「争议率→ops」双头路由（现明确转 payments）；ops/convert/retain 三处支付相关内容补边界互注；payments 补订阅扣款失败通道侧条目与反向互注。

## v2.7.0 — 产品化功能版

从「工程完美」走向「上手即有用」：①新增包内 README（安装/第一句话说什么/架构与模块速查）与 `examples/`（10 分钟上手 + 三段黄金示例会话 + brand-brain 示例 fixture 含 5 条 learnings 样例）；②afa-payments 补厚为武器级——新增 `chargeback-evidence-playbook.md`（按 reason code 四大家族分型证据包 + 响应时间线 + 英文反驳信骨架 + 应诉/接受利润算术）与 `freeze-response-sop.md`（冻结分型 + 黄金 72 小时 SOP + 申诉材料清单 + Rolling Reserve 现金流可复算推演 + 结构性预防）；③afa-messaging 新增 `whatsapp-flows-playbook.md`（模板/会话双轨与 24h 窗口机制、三大核心 Flow 与三渠道瀑布对齐、合规底座）；④新增两个数据脚本：`afa-dashboard/scripts/metrics_snapshot.py`（订单 CSV → 自基准画像：趋势/复购/cohort，把「用户自基准」从口径变成能力）与 `afa-expand/scripts/landed_cost.py`（多关税情景落地成本 + 敏感度）；⑤各模块 SKILL 与文档补脚本优先加载指引；lint 版本白名单纳入 README。

## v2.6.7 — 语义深检补丁

落实《AFA v2.6.6 语义深检与提升空间报告》第二章全部 17 条（中 7 / 低 7 / 优化 3）：launch Go/No-Go 判定修正并补 4/7 档；fb 扩量口径统一 20%（5 处）；gg RSA 超限示例重写至硬限内（标题 ≤30 / 描述 ≤90）并为 ICE 旧锚点加口径注；influencer 食品佣金对齐基准并两表互注；ops 新增「运营准备度评估（七维）」承接节、expand 前置检查加真源注；email 补 Browse×Win-Back 互斥；sms 字符预算加总控注（两处）+ 混排修正；retain §2.4/§9.1 互注；A/B 速查表与脚本口径互注；pr 声量阈值定性化 + §5 补治理说明；reasoning-rules 退货率品类化；product LTV:CAC 与仪表盘互注；social 支柱统一四支柱 30/30/20/20；tt 补 100-120% 档。补丁级：in-file 版本头维持 v2.6。

## v2.6.6 — 红线类横扫收尾

落实《AFA v2.6.5 收官验收报告》第三章的唯一残余（红线类横扫的最后一处）。补丁级：in-file 版本头维持 v2.6。

- **毛利率健康线口径注释**：`afa-diagnose/references/core-frameworks.md` L142 的「DTC 健康线 >65%」与全局分诊真源 `afa/references/diagnostic-rules.md`（健康 >60%）存在 5 点漂移、原无互注。查明该 65% 并非笔误——与同文件 L147「毛利率 <65% 即逐层排查溢价缺失」是同一条溢价排查触发线，属本模块内部自洽的有意口径。故照 product 先例**保留 65%** 并补口径注释：说明 65% 为本模块溢价排查触发线、全局分诊健康线取 >60% 以 diagnostic-rules 为真源、危险线 <40% 两处一致。至此打开率 / 频次 / 毛利率三类红线全部完成「真源 + 指向注释」闭环。

## v2.6.5 — 发版终审收尾

落实《AFA v2.6.4 发版终审报告》第二章 5 项润色级收尾（评审总裁决为「放行发版、零阻断」）。补丁级：in-file 版本头维持 v2.6。三道门禁修后全绿。

- **#1 时间表消歧**：`afa-gg/references/search-ads-playbook.md` DSA→AI Max 表——2027-02 行的括注补「与上行 2026-09 为不同子项」，区分「ACA/广泛匹配按原计划 2026-09 迁入」与「剩余 DSA 原定 2026-09、延期至 2027-02」两个子事件，消除两处 2026-09 的表面歧义。
- **#2 打开率口径注释**：`afa-dashboard/references/core-frameworks.md` Email 打开率红线（<20%🔴）照「频次」先例补口径注释，指明细分诊口径以 `afa/references/diagnostic-rules.md` 邮件六维表（危险 <18% / 警告 18-25%）为真源。
- **#3 毛利率失实声明修正**：`afa-product/references/benchmark-data.md` 产品毛利率红线（危险 <50%）原括注「（与全局诊断模块统一）」失实（全局分诊为 <40%）。保留本模块更严的 50% 数值（有付费流量存活性依据），把括注改为如实说明「本模块取更严口径、较全局 <40% 更严格」，并指向全局真源。
- **#4 检查清单中文化**：`afa-geo/SKILL.md` 完成前检查清单的中英混排项统一为中文（代码引用与路径保留原样）。
- **#5 时效治理提醒**：`afa/_system/benchmark-governance.md` 分层新鲜度节增「集中复核提醒」——批次 12/13 平台功能类事实（`last_verified: 2026-07`）将于 2027-01 前后集中到期，建议以 2027-01 为集中复核窗口，避免逐条遗漏。

## v2.6.4 — 措辞消歧

经 Max 确认，落实 v2.6.3 报告里留作待定的可选润色。补丁级：in-file 版本头维持 v2.6。

- **措辞消歧**：`afa-email/references/core-flows-playbook.md` 标准路径分支第二轮 `[WAIT]` 由「按**高价值路径**的第二轮复查节奏」改为「按**标准路径**第二轮复查节奏」。改前两条路径的第二轮 wait 互相指向对方（循环引用、无锚点）；改后两者统一引用「标准路径第二轮复查节奏」，定义锚定在标准路径、由高价值路径借用，消除循环并更符合运营语义（标准购物车不继承高价值路径的更快节奏）。措辞与同文件 L198 完全一致。

## v2.6.3 — 单点格式收尾

针对《AFA v2.6.2 终验报告》第三章唯一遗留项的单点修复。补丁级：in-file 版本头维持 v2.6。

- **必修（机械格式）**：`afa-email/references/core-flows-playbook.md` 废弃购物车·标准路径分支的 `[WAIT]` 节点（#2B 与 #3B 之间）原为 0 缩进（v2.4.7 出厂缺陷，非补丁引入），对齐为分支内 6 空格缩进、子行 8 空格，并删除其后多余空行。修后全文件已无「分支内 0 缩进」的树节点（主干无分支的 0 缩进 `[WAIT]` 属正常）。
- **保留（待 Max 定夺，非错误）**：该节点措辞「按高价值路径的第二轮复查节奏」按终验意见维持原文——语义可解析为标准路径借用高价值路径的节奏定义；是否改直白留作可选润色，未作为缺陷处理。

## v2.6.2 — 终验微补丁

针对《AFA v2.6.1 终验报告（终版）》第二章 4 项收尾问题的最小 diff 修复。补丁级：in-file 版本头维持 v2.6。三道门禁修后全绿；第三章「勿修清单」未改动。

- **🟡中 #1**：`afa-email/references/core-flows-playbook.md` 废弃购物车 Flow 高价值分支编辑损伤重建——去重 `[SMS] [SMS]` / `[EMAIL] [EMAIL]` 标签、补回 `│` 列缩进前缀、删孤立残片「扣码）」，按同文件其余 Flow 的「照图施工」节点格式对齐。
- **🟡低中 #2**：`afa-geo/SKILL.md` §5 边界声明补齐——「仅负责」清单加 Agentic Commerce 接入评估（ACP/UCP/Instant Checkout/Catalog 收录），「不拥有」清单加支付合规/收单/争议率裁决（转支付风控体系），消除与 Phase 1 Mode 4 路由的自相矛盾。
- **🟢低 #3**：修复打包脚本 `.git*` 通配误伤——改用精确排除 `.git/`，恢复 `.github/workflows/lint.yml` 入包，使 `evals/README.md` 对 CI 配置的引用在分发包内不再悬空。
- **🟢注释级 #4**：`afa-dashboard/references/core-frameworks.md` 频次红线（>3.0🟡/>5.0🔴）补统计窗口标注，指向 `afa-dashboard/references/benchmark-database.md`「频次 (7 天) >4.0🔴」为口径真源，避免跨窗口误比。

## v2.6.1 — 全量验收收尾补丁

针对《AFA v2.6 全量验收报告（终版）》第四章 9 项收尾问题的最小 diff 修复。属补丁级：in-file 版本头维持 v2.6（不逐文件重编号），版本沿革仅在此登记。三道门禁（repo_lint / build_inject --check / evals）修后全绿。

- **必修 2 项**：① `afa/SKILL.md` 架构描述与架构图两处 「24 Worker」 → 「26 Worker」（monetize 7 / scale 3 + 2 全局引擎 = 26），与 routing-checklist 计数及 L51-52 覆盖列一致；② `afa-geo/SKILL.md` Phase 1 意图路由表补 Mode 4 行（ACP/UCP、AI 内下单、Instant Checkout、Catalog 收录 → agentic-commerce-playbook）。
- **轻改 6 项**：③ Hub 意图信号表 monetize 行补「WhatsApp、消息营销」、scale 行补「支付冻结、争议率、chargeback」；④ `afa-geo/references/work-modes-and-templates.md` 按 Mode 1-3 同构补 Mode 4（KPI §1.4 + 模式 4 + 输出模板 §3.3）；⑤ `afa-aov/references/benchmark-data.md` 表头「2026 平均 AOV」→「平均 AOV（前瞻估算）」；⑥ `afa-email/references/core-flows-playbook.md` 删两处编辑残留孤立 「0」；⑦ `afa/references/case-library.md` 章节编号重复「## 七」→「## 九」（并同步 self-ref 与 CHANGELOG 叙述）；⑧ 打包排除 `.git/`（及 `afa-ops/scripts/vamp_check.py` 孤儿副本）。
- **建议 1 项**：⑨ `afa-convert/scripts/ab_sample_size.py` 加小数误用防呆——`--baseline < 0.5` 时输出警告（stderr + JSON `warning` 字段），提示按百分数传参。

## v2.6 — 能力扩容 + 系统工程化（in-file 版本头统一为 v2.6）

在 v2.5 时效与工程底座之上，做能力扩容（agentic commerce + 支付风控 + 富媒体消息）与系统工程化（协议内核化、路由重构、评测）。模块数 30→32，路由与交接纪律首次可机判回归。所有平台事实带来源脚注（铁律 1）。

- **批次12（afa-geo 旗舰化）**：新写 `agentic-commerce-playbook`（ACP/UCP 双协议决策树 + Instant Checkout + Shopify Catalog + `llms.txt` + Alexa for Shopping/Gemini 购物 + LLM Visibility Score）；geo 增设「Mode 4: Agentic Commerce 接入」。
- **批次13（afa-payments 新 Worker，挂 afa-scale）**：VAMP 争议率自查 + chargeback 反驳证据包 + Stripe/PayPal 冻结与 Rolling Reserve 应对 + 支付组合/BNPL + 欺诈过滤；`vamp_check.py` 迁入本模块。
- **批次14（afa-messaging 新 Worker，挂 afa-monetize）**：WhatsApp Business（模板审核 + 24h 会话窗口 + Meta 商业政策）+ RCS；与 email/sms 三渠道瀑布抑制强制对齐；含市场适用性前置（LatAm/东南亚/欧洲强、纯美弱）。
- **批次15（D1 协议内核化）**：新写 `afa/_system/kernel.md` 内核源 + `scripts/build_inject.py` 幂等注入器，把「十一条铁律 + completion 四态 + 五个不丢字段 + display_name + 三级降级 + 四段式」注入 32 个 SKILL.md，单模块安装即自含可用协议；CI 加内核同步校验。
- **批次16（description 三层重构·方案A）**：Worker 收窄到区分性触发词 + 追加「复杂问题先经 afa」路由提示；Supervisor 去除与下属重复的症状词；Hub 增综合触发词（90 天计划/不知道从哪开始/多个问题）。description 合计 6,859→3,667 字符，消除 size 警告，修正三重触发倒挂。
- **批次17（evals 首版）**：新增 `evals/`——路由回归 harness（纯标准库）+ 7 条业务线 41 条可机判用例，四类断言（路由可达 / 五字段在位 / 无代号泄漏 / 带成本标签）；接入 CI 门禁。
- **case-library 换血**：§九 新增 3 例联网核实案例（Marais USA / Wonderskin / Mejuri），全部「据 XX 报道」出处标注。

## v2.5 — 时效补丁 + 计算脚本 + CI + 基准治理（in-file 版本头曾统一为 v2.5）

在 v2.4.8 结构修复之上，落地 2024-2026 平台/法规时效补丁、首批计算脚本、CI 门禁与基准治理。所有平台事实带来源脚注（铁律 1），【复核】项均联网核实。

- **批次5（付费线）**：Meta Andromeda「AI 监督者」范式；TikTok GMV Max 2026-07 默认化 + Smart+；Google AI Max for Search/Shopping + DSA→AI Max 迁移（延至 2027-02）；paid 层 MMM/增量测试 + 服务器端追踪 + CTV/AppLovin 条件性小节。
- **批次6（变现线）**：email Gmail/Yahoo/Microsoft 批量发件人门槛 + Apple Intelligence 摘要；sms 10DLC 前置 + TCPA 2025 时间线（revoke-all 延至 2027-01-31）+ RCS。
- **批次7（三张事实卡）**：retain 订阅合规（Click-to-Cancel 被废 + ANPRM 重启）；convert ADA 无障碍法务风险；ops Visa VAMP 预告（暂置，待支付风控模块迁移）。
- **批次8（关税新常态）**：新写 tariff-new-normal-playbook（de minimis 2025-08-29 终止 + EU 2026-2028 分阶段）；ops 风险矩阵升级；scale 第七维「关税与合规韧性」；localization 美国行。
- **批次9（首批脚本）**：unit_economics / ab_sample_size / promo_breakeven / vamp_check（纯标准库，脚本优先 + 文字回退）。
- **批次10（CI）**：repo_lint 入库 scripts/ + learnings 白名单（死链归零）+ error/warn 分级；GitHub Actions 门禁。
- **批次11（基准治理）**：新写 _system/benchmark-governance（三字段 + 分层新鲜度 + 订阅源清单）；17 个 benchmark 文件补三字段治理头。

## v2.4.8 — A1 硬伤修复版（本次升级，4 批次）

修复《AFA DTC v2.4.7 最终版问题与执行清单》A1 章十六条文件级硬伤，纯编辑，无内容时效改动（时效补丁属 v2.5）。

- **批次1**：#1 PMF 评分体系三处统一为四维 25/25/30/20（launch）；#2 `tariff-arbitrage-strategies` 名实不符→改名 `trend-timing-arbitrage` 并更正引用（expand/geo）；#3 gg KPI 硬编码阈值→区间化；#4 tt affiliate 死链修复。
- **批次2**：#5 基准分层规则（硬阈值仅限路由分诊、深诊走用户自基准）三份文件互注；#11 aov 「2026 基准数据」→「基于 2024-2025 前瞻估算」；#12 seo 错列 geo 职责→改为转交 afa-expand；#16 routing 「24 模块」计数注（Worker 层，30=1+5+24）。
- **批次3**：#6 `_system/` 悬空路径根治——29 个非 Hub SKILL.md → `../afa/_system/`，`_system/` 内部文件 → 同目录裸名（Hub 不动）；#7 24 处真死链补严格相对路径；#8 运行时交付物统一 `./deliverables/` 前缀。死链 288→2（余 2 为 learnings.md 合法运行时迁移引用）。
- **批次4**：#9 历史版本串清零（正文 83 处 → 0，迁入本 CHANGELOG）+ 模块头部版本统一 v2.4.8；#13 retain 流失风险权重统一；#14 dashboard 首单利润率补关税项、与 ops 六层成本对齐；#15 pr 内部代号映射表移出 reference 正文。

## v2.4.7 — 上传基线

Max 提供的审计与升级基线包（311 文件 / 30 模块）。

## v2.4.6

GitHub 发布版（README 曾停留于此版本，v2.4.8 起同步）。

## v2.4.1

路由前检查清单、多模块协同规则、用户确认节点（最高优先级）重写。

## v2.3.4

Confidence（数据基础）评分标准收口封版；付费线 anti-patterns「用户拒绝提供信息 / 执行类任务最低门槛」收口封版。

## v2.3.0

零数据降级规则修订。

## v2.2.8

`urgency_level`（紧急程度枚举）字段补全，由诊断引擎或 Hub 根据情境判定。

## v2.1 / v2.1.0

启动检查序列新增 `learnings.jsonl` 结构化记忆加载步骤；「老朋友回来」流程新增记忆加载与向后兼容逻辑。

## v2.0.9

冲突检测与处理规则新增；路由检查表第二章「传递上下文」由描述性文本升级为声明式 Context Matrix（Requires/Optional/Never）。

## v2.0.8

completion 回传 `status` 升级为四状态码枚举（DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT），新增 `handoff_summary` 字段；可操作错误模板新增。

## v1.9.8

`premium_tier`（四维溢价阶梯当前主攻层级）字段新增。

## v1.9.7

四维溢价阶梯（4-Tier Premium Staircase）核心升级。

## v1.9.5

供应链模式检测（`supply_chain_mode` = dropshipping/wholesale/manufacturing/dtc）与各模块适配；物流与供应链强化；淡季创意策略新增。

## v1.9.3

季节性模式（`seasonal_mode`）与季节性排除规则新增。

## v1.9.2

用户拒绝提供信息时的处理、执行类任务最低门槛（-p8 重写）。

## v1.9

危机模式（`crisis_mode` / `health_status`）；铁律 11「不充当法律/合规/财务顾问」；前置条件检查、Level 0 边界。

## v1.8

成本标签体系；降级规则重构与用户提示；常见市场快速参考表与多市场策略差异化；路由前检查清单升级、角色边界规则；诊断行为准则与异常诊断行为准则。

## v1.7

Brand Brain 子目录扩展协议；状态灯量化标准；`learnings.jsonl` 写入规范；AOV 诊断前置数据采集补充。
