document.addEventListener('DOMContentLoaded', function() {
    // 确保搜索弹窗初始状态正确
    const modal = document.getElementById('fullscreen-search');
    modal.style.display = 'none';
    modal.style.visibility = 'hidden';
    modal.style.opacity = '0';
    
    // 打开搜索弹窗
    document.querySelectorAll('.bi-search').forEach(function(el) {
        el.addEventListener('click', function(e) {
            e.preventDefault();
            openSearchModal();
        });
    });
    
    // 关闭弹窗
    document.getElementById('close-search').onclick = function() {
        closeSearchModal();
    };
    
    // 按ESC关闭
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeSearchModal();
        }
    });
    
    // 点击背景关闭
    document.getElementById('fullscreen-search').addEventListener('click', function(e) {
        if (e.target === this) {
            closeSearchModal();
        }
    });
    
    // 搜索表单提交
    document.getElementById('fullscreen-search-form').addEventListener('submit', function(e) {
        const input = document.querySelector('.search-input');
        if (!input.value.trim()) {
            e.preventDefault();
            input.focus();
            return false;
        }
    });
});

// 打开搜索弹窗
function openSearchModal() {
    const modal = document.getElementById('fullscreen-search');
    modal.style.display = 'flex';
    modal.style.visibility = 'visible';
    modal.style.opacity = '0';
    
    // 添加动画效果
    setTimeout(function() {
        modal.style.opacity = '1';
        document.querySelector('.search-input').focus();
    }, 10);
}

// 关闭搜索弹窗
function closeSearchModal() {
    const modal = document.getElementById('fullscreen-search');
    modal.style.opacity = '0';
    
    setTimeout(function() {
        modal.style.display = 'none';
        modal.style.visibility = 'hidden';
        document.querySelector('.search-input').value = '';
    }, 300);
}

// 搜索建议功能
function searchSuggestion(term) {
    const input = document.querySelector('.search-input');
    input.value = term;
    input.focus();
    
    // 添加点击效果
    const tag = event.target;
    tag.style.transform = 'scale(0.95)';
    setTimeout(() => {
        tag.style.transform = '';
    }, 150);
}
