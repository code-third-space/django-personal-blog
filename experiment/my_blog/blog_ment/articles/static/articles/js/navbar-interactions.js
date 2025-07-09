/*
 * 现代化导航栏交互脚本
 * 提供丰富的用户体验和交互功能
 */

class ModernNavbar {
    constructor() {
        this.navbar = document.querySelector('.navbar-modern');
        this.navbarCollapse = document.querySelector('.navbar-collapse');
        this.navLinks = document.querySelectorAll('.nav-link-modern');
        this.actionBtns = document.querySelectorAll('.action-btn');
        this.mobileActionBtns = document.querySelectorAll('.mobile-action-btn');
        this.isScrolled = false;
        
        this.init();
    }
    
    init() {
        this.setupScrollEffect();
        this.setupMobileMenu();
        this.setupActionButtons();
        this.setupAccessibility();
        this.setupVoiceControl();
        this.setupSearchEnhancement();
        this.setupKeyboardNavigation();
    }
    
    /**
     * 滚动效果设置
     */
    setupScrollEffect() {
        let scrollTimeout;
        
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            
            scrollTimeout = setTimeout(() => {
                const scrollY = window.scrollY;
                
                if (scrollY > 50 && !this.isScrolled) {
                    this.navbar.classList.add('scrolled');
                    this.isScrolled = true;
                } else if (scrollY <= 50 && this.isScrolled) {
                    this.navbar.classList.remove('scrolled');
                    this.isScrolled = false;
                }
            }, 10);
        });
    }
    
    /**
     * 移动端菜单优化
     */
    setupMobileMenu() {
        // 点击导航链接关闭菜单
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                if (window.innerWidth < 992) {
                    setTimeout(() => {
                        const bsCollapse = new bootstrap.Collapse(this.navbarCollapse);
                        bsCollapse.hide();
                    }, 100);
                }
            });
        });
        
        // 点击外部关闭菜单
        document.addEventListener('click', (e) => {
            if (!this.navbar.contains(e.target) && this.navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(this.navbarCollapse);
                bsCollapse.hide();
            }
        });
        
        // 窗口大小改变时处理
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 992 && this.navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(this.navbarCollapse);
                bsCollapse.hide();
            }
        });
    }

    /**
     * 功能按钮设置
     */
    setupActionButtons() {
        // 搜索按钮事件处理已移至search.js，避免重复绑定
        
        // 主题切换按钮事件已移至theme-toggle.js处理，避免重复绑定
        
        // 语音播报按钮
        const voiceBtns = document.querySelectorAll('.action-btn, .mobile-action-btn');
        voiceBtns.forEach(btn => {
            if (btn.querySelector('.bi-volume-up') || btn.querySelector('.bi-volume-mute')) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.toggleVoiceControl();
                });
            }
        });
        
        // RSS订阅按钮
        const rssBtns = document.querySelectorAll('.action-btn, .mobile-action-btn');
        rssBtns.forEach(btn => {
            if (btn.querySelector('.bi-rss')) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.openRSSFeed();
                });
            }
        });
    }
    
    /**
     * 无障碍支持
     */
    setupAccessibility() {
        // 键盘导航支持
        this.navLinks.forEach(link => {
            link.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    link.click();
                }
            });
        });
        
        // 焦点管理
        this.navbar.addEventListener('focusin', (e) => {
            if (e.target.classList.contains('nav-link-modern')) {
                e.target.classList.add('focus-visible');
            }
        });
        
        this.navbar.addEventListener('focusout', (e) => {
            if (e.target.classList.contains('nav-link-modern')) {
                e.target.classList.remove('focus-visible');
            }
        });
        
        // 屏幕阅读器支持
        this.navLinks.forEach(link => {
            const text = link.textContent.trim();
            link.setAttribute('aria-label', `导航到${text}页面`);
        });
    }
    
    /**
     * 语音播报功能
     */
    setupVoiceControl() {
        this.isVoiceEnabled = false;
        this.speechSynthesis = window.speechSynthesis;
    }
    
    toggleVoiceControl() {
        if (!this.speechSynthesis) {
            this.showNotification('您的浏览器不支持语音播报功能');
            return;
        }
        
        this.isVoiceEnabled = !this.isVoiceEnabled;
        
        if (this.isVoiceEnabled) {
            this.speechSynthesis.cancel();
            this.speak('语音播报已启用');
            this.showNotification('语音播报已启用');
        } else {
            this.speechSynthesis.cancel();
            this.showNotification('语音播报已关闭');
        }
        
        // 更新按钮状态
        const voiceBtns = document.querySelectorAll('.bi-volume-up');
        voiceBtns.forEach(btn => {
            btn.className = this.isVoiceEnabled ? 'bi bi-volume-mute' : 'bi bi-volume-up';
        });
    }
    
    speak(text) {
        if (!this.isVoiceEnabled) return;
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'zh-CN';
        utterance.rate = 0.9;
        utterance.pitch = 1;
        this.speechSynthesis.speak(utterance);
    }
    
    /**
     * 搜索功能增强
     */
    setupSearchEnhancement() {
        // 搜索功能已完全移至search.js处理
        // 此处保留空方法以维持向后兼容性
    }
    
    /**
     * 键盘导航
     */
    setupKeyboardNavigation() {
        document.addEventListener('keydown', (e) => {
            // 方向键导航
            if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                const activeElement = document.activeElement;
                if (activeElement.classList.contains('nav-link-modern')) {
                    e.preventDefault();
                    this.navigateWithArrowKeys(e.key, activeElement);
                }
            }
        });
    }
    
    navigateWithArrowKeys(direction, currentElement) {
        const navLinks = Array.from(this.navLinks);
        const currentIndex = navLinks.indexOf(currentElement);
        let nextIndex;
        
        if (direction === 'ArrowRight') {
            nextIndex = currentIndex + 1 >= navLinks.length ? 0 : currentIndex + 1;
        } else {
            nextIndex = currentIndex - 1 < 0 ? navLinks.length - 1 : currentIndex - 1;
        }
        
        navLinks[nextIndex].focus();
    }
    
    /**
     * RSS订阅
     */
    openRSSFeed() {
        const rssUrl = '/rss/';
        window.open(rssUrl, '_blank');
        this.showNotification('正在打开RSS订阅页面');
    }
    
    /**
     * 关闭搜索模态框
     */
    closeSearchModal() {
        // 搜索功能已移至 search.js
        if (typeof window.closeSearchModal === 'function') {
            window.closeSearchModal();
        }
    }
    
    /**
     * 显示通知
     */
    showNotification(message) {
        // 创建通知元素
        const notification = document.createElement('div');
        notification.className = 'navbar-notification';
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
        `;
        
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
}

// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.modernNavbar = new ModernNavbar();
    });
} else {
    window.modernNavbar = new ModernNavbar();
} 