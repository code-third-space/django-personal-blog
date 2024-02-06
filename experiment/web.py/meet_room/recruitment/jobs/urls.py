from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path("", views.joblist, name='joblist'),
    path("job/<int:job_id>/", views.detail, name="detail"),
]
