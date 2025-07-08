// 只保留表格/卡片切换功能，其它全部注释掉

document.addEventListener('DOMContentLoaded', function() {
    const tableBtn = document.querySelector('.btn-table-view');
    const cardBtn = document.querySelector('.btn-card-view');
    const tableView = document.getElementById('table-view');
    const cardView = document.getElementById('card-view');

    function setView(isTable) {
        if (isTable) {
            tableView.classList.remove('d-none');
            cardView.classList.add('d-none');
            tableBtn.classList.add('active');
            cardBtn.classList.remove('active');
        } else {
            tableView.classList.add('d-none');
            cardView.classList.remove('d-none');
            cardBtn.classList.add('active');
            tableBtn.classList.remove('active');
        }
    }

    if (tableBtn && cardBtn && tableView && cardView) {
        tableBtn.addEventListener('click', function() { setView(true); });
        cardBtn.addEventListener('click', function() { setView(false); });
    }
}); 