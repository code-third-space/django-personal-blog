// theme-toggle.js
// 全局主题切换，支持本地存储记忆

document.addEventListener('DOMContentLoaded', function() {
    const darkBtn = document.querySelector('.btn-toggle-dark');
    // 读取本地存储
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
    }
    if (darkBtn) {
        darkBtn.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            // 记住用户选择
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
}); 