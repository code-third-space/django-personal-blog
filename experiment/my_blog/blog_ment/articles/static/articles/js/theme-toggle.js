// theme-toggle.js
// 模块化主题切换系统，支持本地存储记忆

class ThemeToggle {
    constructor() {
        this.currentTheme = localStorage.getItem('theme') || 'light';
        this.themeButtons = [];
        this.init();
    }

    init() {
        // 初始化主题
        this.applyTheme(this.currentTheme);
        
        // 查找所有主题切换按钮（桌面端和移动端）
        this.themeButtons = document.querySelectorAll('.btn-toggle-theme');
        
        // 如果没有找到带有特定类的按钮，尝试查找所有包含主题切换图标的按钮
        if (this.themeButtons.length === 0) {
            const allButtons = document.querySelectorAll('.action-btn, .mobile-action-btn');
            this.themeButtons = Array.from(allButtons).filter(btn => {
                const icon = btn.querySelector('i');
                return icon && (icon.classList.contains('bi-brightness-high') || 
                               icon.classList.contains('bi-moon-stars') || 
                               icon.classList.contains('bi-moon'));
            });
        }
        
        console.log('找到主题切换按钮:', this.themeButtons.length);
        
        // 为每个按钮添加事件监听器
        this.themeButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggle();
            });
        });
        
        // 暴露到全局，供其他模块使用
        window.ThemeToggle = this;
    }

    toggle() {
        console.log('主题切换触发，当前主题:', this.currentTheme);
        
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        this.applyTheme(this.currentTheme);
        localStorage.setItem('theme', this.currentTheme);
        
        console.log('主题切换完成，新主题:', this.currentTheme);
        
        // 使用安全的通知系统
        this.showNotification(`已切换到${this.currentTheme === 'light' ? '浅色' : '深色'}主题`);
    }

    applyTheme(theme) {
        document.body.setAttribute('data-theme', theme);
        
        // 更新按钮图标
        this.updateButtonIcons(theme);
    }

    updateButtonIcons(theme) {
        try {
            // 重新获取按钮以确保包含动态添加的按钮
            const allThemeButtons = document.querySelectorAll('.btn-toggle-theme');
            const additionalButtons = document.querySelectorAll('.action-btn, .mobile-action-btn');
            
            // 合并所有可能的主题切换按钮
            const buttonsToUpdate = new Set([...allThemeButtons]);
            
            additionalButtons.forEach(btn => {
                const icon = btn.querySelector('i');
                if (icon && (icon.classList.contains('bi-brightness-high') || 
                           icon.classList.contains('bi-moon-stars') || 
                           icon.classList.contains('bi-moon'))) {
                    buttonsToUpdate.add(btn);
                }
            });
            
            console.log('更新按钮图标，找到按钮数量:', buttonsToUpdate.size);
            
            buttonsToUpdate.forEach(button => {
                const icon = button.querySelector('i');
                if (icon) {
                    // 清除所有可能的主题图标类
                    icon.classList.remove('bi-brightness-high', 'bi-moon-stars', 'bi-moon');
                    
                    // 根据主题设置正确的图标
                    if (theme === 'light') {
                        icon.classList.add('bi-moon-stars');
                    } else {
                        icon.classList.add('bi-brightness-high');
                    }
                }
            });
        } catch (error) {
            console.warn('Icon update failed:', error);
        }
    }

    showNotification(message) {
        // 优先使用 BaseInteractions 通知系统
        if (window.baseInteractions && typeof window.baseInteractions.showNotification === 'function') {
            window.baseInteractions.showNotification(message, 'info');
            return;
        }
        
        // 备用通知系统
        this.createSimpleNotification(message);
    }
    
    createSimpleNotification(message) {
        // 创建通知元素
        const notification = document.createElement('div');
        notification.className = 'theme-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            z-index: 9999;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            font-size: 14px;
            font-weight: 500;
            max-width: 300px;
            word-wrap: break-word;
        `;
        
        try {
            document.body.appendChild(notification);
            
            // 显示动画
            setTimeout(() => {
                notification.style.transform = 'translateX(0)';
            }, 100);
            
            // 自动隐藏
            setTimeout(() => {
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    if (document.body.contains(notification)) {
                        document.body.removeChild(notification);
                    }
                }, 300);
            }, 3000);
        } catch (error) {
            console.warn('通知创建失败:', error);
        }
    }

    // 供其他模块调用的方法
    getCurrentTheme() {
        return this.currentTheme;
    }

    setTheme(theme) {
        if (theme === 'light' || theme === 'dark') {
            this.currentTheme = theme;
            this.applyTheme(theme);
            localStorage.setItem('theme', theme);
        }
    }
}

// 初始化主题切换系统
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM加载完成，开始初始化主题切换系统');
    
    // 延迟初始化以确保所有元素都已加载
    setTimeout(() => {
        const themeToggle = new ThemeToggle();
        console.log('主题切换系统初始化完成');
        
        // 添加全局测试函数
        window.testThemeToggle = function() {
            console.log('测试主题切换功能');
            themeToggle.toggle();
        };
        
        window.getCurrentTheme = function() {
            return themeToggle.getCurrentTheme();
        };
    }, 100);
}); 