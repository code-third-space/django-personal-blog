document.addEventListener('DOMContentLoaded', function() {
    // 打开搜索弹窗
    document.querySelectorAll('.bi-search').forEach(function(el) {
        el.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('fullscreen-search').style.display = 'flex';
            setTimeout(function() {
                document.querySelector('.search-input').focus();
            }, 100);
        });
    });
    // 关闭弹窗
    document.getElementById('close-search').onclick = function() {
        document.getElementById('fullscreen-search').style.display = 'none';
    };
    // 按ESC关闭
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.getElementById('fullscreen-search').style.display = 'none';
        }
    });
});
