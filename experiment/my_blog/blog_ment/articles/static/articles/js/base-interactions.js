/**
 * Base.html 专用交互脚本
 * 处理搜索弹窗和基础交互功能
 */

class BaseInteractions {
    constructor() {
        this.searchModal = document.getElementById('fullscreen-search');
        this.searchInput = document.querySelector('.search-input');
        this.searchForm = document.getElementById('fullscreen-search-form');
        this.closeBtn = document.getElementById('close-search');
        this.suggestionTags = document.querySelectorAll('.search-suggestion-tag');
        
        this.isSearchOpen = false;
        this.searchHistory = JSON.parse(localStorage.getItem('searchHistory') || '[]');
        
        this.init();
    }
    
    init() {
        this.setupSearchModal();
        this.setupKeyboardShortcuts();
        this.setupSearchSuggestions();
        this.setupAccessibility();
        this.setupErrorHandling();
    }
    
    /**
     * 搜索弹窗设置
     */
    setupSearchModal() {
        // 打开搜索弹窗
        window.openSearchModal = () => {
            this.openSearchModal();
        };
        
        // 关闭搜索弹窗
        window.closeSearchModal = () => {
            this.closeSearchModal();
        };
        
        // 搜索建议点击
        window.searchSuggestion = (query) => {
            this.performSearch(query);
        };
        
        // 关闭按钮事件
        if (this.closeBtn) {
            this.closeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.closeSearchModal();
            });
        }
        
        // 点击外部关闭
        if (this.searchModal) {
            this.searchModal.addEventListener('click', (e) => {
                if (e.target === this.searchModal) {
                    this.closeSearchModal();
                }
            });
        }
        
        // 搜索表单提交
        if (this.searchForm) {
            this.searchForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const query = this.searchInput.value.trim();
                if (query) {
                    this.performSearch(query);
                }
            });
        }
    }
    
    /**
     * 打开搜索弹窗
     */
    openSearchModal() {
        if (!this.searchModal) return;
        
        this.searchModal.style.display = 'flex';
        this.searchModal.setAttribute('aria-hidden', 'false');
        this.isSearchOpen = true;
        
        // 添加显示动画
        setTimeout(() => {
            this.searchModal.classList.add('show');
        }, 10);
        
        // 聚焦到搜索输入框
        setTimeout(() => {
            if (this.searchInput) {
                this.searchInput.focus();
                this.searchInput.select();
            }
        }, 100);
        
        // 阻止背景滚动
        document.body.style.overflow = 'hidden';
        
        // 触发自定义事件
        this.dispatchEvent('searchModalOpened');
    }
    
    /**
     * 关闭搜索弹窗
     */
    closeSearchModal() {
        if (!this.searchModal) return;
        
        this.searchModal.classList.remove('show');
        
        setTimeout(() => {
            this.searchModal.style.display = 'none';
            this.searchModal.setAttribute('aria-hidden', 'true');
            this.isSearchOpen = false;
            
            // 恢复背景滚动
            document.body.style.overflow = '';
            
            // 清空搜索输入
            if (this.searchInput) {
                this.searchInput.value = '';
            }
        }, 300);
        
        // 触发自定义事件
        this.dispatchEvent('searchModalClosed');
    }
    
    /**
     * 执行搜索
     */
    performSearch(query) {
        if (!query || !query.trim()) {
            this.showNotification('请输入搜索关键词', 'warning');
            return;
        }
        
        // 保存搜索历史
        this.saveSearchHistory(query);
        
        // 显示搜索中提示
        this.showNotification(`正在搜索: ${query}`, 'info');
        
        // 提交搜索表单
        if (this.searchForm) {
            const input = this.searchForm.querySelector('input[name="q"]');
            if (input) {
                input.value = query;
            }
            this.searchForm.submit();
        }
    }
    
    /**
     * 保存搜索历史
     */
    saveSearchHistory(query) {
        // 移除重复项
        this.searchHistory = this.searchHistory.filter(item => item !== query);
        
        // 添加到开头
        this.searchHistory.unshift(query);
        
        // 限制历史记录数量
        if (this.searchHistory.length > 10) {
            this.searchHistory = this.searchHistory.slice(0, 10);
        }
        
        // 保存到本地存储
        localStorage.setItem('searchHistory', JSON.stringify(this.searchHistory));
    }
    
    /**
     * 键盘快捷键设置
     */
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl+K 或 Cmd+K 打开搜索
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                this.openSearchModal();
            }
            
            // ESC 关闭搜索
            if (e.key === 'Escape' && this.isSearchOpen) {
                e.preventDefault();
                this.closeSearchModal();
            }
            
            // 在搜索弹窗中的键盘导航
            if (this.isSearchOpen) {
                this.handleSearchKeyboardNavigation(e);
            }
        });
    }
    
    /**
     * 搜索弹窗键盘导航
     */
    handleSearchKeyboardNavigation(e) {
        const suggestionTags = Array.from(this.suggestionTags);
        const activeElement = document.activeElement;
        
        switch (e.key) {
            case 'ArrowDown':
                e.preventDefault();
                this.navigateSuggestions('down', suggestionTags, activeElement);
                break;
            case 'ArrowUp':
                e.preventDefault();
                this.navigateSuggestions('up', suggestionTags, activeElement);
                break;
            case 'Enter':
                if (activeElement.classList.contains('search-suggestion-tag')) {
                    e.preventDefault();
                    this.performSearch(activeElement.textContent);
                }
                break;
            case 'Tab':
                // 允许正常的Tab导航
                break;
            default:
                // 其他按键不做处理
                break;
        }
    }
    
    /**
     * 搜索建议导航
     */
    navigateSuggestions(direction, suggestions, currentElement) {
        let currentIndex = -1;
        
        if (currentElement.classList.contains('search-suggestion-tag')) {
            currentIndex = suggestions.indexOf(currentElement);
        }
        
        let nextIndex;
        if (direction === 'down') {
            nextIndex = currentIndex + 1 >= suggestions.length ? 0 : currentIndex + 1;
        } else {
            nextIndex = currentIndex - 1 < 0 ? suggestions.length - 1 : currentIndex - 1;
        }
        
        suggestions[nextIndex].focus();
    }
    
    /**
     * 搜索建议设置
     */
    setupSearchSuggestions() {
        this.suggestionTags.forEach(tag => {
            // 点击事件
            tag.addEventListener('click', (e) => {
                e.preventDefault();
                const query = tag.textContent.trim();
                this.performSearch(query);
            });
            
            // 键盘事件
            tag.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    const query = tag.textContent.trim();
                    this.performSearch(query);
                }
            });
            
            // 悬停效果
            tag.addEventListener('mouseenter', () => {
                tag.style.transform = 'translateY(-2px) scale(1.05)';
            });
            
            tag.addEventListener('mouseleave', () => {
                tag.style.transform = 'translateY(0) scale(1)';
            });
        });
    }
    
    /**
     * 无障碍支持
     */
    setupAccessibility() {
        // 为搜索建议添加ARIA标签
        this.suggestionTags.forEach((tag, index) => {
            tag.setAttribute('role', 'button');
            tag.setAttribute('tabindex', '0');
            tag.setAttribute('aria-label', `搜索建议: ${tag.textContent}`);
            tag.setAttribute('aria-describedby', 'search-suggestions-desc');
        });
        
        // 添加搜索建议描述
        if (!document.getElementById('search-suggestions-desc')) {
            const desc = document.createElement('div');
            desc.id = 'search-suggestions-desc';
            desc.className = 'sr-only';
            desc.textContent = '使用方向键浏览搜索建议，按Enter键选择';
            document.body.appendChild(desc);
        }
        
        // 焦点管理
        if (this.searchModal) {
            this.searchModal.addEventListener('focusin', (e) => {
                if (e.target.classList.contains('search-suggestion-tag')) {
                    e.target.classList.add('focus-visible');
                }
            });
            
            this.searchModal.addEventListener('focusout', (e) => {
                if (e.target.classList.contains('search-suggestion-tag')) {
                    e.target.classList.remove('focus-visible');
                }
            });
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
        
        // 搜索错误处理
        if (this.searchForm) {
            this.searchForm.addEventListener('error', (e) => {
                console.error('Search form error:', e);
                this.showNotification('搜索功能暂时不可用，请稍后重试', 'error');
            });
        }
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
    
    /**
     * 获取搜索历史
     */
    getSearchHistory() {
        return [...this.searchHistory];
    }
    
    /**
     * 清空搜索历史
     */
    clearSearchHistory() {
        this.searchHistory = [];
        localStorage.removeItem('searchHistory');
        this.showNotification('搜索历史已清空', 'success');
    }
    
    /**
     * 检查搜索功能是否可用
     */
    isSearchAvailable() {
        return !!(this.searchModal && this.searchInput && this.searchForm);
    }
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    window.baseInteractions = new BaseInteractions();
});

// 导出类供其他脚本使用
window.BaseInteractions = BaseInteractions; 