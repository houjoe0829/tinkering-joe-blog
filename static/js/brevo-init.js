// Brevo 邮件订阅功能初始化
document.addEventListener('DOMContentLoaded', function() {
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
      // 尝试不同的触发方式
      window.Brevo.push(['trigger', 'newsletter_subscription']);
      // 如果上面的方式不起作用，尝试直接打开 Brevo 框架页面
      setTimeout(function() {
        window.open('/brevo-frame.html', '_blank', 'width=500,height=600');
      }, 500);
    } else {
      console.error('Brevo SDK 未正确加载');
      // 如果 Brevo SDK 未加载，直接打开 Brevo 框架页面
      window.open('/brevo-frame.html', '_blank', 'width=500,height=600');
    }
  }
});
