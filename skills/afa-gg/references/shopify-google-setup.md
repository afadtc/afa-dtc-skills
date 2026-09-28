# Shopify × Google 基础设施搭建完整手册

> **层级声明**：本文件默认作为 **internal-only** 的内部搭建与审查参考使用，不得将 SOP、审核窗口、受众天数、政策要求或追踪配置整段直接粘贴给用户。
> 本手册覆盖从零开始搭建 Shopify 独立站与 Google 广告生态系统的全部基础设施，包括 Google Merchant Center 创建与配置、追踪代码部署、增强型转化、微转化事件、再营销受众、GA4 配置、产品评论集成、产品 Feed 优化。每一步都提供可执行的 SOP，确保用户在投放第一个广告之前拥有完整、准确的技术基础。
> **渲染规则**：本文件中的邮箱一致性、政策页要求、页面速度、评论数量、审核次数、观察期、窗口期、受众天数、评分门槛与等待时间，只能作为排查起点或说明性样例；不得写成跨品牌统一红线或确定性审核承诺。

---

## 一、Google Merchant Center（GMC）完整设置

### 1.1 创建 GMC 账户

**步骤 SOP：**

1. 访问 [merchants.google.com](https://merchants.google.com)，使用与 Google Ads 相同的 Gmail 登录
2. 选择 **Merchant Center Next**（2025+ 新版本，推荐）
3. 填写商家信息：
   - **商家名称**：与品牌名一致
   - **网站 URL**：填写 Shopify 店铺的自定义域名（非 myshopify.com）
   - **国家**：选择主要目标市场国家
   - **时区**：与 Google Ads 账户保持一致
4. 验证网站所有权：
   - **推荐方式**：通过 Shopify 的 Google & YouTube 渠道自动验证
   - **备选方式**：HTML 标签验证（在 Shopify → Online Store → Themes → Edit Code → theme.liquid 的 `<head>` 中添加）
5. 完成基础设置后，进入产品提交流程

**关键注意事项：**
- GMC 账户的邮箱应尽量与 Google Ads 账户保持同一管理主体，或至少在同一个 Google 账户管理下
- 如果使用 Merchant Center Next（新版），Dynamic Remarketing 和 Free Listing 程序通常已启用，但仍应实际核查
- 如果使用 Merchant Center Classic（旧版），通常需要手动在 Growth → Manage Programs 中启用

### 1.2 非目标国家卖家定位其他市场（Country Switch SOP）

> 适用场景：卖家实际位于中国/东南亚/东欧等地区，但需要定位美国/英国/欧盟等市场

**步骤 SOP：**

1. **GMC 创建时**：国家设置应与实际运营市场、物流能力和合规主体一致，避免只为通过审核而机械伪装所在地
2. **Shopify 店铺设置**：
   - Settings → General → Store Address：填写目标市场的地址（可使用仓库/代发地址）
   - Settings → Payments → Billing Address：与 Store Address 一致
3. **产品 Feed 设置**：
   - 目标国家（Target Country）：设为目标市场
   - 货币：设为目标市场货币（如 USD）
   - 语言：设为目标市场语言（如 English）
4. **运费设置**：
   - 在 GMC 中设置符合目标市场的运费规则
   - 确保与 Shopify 的 Shipping Settings 一致
5. **退货政策**：
   - 应有清晰的退货政策页面
   - 退货地址应与真实履约安排一致，可使用合规的第三方退货服务

**常见问题：**
- 如果 Google 检测到 IP 地址与声称的国家不一致，通常不会直接拒绝，但可能触发额外审核
- 使用 VPN 登录 GMC 不是必需条件；如使用，也应确保与真实业务主体和合规做法一致，避免制造额外风控信号
- 确保所有页面（包括 About Us、Contact）的信息与目标市场一致

### 1.3 Misrepresentation 封号与解封 SOP

> Misrepresentation（虚假陈述）是 GMC 最常见的封号原因，尤其对 Dropshipping 店铺

**预防措施（上线前必做）：**

| 检查项 | 要求 | 常见错误 |
|:---|:---|:---|
| **退货政策页面** | 应存在且可访问，并清晰说明退货时限、条件、流程 | 使用模板未修改、退货地址缺失 |
| **运费政策页面** | 应存在，并明确运费标准和预计送达时间 | 未说明国际运费、送达时间过于模糊 |
| **隐私政策页面** | 应存在，并符合目标市场适用法规 | 使用其他品牌名的模板 |
| **服务条款页面** | 应存在 | 缺失或内容空白 |
| **联系方式** | 应有真实的联系方式（邮箱/电话/表单） | 仅有 email，无电话或联系表单 |
| **About Us 页面** | 应有品牌故事和主体信息 | 空白或一句话带过 |
| **产品页面** | 图片应真实、描述应准确 | 使用供应商原图未修改、描述与实物不符 |
| **价格一致性** | GMC Feed 中的价格应与网站实际价格保持一致 | 促销价未同步更新 |
| **库存一致性** | GMC Feed 中的库存状态应与网站一致 | 显示有货但实际缺货 |
| **结账流程** | 应可以正常完成购买 | 测试订单未验证、支付网关未配置 |
| **SSL 证书** | 网站应使用 HTTPS | Shopify 默认提供，但自定义域名需确认 |
| **网站速度** | 页面速度不应明显拖累审核与购买体验 | 图片未压缩、过多 App 拖慢速度 |

**解封 SOP（已被封号后）：**

1. **诊断封号原因**：
   - 登录 GMC → 查看通知/警告信息
   - 常见原因：Misrepresentation of self or product、Untrustworthy promotions、Circumventing systems
2. **逐项修复**：
   - 按上表逐项检查并修复所有问题
   - 特别关注：退货政策、联系方式、产品描述准确性
3. **提升网站可信度**：
   - 添加真实的客户评论（数量以能支撑信任建立为准，不套用固定门槛）
   - 添加品牌 Logo 和专业的 About Us 页面
   - 确保所有链接可正常访问（无 404 页面）
   - 添加 FAQ 页面
4. **提交申诉**：
   - 在 GMC 中点击 "Request Review"
   - 详细说明你已修复的问题
   - 等待平台审核完成，并预留不确定审核时间
5. **申诉失败后的备选方案**：
   - 如果第一次申诉失败，继续优化后再次申诉（具体机会数以平台当期规则为准）
   - 如果多次失败，评估是否需要进入更长冷却期后重新申诉
   - 最终方案：使用新的域名和 GMC 账户重新开始

**Pro Tips：**
- 在提交产品到 GMC 之前，先用 Google 的 [Merchant Center 诊断工具](https://merchants.google.com) 检查所有问题
- 新账户初期通常更敏感，应避免频繁大改产品信息与政策页
- 使用 Google 的 [Rich Results Test](https://search.google.com/test/rich-results) 验证结构化数据

---

## 二、追踪代码完整部署

### 2.1 追踪架构概览

```
Shopify 店铺
    ├── Google Ads Conversion Tracking（核心）
    │   ├── Purchase（主要转化 — Primary）
    │   ├── Add to Cart（微转化 — Secondary）
    │   └── Begin Checkout（微转化 — Secondary）
    ├── Enhanced Conversions（增强型转化）
    │   └── 发送 email、phone、name 等用户数据到 Google
    ├── Google Analytics 4（分析）
    │   └── 通过 Shopify Google & YouTube 渠道连接
    └── Remarketing Tag（再营销）
        └── 通过 GMC Dynamic Remarketing 实现
```

### 2.2 通过 Shopify App 部署追踪代码（推荐方式）

> 推荐使用 **S Process Feed** 或 **Analyzify** 等专业追踪 App，而非手动安装代码

**S Process Feed 部署 SOP：**

1. **安装 App**：
   - Shopify App Store → 搜索 "S Process Feed" 或 "Analyzify"
   - 安装并授权
2. **连接 Google Ads 账户**：
   - 在 App 中选择你的 Google Ads 账户
   - 如果有多个账户，确保选择正确的 Customer ID
3. **嵌入追踪代码**：
   - 点击 "Active App Embed" → 进入 Theme Settings
   - 确认 "S Process Tracking Tag" 已启用
   - 保存设置
4. **配置转化事件**：
   - 返回 App → 点击 "Update Conversion Tags"
   - App 会自动创建以下转化事件：
     - **Purchase**（购买）— 设为 Primary
     - **Add to Cart**（加购）— 设为 Secondary
     - **Begin Checkout**（开始结账）— 设为 Secondary
5. **验证部署**：
   - 点击 "Recheck Extension" 验证代码嵌入状态
   - 所有追踪代码应显示为 "Active" 或 "Enabled"

### 2.3 转化事件配置（Google Ads 端）

**关键配置 SOP：**

1. **进入转化设置**：
   - Google Ads → Goals → Conversions → Summary
2. **确保 Primary/Secondary 正确设置**：
   - **Purchase**：通常应作为 **Primary**（用于广告优化），除非账户有清晰的主转化例外设计
   - **Add to Cart**：通常设为 **Secondary**（仅观察，不用于优化）
   - **Begin Checkout**：通常设为 **Secondary**（仅观察，不用于优化）

> **关键警告**：如果有多个 Purchase 追踪代码都设为 Primary，会导致转化数据重复计算（Double Counting），严重扭曲 ROAS 数据。应尽量确保只有一个 Purchase 标签承担主优化角色，除非有经过验证的特殊结构设计。

3. **配置每个转化事件的参数**：

| 参数 | Purchase | Add to Cart | Begin Checkout |
|:---|:---|:---|:---|
| **Category** | Purchase | Add to Cart | Begin Checkout |
| **Goal Optimization** | 通常设为 Primary | 通常设为 Secondary | 通常设为 Secondary |
| **Value** | Use different values for each conversion | Don't use a value | Don't use a value |
| **Count** | Every（每次购买都计） | One（每用户只计一次） | One（每用户只计一次） |
| **Click-through Window** | 按购买周期与归因策略校准 | 按漏斗诊断需求校准 | 按漏斗诊断需求校准 |
| **View-through Window** | 按渠道角色与归因策略校准 | 按渠道角色与归因策略校准 | 按渠道角色与归因策略校准 |
| **Attribution Model** | 通常优先 Data-driven | 通常优先 Data-driven | 通常优先 Data-driven |

4. **命名规范**：
   - 删除 App 自动生成的冗余命名后缀
   - 保持简洁：`Purchase`、`Add to Cart`、`Begin Checkout`

### 2.4 增强型转化（Enhanced Conversions）部署

> Enhanced Conversions 通过发送哈希化的用户数据（email、phone、name）到 Google，显著提升转化追踪准确性，尤其在 iOS 14.5+ 隐私限制下至关重要。

**部署 SOP：**

1. **Google Ads 端启用**：
   - Goals → Conversions → Summary → 点击 Purchase 标签
   - 找到 "Enhanced Conversions" 选项
   - 点击 "Turn on Enhanced Conversions"
   - 选择 **API** 方式（不是 Google Tag 方式）
   - 点击 Next → Save
   
   > **注意**：在不同版本的 Google Ads UI 中，Enhanced Conversions 的位置可能不同。新版在标签详情页内，旧版在 Settings 标签页中。

2. **Shopify App 端启用**：
   - 返回追踪 App（S Process Feed / Analyzify）
   - 找到 Enhanced Conversions 选项并启用
   - 确认发送的数据字段：Email、Phone、Order ID、Name
   - 保存设置

3. **验证**：
   - Enhanced Conversions 状态可能显示 "Pending"
   - 需要通过 Google Ads 获得实际销售后才能验证
   - 完全验证所需时间受转化量与数据稳定性影响，不写固定天数
   - 在 Conversions → Diagnosis 标签页中查看状态

**发送的数据字段：**

| 字段 | 说明 | 隐私处理 |
|:---|:---|:---|
| Email | 购买者邮箱 | SHA-256 哈希后发送 |
| Phone | 购买者电话 | SHA-256 哈希后发送 |
| First Name | 购买者名 | SHA-256 哈希后发送 |
| Last Name | 购买者姓 | SHA-256 哈希后发送 |
| Order ID | 订单编号 | 明文发送（用于去重） |

### 2.5 微转化的战略价值

> 微转化（Add to Cart、Begin Checkout）不仅是观察指标，更是诊断漏斗问题的关键数据。

**诊断应用场景：**

| 数据模式 | 诊断结论 | 行动方向 |
|:---|:---|:---|
| 高 Add to Cart + 低 Begin Checkout | 购物车页面有问题（运费惊吓、缺少信任信号） | 优化购物车页面、添加运费预告 |
| 高 Begin Checkout + 低 Purchase | 结账流程有问题（支付方式不足、页面加载慢） | 增加支付方式、优化结账速度 |
| 低 Add to Cart | 产品页面有问题（价格、描述、图片、社证不足） | 优化 PDP、增加评论、调整价格 |
| 所有微转化都低 | 流量质量问题（关键词不精准、受众不匹配） | 优化关键词/受众定向 |

---

## 三、Google Analytics 4（GA4）完整配置

### 3.1 创建 GA4 Property

**步骤 SOP：**

1. 访问 [analytics.google.com](https://analytics.google.com)
2. 点击 "Start Measuring" → 创建账户
3. **账户设置**：
   - 账户名称：品牌名
   - 取消勾选不需要的邮件通知
4. **Property 设置**：
   - Property 名称：品牌名 + " Website"
   - 时区：目标市场时区
   - 货币：目标市场货币
5. **业务信息**：
   - 行业：选择最接近的类别
   - 规模：据实选择
   - 目标：选择 "Drive online sales"、"Raise brand awareness"、"Examine user behavior"
6. **创建 Data Stream**：
   - 选择 "Web"
   - 输入网站 URL（自定义域名，非 myshopify.com）
   - 命名 Data Stream
   - 确认 Enhanced Measurement 已启用

### 3.2 关键配置项

**3.2.1 排除自引荐（Self-Referral Exclusion）**

> 自引荐会导致数据膨胀和来源归因错误，必须在开始收集数据前配置。

**SOP：**
1. Admin → Data Streams → 点击你的 Stream
2. Configure Tag Settings → Show All → List Unwanted Referrals
3. 添加以下域名（Match Type: Contains）：
   - `myshopify.com`
   - 你的自定义域名（如 `yourbrand.com`）
   - 支付网关域名（如 `paypal.com`、`klarna.com`、`affirm.com`）
4. 保存

**3.2.2 启用 Google Signals**

**SOP：**
1. Admin → Data Settings → Data Collection
2. 点击 "Get Started" → Activate Google Signals
3. 确认并完成

**3.2.3 数据保留期设置**

**SOP：**
1. Admin → Data Settings → Data Retention
2. 将 Event Data Retention 从 2 个月改为 **14 个月**（如果当地法律允许）
3. 保存

**3.2.4 连接 Shopify**

**SOP：**
1. 回到 Shopify → Online Store → Preferences
2. 找到 Google Analytics 部分
3. 选择刚创建的 GA4 Property → Connect
4. 验证连接成功：Shopify 会自动发送 `page_view`、`purchase`、`add_to_cart`、`begin_checkout` 等事件

### 3.3 连接 GA4 与 Google Ads

**SOP：**
1. GA4 → Admin → Google Ads Links
2. 点击 "Link" → 选择你的 Google Ads 账户
3. 启用以下选项：
   - **Enable Personalized Advertising**：启用（允许 GA4 受众用于 Google Ads 定向）
   - **Enable Auto-tagging**：启用（自动为 Google Ads 流量添加 gclid 参数）
4. 确认并保存

**连接后的价值：**
- GA4 中创建的受众可以直接用于 Google Ads 再营销
- Google Ads 中可以查看 GA4 的转化数据
- 支持跨平台归因分析

### 3.4 连接 GA4 与 Merchant Center

**SOP：**
1. GMC → Settings → Conversion Settings
2. 启用 Auto-tagging
3. 添加 Conversion Source → 选择 Google Analytics
4. 选择你的 GA4 Property → 保存
5. 这样可以追踪 Free Listing 带来的流量和转化

---

## 四、再营销受众创建

### 4.1 在 Google Ads 中创建再营销受众

> 再营销受众允许你向曾经访问过网站但未购买的用户展示广告，是 DTC 品牌最高 ROI 的广告策略之一。

**前提条件：**
- GMC 已与 Google Ads 连接
- Dynamic Remarketing 程序已启用
- 追踪代码已正确部署

**创建 SOP：**

1. **Google Ads → Tools & Settings → Audience Manager**
2. 点击 "+" 创建新受众
3. **推荐创建的受众列表：**

| 受众名称 | 规则 | 有效期 | 用途 |
|:---|:---|:---|:---|
| All Visitors - Short Window | 访问过网站的所有用户 | 按站点回访周期设置短窗 | 通用再营销 |
| All Visitors - Mid Window | 访问过网站的所有用户 | 按站点回访周期设置中窗 | 扩大再营销池 |
| All Visitors - Long Window | 访问过网站的所有用户 | 按站点回访周期设置长窗 | 长周期再营销 |
| Product Viewers | 查看过产品页面但未购买 | 按意向衰减速度设置 | 高意向再营销 |
| Cart Abandoners | 加购但未购买 | 按购买决策时效设置较短窗口 | 高意向再营销 |
| Checkout Abandoners | 开始结账但未完成 | 按结账挽回时效设置最短窗口 | 紧急挽回 |
| Past Purchasers - Short Window | 已购买用户 | 按复购节奏设置短窗 | 排除或交叉销售 |
| Past Purchasers - Long Window | 已购买用户 | 按复购节奏设置长窗 | 复购营销 |
| High-Value Customers | 购买金额显著高于品牌平均值 | 按 LTV 周期设置 | VIP 营销 |

4. **设置受众规则**：
   - 选择 "Website visitors" 作为来源
   - 配置具体的页面 URL 或事件条件
   - 设置有效期（Membership Duration）

### 4.2 在 GA4 中创建受众（高级）

> GA4 受众更灵活，支持基于事件序列和用户属性的复杂条件。

**SOP：**
1. GA4 → Admin → Audiences → New Audience
2. 可以使用预设模板或自定义创建
3. **推荐的 GA4 高级受众：**

| 受众名称 | 条件 | 用途 |
|:---|:---|:---|
| Engaged Non-Buyers | 站内参与度显著高于普通访客且未购买 | 高参与度但未购买 |
| Multi-Visit Non-Buyers | 多次访问但未购买 | 多次访问但未购买 |
| Category Browsers | 浏览过特定品类页面 | 特定品类兴趣用户 |
| High-Scroll Users | 深度浏览但未购买 | 深度浏览但未购买 |

4. 创建后，这些受众会自动同步到已连接的 Google Ads 账户

### 4.3 Dynamic Remarketing 设置

**SOP：**
1. **GMC Classic 版本**：
   - Growth → Manage Programs → 启用 Dynamic Remarketing
   - 启用 Free Listing Program
2. **GMC Next 版本**：
   - Dynamic Remarketing 和 Free Listing 通常已启用，但仍应实际确认
   - 在 Organic 标签页确认 Free Listing 状态
3. **连接 GMC 与 Google Ads**：
   - GMC → Settings → Apps → Add Google Ads
   - 输入 Google Ads Customer ID（右上角的 10 位数字）
   - 发送连接请求
   - 在 Google Ads 中批准连接请求：
     - Google Ads → Tools & Settings → Linked Accounts → Google Merchant Center → 批准

---

## 五、产品评论集成（Google Shopping 星级评分）

> 产品评论星级通常是 Google Shopping 广告中非常强的 CTR 影响因素之一。有星级评分的产品广告往往比无评分的更容易获得点击，但提升幅度应以真实数据验证。

### 5.1 评论 App 选择

| 特性 | Judge.me | Loox |
|:---|:---|:---|
| **价格** | 免费版可用 / $15/月 Pro | $9.99/月起 / Growth $34.99/月 |
| **Google Shopping 集成** | 免费版即支持 | 需要 Growth 计划 |
| **照片评论** | 支持 | 支持（核心功能） |
| **视频评论** | Pro 版支持 | Growth 版支持 |
| **AliExpress 导入** | 支持 | 支持 |
| **自动请求评论** | 支持 | 支持 |
| **推荐** | **性价比首选** | 视觉效果优先选择 |

### 5.2 Judge.me 集成 SOP

1. **安装 Judge.me**：Shopify App Store → 搜索 "Judge.me" → 安装
2. **配置 Google Shopping 集成**：
   - Judge.me Dashboard → Integrations → Google Shopping
   - 启用 "Push reviews to Google Shopping"
3. **配置 Product Identifier**：
   - **MPN（Manufacturer Part Number）**：设为 "Include from SKU"
   - **GTIN**：如果有则启用，没有则禁用
   
   > **关键**：MPN 设置必须与 GMC Feed 中的 MPN 字段一致。如果 Feed 使用 SKU 作为 MPN，则 Judge.me 也必须设为 "Include from SKU"。

4. **其他设置**：
   - 启用 "Upload reviews with photos"
   - 启用 "Product Groups"（将同一产品的不同变体评论合并显示）
   - 设置 Reviewer Name 格式（推荐：First Name + Last Initial）
   - 排除缺货产品的评论：保持禁用（正面评论应保留）
5. **获取 XML Feed URL**：
   - 在集成页面底部找到 Product Reviews Feed URL
   - 复制此 URL，后续提交到 GMC

### 5.3 Loox 集成 SOP

1. **安装 Loox**：Shopify App Store → 搜索 "Loox" → 安装
2. **升级到 Growth 计划**（Google Shopping 集成需要）
3. **配置 Google Shopping 集成**：
   - Settings → General → Integration → Google Shopping
   - **GTIN**：如有则从 Barcode 包含，否则禁用
   - **MPN**：设为 "Include from SKU"
   - **Prefix**：根据目标国家选择（美国选 SP，其他国家选对应代码）
4. **获取集成链接**：
   - Loox 的自动同步功能可能不稳定
   - **推荐**：联系 Loox 客服，请求 "Manual integration link for Google Shopping"
   - 客服会提供一个专属的 XML Feed URL
5. **提交到 GMC**：使用获取的 URL 提交

### 5.4 将评论 Feed 提交到 GMC

**SOP：**

1. **GMC Classic 版本**：
   - Growth → Manage Programs → Product Ratings
   - 如果未启用，点击 "Get Started"
   - 选择 "Use a third-party reviews aggregator"
   - 输入评论 Feed URL（从 Judge.me 或 Loox 获取）
   - 提交并等待审核，预留不确定审核时间
2. **GMC Next 版本**：
   - 在 Product Ratings 部分添加 Feed URL
   - 或通过 Google 的 [Product Ratings Interest Form](https://support.google.com/merchants/contact/product_ratings_interest) 申请

**审核要求：**
- 评论数量应达到足以支撑审核与展示的水平，具体门槛以平台当期规则为准
- 评论应是真实的客户评论
- 审核周期存在波动，不写固定周数
- 审核通过后，星级评分通常会自动显示在 Shopping 广告中

**常见问题与解决：**

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| 评论未匹配到产品 | MPN/GTIN 不一致 | 检查 Feed 中的 MPN 与评论 App 中的设置是否一致 |
| 评论被拒绝 | 评论内容不符合政策 | 检查是否有虚假评论或违规内容 |
| 星级未显示 | 评论数不足或审核未通过 | 先确认评论规模是否足够，再等待审核结果 |
| Loox 自动同步失败 | 已知 Bug | 联系 Loox 客服获取手动集成链接 |

---

## 六、产品 Feed 优化

### 6.1 Feed 提交方式

**推荐方式：通过 Shopify Google & YouTube 渠道**

1. Shopify → Sales Channels → Google & YouTube
2. 连接 GMC 账户
3. 选择目标市场和语言
4. App 会自动将 Shopify 产品同步到 GMC
5. 产品更新会自动同步（通常 24 小时内）

**备选方式：通过第三方 Feed App**
- **推荐 App**：S Process Feed、DataFeedWatch、Feedonomics
- 优势：更灵活的 Feed 定制、规则化标题优化、多渠道支持

### 6.2 标题优化（最重要的 Feed 字段）

> 产品标题是 Google Shopping 广告中决定关键词匹配的最关键字段。与搜索广告不同，Shopping 广告无法直接设置关键词——Google 通过标题和描述来判断匹配哪些搜索查询。

**标题公式（按品类）：**

| 品类 | 公式 | 示例 |
|:---|:---|:---|
| **服装** | 品牌 + 性别 + 产品类型 + 属性（颜色/材质/尺码） | "Nike Men's Running Shoes Breathable Mesh Black Size 10" |
| **电子产品** | 品牌 + 产品类型 + 型号 + 关键规格 | "Samsung Galaxy S24 Ultra 256GB Titanium Black Unlocked" |
| **家居** | 品牌 + 材质 + 产品类型 + 尺寸 + 风格 | "West Elm Solid Oak Coffee Table 48 inch Mid-Century Modern" |
| **美妆** | 品牌 + 产品线 + 产品类型 + 容量/色号 | "Charlotte Tilbury Pillow Talk Matte Lipstick 3.5g Shade 01" |
| **食品/保健** | 品牌 + 产品类型 + 口味/成分 + 规格 + 认证 | "Optimum Nutrition Whey Protein Powder Chocolate 5lb USDA Organic" |
| **通用** | 品牌 + 核心关键词 + 产品类型 + 关键属性 + 差异化特征 | "BrandX Ergonomic Office Chair Lumbar Support Adjustable Armrest Black" |

**标题优化规则：**
1. **最大长度**：150 字符，但前 70 字符最重要（移动端截断点）
2. **关键词前置**：最重要的关键词放在标题最前面
3. **避免**：全大写、促销语言（"Best Price"、"Free Shipping"）、特殊字符
4. **包含**：品牌名、核心产品词、最重要的属性（颜色/尺寸/材质）
5. **使用 Google Keyword Planner** 研究搜索量最高的产品关键词，融入标题

### 6.3 描述优化

**规则：**
- 最大长度：5,000 字符，但前 150 字符最重要
- 包含标题中的关键词 + 补充的长尾关键词
- 描述产品的核心卖点、使用场景、材质/规格
- 避免 HTML 标签、促销语言、与其他产品的比较

### 6.4 图片优化

**要求：**

| 参数 | 要求 |
|:---|:---|
| **最小尺寸** | 100×100 px（服装类 250×250 px） |
| **推荐尺寸** | 800×800 px 以上 |
| **格式** | JPEG、PNG、GIF、BMP、TIFF |
| **背景** | 纯白或浅色背景（主图） |
| **内容** | 仅展示产品本身，无水印、无文字覆盖、无边框 |
| **additional_image_link** | 可添加生活场景图、细节图、使用图 |

### 6.5 自定义标签（Custom Labels）策略

> Custom Labels 允许你在 Google Ads 中按自定义维度细分产品，实现更精细的出价和预算控制。

**推荐的 Custom Label 方案：**

| Label | 维度 | 值示例 | 用途 |
|:---|:---|:---|:---|
| `custom_label_0` | 利润率 | high_margin, medium_margin, low_margin | 按利润率差异化出价 |
| `custom_label_1` | 产品表现 | bestseller, new_arrival, clearance | 按表现分配预算 |
| `custom_label_2` | 价格区间 | under_25, 25_50, 50_100, over_100 | 按价格段优化 |
| `custom_label_3` | 季节性 | spring, summer, fall, winter, evergreen | 季节性预算调整 |
| `custom_label_4` | 促销状态 | on_sale, full_price, bundle | 促销期间特殊出价 |

### 6.6 Feed 健康检查清单

| 检查项 | 状态 | 影响 |
|:---|:---|:---|
| 所有产品都有唯一的 GTIN 或 MPN | ☐ | 产品匹配准确性 |
| 标题包含核心关键词且 < 150 字符 | ☐ | 搜索匹配质量 |
| 描述 > 500 字符且包含关键词 | ☐ | 搜索匹配广度 |
| 主图为白底产品图且 > 800px | ☐ | 广告展示质量 |
| 价格与网站实时一致 | ☐ | 避免 Misrepresentation |
| 库存状态与网站实时一致 | ☐ | 避免用户体验问题 |
| 运费信息准确 | ☐ | 避免结账放弃 |
| 产品类目（google_product_category）正确 | ☐ | 广告展示准确性 |
| Custom Labels 已配置 | ☐ | 广告优化灵活性 |
| 无 GMC 警告或错误 | ☐ | 产品审核通过率 |

---

## 七、关键词研究工具与方法

### 7.1 Google Keyword Planner（免费，推荐）

**使用 SOP：**
1. Google Ads → Tools & Settings → Keyword Planner
2. 选择 "Discover new keywords"
3. 输入种子关键词（如产品核心词）
4. 查看结果：
   - **Average Monthly Searches**：搜索量
   - **Competition**：竞争程度（Low/Medium/High）
   - **Top of Page Bid**：预估首页出价

**注意事项：**
- 新账户（未花费 ~$1,050+）显示的搜索量是范围而非精确值
- 活跃账户会显示更精确的月度搜索量数据
- 按 "Average Monthly Searches" 降序排列，找到高搜索量关键词
- 滚动到底部找到长尾关键词（竞争更低）

### 7.2 关键词研究最佳实践

1. **从产品核心词开始**：输入你的主要产品类型
2. **记录高价值关键词**：搜索量 > 1,000 且竞争 ≤ Medium
3. **寻找长尾机会**：3-5 个词的组合，竞争更低
4. **融入 Feed 标题**：将研究到的关键词自然融入产品标题
5. **用于搜索广告**：高搜索量关键词用于搜索广告系列的关键词列表
6. **定期更新**：每月检查一次关键词趋势变化

---

## 八、完整搭建检查清单

> 在投放第一个 Google 广告之前，确保以下所有项目已完成。

### 8.1 网站基础（Shopify）

- [ ] 自定义域名已绑定且 SSL 已启用
- [ ] 退货政策页面已创建且内容完整
- [ ] 运费政策页面已创建且内容完整
- [ ] 隐私政策页面已创建且符合 GDPR/CCPA
- [ ] 服务条款页面已创建
- [ ] About Us 页面已创建且有品牌故事
- [ ] Contact 页面已创建且有真实联系方式（邮箱 + 电话/表单）
- [ ] FAQ 页面已创建
- [ ] 产品页面图片清晰、描述准确
- [ ] 结账流程可正常完成（已测试）
- [ ] 页面加载速度 < 3 秒

### 8.2 Google Merchant Center

- [ ] GMC 账户已创建并验证网站
- [ ] 产品 Feed 已提交且产品已获批
- [ ] 无 Misrepresentation 或其他政策警告
- [ ] Dynamic Remarketing 已启用
- [ ] Free Listing 已启用
- [ ] GMC 已与 Google Ads 连接

### 8.3 追踪代码

- [ ] Purchase 转化追踪已部署（Primary）
- [ ] Add to Cart 微转化已部署（Secondary）
- [ ] Begin Checkout 微转化已部署（Secondary）
- [ ] Enhanced Conversions 已启用（API 方式）
- [ ] 仅一个 Purchase 标签设为 Primary（无重复计数）
- [ ] Attribution Model 设为 Data-driven
- [ ] Click-through Window 设为 45 天

### 8.4 Google Analytics 4

- [ ] GA4 Property 已创建
- [ ] Data Stream 已配置
- [ ] Self-Referral 已排除（myshopify.com + 自定义域名 + 支付网关）
- [ ] Google Signals 已启用
- [ ] Data Retention 已设为 14 个月
- [ ] GA4 已与 Shopify 连接
- [ ] GA4 已与 Google Ads 连接
- [ ] GA4 已与 GMC 连接（用于 Free Listing 追踪）

### 8.5 再营销受众

- [ ] All Visitors 受众已创建（30d / 90d / 180d）
- [ ] Product Viewers 受众已创建（14d）
- [ ] Cart Abandoners 受众已创建（7d）
- [ ] Past Purchasers 受众已创建（30d / 180d）

### 8.6 产品评论

- [ ] 评论 App 已安装（Judge.me 或 Loox）
- [ ] Google Shopping 集成已配置
- [ ] MPN/GTIN 设置与 GMC Feed 一致
- [ ] 评论 Feed URL 已提交到 GMC
- [ ] 至少 50 条真实评论（等待审核通过）

### 8.7 产品 Feed 优化

- [ ] 标题已按品类公式优化
- [ ] 描述已包含关键词且 > 500 字符
- [ ] 主图为白底产品图且 > 800px
- [ ] Custom Labels 已配置（至少利润率和产品表现）
- [ ] 价格和库存与网站实时同步
- [ ] 无 GMC Feed 错误或警告

---

## 九、常见问题与故障排除

### 9.1 追踪相关

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| 转化数据为 0 | 追踪代码未正确安装 | 使用 Google Tag Assistant 验证 |
| 转化数据翻倍 | 多个 Primary Purchase 标签 | 仅保留一个 Primary，其余设为 Secondary |
| Enhanced Conversions 状态 "Not verified" | 数据量不足 | 需要更多实际转化，等待 3-21 天 |
| ROAS 数据异常高 | 转化值设置错误 | 检查是否使用了 "Use different values for each conversion" |
| 追踪代码状态 "Inactive" | 尚未有广告流量 | 开始投放广告后会自动激活 |

### 9.2 GMC 相关

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| 产品被拒绝 | 违反 Shopping 政策 | 检查 GMC Diagnostics 中的具体原因 |
| Misrepresentation 封号 | 网站信息不完整/不准确 | 按 1.3 节 SOP 逐项修复并申诉 |
| 价格不匹配 | Feed 价格与网站不同步 | 检查 Feed 更新频率，确保实时同步 |
| 运费不匹配 | GMC 运费设置与 Shopify 不一致 | 统一两端的运费规则 |
| Free Listing 产品被拒 | 与 Shopping Ads 审核标准不同 | 等待 2-4 周，Google 可能自动批准 |

### 9.3 GA4 相关

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| 数据不显示 | 刚连接，需要等待 | 等待 24-48 小时 |
| 流量来源显示 "referral" | 自引荐未排除 | 按 3.2.1 节配置排除 |
| 受众不同步到 Google Ads | 账户未连接 | 检查 GA4 → Google Ads Links |
| 转化数据与 Google Ads 不一致 | 归因模型不同 | 正常现象，两个平台使用不同的归因窗口 |

---

> **本手册说明**：基于 2026 年最新 Google Ads / GMC / GA4 / Shopify 界面
> **适用范围**：Shopify 独立站 + Google 广告生态系统
> **更新频率**：Google 平台 UI 和政策频繁更新，建议每季度检查一次本手册中的具体步骤
