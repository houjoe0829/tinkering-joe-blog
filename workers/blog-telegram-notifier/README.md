# Blog Telegram 通知服务

这是一个 Cloudflare Worker 服务，用于自动检查博客的 RSS 更新并将新文章推送到 Telegram Channel。

## 功能特点

- 每小时自动检查博客 RSS 更新
- 检查最近7天内发布的文章
- 将新文章以简洁的格式推送到 Telegram Channel
- 支持显示文章标题、描述和链接
- 支持测试模式，方便调试和验证
- 防重复推送机制，确保同一篇文章不会被多次发送

## 部署步骤

1. **创建 Worker**
   - 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
   - 进入 "Workers & Pages"
   - 点击 "Create Worker"
   - 将 `src/index.js` 的代码复制粘贴到编辑器中
   - 点击 "Save and Deploy"

2. **配置环境变量**
   - 在 Worker 的设置页面中找到 "Settings" -> "Variables"
   - 添加以下环境变量：
     ```
     TELEGRAM_BOT_TOKEN = "您的 Telegram Bot Token"  # 类型选择：Secret
     TELEGRAM_CHANNEL_ID = "@您的频道ID"            # 类型选择：String
     BLOG_RSS_URL = "https://houjoe.me/index.xml"   # 类型选择：String
     IS_TEST_MODE = "true"                          # 类型选择：String，测试时设为 true
     TELEGRAM_TEST_USER_ID = "您的用户ID"           # 类型选择：String，测试时需要
     ```

3. **创建并绑定 KV 存储**
   - 在 Cloudflare Dashboard 中创建一个 KV 命名空间
   - 在 Worker 设置中绑定该 KV 命名空间，变量名设为 `KV`

4. **设置定时任务**
   - 在 Worker 的设置页面中找到 "Triggers" -> "Cron Triggers"
   - 添加 Cron 触发器：`0 * * * *`（每小时运行一次）

## 工作原理

本服务的工作流程如下：

1. **检查时间范围**：服务会检查最近7天内发布的所有文章
2. **防重复机制**：使用 KV 存储记录已发送的文章，确保同一篇文章不会被重复发送（记录保存30天）
3. **执行锁机制**：使用 KV 存储实现执行锁，防止多个实例同时运行导致的重复推送
4. **随机延迟**：在发送消息前添加随机延迟，进一步防止并发问题

## 测试模式说明

本服务支持测试模式，便于在正式部署前进行功能验证：

1. **测试模式特点**
   - 消息会发送到个人而不是频道
   - 消息中会显示"测试模式"标记
   - 仍然会记录已发送的文章状态，防止重复发送

2. **如何使用测试模式**
   - 设置 `IS_TEST_MODE = "true"`
   - 设置 `TELEGRAM_TEST_USER_ID` 为您的个人 Telegram ID
   - 直接访问 Worker URL 或使用 Quick Edit 中的 "Send" 按钮触发测试

3. **切换到正式模式**
   - 将 `IS_TEST_MODE` 改为 `"false"` 或删除该变量
   - 确保 `TELEGRAM_CHANNEL_ID` 已正确设置
   - 移除 `TELEGRAM_TEST_USER_ID`（可选）

## 消息格式

推送到 Telegram Channel 的消息格式如下：

```
📝 文章标题

文章描述（最多 200 字）...

🔗 阅读全文

发布日期: 2024-02-19
```

## 注意事项

1. 确保您的 Telegram Bot 已被添加到 Channel 并具有管理员权限
2. Channel ID 必须包含 @ 符号（例如：@mychannel）
3. 部署完成后，可以直接访问 Worker URL 来测试功能
4. 默认每小时检查一次，可以通过修改 Cron 表达式来调整检查频率

## 测试步骤

1. **快速测试**
   - 在 Cloudflare Worker 页面中点击 "Quick Edit"
   - 点击右侧的 "Send" 按钮触发测试
   - 如果配置正确，您的 Telegram 将收到最近7天内未发送过的博客文章

2. **手动测试**
   - 复制 Worker 的 URL（格式如：https://your-worker.your-name.workers.dev）
   - 在浏览器中访问该 URL
   - 您会看到一个 JSON 响应，包含处理结果和详细日志

3. **定时任务测试**
   - 等待下一个整点时间
   - 如果您在最近7天内发布了新文章且未被发送过，将会收到推送

## 常见问题

1. **没有收到推送**
   - 检查 Worker 的 "Logs" 页面是否有错误信息
   - 确认文章的发布时间是否在最近7天内
   - 验证 RSS feed 是否包含最新文章
   - 检查文章是否已经被标记为发送过
   - 检查是否处于测试模式（此时消息会发送到测试用户而不是频道）

2. **收到错误响应**
   - `{"success": false, "error": "Failed to send Telegram message"}` 
     → 检查 Bot Token 和 Channel ID（测试模式下检查 Test User ID）
   - `{"success": false, "error": "Failed to fetch RSS feed"}`
     → 检查 RSS URL 是否可访问
   - `{"success": false, "error": "KV 存储未配置"}`
     → 检查是否已创建并绑定 KV 存储

3. **收到重复推送**
   - 检查是否有多个 Worker 实例同时运行
   - 检查 KV 存储是否正常工作
   - 检查执行锁机制是否正常工作

## 故障排除

如果消息推送失败，请检查：

1. Telegram Bot Token 是否正确
2. Bot 是否已被添加到 Channel 并设为管理员
3. Channel ID 格式是否正确（需要 @ 符号）
4. RSS Feed URL 是否可以正常访问
5. KV 存储是否已正确配置和绑定
6. 检查 Worker 的日志，查看详细的错误信息

## 高级功能

1. **执行锁机制**：服务使用 KV 存储实现执行锁，防止多个实例同时运行
2. **唯一执行ID**：每次执行都有唯一的ID，便于跟踪和调试
3. **详细日志**：记录详细的执行日志，便于排查问题
4. **随机延迟**：在发送消息前添加随机延迟，进一步防止并发问题 