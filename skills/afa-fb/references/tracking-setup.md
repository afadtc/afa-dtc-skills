# Meta 追踪与归因设置手册

> 混合冗余追踪框架：Pixel + CAPI 双保险，确保数据完整性和归因准确性。

---

## 一、追踪基础设施架构

```
追踪层级：

层级 1：Facebook Pixel（浏览器端）
├── 安装方式：Shopify 原生集成 / GTM
├── 触发事件：PageView, ViewContent, AddToCart, InitiateCheckout, Purchase
├── 局限性：被 iOS ATT / 广告拦截器 / 浏览器隐私设置阻断
└── 数据完整度：约 60-70%（2026 年）

层级 2：Conversions API（服务器端）
├── 安装方式：Shopify 原生 CAPI / 第三方工具
├── 触发事件：与 Pixel 相同的事件
├── 优势：不受浏览器限制，数据更完整
├── 数据完整度：约 85-95%
└── 关键：必须与 Pixel 去重

层级 3：离线转化（Offline Conversions）
├── 适用场景：线下销售、电话订单、B2B
├── 上传方式：手动 CSV / API 自动上传
└── 数据完整度：取决于上传频率

三层叠加 = 最大化数据捕获
```

---

## 二、Pixel 设置最佳实践

```
标准事件配置（DTC 电商）：

事件 1：PageView
├── 触发：所有页面加载
├── 参数：无特殊参数
└── 用途：基础追踪 + 再营销受众

事件 2：ViewContent
├── 触发：产品页浏览
├── 必须参数：
│   ├── content_ids: ['{product_id}']
│   ├── content_type: 'product'
│   ├── content_name: '{product_name}'
│   ├── value: {price}
│   └── currency: '{currency_code}'
└── 用途：产品级再营销 + DPA

事件 3：AddToCart
├── 触发：点击加入购物车
├── 必须参数：
│   ├── content_ids: ['{product_id}']
│   ├── content_type: 'product'
│   ├── value: {price}
│   ├── currency: '{currency_code}'
│   └── num_items: {quantity}
└── 用途：高意图再营销 + 转化优化

事件 4：InitiateCheckout
├── 触发：进入结账页面
├── 必须参数：
│   ├── content_ids: ['{product_ids}']
│   ├── value: {cart_total}
│   ├── currency: '{currency_code}'
│   └── num_items: {total_items}
└── 用途：结账放弃再营销

事件 5：Purchase
├── 触发：订单确认页（感谢页）
├── 必须参数：
│   ├── content_ids: ['{product_ids}']
│   ├── content_type: 'product'
│   ├── value: {order_total}（不含税和运费）
│   ├── currency: '{currency_code}'
│   └── num_items: {total_items}
├── 可选参数：
│   ├── order_id: '{order_id}'（去重用）
│   └── content_name: '{product_names}'
└── 用途：转化优化 + ROAS 计算 + 相似受众

Pixel 验证清单：
□ 使用 Facebook Pixel Helper 扩展验证
□ 所有 5 个标准事件正确触发
□ 参数值正确（特别是 value 和 currency）
□ 无重复触发（特别是 Purchase）
□ 跨浏览器测试（Chrome, Safari, Firefox）
□ 移动端测试
□ Events Manager 中事件显示正常
□ 测试购买的数据在 Events Manager 中可见
```

---

## 三、CAPI 设置指南

```
Shopify 原生 CAPI（推荐）：
├── 路径：Shopify 后台 → 设置 → 客户事件 → Facebook & Instagram
├── 优势：零代码，自动去重，自动更新
├── 配置步骤：
│   1. 连接 Facebook 频道
│   2. 启用 CAPI
│   3. 选择共享的客户数据级别："最大"
│   4. 验证事件在 Events Manager 中显示
│   5. 检查事件匹配质量
└── 注意：确保 Shopify 版本支持最新 CAPI

第三方工具 CAPI：
├── Elevar（推荐）
│   ├── 优势：最精准的追踪，支持服务器端 GTM
│   ├── 价格：$150-$500/月
│   └── 适用：月广告费 > $10,000 的品牌
├── Stape
│   ├── 优势：服务器端 GTM 托管
│   ├── 价格：$20-$100/月
│   └── 适用：技术团队可以配置 GTM
└── Triple Whale / Northbeam
    ├── 优势：多触点归因 + CAPI
    ├── 价格：$300-$1,000/月
    └── 适用：多渠道广告投放的品牌

CAPI 去重设置：
├── 去重键：event_id
├── Pixel 和 CAPI 发送相同的 event_id
├── Meta 自动去重相同 event_id 的事件
├── 验证：Events Manager → 事件概览 → 检查"重复率"
└── 目标重复率：< 5%
```

---

## 四、事件匹配质量（EMQ）

```
EMQ 评分标准（1-10 分）：

10 分（完美）：
├── 发送了所有可用的客户信息参数
├── 包括：email, phone, first_name, last_name, city, state, zip, country
└── 匹配率 > 95%

8-9 分（优秀）：
├── 发送了 email + phone + 姓名
├── 匹配率 > 85%
└── 目标：大多数品牌应该达到这个水平

6-7 分（良好）：
├── 发送了 email + 部分其他参数
├── 匹配率 > 70%
└── 可以接受，但有提升空间

< 6 分（需要改善）：
├── 只发送了少量参数
├── 匹配率 < 70%
└── 严重影响 AI 优化效果

提升 EMQ 的方法：
├── 1. 确保 CAPI 发送所有可用的客户数据
├── 2. 对 email 和 phone 进行 SHA-256 哈希
├── 3. 确保数据格式正确（小写、去空格）
├── 4. 使用 Shopify 原生集成（自动处理格式）
└── 5. 定期检查 Events Manager 中的 EMQ 评分
```

