from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('article/<int:pk>/', views.article_with_images, name='article_with_images'),
]