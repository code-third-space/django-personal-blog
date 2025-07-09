/**
 * 搜索功能专用脚本
 * 统一处理搜索弹窗的打开、关闭和交互功能
 */

// 搜索状态管理
let searchModalOpen = false;
let searchModal = null;
let searchInput = null;
let searchForm = null;
let closeBtn = null;

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
});

/**
 * 初始化搜索功能
 */
function initializeSearch() {
    // 获取DOM元素
    searchModal = document.getElementById('fullscreen-search');
    searchInput = document.querySelector('.search-input');
    searchForm = document.getElementById('fullscreen-search-form');
    closeBtn = document.getElementById('close-search');
    
    if (!searchModal) {
        console.error('搜索弹窗元素未找到');
        return;
    }
    
    // 确保搜索弹窗初始状态正确
    resetSearchModal();
    
    // 绑定搜索按钮事件
    setupSearchButtons();
    
    // 绑定关闭按钮事件
    setupCloseButton();
    
    // 绑定背景点击事件
    setupBackgroundClick();
    
    // 绑定ESC键事件
    setupEscapeKey();
    
    // 绑定表单提交事件
    setupFormSubmit();
    
    // 绑定搜索建议事件
    setupSearchSuggestions();
    
    console.log('搜索功能初始化完成');
}

/**
 * 重置搜索弹窗状态
 */
function resetSearchModal() {
    searchModal.style.display = 'none';
    searchModal.style.visibility = 'hidden';
    searchModal.style.opacity = '0';
    searchModalOpen = false;
}

/**
 * 设置搜索按钮事件
 */
function setupSearchButtons() {
    const searchBtns = document.querySelectorAll('.search-btn, .mobile-action-btn');
    
    searchBtns.forEach(function(btn) {
        // 只处理包含搜索图标的按钮
        if (btn.querySelector('.bi-search')) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                openSearchModal();
            });
        }
    });
}

/**
 * 设置关闭按钮事件
 */
function setupCloseButton() {
    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            closeSearchModal();
        });
    }
}

/**
 * 设置背景点击事件
 */
function setupBackgroundClick() {
    searchModal.addEventListener('click', function(e) {
        if (e.target === searchModal && searchModalOpen) {
            closeSearchModal();
        }
    });
}

/**
 * 设置ESC键事件
 */
function setupEscapeKey() {
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && searchModalOpen) {
            e.preventDefault();
            closeSearchModal();
        }
    });
}

/**
 * 设置表单提交事件
 */
function setupFormSubmit() {
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            if (!searchInput.value.trim()) {
                e.preventDefault();
                searchInput.focus();
                showSearchHint('请输入搜索关键词');
                return false;
            }
        });
    }
}

/**
 * 设置搜索建议事件
 */
function setupSearchSuggestions() {
    const suggestionTags = document.querySelectorAll('.search-suggestion-tag');
    
    suggestionTags.forEach(function(tag) {
        tag.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const query = this.textContent.trim();
            searchSuggestion(query);
        });
        
        // 键盘支持
        tag.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const query = this.textContent.trim();
                searchSuggestion(query);
            }
        });
    });
}

/**
 * 打开搜索弹窗
 */
function openSearchModal() {
    if (searchModalOpen) {
        return; // 如果已经打开，不重复处理
    }
    
    console.log('打开搜索弹窗');
    
    // 设置显示状态
    searchModal.style.display = 'flex';
    searchModal.style.visibility = 'visible';
    searchModal.style.opacity = '0';
    
    // 防止页面滚动
    document.body.style.overflow = 'hidden';
    
    // 标记为已打开
    searchModalOpen = true;
    
    // 延迟显示和聚焦
    setTimeout(function() {
        if (searchModalOpen) {
            searchModal.style.opacity = '1';
            
            // 聚焦并选中输入框文本
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
    }, 100);
}

/**
 * 关闭搜索弹窗
 */
function closeSearchModal() {
    if (!searchModalOpen) {
        return; // 如果已经关闭，不重复处理
    }
    
    console.log('关闭搜索弹窗');
    
    // 设置渐隐效果
    searchModal.style.opacity = '0';
    
    setTimeout(function() {
        searchModal.style.display = 'none';
        searchModal.style.visibility = 'hidden';
        
        // 恢复页面滚动
        document.body.style.overflow = '';
        
        // 清空搜索框
        if (searchInput) {
            searchInput.value = '';
        }
        
        // 标记为已关闭
        searchModalOpen = false;
    }, 300);
}

/**
 * 搜索建议功能
 */
function searchSuggestion(term) {
    if (!searchInput) return;
    
    searchInput.value = term;
    searchInput.focus();
    
    // 提交搜索
    if (searchForm) {
        searchForm.submit();
    }
}

/**
 * 显示搜索提示
 */
function showSearchHint(message) {
    if (!searchInput) return;
    
    // 创建提示元素
    const hint = document.createElement('div');
    hint.className = 'search-hint';
    hint.textContent = message;
    hint.style.cssText = `
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: #dc3545;
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 14px;
        z-index: 1000;
        margin-top: 5px;
    `;
    
    // 添加到搜索框容器
    const container = searchInput.closest('.search-input-group');
    if (container) {
        container.style.position = 'relative';
        container.appendChild(hint);
        
        // 3秒后自动消失
        setTimeout(() => {
            if (hint.parentNode) {
                hint.parentNode.removeChild(hint);
            }
        }, 3000);
    }
}

// 将函数暴露到全局作用域
window.openSearchModal = openSearchModal;
window.closeSearchModal = closeSearchModal;
window.searchSuggestion = searchSuggestion;