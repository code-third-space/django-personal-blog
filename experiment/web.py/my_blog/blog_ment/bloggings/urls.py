from django.urls import path
from . import views
from .views import custom_logout
app_name = 'bloggings'

urlpatterns = [
    path("blog_display/", views.blog_display, name='blog_display'),
    path("blog_detail/<int:blog_id>/", views.detail, name='blog_detail'),
    path("blog_add/", views.BlogCreateView.as_view(), name='blog_add'),
    path("blog_all/", views.blog_all, name='blog_all'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('', views.blog_display, name='home'),
]