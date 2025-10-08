// 当前已加载的文章数量
let loadedPosts = 0;
const postsPerPage = 10;  // 每次加载10篇，与初始加载保持一致
const initialPosts = 10; // 初始显示10篇
let totalPosts = 0;
let isLoading = false; // 是否正在加载中
let currentPage = 2; // 从第2页开始加载，因为第1页是初始的10篇
let currentPath = normalizePath(window.location.pathname); // 获取当前页面路径
let listType = 'mixed'; // 当前列表类型：posts | thoughts | mixed

// 初始化加载更多功能
function initLoadMore() {
    const loadMoreBtn = document.getElementById('load-more');
    if (!loadMoreBtn) return;

    determineListType();

    // 获取总文章数
    const totalPostsAttr = loadMoreBtn.getAttribute('data-total-posts');
    if (!totalPostsAttr) return;

    totalPosts = parseInt(totalPostsAttr, 10);
    if (Number.isNaN(totalPosts)) return;

    const postsContainer = document.querySelector('.posts');
    if (postsContainer) {
        loadedPosts = getEntriesByListType(postsContainer).length;
    } else {
        loadedPosts = initialPosts;
    }

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
    
    // 获取想法的数量
    const loadMoreBtn = document.getElementById('load-more');
    const totalThoughts = loadMoreBtn ? loadMoreBtn.getAttribute('data-total-thoughts') : null;

    let completionText = `☕️ 你已成功解锁全部 ${totalPosts} 篇博文，${totalThoughts || 0} 条想法！`;

    if (listType === 'thoughts') {
        completionText = `☕️ 你已成功解锁全部 ${totalPosts} 条想法！`;
    } else if (listType === 'posts') {
        completionText = `☕️ 你已成功解锁全部 ${totalPosts} 篇博文！`;
    } else if (totalThoughts === null) {
        completionText = `☕️ 你已成功解锁全部 ${totalPosts} 篇内容！`;
    }
    
    // 显示完成消息
    loadMoreContainer.innerHTML = `<p class="no-more">${completionText}</p>`;
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
        const nextPageUrl = buildNextPageUrl();

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
        const newPosts = getEntriesByListType(doc);
        
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

/**
 * 根据当前页面路径构建下一页链接
 */
function buildNextPageUrl() {
    if (!currentPath) {
        return `/page/${currentPage}/`;
    }
    return `${currentPath}/page/${currentPage}/`;
}

/**
 * 根据列表类型获取对应的文章节点
 */
function getEntriesByListType(root) {
    if (listType === 'thoughts') {
        return root.querySelectorAll('.thought-entry');
    }
    if (listType === 'posts') {
        return root.querySelectorAll('.post-entry:not(.thought-entry)');
    }
    return root.querySelectorAll('.post-entry');
}

/**
 * 去掉路径末尾的斜杠，根路径保持为空字符串
 */
function normalizePath(pathname) {
    if (!pathname || pathname === '/') return '';
    let normalized = pathname;
    if (normalized.endsWith('/')) {
        normalized = normalized.slice(0, -1);
    }
    normalized = normalized.replace(/\/page\/\d+$/, '');
    if (normalized === '') return '';
    return normalized;
}

/**
 * 判断当前列表类型
 */
function determineListType() {
    const postsContainer = document.querySelector('.posts');
    if (!postsContainer) return;

    const hasThoughts = postsContainer.querySelector('.thought-entry') !== null;
    const hasRegularPosts = postsContainer.querySelector('.post-entry:not(.thought-entry)') !== null;

    if (hasThoughts && !hasRegularPosts) {
        listType = 'thoughts';
    } else if (!hasThoughts && hasRegularPosts) {
        listType = 'posts';
    } else {
        listType = 'mixed';
    }
}
