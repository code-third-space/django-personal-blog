/**
 * 博客详情页交互脚本
 * 处理评论系统的交互功能
 * 版本: 1.0.0
 * 作者: Blog System
 */

(function(window, document) {
    'use strict';
    
    // 常量定义
    const SELECTORS = {
        REPLY_BUTTONS: '.reply-btn',
        CANCEL_BUTTONS: '.cancel-btn',
        REPLY_FORMS: '.reply-form-container',
        COMMENT_FORM: '#comment-form',
        COMMENT_LINKS: 'a[href="#comments"]',
        COMMENTS_SECTION: '#comments',
        COMMENTS: '.comment',
        TEXTAREA: 'textarea'
    };
    
    const CSS_CLASSES = {
        HIGHLIGHTED: 'highlighted',
        FADE_IN: 'fade-in',
        LOADING: 'loading',
        ERROR: 'error'
    };
    
    const ANIMATION_DELAY = 100;
    const SCROLL_BEHAVIOR = 'smooth';
    
    /**
     * 博客详情页交互类
     */
    class BlogDetailInteractions {
        constructor() {
            this.isInitialized = false;
            this.activeReplyForm = null;
            
            // 检查是否已经初始化
            if (window.blogDetailInteractions) {
                console.warn('BlogDetailInteractions 已经初始化');
                return window.blogDetailInteractions;
            }
            
            this.init();
        }
        
        /**
         * 初始化
         */
        init() {
            if (this.isInitialized) {
                return;
            }
            
            try {
                this.setupReplyButtons();
                this.setupCancelButtons();
                this.setupCommentLinks();
                this.setupFormValidation();
                this.setupCommentHighlighting();
                this.setupCommentAnimation();
                
                this.isInitialized = true;
                console.log('BlogDetailInteractions 初始化完成');
            } catch (error) {
                console.error('BlogDetailInteractions 初始化失败:', error);
            }
        }
        
        /**
         * 设置回复按钮事件
         */
        setupReplyButtons() {
            const replyButtons = document.querySelectorAll(SELECTORS.REPLY_BUTTONS);
            
            replyButtons.forEach(button => {
                button.addEventListener('click', this.handleReplyClick.bind(this));
            });
        }
        
        /**
         * 处理回复按钮点击
         */
        handleReplyClick(event) {
            event.preventDefault();
            
            const button = event.currentTarget;
            const commentId = button.dataset.commentId;
            
            if (!commentId) {
                console.warn('未找到评论 ID');
                return;
            }
            
            try {
                this.toggleReplyForm(commentId);
            } catch (error) {
                console.error('回复表单切换失败:', error);
            }
        }
        
        /**
         * 切换回复表单显示状态
         */
        toggleReplyForm(commentId) {
            const replyForm = document.getElementById(`reply-form-${commentId}`);
            
            if (!replyForm) {
                console.warn(`未找到回复表单: reply-form-${commentId}`);
                return;
            }
            
            // 隐藏其他所有回复表单
            this.hideAllReplyForms(commentId);
            
            // 切换当前表单的显示状态
            const isVisible = replyForm.style.display === 'block';
            replyForm.style.display = isVisible ? 'none' : 'block';
            
            if (!isVisible) {
                this.activeReplyForm = replyForm;
                this.focusReplyForm(replyForm);
            } else {
                this.activeReplyForm = null;
            }
        }
        
        /**
         * 隐藏所有回复表单
         */
        hideAllReplyForms(excludeId = null) {
            const replyForms = document.querySelectorAll(SELECTORS.REPLY_FORMS);
            
            replyForms.forEach(form => {
                if (!excludeId || form.id !== `reply-form-${excludeId}`) {
                    form.style.display = 'none';
                }
            });
            
            if (this.activeReplyForm && this.activeReplyForm.id !== `reply-form-${excludeId}`) {
                this.activeReplyForm = null;
            }
        }
        
        /**
         * 聚焦回复表单
         */
        focusReplyForm(replyForm) {
            const textarea = replyForm.querySelector(SELECTORS.TEXTAREA);
            
            if (textarea) {
                setTimeout(() => {
                    textarea.focus();
                    // 将光标移动到文本末尾
                    textarea.setSelectionRange(textarea.value.length, textarea.value.length);
                }, 100);
            }
        }
        
        /**
         * 设置取消按钮事件
         */
        setupCancelButtons() {
            const cancelButtons = document.querySelectorAll(SELECTORS.CANCEL_BUTTONS);
            
            cancelButtons.forEach(button => {
                button.addEventListener('click', this.handleCancelClick.bind(this));
            });
        }
        
        /**
         * 处理取消按钮点击
         */
        handleCancelClick(event) {
            event.preventDefault();
            
            const button = event.currentTarget;
            const commentId = button.dataset.commentId;
            
            if (!commentId) {
                console.warn('未找到评论 ID');
                return;
            }
            
            try {
                this.hideReplyForm(commentId);
            } catch (error) {
                console.error('隐藏回复表单失败:', error);
            }
        }
        
        /**
         * 隐藏指定的回复表单
         */
        hideReplyForm(commentId) {
            const replyForm = document.getElementById(`reply-form-${commentId}`);
            
            if (replyForm) {
                replyForm.style.display = 'none';
                
                if (this.activeReplyForm === replyForm) {
                    this.activeReplyForm = null;
                }
            }
        }
        
        /**
         * 设置评论链接事件
         */
        setupCommentLinks() {
            const commentLinks = document.querySelectorAll(SELECTORS.COMMENT_LINKS);
            
            commentLinks.forEach(link => {
                link.addEventListener('click', this.handleCommentLinkClick.bind(this));
            });
        }
        
        /**
         * 处理评论链接点击
         */
        handleCommentLinkClick(event) {
            event.preventDefault();
            
            const commentsSection = document.getElementById('comments');
            
            if (commentsSection) {
                this.scrollToElement(commentsSection);
            }
        }
        
        /**
         * 平滑滚动到指定元素
         */
        scrollToElement(element) {
            if (element && typeof element.scrollIntoView === 'function') {
                element.scrollIntoView({ 
                    behavior: SCROLL_BEHAVIOR,
                    block: 'start'
                });
            }
        }
        
        /**
         * 设置表单验证
         */
        setupFormValidation() {
            const commentForm = document.getElementById('comment-form');
            
            if (commentForm) {
                commentForm.addEventListener('submit', this.handleFormSubmit.bind(this));
            }
        }
        
        /**
         * 处理表单提交
         */
        handleFormSubmit(event) {
            const form = event.currentTarget;
            const textarea = form.querySelector(SELECTORS.TEXTAREA);
            
            if (!textarea) {
                console.warn('未找到文本区域');
                return;
            }
            
            const content = textarea.value.trim();
            
            if (!content) {
                event.preventDefault();
                this.showFormError(textarea, '评论内容不能为空！');
                return;
            }
            
            if (content.length > 1000) {
                event.preventDefault();
                this.showFormError(textarea, '评论内容不能超过 1000 个字符！');
                return;
            }
            
            // 显示提交动画
            this.showFormLoading(form);
        }
        
        /**
         * 显示表单错误
         */
        showFormError(textarea, message) {
            // 移除旧的错误信息
            const existingError = textarea.parentNode.querySelector('.error-message');
            if (existingError) {
                existingError.remove();
            }
            
            // 创建错误信息
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = message;
            errorDiv.style.cssText = `
                color: #dc3545;
                font-size: 14px;
                margin-top: 5px;
                padding: 8px;
                background: #f8d7da;
                border: 1px solid #f5c6cb;
                border-radius: 4px;
            `;
            
            textarea.parentNode.appendChild(errorDiv);
            textarea.focus();
            
            // 3秒后自动隐藏错误信息
            setTimeout(() => {
                if (errorDiv.parentNode) {
                    errorDiv.remove();
                }
            }, 3000);
        }
        
        /**
         * 显示表单加载状态
         */
        showFormLoading(form) {
            const submitButton = form.querySelector('button[type="submit"]');
            
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = '提交中...';
                submitButton.classList.add(CSS_CLASSES.LOADING);
            }
        }
        
        /**
         * 设置评论高亮功能
         */
        setupCommentHighlighting() {
            // 页面加载时执行高亮
            this.highlightCommentFromURL();
            
            // 监听 URL hash 变化
            window.addEventListener('hashchange', () => {
                this.highlightCommentFromURL();
            });
        }
        
        /**
         * 根据 URL 高亮评论
         */
        highlightCommentFromURL() {
            const hash = window.location.hash;
            
            if (!hash || !hash.startsWith('#comment-')) {
                return;
            }
            
            try {
                const commentId = hash.substring(9); // 去掉 '#comment-'
                const comment = document.getElementById(`comment-${commentId}`);
                
                if (comment) {
                    this.highlightComment(comment);
                }
            } catch (error) {
                console.error('评论高亮失败:', error);
            }
        }
        
        /**
         * 高亮指定评论
         */
        highlightComment(comment) {
            // 移除其他评论的高亮
            const highlightedComments = document.querySelectorAll(`.${CSS_CLASSES.HIGHLIGHTED}`);
            highlightedComments.forEach(c => {
                c.classList.remove(CSS_CLASSES.HIGHLIGHTED);
            });
            
            // 高亮当前评论
            comment.classList.add(CSS_CLASSES.HIGHLIGHTED);
            
            // 滚动到评论
            this.scrollToElement(comment);
            
            // 5秒后移除高亮
            setTimeout(() => {
                comment.classList.remove(CSS_CLASSES.HIGHLIGHTED);
            }, 5000);
        }
        
        /**
         * 设置评论动画
         */
        setupCommentAnimation() {
            const comments = document.querySelectorAll(SELECTORS.COMMENTS);
            
            if (comments.length === 0) {
                return;
            }
            
            // 使用 Intersection Observer 实现懒加载动画
            if ('IntersectionObserver' in window) {
                this.setupIntersectionObserver(comments);
            } else {
                // 如果不支持，则直接显示所有评论
                this.animateComments(comments);
            }
        }
        
        /**
         * 设置交叉观察器
         */
        setupIntersectionObserver(comments) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add(CSS_CLASSES.FADE_IN);
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '50px'
            });
            
            comments.forEach(comment => {
                observer.observe(comment);
            });
        }
        
        /**
         * 动画显示评论
         */
        animateComments(comments) {
            comments.forEach((comment, index) => {
                setTimeout(() => {
                    comment.classList.add(CSS_CLASSES.FADE_IN);
                }, index * ANIMATION_DELAY);
            });
        }
        
        /**
         * 销毁方法
         */
        destroy() {
            // 隐藏活动的回复表单
            if (this.activeReplyForm) {
                this.activeReplyForm.style.display = 'none';
                this.activeReplyForm = null;
            }
            
            this.isInitialized = false;
        }
    }
    
    // 防止在不支持的环境中运行
    if (typeof window === 'undefined' || typeof document === 'undefined') {
        console.warn('BlogDetailInteractions 需要浏览器环境');
        return;
    }
    
    // 页面加载完成后初始化
    function initializeWhenReady() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                window.blogDetailInteractions = new BlogDetailInteractions();
            });
        } else {
            window.blogDetailInteractions = new BlogDetailInteractions();
        }
    }
    
    // 导出类供其他脚本使用
    window.BlogDetailInteractions = BlogDetailInteractions;
    
    // 初始化
    initializeWhenReady();
    
})(window, document);