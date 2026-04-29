# 追踪与归因设置

## 九、追踪与归因设置

### 9.1 增强型转化设置

```
增强型转化（Enhanced Conversions）：

原理：
├── 用户完成转化时，收集第一方数据（邮箱、电话、地址）
├── 数据经过 SHA-256 哈希加密
├── 发送给 Google 进行匹配
└── 提升转化追踪的准确性（尤其在 Cookie 受限环境下）

设置步骤：
1. Google Ads → 工具 → 转化 → 设置
2. 开启"增强型转化"
3. 选择实现方式：
   ├── Google 代码（gtag.js）：最简单
   ├── Google Tag Manager：推荐
   └── Google Ads API：最灵活
4. 配置数据字段：
   ├── 优先：邮箱地址（通常最关键）
   ├── 推荐：电话号码
   ├── 推荐：姓名 + 地址
   └── 注意：数据在浏览器端哈希，Google 不接收明文
5. 验证：检查转化报告中"增强型转化"标签

推算依据：
├── 转化追踪准确性通常会改善，但提升幅度需以真实数据验证
├── 智能出价优化效果可能改善
└── 受众列表匹配率可能提升
```

### 9.2 服务器端追踪

```
服务器端追踪（Server-Side Tracking）：

原理：
├── 传统：浏览器 → Google（受 Cookie 限制、广告拦截器影响）
├── 服务器端：浏览器 → 你的服务器 → Google（绕过限制）
└── 效果：数据更完整、更准确

推荐方案：
├── Google Tag Manager Server-Side Container
├── 部署在 Google Cloud Run 或 AWS
├── 配合 Shopify 的 Customer Events API
└── 成本：根据流量规模、部署方式与维护复杂度而变化

关键事件追踪：
├── page_view：页面浏览
├── view_item：产品浏览
├── add_to_cart：加入购物车
├── begin_checkout：开始结账
├── purchase：完成购买（含订单价值）
├── sign_up：注册
└── 自定义事件：根据业务需求
```

---

