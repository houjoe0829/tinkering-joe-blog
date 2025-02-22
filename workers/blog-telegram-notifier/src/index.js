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

// 获取上一次检查的时间范围（北京时间）
function getTimeRange() {
  // 获取当前北京时间
  const nowBeijing = convertToBeijingTime(new Date());
  const yesterdayBeijing = new Date(nowBeijing);
  yesterdayBeijing.setDate(yesterdayBeijing.getDate() - 1);
  
  // 设置为前一天的北京时间 00:00:00
  yesterdayBeijing.setHours(0, 0, 0, 0);
  
  // 设置为前一天的北京时间 23:59:59
  const endOfYesterdayBeijing = new Date(yesterdayBeijing);
  endOfYesterdayBeijing.setHours(23, 59, 59, 999);
  
  // 转换回 UTC 时间用于比较
  return {
    start: convertToUTC(yesterdayBeijing),
    end: convertToUTC(endOfYesterdayBeijing)
  };
}

// 从 XML 中提取标签内容
function extractTag(xml, tag) {
  const regex = new RegExp(`<${tag}[^>]*>(.*?)<\/${tag}>`, 's');
  const match = xml.match(regex);
  return match ? match[1].trim() : '';
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

// 发送 Telegram 消息
async function sendTelegramMessage(text, env) {
  // 判断是否为测试模式
  const chatId = env.IS_TEST_MODE === 'true' ? env.TELEGRAM_TEST_USER_ID : env.TELEGRAM_CHANNEL_ID;
  
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
    throw new Error(`Failed to send Telegram message: ${response.statusText}`);
  }
  
  return await response.json();
}

// 检查新文章并发送通知
async function checkAndNotify(env) {
  try {
    if (!env.KV) {
      throw new Error('KV 存储未配置');
    }

    // 从 KV 获取上次检查时间
    let lastCheckTime;
    try {
      const storedTime = await env.KV.get('lastCheckTime');
      console.log('上次检查时间:', storedTime);
      
      if (storedTime) {
        lastCheckTime = new Date(storedTime);
        if (isNaN(lastCheckTime.getTime())) {
          lastCheckTime = new Date();
        }
      } else {
        lastCheckTime = new Date();
      }
    } catch (kvError) {
      console.error('读取 KV 时出错:', kvError);
      lastCheckTime = new Date();
    }
    
    const now = new Date();
    
    // 获取 RSS Feed
    const response = await fetch(env.BLOG_RSS_URL);
    if (!response.ok) {
      throw new Error('获取 RSS feed 失败');
    }
    
    const xml = await response.text();
    const items = parseRSS(xml);
    
    // 筛选新文章
    const newPosts = [];
    for (const item of items) {
      const pubDate = new Date(item.pubDate);
      console.log('原始文章发布时间:', item.pubDate);
      console.log('解析后的发布时间:', pubDate.toISOString());
      
      // 将发布时间和上次检查时间都转换为 UTC 时间进行比较
      const pubDateUTC = new Date(pubDate.getTime() - pubDate.getTimezoneOffset() * 60 * 1000);
      const lastCheckTimeUTC = new Date(lastCheckTime.getTime() - lastCheckTime.getTimezoneOffset() * 60 * 1000);
      
      // 只比较日期部分
      const pubDateString = pubDateUTC.toISOString().split('T')[0];
      const lastCheckTimeString = lastCheckTimeUTC.toISOString().split('T')[0];
      
      console.log('文章发布日期:', pubDateString);
      console.log('上次检查日期:', lastCheckTimeString);
      
      const postKey = `sent_${item.link}`;
      const isSent = await env.KV.get(postKey);
      
      if (pubDateString >= lastCheckTimeString && !isSent) {
        if (env.IS_TEST_MODE === 'true') {
          console.log('测试模式：发现新文章');
        } else {
          console.log('正常模式：发现新文章');
        }
        newPosts.push(item);
      }
    }
    
    console.log(`发现 ${newPosts.length} 篇新文章需要发送`);
    
    // 发送新文章
    for (const post of newPosts) {
      const message = `
📝 <b>${post.title}</b>

${post.description ? `${post.description.slice(0, 200)}...` : ''}

🔗 <a href="${post.link}">阅读全文</a>

${env.IS_TEST_MODE === 'true' ? '⚠️ 测试模式消息' : ''}
发布日期: ${new Date(post.pubDate).toLocaleDateString('zh-CN', { timeZone: 'Asia/Shanghai' })}
`;
      
      await sendTelegramMessage(message, env);
      
      // 无论是否测试模式，都设置发送标记
      const postKey = `sent_${post.link}`;
      try {
        await env.KV.put(postKey, 'true', {expirationTtl: 60 * 60 * 24 * 7});
        console.log(`已发送文章: ${post.title}`);
      } catch (kvError) {
        console.error(`标记文章发送状态失败: ${post.title}`);
      }
    }
    
    if (env.IS_TEST_MODE !== 'true') {
      try {
        await env.KV.put('lastCheckTime', now.toISOString());
        console.log('已更新最后检查时间');
      } catch (kvError) {
        console.error('更新最后检查时间失败');
      }
    }
    
    return { 
      success: true, 
      processed: newPosts.length,
      lastCheckTime: lastCheckTime.toISOString(),
      currentTime: now.toISOString(),
      isTestMode: env.IS_TEST_MODE === 'true'
    };
  } catch (error) {
    console.error('运行出错:', error.message);
    return { 
      success: false, 
      error: error.message,
      lastCheckTime: lastCheckTime?.toISOString(),
      currentTime: new Date().toISOString(),
      isTestMode: env.IS_TEST_MODE === 'true'
    };
  }
}

// Worker 入口函数
export default {
  // 处理定时任务
  async scheduled(event, env, ctx) {
    return await checkAndNotify(env);
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