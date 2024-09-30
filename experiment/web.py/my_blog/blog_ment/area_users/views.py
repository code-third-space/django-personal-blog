from django.shortcuts import render
from area_users.models import Area_User
from bloggings.models import Me_blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#从请求中获取用户信息，并展示用户界面
@login_required
def user_detail(request):
    try:
        current_user = Area_User.objects.get(creator=request.user)
    except Area_User.DoesNotExistL:
        current_user = None

    context = {
        'current_user':current_user,
    } 
    return render(request, "area_users/user_detail.html", context)

@login_required
def user_myself(request):
    user_blogs = Me_blog.objects.filter(creator=request.user)
    context = {
        'user_blogs':user_blogs,
    }
    return render(request, "area_users/user_myself.html", context)