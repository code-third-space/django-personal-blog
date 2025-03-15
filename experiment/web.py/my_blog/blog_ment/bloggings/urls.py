from django.urls import path
from . import views
from .views import custom_logout

app_name = 'bloggings'

urlpatterns = [
    path("blog_search/", views.blog_search, name='searchBlogAll'),
    path("blog_display/", views.blog_display, name='blog_display'),
    path("blog_detail/<int:blog_id>/", views.blog_detail, name='blog_detail'),
    path("delete_comment/<int:comment_id>/", views.delete_comment, name='delete_comment'),
    path("blog_add/", views.BlogCreateView.as_view(), name='blog_add'),
    path("blog_all/", views.blog_all, name='blog_all'),
    path("blog_tech/", views.blog_tech, name='blog_tech'),
    path("blog_current/", views.blog_current, name='blog_current'),
    path("blog_finance/", views.blog_finance, name='blog_finance'),
    path("blog_read", views.blog_read, name='blog_read'),
    path("blog_scenery", views.blog_scenery, name='blog_scenery'),
    path("blog_products", views.blog_products, name='blog_products'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('', views.blog_display, name='home'),
]