// 格式化日期时间为 ISO 字符串
function formatDate(date) {
  return date.toISOString();
}

// 转换为北京时间
function convertToBeijingTime(date) {
  const utcDate = new Date(date);
  return new Date(utcDate.getTime() + 8 * 60 * 60 * 1000);
}

// 转换为 UTC 时间
function convertToUTC(date) {
  const beijingDate = new Date(date);
  return new Date(beijingDate.getTime() - 8 * 60 * 60 * 1000);
}

// 获取最近7天的时间范围
function getTimeRange() {
  // 获取当前北京时间
  const nowBeijing = convertToBeijingTime(new Date());
  
  // 获取7天前的北京时间
  const sevenDaysAgoBeijing = new Date(nowBeijing);
  sevenDaysAgoBeijing.setDate(sevenDaysAgoBeijing.getDate() - 7);
  
  // 设置为7天前的北京时间 00:00:00
  sevenDaysAgoBeijing.setHours(0, 0, 0, 0);
  
  // 设置为当前北京时间 23:59:59
  const endOfTodayBeijing = new Date(nowBeijing);
  endOfTodayBeijing.setHours(23, 59, 59, 999);
  
  // 转换回 UTC 时间用于比较
  return {
    start: convertToUTC(sevenDaysAgoBeijing),
    end: convertToUTC(endOfTodayBeijing)
  };
}

// 解码 HTML 实体
function decodeHTMLEntities(text) {
  const entities = {
    '&quot;': '"',
    '&apos;': "'",
    '&#39;': "'",
    '&lt;': '<',
    '&gt;': '>',
    '&amp;': '&',
    '&nbsp;': ' '
  };
  
  return text.replace(/&[^;]+;/g, entity => {
    return entities[entity] || entity;
  });
}

// 从 XML 中提取标签内容
function extractTag(xml, tag) {
  const regex = new RegExp(`<${tag}[^>]*>(.*?)<\/${tag}>`, 's');
  const match = xml.match(regex);
  return match ? decodeHTMLEntities(match[1].trim()) : '';
}

// 解析 RSS XML
function parseRSS(xml) {
  const itemRegex = /<item>(.*?)<\/item>/gs;
  const items = [...xml.matchAll(itemRegex)];
  
  console.log('RSS 解析完成，共找到文章:', items.length);
  
  return items.map(item => {
    const itemXml = item[1];
    return {
      title: extractTag(itemXml, 'title'),
      link: extractTag(itemXml, 'link'),
      pubDate: extractTag(itemXml, 'pubDate'),
      description: extractTag(itemXml, 'description').replace(/<\/?[^>]+(>|$)/g, '')
    };
  });
}

// 生成唯一的执行ID
function generateExecutionId() {
  return `exec_${Date.now()}_${Math.random().toString(36).substring(2, 15)}`;
}

// 等待指定的毫秒数
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// 发送 Telegram 消息
async function sendTelegramMessage(text, env) {
  // 判断是否为测试模式
  const chatId = env.IS_TEST_MODE === 'true' ? env.TELEGRAM_TEST_USER_ID : env.TELEGRAM_CHANNEL_ID;
  
  console.log('发送消息到:', chatId);
  
  const url = `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      chat_id: chatId,
      text: text,
      parse_mode: 'HTML',
      disable_web_page_preview: false
    }),
  });
  
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Failed to send Telegram message: ${response.statusText}, ${errorText}`);
  }
  
  return await response.json();
}

