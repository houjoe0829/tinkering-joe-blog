// Brevo 邮件订阅功能初始化
document.addEventListener('DOMContentLoaded', function() {
  // 手动触发页面浏览事件，帮助 Brevo 检测网站活动
  if (window.Brevo) {
    window.Brevo.push(['page_view']);
    console.log('手动触发 Brevo 页面浏览事件');
    
    // 模拟用户交互，触发更多事件
    setTimeout(function() {
      window.Brevo.push(['track', 'page_viewed', { page_name: window.location.pathname }]);
      console.log('触发自定义事件：page_viewed');
    }, 2000);
  }

  // 查找“通过邮件订阅”菜单项
  // 首先尝试查找菜单标识符
  let newsletterLinks = document.querySelectorAll('a[href="#"][data-id="newsletter"], li[data-id="newsletter"] a');
  
  // 如果没有找到，则尝试通过菜单标识符查找
  if (newsletterLinks.length === 0) {
    newsletterLinks = document.querySelectorAll('a[href="#"][data-identifier="newsletter"], li[data-identifier="newsletter"] a');
  }
  
  // 如果还是没有找到，则查找父元素为 subscribe 的菜单项
  if (newsletterLinks.length === 0) {
    const subscribeMenus = document.querySelectorAll('li[data-identifier="subscribe"] ul, li[data-id="subscribe"] ul');
    subscribeMenus.forEach(menu => {
      const links = menu.querySelectorAll('a');
      links.forEach(link => {
        if (link.textContent.trim().includes('通过邮件订阅')) {
          newsletterLinks = Array.from(newsletterLinks || []).concat(link);
        }
      });
    });
  }
  
  // 如果仍然没有找到，则查找所有包含“通过邮件订阅”文本的链接
  if (!newsletterLinks || newsletterLinks.length === 0) {
    const allLinks = document.querySelectorAll('a');
    allLinks.forEach(link => {
      if (link.textContent.trim().includes('通过邮件订阅')) {
        link.addEventListener('click', triggerBrevoPopup);
      }
    });
  } else {
    // 为找到的菜单项添加点击事件
    if (Array.isArray(newsletterLinks)) {
      newsletterLinks.forEach(link => {
        link.addEventListener('click', triggerBrevoPopup);
      });
    } else {
      newsletterLinks.forEach(link => {
        link.addEventListener('click', triggerBrevoPopup);
      });
    }
  }
  
  // 触发 Brevo 弹窗的函数
  function triggerBrevoPopup(e) {
    // 阻止默认的链接跳转行为
    e.preventDefault();
    
    console.log('触发 Brevo 订阅弹窗');
    
    // 调用 Brevo API 显示订阅表单
    if (window.Brevo) {
      // 使用 Brevo 的内置弹窗 API
      window.Brevo.push(['trigger', 'newsletter_subscription']);
    } else {
      console.error('Brevo SDK 未正确加载');
    }
  }
});
