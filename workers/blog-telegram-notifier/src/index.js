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

// 从 XML 中提取所有标签内容
function extractAllTags(xml, tag) {
  const regex = new RegExp(`<${tag}[^>]*>(.*?)<\/${tag}>`, 'gs');
  const matches = [...xml.matchAll(regex)];
  return matches.map(match => match[1].trim());
}

// 解析 RSS XML
function parseRSS(xml) {
  // 提取所有 item 标签
  const itemRegex = /<item>(.*?)<\/item>/gs;
  const items = [...xml.matchAll(itemRegex)];
  
  return items.map(item => {
    const itemXml = item[1];
    return {
      title: extractTag(itemXml, 'title'),
      link: extractTag(itemXml, 'link'),
      pubDate: extractTag(itemXml, 'pubDate'),
      description: extractTag(itemXml, 'description').replace(/<\/?[^>]+(>|$)/g, ''), // 移除 HTML 标签
      categories: extractAllTags(itemXml, 'category')
    };
  });
}

// 发送 Telegram 消息
async function sendTelegramMessage(text, env) {
  const url = `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      chat_id: env.TELEGRAM_CHANNEL_ID,
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
    // 获取时间范围
    const { start, end } = getTimeRange();
    
    // 获取 RSS Feed
    const response = await fetch(env.BLOG_RSS_URL);
    if (!response.ok) {
      throw new Error('Failed to fetch RSS feed');
    }
    
    const xml = await response.text();
    const items = parseRSS(xml);
    
    // 筛选在时间范围内的文章
    const newPosts = items.filter(item => {
      const pubDate = new Date(item.pubDate);
      return pubDate >= start && pubDate < end;
    });
    
    // 如果有新文章，发送通知
    for (const post of newPosts) {
      const message = `
📝 <b>${post.title}</b>

${post.description ? `${post.description.slice(0, 200)}...` : ''}

🏷 标签: ${post.categories.length > 0 ? post.categories.join(', ') : '无标签'}

🔗 <a href="${post.link}">阅读全文</a>
`;
      
      await sendTelegramMessage(message, env);
    }
    
    return { success: true, processed: newPosts.length };
  } catch (error) {
    console.error('Error:', error);
    return { success: false, error: error.message };
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
    const result = await checkAndNotify(env);
    return new Response(JSON.stringify(result), {
      headers: { 'Content-Type': 'application/json' },
    });
  },
}; 