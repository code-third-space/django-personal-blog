/**
 * Base.html 专用交互脚本
 * 处理基础交互功能（搜索功能已移至search.js）
 */

class BaseInteractions {
    constructor() {
        // 移除搜索相关的初始化，交由search.js处理
        this.init();
    }
    
    init() {
        this.setupKeyboardShortcuts();
        this.setupAccessibility();
        this.setupErrorHandling();
    }
    
    /**
     * 键盘快捷键设置
     */
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl+K 或 Cmd+K 打开搜索 - 调用search.js中的函数
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                if (typeof window.openSearchModal === 'function') {
                    window.openSearchModal();
                }
            }
        });
    }
    
    /**
     * 无障碍支持
     */
    setupAccessibility() {
        // 添加搜索建议描述
        if (!document.getElementById('search-suggestions-desc')) {
            const desc = document.createElement('div');
            desc.id = 'search-suggestions-desc';
            desc.className = 'sr-only';
            desc.textContent = '使用方向键浏览搜索建议，按Enter键选择';
            document.body.appendChild(desc);
        }
    }
    
    /**
     * 错误处理
     */
    setupErrorHandling() {
        // 全局错误处理
        window.addEventListener('error', (e) => {
            console.error('Base interactions error:', e.error);
            this.showNotification('发生了一个错误，请刷新页面重试', 'error');
        });
    }
    
    /**
     * 显示通知
     */
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `base-notification base-notification-${type}`;
        notification.textContent = message;
        
        // 设置样式
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            padding: 12px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 500;
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            font-size: 14px;
            max-width: 300px;
            word-wrap: break-word;
        `;
        
        // 根据类型设置颜色
        const colors = {
            info: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            success: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
            warning: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            error: 'linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%)'
        };
        
        notification.style.background = colors[type] || colors.info;
        notification.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
        
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
        }, 4000);
    }
    
    /**
     * 触发自定义事件
     */
    dispatchEvent(eventName, detail = {}) {
        const event = new CustomEvent(eventName, {
            detail: { ...detail, timestamp: Date.now() }
        });
        document.dispatchEvent(event);
    }
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    window.baseInteractions = new BaseInteractions();
});

// 导出类供其他脚本使用
window.BaseInteractions = BaseInteractions; 