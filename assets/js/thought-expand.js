/**
 * Thoughts 卡片展开/收起功能
 * 处理列表页中 Thoughts 卡片的展开、收起交互
 */

document.addEventListener('DOMContentLoaded', function() {
  // 移除 no-js 类，表示 JavaScript 已加载
  document.documentElement.classList.remove('no-js');
  document.documentElement.classList.add('js');

  const postsContainer = document.querySelector('.posts');
  if (!postsContainer) return;

  /**
   * 使用事件委托处理展开按钮点击
   * 允许后续加载的卡片自动具备交互能力
   */
  postsContainer.addEventListener('click', function(event) {
    const detailLink = event.target.closest('.thought-entry .detail-link-btn');
    if (detailLink) {
      event.stopPropagation();
      return;
    }

    const expandBtn = event.target.closest('.thought-entry .expand-btn');
    if (!expandBtn || expandBtn.classList.contains('detail-link-btn')) return;

    const card = expandBtn.closest('.thought-entry');
    if (!card) return;

    event.preventDefault();
    event.stopPropagation();

    if (card.classList.contains('expanded')) return;

    card.classList.add('expanded');
    expandBtn.setAttribute('aria-expanded', 'true');

    // 懒加载图片
    lazyLoadImages(card);

    // 保持卡片顶部在视口内
    setTimeout(() => scrollToCard(card), 50);
  });

  /**
   * 键盘支持：回车 / 空格触发展开
   */
  postsContainer.addEventListener('keydown', function(event) {
    const expandBtn = event.target.closest('.thought-entry .expand-btn');
    if (!expandBtn || expandBtn.classList.contains('detail-link-btn')) return;

    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      expandBtn.click();
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
    
    const observeImages = (root) => {
      root.querySelectorAll('.content-full img[data-src]').forEach(img => {
        imageObserver.observe(img);
      });
    };

    // 初始观察已有图片
    observeImages(postsContainer);

    // 监听后续加载的卡片
    const mutationObserver = new MutationObserver((mutations) => {
      mutations.forEach(mutation => {
        mutation.addedNodes.forEach(node => {
          if (node.nodeType !== Node.ELEMENT_NODE) return;
          if (node.classList && node.classList.contains('thought-entry')) {
            observeImages(node);
          }
        });
      });
    });

    mutationObserver.observe(postsContainer, { childList: true });
  }
});
