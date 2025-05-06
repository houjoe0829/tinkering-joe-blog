// Brevo Newsletter 订阅功能
document.addEventListener('DOMContentLoaded', function() {
  // 查找所有带有 brevo-newsletter 类的元素
  const newsletterButtons = document.querySelectorAll('.brevo-newsletter');
  
  // 为每个按钮添加点击事件
  newsletterButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      e.preventDefault();
      
      // 调用 Brevo API 显示订阅表单
      if (window.Brevo) {
        window.Brevo.push(['trigger', 'newsletter_subscription']);
      } else {
        console.error('Brevo SDK 未正确加载');
      }
    });
  });
});
