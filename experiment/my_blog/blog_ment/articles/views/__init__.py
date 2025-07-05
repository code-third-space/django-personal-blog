from .home import index
from .article import blog_detail, delete_comment, BlogDetailView, BlogCreateView
from .category import (
    all, python, web, backend, database, algo, tools
)
from .auth import custom_logout
from .search import search
from .utils import send_blog_creation_email

__all__ = [
    'index',
    'blog_detail', 'delete_comment', 'BlogDetailView', 'BlogCreateView',
    'all', 'python', 'web', 'backend', 'database', 'algo', 'tools',
    'custom_logout', 'search', 'send_blog_creation_email'
]
