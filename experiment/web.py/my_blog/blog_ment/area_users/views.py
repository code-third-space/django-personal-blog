from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Q
from area_users.models import Area_User
from bloggings.models import Me_blog
from bloggings.models import Me_blog, Cities, BlogTypes, Countries
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#从请求中获取用户信息，并展示用户界面
@login_required
def user_detail(request):
    try:
        current_user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        current_user = None

    context = {
        'current_user':current_user,
    } 
    return render(request, "area_users/user_detail.html", context)

@login_required
def user_myself(request):
    user_blogs = Me_blog.objects.filter(creator=request.user)

    # 过滤没有图片的博客
    user_blogs = [blog for blog in user_blogs if blog.picture]

    for blog in user_blogs:
        blog.city_name = Cities[blog.blog_city][1]
        blog.blog_type = BlogTypes[blog.blog_type][1]
        blog.blog_countries = Countries[blog.blog_countries][1]
    context = {
        'user_blogs':user_blogs,
    }
    return render(request, "area_users/user_myself.html", context)

def Search(request):
    titleName = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        titleName = Me_blog.objects.filter(blog_title__icontains=q
                                           ).values('id', 'blog_title', 'blog_detail_one', 'created_date')
        cache.clear()
    content = {
        'titleName': titleName,
    }
    return render(request, "area_users/user_myself.html", content)