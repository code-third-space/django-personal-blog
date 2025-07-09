/**
 * Base.html 专用交互脚本
 * 处理基础交互功能（搜索功能已移至search.js）
 * 版本: 1.0.0
 * 作者: Blog System
 */

(function(window, document) {
    'use strict';
    
    // 事件类型常量
    const EVENT_TYPES = {
        KEYDOWN: 'keydown',
        ERROR: 'error',
        DOM_CONTENT_LOADED: 'DOMContentLoaded',
        CUSTOM_EVENT: 'CustomEvent'
    };
    
    // 通知类型常量
    const NOTIFICATION_TYPES = {
        INFO: 'info',
        SUCCESS: 'success',
        WARNING: 'warning',
        ERROR: 'error'
    };
    
    // 通知颜色配置
    const NOTIFICATION_COLORS = {
        [NOTIFICATION_TYPES.INFO]: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        [NOTIFICATION_TYPES.SUCCESS]: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        [NOTIFICATION_TYPES.WARNING]: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        [NOTIFICATION_TYPES.ERROR]: 'linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%)'
    };
    
    // 数值配置
    const CONFIG = {
        NOTIFICATION_DURATION: 4000,
        ANIMATION_DELAY: 100,
        ANIMATION_DURATION: 300,
        Z_INDEX: 10000
    };
    
    /**
     * 基础交互类
     */
    class BaseInteractions {
        constructor() {
            this.isInitialized = false;
            this.errorHandler = null;
            this.activeNotifications = new Set();
            
            // 防止重复初始化
            if (window.baseInteractions) {
                console.warn('BaseInteractions 已经初始化');
                return window.baseInteractions;
            }
            
            this.init();
        }
        
        /**
         * 初始化系统
         */
        init() {
            if (this.isInitialized) {
                return;
            }
            
            try {
                this.setupKeyboardShortcuts();
                this.setupAccessibility();
                this.setupErrorHandling();
                this.isInitialized = true;
                
                // 发送初始化完成事件
                this.dispatchEvent('base-interactions-initialized');
            } catch (error) {
                console.error('BaseInteractions 初始化失败:', error);
                this.handleError(error);
            }
        }
        
        /**
         * 键盘快捷键设置
         */
        setupKeyboardShortcuts() {
            if (!document || !document.addEventListener) {
                console.warn('文档对象不可用，跳过键盘快捷键设置');
                return;
            }
            
            document.addEventListener(EVENT_TYPES.KEYDOWN, this.handleKeydown.bind(this));
        }
        
        /**
         * 处理键盘事件
         */
        handleKeydown(event) {
            if (!event) return;
            
            try {
                // Ctrl+K 或 Cmd+K 打开搜索
                if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
                    event.preventDefault();
                    this.openSearchModal();
                }
                
                // ESC 关闭模态框
                if (event.key === 'Escape') {
                    this.closeModals();
                }
            } catch (error) {
                console.error('键盘事件处理失败:', error);
            }
        }
        
        /**
         * 打开搜索模态框
         */
        openSearchModal() {
            if (typeof window.openSearchModal === 'function') {
                window.openSearchModal();
            } else {
                console.warn('搜索功能不可用，请确保 search.js 已加载');
            }
        }
        
        /**
         * 关闭所有模态框
         */
        closeModals() {
            const modals = document.querySelectorAll('.modal, .overlay, .fullscreen-search-overlay');
            modals.forEach(modal => {
                if (modal.style.display !== 'none') {
                    modal.style.display = 'none';
                }
            });
        }
        
        /**
         * 无障碍支持设置
         */
        setupAccessibility() {
            if (!document || !document.getElementById) {
                console.warn('文档对象不可用，跳过无障碍设置');
                return;
            }
            
            // 添加搜索建议描述
            if (!document.getElementById('search-suggestions-desc')) {
                const desc = document.createElement('div');
                desc.id = 'search-suggestions-desc';
                desc.className = 'sr-only';
                desc.textContent = '使用方向键浏览搜索建议，按Enter键选择';
                desc.setAttribute('aria-live', 'polite');
                document.body.appendChild(desc);
            }
            
            // 添加跳过链接
            this.addSkipLink();
        }
        
        /**
         * 添加跳过链接
         */
        addSkipLink() {
            if (document.getElementById('skip-link')) return;
            
            const skipLink = document.createElement('a');
            skipLink.id = 'skip-link';
            skipLink.href = '#main-content';
            skipLink.textContent = '跳过到主内容';
            skipLink.className = 'sr-only';
            skipLink.style.cssText = `
                position: absolute;
                top: -40px;
                left: 6px;
                background: #000;
                color: #fff;
                padding: 8px;
                text-decoration: none;
                z-index: 100000;
                transition: top 0.3s;
            `;
            
            skipLink.addEventListener('focus', () => {
                skipLink.style.top = '0';
            });
            
            skipLink.addEventListener('blur', () => {
                skipLink.style.top = '-40px';
            });
            
            document.body.insertBefore(skipLink, document.body.firstChild);
        }
        
        /**
         * 错误处理设置
         */
        setupErrorHandling() {
            if (!window || !window.addEventListener) {
                console.warn('窗口对象不可用，跳过错误处理设置');
                return;
            }
            
            this.errorHandler = this.handleError.bind(this);
            window.addEventListener(EVENT_TYPES.ERROR, this.errorHandler);
            
            // 捕获未处理的Promise拒绝
            window.addEventListener('unhandledrejection', (event) => {
                console.error('Unhandled Promise rejection:', event.reason);
                this.handleError(new Error('出现了一个未处理的错误'));
            });
        }
        
        /**
         * 错误处理
         */
        handleError(error) {
            const errorMessage = error instanceof Error ? error.message : '发生了一个未知错误';
            console.error('Base interactions error:', error);
            
            // 显示错误通知
            this.showNotification('发生了一个错误，请刷新页面重试', NOTIFICATION_TYPES.ERROR);
            
            // 发送错误事件
            this.dispatchEvent('base-interactions-error', { error: errorMessage });
        }
        
        /**
         * 显示通知
         */
        showNotification(message, type = NOTIFICATION_TYPES.INFO) {
            if (!message || typeof message !== 'string') {
                console.warn('无效的通知消息');
                return;
            }
            
            const notification = this.createNotification(message, type);
            this.activeNotifications.add(notification);
            
            document.body.appendChild(notification);
            
            // 显示动画
            setTimeout(() => {
                notification.style.transform = 'translateX(0)';
            }, CONFIG.ANIMATION_DELAY);
            
            // 自动隐藏
            setTimeout(() => {
                this.hideNotification(notification);
            }, CONFIG.NOTIFICATION_DURATION);
            
            return notification;
        }
        
        /**
         * 创建通知元素
         */
        createNotification(message, type) {
            const notification = document.createElement('div');
            notification.className = `base-notification base-notification-${type}`;
            notification.textContent = message;
            notification.setAttribute('role', 'alert');
            notification.setAttribute('aria-live', 'assertive');
            
            // 设置样式
            notification.style.cssText = `
                position: fixed;
                top: 100px;
                right: 20px;
                padding: 12px 20px;
                border-radius: 8px;
                color: white;
                font-weight: 500;
                z-index: ${CONFIG.Z_INDEX};
                transform: translateX(100%);
                transition: transform 0.3s ease;
                font-size: 14px;
                max-width: 300px;
                word-wrap: break-word;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                background: ${NOTIFICATION_COLORS[type] || NOTIFICATION_COLORS[NOTIFICATION_TYPES.INFO]};
            `;
            
            // 添加关闭按钮
            const closeBtn = document.createElement('button');
            closeBtn.innerHTML = '&times;';
            closeBtn.style.cssText = `
                position: absolute;
                top: 4px;
                right: 8px;
                background: none;
                border: none;
                color: white;
                font-size: 18px;
                cursor: pointer;
                line-height: 1;
                padding: 0;
                width: 20px;
                height: 20px;
            `;
            
            closeBtn.addEventListener('click', () => {
                this.hideNotification(notification);
            });
            
            notification.appendChild(closeBtn);
            
            return notification;
        }
        
        /**
         * 隐藏通知
         */
        hideNotification(notification) {
            if (!notification || !document.body.contains(notification)) {
                return;
            }
            
            notification.style.transform = 'translateX(100%)';
            
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
                this.activeNotifications.delete(notification);
            }, CONFIG.ANIMATION_DURATION);
        }
        
        /**
         * 触发自定义事件
         */
        dispatchEvent(eventName, detail = {}) {
            if (!eventName || typeof eventName !== 'string') {
                console.warn('无效的事件名称');
                return;
            }
            
            try {
                const event = new CustomEvent(eventName, {
                    detail: { 
                        ...detail, 
                        timestamp: Date.now(),
                        source: 'BaseInteractions'
                    },
                    bubbles: true,
                    cancelable: true
                });
                
                document.dispatchEvent(event);
            } catch (error) {
                console.error('事件分发失败:', error);
            }
        }
        
        /**
         * 销毁方法
         */
        destroy() {
            if (!this.isInitialized) {
                return;
            }
            
            // 移除事件监听器
            if (this.errorHandler) {
                window.removeEventListener(EVENT_TYPES.ERROR, this.errorHandler);
            }
            
            // 清理活动通知
            this.activeNotifications.forEach(notification => {
                this.hideNotification(notification);
            });
            
            this.isInitialized = false;
            this.dispatchEvent('base-interactions-destroyed');
        }
    }
    
    // 防止在不支持的环境中运行
    if (typeof window === 'undefined' || typeof document === 'undefined') {
        console.warn('BaseInteractions 需要浏览器环境');
        return;
    }
    
    // 页面加载完成后初始化
    function initializeWhenReady() {
        if (document.readyState === 'loading') {
            document.addEventListener(EVENT_TYPES.DOM_CONTENT_LOADED, () => {
                window.baseInteractions = new BaseInteractions();
            });
        } else {
            // 文档已经加载完成
            window.baseInteractions = new BaseInteractions();
        }
    }
    
    // 导出类供其他脚本使用
    window.BaseInteractions = BaseInteractions;
    
    // 初始化
    initializeWhenReady();
    
})(window, document); 