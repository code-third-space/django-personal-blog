from django.urls import path
from . import views
from .views import custom_logout
from gallery.views import article_with_images
from .feeds import LatestArticlesFeed

app_name = 'articles'

urlpatterns = [
    path("search/", views.search, name='search'),
    path("blog_detail/<int:blog_id>/", article_with_images, name='blog_detail'),
    path("delete_comment/<int:comment_id>/", views.delete_comment, name='delete_comment'),
    path("blog_add/", views.BlogCreateView.as_view(), name='blog_add'),
    path("all/", views.all, name='all'),
    path("python/", views.python, name='python'),
    path("web/", views.web, name='web'),
    path("wackend/", views.backend, name='backend'),
    path("database/", views.database, name='database'),
    path("algo/", views.algo, name='algo'),
    path("tools/", views.tools, name='tools'),
    path('', views.index, name='home'),
    path('rss/', LatestArticlesFeed(), name='rss_feed'),
]