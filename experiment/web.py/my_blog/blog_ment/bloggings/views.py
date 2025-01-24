from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, JsonResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout
from bloggings.utils import my_function
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
from django.conf import settings
import logging
logger = logging.getLogger('area_users.performance')

from .models import Me_blog, Comment
from .models import Cities,Countries,BlogTypes
from .forms import CommentForm

# Create your views here.


def blog_display(request):
    # 定义 display的视图函数
    blog_list = Me_blog.objects.order_by("blog_type")

    catego_blogs = {
        # 每个分类的第一个blog
        'tech_blogs':Me_blog.objects.filter(blog_type=0).order_by('-id').first(),
        'current_blogs':Me_blog.objects.filter(blog_type=1).order_by('-id').first(),
        'finance_blogs':Me_blog.objects.filter(blog_type=2).order_by('-id').first(),
        'read_blogs':Me_blog.objects.filter(blog_type=3).order_by('-id').first(),
        'scenery_blogs':Me_blog.objects.filter(blog_type=4).order_by('-id').first(),
        'products_blogs':Me_blog.objects.filter(blog_type=5).order_by('-id').first(),
    }

    categorized_blogs = {
        # 定义了分类的列表
        'type_a_blogs':[],
        'type_b_blogs':[],
        'type_c_blogs':[],
        'type_d_blogs':[],
        'type_e_blogs':[],
        'type_f_blogs':[],
    }

    for blog in blog_list:
        blog.city_name = Cities[blog.blog_city][1]
        blog.type_name = BlogTypes[blog.blog_type][1]
        blog.countries_name = Countries[blog.blog_countries][1]

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
        
    # print("Number of blogs:", len(blog_list))

    overview_blogs = blog_list[:8]
    type_a_blogs = categorized_blogs["type_a_blogs"][:4]
    type_b_blogs = categorized_blogs["type_b_blogs"][:4]
    type_c_blogs = categorized_blogs["type_c_blogs"][:4]
    type_d_blogs = categorized_blogs["type_d_blogs"][:4]
    type_e_blogs = categorized_blogs["type_e_blogs"][:4]
    type_f_blogs = categorized_blogs["type_f_blogs"][:4]

    context = {
        "blog_list": overview_blogs,
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
        }
    
    my_function()

    return render(request, 'bloggings/blog_display.html',context)

def detail(request, blog_id):
    # 详情页
    blog= get_object_or_404(Me_blog, pk=blog_id) 
    blog.city_name = Cities[blog.blog_city][1]

    # comments = blog.comments.all()
    logger.info('blog info fetched from databases blogid')

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog # 关联到当前博客
            comment.user = request.user # 设置评论的用户
            comment.save()

            comments = blog.comments.all()
            cache.clear()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                comments_html = render_to_string('bloggings/comments_list.html', {'comments': comments})
                return JsonResponse({'comments_html': comments_html})
            
            return redirect('bloggings:blog_detail', blog_id=blog.id) #重定向到该博客详情页
    comments = blog.comments.all()

    context = {
        "blog": blog,
        "comments": comments,
        "form": form,
    }

    return render(request, "bloggings/blog_detail.html", context)

@login_required
def delete_comment(request, comment_id):
    # 删除评论视图
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        cache.clear()
        return redirect('bloggings:blog_detail', blog_id=comment.blog.id)
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

def blog_all(request):
    # 全部blog视图
    blog_all_list = Me_blog.objects.order_by("blog_type")

    # 过滤没有图片的博客
    blog_all_list = [blog for blog in blog_all_list if blog.picture]
    

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
        "page_obj": page_obj,
        }
    return render(request, "bloggings/blog_all.html", context)

def blog_tech(request):
    # 科技视图
    blog_tech_list = Me_blog.objects.filter(blog_type=0).order_by("created_date")

    # 过滤没有图片的博客
    blog_tech_list = [blog for blog in blog_tech_list if blog.picture]

    for blog_item in blog_tech_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_tech_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_tech_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_tech.html", context)

