from django.shortcuts import render
from django.urls import reverse
from ..models import Article, Cities, Countries, BlogTypes
from ..utils import my_function


def index(request):
    # 定义首页视图函数
    blog_list = Article.objects.order_by("blog_type")
    # 主推文章
    feature_articles = Article.objects.order_by('-created_at')[:12]
    #热门文章
    popular_articles = Article.objects.order_by('-view_count')[:12]
    # 分类标签
    categories = [
        {'name': 'Python', 'url': reverse('articles:python')},
        {'name': 'Web', 'url': reverse('articles:web')},
        {'name': 'Backend', 'url': reverse('articles:backend')},
        {'name': 'Database', 'url': reverse('articles:database')},
        {'name': 'Algo', 'url': reverse('articles:algo')},
        {'name': 'Tools', 'url': reverse('articles:tools')},
    ]

    catego_blogs = {
        'tech_blogs':Article.objects.filter(blog_type=0).order_by('-id').first(),
        'current_blogs':Article.objects.filter(blog_type=1).order_by('-id').first(),
        'finance_blogs':Article.objects.filter(blog_type=2).order_by('-id').first(),
        'read_blogs':Article.objects.filter(blog_type=3).order_by('-id').first(),
        'scenery_blogs':Article.objects.filter(blog_type=4).order_by('-id').first(),
        'products_blogs':Article.objects.filter(blog_type=5).order_by('-id').first(),
    }

    categorized_blogs = {
        'type_a_blogs':[],
        'type_b_blogs':[],
        'type_c_blogs':[],
        'type_d_blogs':[],
        'type_e_blogs':[],
        'type_f_blogs':[],
    }

    for blog in blog_list:
        blog.city_name = blog.get_city_display()
        blog.type_name = blog.get_blog_type_display()
        blog.countries_name = blog.get_country_display()

        if blog.blog_type==0:
            categorized_blogs['type_a_blogs'].append(blog)
        elif blog.blog_type==2:
            categorized_blogs["type_b_blogs"].append(blog)
        elif blog.blog_type==1:
            categorized_blogs['type_c_blogs'].append(blog)
        elif blog.blog_type==3:
            categorized_blogs['type_d_blogs'].append(blog)
        elif blog.blog_type==4:
            categorized_blogs['type_e_blogs'].append(blog)
        elif blog.blog_type==5:
            categorized_blogs['type_f_blogs'].append(blog)
        
    article_blogs = blog_list[:9]
    type_a_blogs = categorized_blogs["type_a_blogs"][:4]
    type_b_blogs = categorized_blogs["type_b_blogs"][:4]
    type_c_blogs = categorized_blogs["type_c_blogs"][:4]
    type_d_blogs = categorized_blogs["type_d_blogs"][:4]
    type_e_blogs = categorized_blogs["type_e_blogs"][:4]
    type_f_blogs = categorized_blogs["type_f_blogs"][:4]

    context = {
        "articles_list": article_blogs,
        "type_a_blogs": type_a_blogs,
        "type_b_blogs": type_b_blogs,
        "type_c_blogs": type_c_blogs,
        "type_d_blogs": type_d_blogs,
        "type_e_blogs": type_e_blogs,
        "type_f_blogs": type_f_blogs,
        "tech_blog":catego_blogs['tech_blogs'],
        "current_blog":catego_blogs['current_blogs'],
        "finance_blog":catego_blogs['finance_blogs'],
        "read_blog":catego_blogs['read_blogs'],
        "scenery_blog":catego_blogs['scenery_blogs'],
        "products_blog":catego_blogs['products_blogs'],
        "feature_articles":feature_articles,
        "popular_articles":popular_articles,
        "categories":categories,
        }
    
    my_function()

    return render(request, 'articles/index.html',context)
