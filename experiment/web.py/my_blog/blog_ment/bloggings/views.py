from django.shortcuts import render
from django.http import Http404 
from .models import Me_blog
from .models import Cities,Countries,BlogTypes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout
from django.shortcuts import redirect
from bloggings.utils import my_function
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

def blog_display(request):
    blog_list = Me_blog.objects.order_by("blog_type")

    type_a_blogs = [ blog for blog in blog_list if blog.blog_type == 0 ]
    type_b_blogs = [ blog for blog in blog_list if blog.blog_type == 2 ]

    for blog in blog_list:
        blog.city_name = Cities[blog.blog_city][1]
        blog.blog_type = BlogTypes[blog.blog_type][1]
    print("Number of blogs:", len(blog_list))    
    context = {
        "blog_list": blog_list,
        "type_a_blogs": type_a_blogs,
        "type_b_blogs": type_b_blogs,
        }
    my_function()

    return render(request, 'bloggings/blog_display.html',context)


def detail(request, blog_id):
    try:
        blog=Me_blog.objects.get(pk=blog_id)
        blog.city_name = Cities[blog.blog_city][1]

    except Me_blog.DoesNotExist:
        raise Http404("blog does not exist")
    return render(request, "bloggings/blog_detail.html", {'blog':blog})

def blog_all(request):
    blog_all_list = Me_blog.objects.order_by("blog_type")
    for blog_item in blog_all_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    #创建分页器, 每页6篇博客
    paginator = Paginator(blog_all_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_all_list": page_obj,
        }
    return render(request, "bloggings/blog_all.html", context)

def blog_tech(request):
    blog_tech_list = Me_blog.objects.filter(blog_type=0).order_by("created_date")
    for blog_item in blog_tech_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_tech_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_tech_list":page_obj,
    }
    return render(request, "bloggings/blog_tech.html", context)

def blog_current(request):
    blog_current_list = Me_blog.objects.filter(blog_type=1).order_by("created_date")
    for blog_item in blog_current_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_current_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_current_list":page_obj,
    }
    return render(request, "bloggings/blog_current.html", context)

def blog_finance(request):
    blog_finance_list = Me_blog.objects.filter(blog_type=2).order_by("created_date")
    for blog_item in blog_finance_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_finance_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_finance_list":page_obj,
    }
    return render(request, "bloggings/blog_finance.html", context)

def blog_read(request):
    blog_read_list = Me_blog.objects.filter(blog_type=3).order_by("created_date")
    for blog_item in blog_read_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]

    paginator = Paginator(blog_read_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_read_list":page_obj,
    }
    return render(request, "bloggings/blog_read.html", context)

def blog_scenery(request):
    blog_scenery_list = Me_blog.objects.filter(blog_type=4).order_by("created_date")
    for blog_item in blog_scenery_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]

    paginator = Paginator(blog_scenery_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_scenery_list":page_obj,
    }
    return render(request, "bloggings/blog_scenery.html", context)

def blog_products(request):
    blog_products_list = Me_blog.objects.filter(blog_type=5).order_by("created_date")
    for blog_item in blog_products_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    paginator = Paginator(blog_products_list,6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_products_list":page_obj,
    }
    return render(request, "bloggings/blog_products.html", context)


def custom_logout(request):
    logout(request)   #调用django的logout（）函数来注销用户
    return redirect('bloggings:name')  #重定向到命名url bloggings：name

class BlogDetailView(DetailView):  #detailview是django提供的一个通用视图类，用于显示模型的详细信息
    model = Me_blog  #指定这个视图要用的模型
    template_name = 'blog_detail.html'  #指定渲染模板的名称

class BlogCreateView(LoginRequiredMixin,CreateView):  #createview 和detailview相同，都是通用视图，用于创建新的模型实例
    #loginrequiredmixin是一个mixin
    template_name = 'blog_form.html'  
    success_url = '/blog_display/'
    model = Me_blog
    fields = [
        'blog_title', 'blog_type', 'blog_countries',
        'blog_city', 'creator', 'created_date', 
        'modified_date','blog_detail', 'picture',
    ]

    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    