---

## 五、归因设置

```
归因窗口选择：

推荐设置：7 天点击 + 1 天浏览
├── 原因：这是 Meta 默认设置，AI 优化基于此窗口
├── 适用：大多数 DTC 品牌
└── 注意：不要频繁更改归因窗口

其他窗口：
├── 1 天点击：适用于低价冲动购买产品
├── 7 天点击 + 1 天浏览：标准推荐
└── 注意：不同窗口的数据不可直接比较

> **历史口径提示**：28 天点击归因窗口已随 iOS 14.5（2021）的 ATT 变更下线，Meta 当前最长支持 **7 天点击**。旧文档或旧账户截图若出现「28 天点击」，属历史数据口径，**不可作为当前可选设置**。

归因模型理解：
├── Meta 默认：最后触点归因
├── 局限：无法看到多触点贡献
├── 补充方案：
│   ├── Google Analytics 4（数据驱动归因）
│   ├── Triple Whale / Northbeam（多触点归因）
│   └── 手动增量测试（最准确但最耗时）
└── 建议：不要只看 Meta 报告的 ROAS

增量测试（Incrementality Testing）：
├── 方法 1：Conversion Lift Study（Meta 原生）
│   ├── 设置：Meta 自动分配测试组和对照组
│   ├── 时长：2-4 周
│   └── 结果：真实的增量转化数据
├── 方法 2：地理位置测试
│   ├── 设置：在部分地区暂停广告，对比转化变化
│   ├── 时长：2-4 周
│   └── 结果：广告对该地区的真实增量贡献
└── 方法 3：暂停测试
    ├── 设置：完全暂停某个活动 1-2 周
    ├── 观察：总体转化是否下降
    └── 结果：该活动的真实增量贡献
```

---

## 六、数据差异排查

```
常见数据差异及原因：

Meta 报告 vs Shopify 报告：
├── 正常差异范围：10-30%
├── 原因 1：归因窗口不同
├── 原因 2：Meta 计算浏览归因，Shopify 不计算
├── 原因 3：退款/取消在 Shopify 中扣除但 Meta 不扣除
├── 原因 4：跨设备归因差异
└── 应对：以 Shopify 实际收入为准，Meta 数据用于优化

Meta 报告 vs GA4 报告：
├── 正常差异范围：20-40%
├── 原因 1：归因模型不同（最后触点 vs 数据驱动）
├── 原因 2：GA4 不计算浏览归因
├── 原因 3：广告拦截器影响 GA4 更多
└── 应对：两个平台都看，取中间值作为参考

Pixel 数据 vs CAPI 数据：
├── 正常差异范围：5-15%
├── 原因：浏览器端和服务器端捕获的事件略有不同
├── 检查：去重是否正常工作
└── 应对：确保去重正常，以 Events Manager 合并数据为准
```

---

## 七、追踪健康检查清单

```
每周检查：
□ Events Manager 中所有事件正常触发
□ 事件匹配质量 > 6.0
□ Pixel 和 CAPI 去重正常（重复率 < 5%）
□ Purchase 事件数量与 Shopify 订单数量基本一致
□ 无新的 Pixel 错误或警告

每月检查：
□ 归因窗口设置未被意外更改
□ 域名验证状态正常（品牌安全 / 链接归属仍需要）
□ 自定义转化设置正确
□ 标准事件命名与去重规则未漂移

每季度检查：
□ 评估是否需要升级追踪工具
□ 检查 Meta 平台更新对追踪的影响
□ 评估第三方追踪工具的 ROI
□ 进行一次增量测试验证归因准确性
```

> **历史注记：聚合事件衡量（AEM）为什么不在清单里了**
> 旧版清单曾要求「每月检查 AEM 配置正确」和「事件优先级排序正确（Purchase > ATC > VC > PV）」。这两项已经**不再是可执行的检查动作**：Meta 自 2025 年 6 月起移除了 Events Manager 中的 **AEM 配置标签页**，同时取消了**8 事件上限**与**手动事件优先级排序**——现在所有符合条件的标准/自定义事件都由 Meta 自动聚合处理，无需人工配置或排序；域名验证也不再是 AEM 事件配置的前置条件（但域名验证本身在品牌安全/链接归属场景仍然要做）。
> 需要说明的是：**AEM 协议本身并未退役**。Apple 的 ATT 仍然存在，AEM 只是从「需要广告主手动配置」转为「后台自动运行」。所以做法上的变化是：**不再花时间配 AEM，把精力放回事件质量（匹配质量、去重、CAPI 覆盖）**。
> **来源**：[Meta 官方：About Aggregated Event Measurement](https://www.facebook.com/business/help/721422165168355)；[Jon Loomer：Meta's AEM Isn't Going Away — It's Changing](https://www.jonloomer.com/qvt/aggregated-event-measurement-isnt-going-away/)。核实于 2026-07。

---

*追踪是一切优化的基础。没有准确的数据，所有的优化决策都是在猜测。投资追踪基础设施的 ROI 远高于投资更多广告预算。*
