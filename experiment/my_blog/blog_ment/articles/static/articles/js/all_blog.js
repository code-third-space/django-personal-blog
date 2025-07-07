document.addEventListener('DOMContentLoaded', function() {
    // 为不同类型的博客设置不同的颜色 - 新分类
    const typeColors = {
        'Python': '#0d6efd',
        'Web': '#28a745',
        'Backend': '#dc3545',
        'Database': '#6f42c1',
        'Algo': '#20c997',
        'Tools': '#fd7e14'
    };
    // 为每个博客类型标签设置颜色
    document.querySelectorAll('.blog-type-badge').forEach(badge => {
        const typeName = badge.textContent.trim();
        if (typeColors[typeName]) {
            badge.style.backgroundColor = typeColors[typeName];
        } else {
            badge.style.backgroundColor = '#6c757d'; // 默认颜色
        }
    });
    // 为城市标签添加随机颜色
    const cityColors = ['#17a2b8', '#6610f2', '#fd7e14', '#20c997', '#e83e8c'];
    document.querySelectorAll('.city-badge').forEach((badge, index) => {
        badge.style.backgroundColor = cityColors[index % cityColors.length];
    });

    // 表格/卡片切换功能
    const tableBtn = document.querySelector('.btn-table-view');
    const cardBtn = document.querySelector('.btn-card-view');
    const tableView = document.getElementById('table-view');
    const cardView = document.getElementById('card-view');
    if (tableBtn && cardBtn && tableView && cardView) {
        tableBtn.addEventListener('click', function() {
            tableView.style.display = '';
            cardView.style.display = 'none';
            tableBtn.classList.add('active');
            cardBtn.classList.remove('active');
        });
        cardBtn.addEventListener('click', function() {
            tableView.style.display = 'none';
            cardView.style.display = '';
            cardBtn.classList.add('active');
            tableBtn.classList.remove('active');
        });
    }

    // 夜间模式切换功能
    const darkBtn = document.querySelector('.btn-toggle-dark');
    if (darkBtn) {
        darkBtn.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
        });
    }
}); 