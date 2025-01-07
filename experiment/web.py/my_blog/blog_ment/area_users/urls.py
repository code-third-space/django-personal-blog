from django.urls import path
from . import views
from bloggings import views as blog_views

app_name = "area_users"

urlpatterns = [
    path("user_detail/", views.user_detail, name="user_detail"),
    path("user_myself/", views.user_myself,name="user_myself"),
    path("blog_add/", blog_views.BlogCreateView.as_view(), name="bolg_add"),
    path("", views.user_detail, name="home_area_users"),
    path('search/', views.Search, name='Search')
]