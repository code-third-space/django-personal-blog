from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from ..models import Article, Cities, Countries, BlogTypes
from gallery.utils import get_pixabay_image


def all(request):
    # 全部blog视图 - 不再只显示有本地图片的博客，全部都查
    blog_all_list = Article.objects.all().order_by("blog_type")

    for blog_item in blog_all_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]
        # 优先用Pixabay图片
        blog_item.image = get_pixabay_image(blog_item.title)
    
    paginator = Paginator(blog_all_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_all_list": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "articles/all.html", context)


def python(request):
    # 科技视图
    python_list = Article.objects.filter(blog_type=0).order_by("created_at")

    # 过滤没有图片的博客
    # python_list = [blog for blog in python_list if blog.featured_image]

    for blog_item in python_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]
    
    paginator = Paginator(python_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/python.html", context)


def web(request):
    # 实事视图
    web_list = Article.objects.filter(blog_type=1).order_by("created_at")

    # 过滤没有图片的博客
    # web_list = [blog for blog in web_list if blog.featured_image]

    for blog_item in web_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]
    
    paginator = Paginator(web_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/web.html", context)


def backend(request):
    # 财经视图
    backend_list = Article.objects.filter(blog_type=2).order_by("created_at")

    # 过滤没有图片的博客
    # backend_list = [blog for blog in backend_list if blog.featured_image]

    for blog_item in backend_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]
    
    paginator = Paginator(backend_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/backend.html", context)


def database(request):
    # 阅读视图
    database_list = Article.objects.filter(blog_type=3).order_by("created_at")

    # 过滤没有图片的博客
    # database_list = [blog for blog in database_list if blog.featured_image]

    for blog_item in database_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]

    paginator = Paginator(database_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/database.html", context)


def algo(request):
    # 风景视图
    algo_list = Article.objects.filter(blog_type=4).order_by("created_at")

    # 过滤没有图片的博客
    # algo_list = [blog for blog in algo_list if blog.featured_image]

    for blog_item in algo_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]

    paginator = Paginator(algo_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/algo.html", context)


def tools(request):
    # 上平视图
    tools_list = Article.objects.filter(blog_type=5).order_by("created_at")

    # 过滤没有图片的博客
    # tools_list = [blog for blog in tools_list if blog.featured_image]
    
    for blog_item in tools_list:
        blog_item.city_name = Cities[blog_item.city][1]
        blog_item.type_name = BlogTypes[blog_item.blog_type][1]
        blog_item.countries_name = Countries[blog_item.country][1]
    paginator = Paginator(tools_list,6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/tools.html", context)
