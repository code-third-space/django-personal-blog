document.addEventListener('DOMContentLoaded', function() {
    // 回复按钮点击事件
    const replyButtons = document.querySelectorAll('.reply-btn');
    replyButtons.forEach(button => {
      button.addEventListener('click', function() {
        const commentId = this.dataset.commentId;
        const replyForm = document.getElementById(`reply-form-${commentId}`);
        
        // 隐藏所有其他回复表单
        document.querySelectorAll('.reply-form-container').forEach(form => {
          if (form.id !== `reply-form-${commentId}`) {
            form.style.display = 'none';
          }
        });
        
        // 切换当前回复表单的显示状态
        replyForm.style.display = replyForm.style.display === 'none' ? 'block' : 'none';
        
        // 如果显示表单，则聚焦到文本区域
        if (replyForm.style.display === 'block') {
          replyForm.querySelector('textarea').focus();
        }
      });
    });
    
    // 取消回复按钮点击事件
    const cancelButtons = document.querySelectorAll('.cancel-btn');
    cancelButtons.forEach(button => {
      button.addEventListener('click', function() {
        const commentId = this.dataset.commentId;
        const replyForm = document.getElementById(`reply-form-${commentId}`);
        replyForm.style.display = 'none';
      });
    });
    
    // 平滑滚动到评论区
    const commentLinks = document.querySelectorAll('a[href="#comments"]');
    commentLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('comments').scrollIntoView({ 
          behavior: 'smooth' 
        });
      });
    });
    
    // 评论表单提交前验证
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
      commentForm.addEventListener('submit', function(e) {
        const textarea = this.querySelector('textarea');
        if (!textarea.value.trim()) {
          e.preventDefault();
          alert('评论内容不能为空！');
          textarea.focus();
        }
      });
    }
    
    // 高亮当前评论（如果URL中有评论ID）
    const highlightComment = () => {
      const hash = window.location.hash;
      if (hash && hash.startsWith('#comment-')) {
        const commentId = hash.substring(9); // 去掉 '#comment-'
        const comment = document.getElementById(`comment-${commentId}`);
        if (comment) {
          comment.classList.add('highlighted');
          comment.scrollIntoView({ behavior: 'smooth' });
        }
      }
    };
    
    // 页面加载时执行高亮
    highlightComment();
    
    // 当hash变化时也执行高亮
    window.addEventListener('hashchange', highlightComment);
    
    // 添加评论动画效果
    const addCommentAnimation = () => {
      const comments = document.querySelectorAll('.comment');
      comments.forEach((comment, index) => {
        setTimeout(() => {
          comment.classList.add('fade-in');
        }, index * 100);
      });
    };
    
    addCommentAnimation();
  });