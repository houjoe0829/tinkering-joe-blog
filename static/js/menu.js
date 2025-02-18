document.addEventListener('DOMContentLoaded', function() {
    // 点击事件监听器
    document.addEventListener('click', function(event) {
        // 获取所有激活的菜单项
        const activeMenuItems = document.querySelectorAll('#menu li.active');
        
        // 遍历所有激活的菜单项
        activeMenuItems.forEach(function(menuItem) {
            // 检查点击是否在菜单项之外
            if (!menuItem.contains(event.target)) {
                // 移除激活状态
                menuItem.classList.remove('active');
            }
        });
    });
}); 