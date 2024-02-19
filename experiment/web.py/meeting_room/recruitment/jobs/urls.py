from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    #职位列表
    path("joblist/", views.joblist, name='joblist'),
    #职位详情
    path("job/<int:job_id>/", views.detail, name="detail"),
    #
    # path('register', views.register, name='register'),
    #提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume_form'),
    #简历详情
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail'),
    #自动跳转
    path('', views.joblist, name='name'),

]
            