def blog_current(request):
    # 实事视图
    blog_current_list = Me_blog.objects.filter(blog_type=1).order_by("created_date")

    # 过滤没有图片的博客
    blog_current_list = [blog for blog in blog_current_list if blog.picture]

    for blog_item in blog_current_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_current_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_current_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_current.html", context)

def blog_finance(request):
    # 财经视图
    blog_finance_list = Me_blog.objects.filter(blog_type=2).order_by("created_date")

    # 过滤没有图片的博客
    blog_finance_list = [blog for blog in blog_finance_list if blog.picture]

    for blog_item in blog_finance_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    
    paginator = Paginator(blog_finance_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_finance_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_finance.html", context)

def blog_read(request):
    # 阅读视图
    blog_read_list = Me_blog.objects.filter(blog_type=3).order_by("created_date")

    # 过滤没有图片的博客
    blog_read_list = [blog for blog in blog_read_list if blog.picture]

    for blog_item in blog_read_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]

    paginator = Paginator(blog_read_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_read_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_read.html", context)

def blog_scenery(request):
    # 风景视图
    blog_scenery_list = Me_blog.objects.filter(blog_type=4).order_by("created_date")

    # 过滤没有图片的博客
    blog_scenery_list = [blog for blog in blog_scenery_list if blog.picture]

    for blog_item in blog_scenery_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]

    paginator = Paginator(blog_scenery_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_scenery_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_scenery.html", context)

def blog_products(request):
    # 上平视图
    blog_products_list = Me_blog.objects.filter(blog_type=5).order_by("created_date")

    # 过滤没有图片的博客
    blog_products_list = [blog for blog in blog_products_list if blog.picture]
    
    for blog_item in blog_products_list:
        blog_item.city_name = Cities[blog_item.blog_city][1]
        blog_item.blog_type = BlogTypes[blog_item.blog_type][1]
        blog_item.blog_countries = Countries[blog_item.blog_countries][1]
    paginator = Paginator(blog_products_list,6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blog_products_list":page_obj,
        "page_obj":page_obj,
    }
    return render(request, "bloggings/blog_products.html", context)


def custom_logout(request):
    logout(request)   #调用django的logout（）函数来注销用户
    return redirect('bloggings:home')  #重定向到命名url bloggings：name

class BlogDetailView(DetailView):  #detailview是django提供的一个通用视图类，用于显示模型的详细信息
    model = Me_blog  #指定这个视图要用的模型
    template_name = 'blog_detail.html'  #指定渲染模板的名称

class BlogCreateView(LoginRequiredMixin,CreateView):  #createview 和detailview相同，都是通用视图，用于创建新的模型实例
    #loginrequiredmixin是一个mixin
    template_name = 'bloggings/blog_form.html'  
    success_url = '/blog_display/'
    model = Me_blog
    fields = [
        'blog_title', 'blog_type', 'blog_countries',
        'blog_city', 'creator', 'created_date', 
        'modified_date','blog_detail_one', 'blog_detail_two',
        'blog_detail_three','picture',
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
        
    
        # 发送邮件
        user_email = "retcryly@163.com"
        blog_title = self.object.blog_title
        send_blog_creation_email(user_email, blog_title)
    
        return HttpResponseRedirect(self.get_success_url())

    #邮件


def send_blog_creation_email(user_email, blog_title):
    subject = f"your blog '{blog_title}' has been created"
    message = f"Hello, \n\nyour blog titled '{blog_title}' has been successfully created on our platform. Thank you"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)

def blog_search(request):
    titleName = []
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            titleName = Me_blog.objects.filter(blog_title__icontains=q
                ).values('id', 'blog_title', 'blog_detail_one', 'created_date')
            content = {
                'titleName': titleName,
            }
            cache.clear()
            return render(request, "bloggings/blog_search.html", content)
        cache.clear()
    return render(request, "bloggings/blog_search.html", {'errors': errors})