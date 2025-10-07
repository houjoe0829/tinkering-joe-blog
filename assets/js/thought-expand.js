/**
 * Thoughts 卡片展开/收起功能
 * 处理列表页中 Thoughts 卡片的展开、收起交互
 */

document.addEventListener('DOMContentLoaded', function() {
  // 移除 no-js 类，表示 JavaScript 已加载
  document.documentElement.classList.remove('no-js');
  document.documentElement.classList.add('js');
  
  // 初始化所有 Thoughts 卡片
  const thoughtCards = document.querySelectorAll('.thought-entry');
  
  thoughtCards.forEach(card => {
    const expandBtn = card.querySelector('.expand-btn');
    const collapseBtn = card.querySelector('.collapse-btn');
    const entryLink = card.querySelector('.entry-link');
    
    // 如果没有展开按钮，说明内容未溢出，无需交互
    if (!expandBtn) return;
    
    // 展开逻辑
    expandBtn.addEventListener('click', function(e) {
      e.stopPropagation(); // 阻止事件冒泡到 entry-link
      e.preventDefault();
      
      card.classList.add('expanded');
      expandBtn.setAttribute('aria-expanded', 'true');
      
      // 懒加载图片
      lazyLoadImages(card);
      
      // 保持卡片顶部在视口内
      setTimeout(() => scrollToCard(card), 50);
    });
    
    // 收起逻辑
    if (collapseBtn) {
      collapseBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        e.preventDefault();
        
        card.classList.remove('expanded');
        expandBtn.setAttribute('aria-expanded', 'false');
        
        // 停止所有多媒体播放
        stopMedia(card);
        
        // 保持卡片顶部在视口内
        setTimeout(() => scrollToCard(card), 50);
      });
    }
    
    // 键盘支持
    [expandBtn, collapseBtn].forEach(btn => {
      if (!btn) return;
      
      btn.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          btn.click();
        }
      });
    });
    
    // 阻止「进入详情页」按钮触发整卡链接
    const detailLinkBtn = card.querySelector('.detail-link-btn');
    if (detailLinkBtn) {
      detailLinkBtn.addEventListener('click', function(e) {
        e.stopPropagation();
      });
    }
  });
  
  /**
   * 懒加载图片
   * 在展开时加载完整内容中的图片
   */
  function lazyLoadImages(card) {
    const images = card.querySelectorAll('.content-full img[data-src]');
    images.forEach(img => {
      if (img.dataset.src) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
      }
    });
  }
  
  /**
   * 停止多媒体播放
   * 在收起时停止所有音视频播放
   */
  function stopMedia(card) {
    const videos = card.querySelectorAll('.content-full video');
    const audios = card.querySelectorAll('.content-full audio');
    
    videos.forEach(v => {
      v.pause();
      v.currentTime = 0;
    });
    
    audios.forEach(a => {
      a.pause();
      a.currentTime = 0;
    });
  }
  
  /**
   * 滚动到卡片顶部
   * 如果卡片顶部不在视口内，平滑滚动使其可见
   */
  function scrollToCard(card) {
    const rect = card.getBoundingClientRect();
    const headerHeight = 60; // 预留顶部导航栏高度
    
    // 如果卡片顶部在视口上方，滚动使其可见
    if (rect.top < headerHeight) {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const targetScroll = scrollTop + rect.top - headerHeight - 20;
      
      window.scrollTo({
        top: targetScroll,
        behavior: 'smooth'
      });
    }
  }
  
  /**
   * 使用 IntersectionObserver 优化图片懒加载
   * 只在卡片即将进入视口时才加载图片
   */
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            observer.unobserve(img);
          }
        }
      });
    }, {
      rootMargin: '50px' // 提前 50px 开始加载
    });
    
    // 观察所有带 data-src 的图片
    document.querySelectorAll('.thought-entry .content-full img[data-src]').forEach(img => {
      imageObserver.observe(img);
    });
  }
});

