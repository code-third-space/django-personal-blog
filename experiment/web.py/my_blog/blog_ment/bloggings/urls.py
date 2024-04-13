from django.urls import path
from . import views
from .views import custom_logout
app_name = 'bloggings'

urlpatterns = [
    path("blog_display/", views.blog_display, name='blog_display'),
    path("blog_detail/<int:blog_id>/", views.detail, name='blog_detail'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('', views.blog_display, name='name'),
]