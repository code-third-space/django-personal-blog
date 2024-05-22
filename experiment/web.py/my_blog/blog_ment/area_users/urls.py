from django.urls import path
from . import views
from bloggings import views as blog_views

app_name = "area_users"

urlpatterns = [
    path("user_detail/", views.user_self, name="user_detail"),
    path("blog_add/", blog_views.BlogCreateView.as_view(), name="bolg_add"),
    path("", views.user_self, name="name"),
]