// 当前已加载的文章数量
let loadedPosts = 0;
const postsPerPage = 10;  // 每次加载10篇，与初始加载保持一致
const initialPosts = 10; // 初始显示10篇
let totalPosts = 0;
let isLoading = false; // 是否正在加载中
let currentPage = 2; // 从第2页开始加载，因为第1页是初始的10篇
let currentPath = window.location.pathname; // 获取当前页面路径

// 初始化加载更多功能
function initLoadMore() {
    const loadMoreBtn = document.getElementById('load-more');
    if (!loadMoreBtn) return;

    // 获取总文章数
    totalPosts = parseInt(loadMoreBtn.getAttribute('data-total-posts'));
    // 初始已加载的文章数量就是10篇
    loadedPosts = initialPosts;

    // 如果总文章数小于等于初始显示数量，直接显示加载完成
    if (loadedPosts >= totalPosts) {
        showCompletionMessage();
        return;
    }

    // 添加点击事件
    loadMoreBtn.addEventListener('click', loadMorePosts);
}

// 显示加载完成提示
function showCompletionMessage() {
    const loadMoreContainer = document.getElementById('load-more-container');
    if (!loadMoreContainer) return;
    loadMoreContainer.innerHTML = `<p class="no-more">☕️ 你已成功解锁全部 ${totalPosts} 篇博文！</p>`;
}

// 设置加载状态
function setLoading(loading) {
    const loadMoreBtn = document.getElementById('load-more');
    if (!loadMoreBtn) return;
    
    isLoading = loading;
    if (loading) {
        loadMoreBtn.classList.add('loading');
        loadMoreBtn.disabled = true;
    } else {
        loadMoreBtn.classList.remove('loading');
        loadMoreBtn.disabled = false;
    }
}

// 加载更多文章
async function loadMorePosts() {
    if (isLoading || loadedPosts >= totalPosts) return;
    
    const loadMoreBtn = document.getElementById('load-more');
    if (!loadMoreBtn) return;

    setLoading(true);

    try {
        // 构建下一页的URL
        let nextPageUrl;
        if (currentPath.endsWith('/')) {
            currentPath = currentPath.slice(0, -1);
        }
        
        // 如果是在标签页面
        if (currentPath.includes('/tags/')) {
            nextPageUrl = `${currentPath}/page/${currentPage}/`;
        } else {
            nextPageUrl = `/page/${currentPage}/`;
        }

        const response = await fetch(nextPageUrl);
        
        // 如果返回404，说明已经没有更多页面了
        if (response.status === 404) {
            showCompletionMessage();
            return;
        }

        const text = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(text, 'text/html');
        
        // 获取新文章
        const newPosts = doc.querySelectorAll('.post-entry');
        
        // 如果没有找到新文章，说明已经到达末尾
        if (newPosts.length === 0) {
            showCompletionMessage();
            return;
        }

        const postsContainer = document.querySelector('.posts');
        
        // 添加新文章到容器中
        newPosts.forEach(post => {
            // 如果还没有达到总文章数，就继续添加
            if (loadedPosts < totalPosts) {
                postsContainer.appendChild(post.cloneNode(true));
                loadedPosts++;
            }
        });

        // 更新当前页码
        currentPage++;

        // 检查是否已加载全部文章
        if (loadedPosts >= totalPosts) {
            showCompletionMessage();
        }

    } catch (error) {
        console.error('Error loading more posts:', error);
        // 只有在404错误时才显示加载完成
        if (error.message.includes('404')) {
            showCompletionMessage();
        }
    } finally {
        // 只有在没有达到总文章数时才重置加载状态
        if (loadedPosts < totalPosts) {
            setLoading(false);
        }
    }
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', initLoadMore); 