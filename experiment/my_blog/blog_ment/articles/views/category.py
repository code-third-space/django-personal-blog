from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from ..models import Article
from django.templatetags.static import static

# 分页配置常量
ARTICLES_PER_PAGE = 6

def all(request):
    # 全部blog视图 - 高性能优化版本
    # 使用select_related优化关联查询，使用数据库层面的分页
    blog_all_list = Article.objects.select_related('author').all().order_by("blog_type")
    
    # 先进行分页
    paginator = Paginator(blog_all_list, ARTICLES_PER_PAGE)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页
        page_obj = paginator.get_page(paginator.num_pages)
    
    # 只对当前页的数据进行处理，避免处理所有数据
    for blog_item in page_obj:
        # 使用模型的内置方法获取显示名称，保持数据一致性
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.country_name = blog_item.get_country_display()
        # 全部用默认图片
        blog_item.image = static('images/default.jpg')
    
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()
    
    paginator = Paginator(python_list, ARTICLES_PER_PAGE)
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()
    
    paginator = Paginator(web_list, ARTICLES_PER_PAGE)
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()
    
    paginator = Paginator(backend_list, ARTICLES_PER_PAGE)
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()

    paginator = Paginator(database_list, ARTICLES_PER_PAGE)
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()

    paginator = Paginator(algo_list, ARTICLES_PER_PAGE)
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
        blog_item.city_name = blog_item.get_city_display()
        blog_item.type_name = blog_item.get_blog_type_display()
        blog_item.countries_name = blog_item.get_country_display()
    paginator = Paginator(tools_list, ARTICLES_PER_PAGE) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": page_obj,
        "article_count": page_obj.paginator.count,
        "page_obj": page_obj,
    }
    return render(request, "articles/tools.html", context)