// 检查新文章并发送通知
async function checkAndNotify(env) {
  let debugInfo = {};
  const executionId = generateExecutionId();
  console.log(`开始执行检查 [${executionId}]`);
  
  try {
    console.log('开始检查新文章...');
    console.log('环境变量检查:');
    console.log('- BLOG_RSS_URL:', env.BLOG_RSS_URL ? '已设置' : '未设置');
    console.log('- TELEGRAM_BOT_TOKEN:', env.TELEGRAM_BOT_TOKEN ? '已设置' : '未设置');
    console.log('- TELEGRAM_CHANNEL_ID:', env.TELEGRAM_CHANNEL_ID);
    console.log('- IS_TEST_MODE:', env.IS_TEST_MODE);
    
    if (!env.KV) {
      throw new Error('KV 存储未配置');
    }

    // 设置执行锁，防止重复执行
    const lockKey = 'execution_lock';
    const existingLock = await env.KV.get(lockKey);
    
    if (existingLock) {
      const lockData = JSON.parse(existingLock);
      const lockTime = new Date(lockData.time);
      const now = new Date();
      
      // 如果锁的时间不超过5分钟，认为有其他实例正在执行
      if ((now - lockTime) < 5 * 60 * 1000) {
        console.log(`检测到另一个执行实例正在运行 [${lockData.id}]，开始于 ${lockData.time}，跳过本次执行`);
        return {
          success: true,
          processed: 0,
          skipped: true,
          reason: 'Another execution is in progress',
          executionId: executionId
        };
      } else {
        console.log(`检测到过期的执行锁 [${lockData.id}]，将覆盖`);
      }
    }
    
    // 设置新的执行锁
    const lockData = {
      id: executionId,
      time: new Date().toISOString()
    };
    await env.KV.put(lockKey, JSON.stringify(lockData), {expirationTtl: 300}); // 5分钟过期
    console.log(`已设置执行锁 [${executionId}]`);

    const now = new Date();
    debugInfo.currentTime = now.toISOString();
    debugInfo.executionId = executionId;
    
    console.log('当前时间:', now.toISOString());
    
    // 获取最近7天的时间范围
    const timeRange = getTimeRange();
    console.log('检查时间范围:', timeRange.start.toISOString(), '至', timeRange.end.toISOString());
    debugInfo.timeRange = {
      start: timeRange.start.toISOString(),
      end: timeRange.end.toISOString()
    };
    
    // 获取 RSS Feed
    console.log('正在获取 RSS Feed:', env.BLOG_RSS_URL);
    const response = await fetch(env.BLOG_RSS_URL);
    if (!response.ok) {
      throw new Error(`获取 RSS feed 失败: ${response.status} ${response.statusText}`);
    }
    
    const xml = await response.text();
    console.log('RSS Feed 获取成功，长度:', xml.length);
    
    const items = parseRSS(xml);
    debugInfo.totalArticles = items.length;
    
    // 筛选最近7天内发布的文章
    const newPosts = [];
    for (const item of items) {
      const pubDate = new Date(item.pubDate);
      console.log('原始文章发布时间:', item.pubDate);
      console.log('解析后的发布时间:', pubDate.toISOString());
      
      // 检查文章是否在最近7天内发布
      if (pubDate >= timeRange.start && pubDate <= timeRange.end) {
        console.log('文章在最近7天内发布:', item.title);
        
        // 检查文章是否已经发送过
        const postKey = `sent_${item.link}`;
        const isSent = await env.KV.get(postKey);
        
        if (!isSent) {
          console.log('文章未发送过，添加到待发送列表:', item.title);
          newPosts.push(item);
        } else {
          console.log('文章已发送过，跳过:', item.title);
        }
      } else {
        console.log('文章不在最近7天内，跳过:', item.title);
      }
    }
    
    console.log(`发现 ${newPosts.length} 篇新文章需要发送`);
    debugInfo.newArticles = newPosts.length;
    
    // 发送新文章
    for (const post of newPosts) {
      // 在发送前先标记文章为已发送，防止并发执行时重复发送
      const postKey = `sent_${post.link}`;
      try {
        // 先检查一次是否已经被标记（可能是其他并发执行标记的）
        const isAlreadyMarked = await env.KV.get(postKey);
        if (isAlreadyMarked) {
          console.log(`文章在准备发送前已被其他进程标记为已发送，跳过: ${post.title}`);
          continue;
        }
        
        // 标记为已发送
        await env.KV.put(postKey, JSON.stringify({
          executionId: executionId,
          time: new Date().toISOString()
        }), {expirationTtl: 60 * 60 * 24 * 7});
        console.log(`已标记文章为已发送: ${post.title}`);
        
        // 添加随机延迟，进一步防止并发问题
        const delay = Math.floor(Math.random() * 1000) + 500; // 500-1500ms
        await sleep(delay);
        
        const message = `
📝 <b>${post.title}</b>

${post.description ? `${post.description.slice(0, 200)}...` : ''}

🔗 <a href="${post.link}">阅读全文</a>

${env.IS_TEST_MODE === 'true' ? '⚠️ 测试模式消息' : ''}
发布日期: ${new Date(post.pubDate).toLocaleDateString('zh-CN', { timeZone: 'Asia/Shanghai' })}
`;
        
        console.log('准备发送消息:', post.title);
        await sendTelegramMessage(message, env);
        console.log(`已发送文章: ${post.title}`);
      } catch (error) {
        console.error(`处理文章时出错: ${post.title}`, error);
      }
    }
    
    // 释放执行锁
    try {
      const currentLock = await env.KV.get(lockKey);
      if (currentLock) {
        const lockData = JSON.parse(currentLock);
        if (lockData.id === executionId) {
          await env.KV.delete(lockKey);
          console.log(`已释放执行锁 [${executionId}]`);
        }
      }
    } catch (error) {
      console.error('释放执行锁时出错:', error);
    }
    
    return { 
      success: true, 
      processed: newPosts.length,
      currentTime: now.toISOString(),
      isTestMode: env.IS_TEST_MODE === 'true',
      executionId: executionId,
      debugInfo
    };
  } catch (error) {
    console.error('运行出错:', error.message);
    
    // 释放执行锁
    try {
      const lockKey = 'execution_lock';
      const currentLock = await env.KV.get(lockKey);
      if (currentLock) {
        const lockData = JSON.parse(currentLock);
        if (lockData.id === executionId) {
          await env.KV.delete(lockKey);
          console.log(`已释放执行锁 [${executionId}]`);
        }
      }
    } catch (lockError) {
      console.error('释放执行锁时出错:', lockError);
    }
    
    return { 
      success: false, 
      error: error.message,
      currentTime: new Date().toISOString(),
      isTestMode: env.IS_TEST_MODE === 'true',
      executionId: executionId,
      debugInfo
    };
  }
}

// Worker 入口函数
export default {
  // 处理定时任务
  async scheduled(event, env, ctx) {
    console.log('定时任务触发，时间:', new Date().toISOString());
    try {
      const result = await checkAndNotify(env);
      console.log('定时任务执行结果:', JSON.stringify(result));
      return result;
    } catch (error) {
      console.error('定时任务执行出错:', error);
      return { success: false, error: error.message };
    }
  },
  
  // 处理 HTTP 请求（用于测试）
  async fetch(request, env, ctx) {
    const debugLogs = [];
    
    // 重写 console.log 来捕获日志
    const originalLog = console.log;
    const originalError = console.error;
    
    console.log = (...args) => {
      debugLogs.push(['log', ...args]);
      originalLog.apply(console, args);
    };
    
    console.error = (...args) => {
      debugLogs.push(['error', ...args]);
      originalError.apply(console, args);
    };
    
    console.log('手动触发，时间:', new Date().toISOString());
    const result = await checkAndNotify(env);
    
    // 恢复原始的 console 方法
    console.log = originalLog;
    console.error = originalError;
    
    return new Response(JSON.stringify({
      ...result,
      debug: {
        logs: debugLogs,
      }
    }, null, 2), {
      headers: { 
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    });
  },
}; 