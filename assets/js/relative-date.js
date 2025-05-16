// 相对日期显示
document.addEventListener('DOMContentLoaded', function() {
  const postDates = document.querySelectorAll('.post-date');
  
  function updateDateDisplay() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    
    postDates.forEach(span => {
      const dateStr = span.getAttribute('data-date');
      const postDate = new Date(dateStr);
      const postDateOnly = new Date(postDate.getFullYear(), postDate.getMonth(), postDate.getDate());
      
      const diffTime = Math.abs(today - postDateOnly);
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      
      let displayText = dateStr;
      if (diffDays === 0) {
        displayText = '今天';
      } else if (diffDays === 1) {
        displayText = '昨天';
      } else if (diffDays === 2) {
        displayText = '前天';
      }
      
      span.textContent = displayText;
    });
  }
  
  // 初始更新
  updateDateDisplay();
  
  // 每天凌晨更新一次
  const now = new Date();
  const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
  const timeUntilMidnight = tomorrow - now;
  
  setTimeout(() => {
    updateDateDisplay();
    // 之后每24小时更新一次
    setInterval(updateDateDisplay, 24 * 60 * 60 * 1000);
  }, timeUntilMidnight);
});
