document.addEventListener('DOMContentLoaded', function() {
    // 获取所有有子菜单的菜单项
    const menuItemsWithChildren = document.querySelectorAll('#menu li a:not([href])');
    
    // 为每个有子菜单的菜单项添加点击事件
    menuItemsWithChildren.forEach(function(menuItem) {
        menuItem.addEventListener('click', function(event) {
            event.preventDefault();
            
            // 获取父级li元素
            const parentLi = this.parentElement;
            
            // 切换激活状态
            if (parentLi.classList.contains('active')) {
                parentLi.classList.remove('active');
            } else {
                // 先移除其他菜单项的激活状态
                document.querySelectorAll('#menu li.active').forEach(function(item) {
                    if (item !== parentLi) {
                        item.classList.remove('active');
                    }
                });
                
                // 添加当前菜单项的激活状态
                parentLi.classList.add('active');
            }
        });
    });
    
    // 点击事件监听器，处理点击菜单项外部时关闭菜单
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