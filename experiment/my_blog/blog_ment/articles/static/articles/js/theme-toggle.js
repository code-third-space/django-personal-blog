// theme-toggle.js
// 全局主题切换，支持本地存储记忆

document.addEventListener('DOMContentLoaded', function() {
    const darkBtn = document.querySelector('.btn-toggle-dark');
    // 读取本地存储
    if (localStorage.getItem('theme') === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
    } else {
        document.body.setAttribute('data-theme', 'light');
    }
    if (darkBtn) {
        darkBtn.addEventListener('click', function() {
            const currentTheme = document.body.getAttribute('data-theme');
            if (currentTheme === 'dark') {
                document.body.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
            } else {
                document.body.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            }
        });
    }
}); 