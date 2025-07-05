from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, JsonResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.conf import settings
from comments.models import Comment
from comments.forms import CommentForm
from ..models import Article, Cities, Countries, BlogTypes


def blog_detail(request, blog_id):
    # 详情页
    blog = get_object_or_404(Article, pk=blog_id) 
    blog.city_name = Cities[blog.city][1]
    blog.type_name = BlogTypes[blog.blog_type][1]
    blog.countries_name = Countries[blog.country][1]

    # 获取博客的ContentType
    content_type = ContentType.objects.get_for_model(Article)

    if request.method == 'POST' and request.user.is_authenticated:
        # 处理评论提交
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user # 设置评论的用户
            new_comment.content_type = content_type #设置内容种类
            new_comment.object_id = blog_id # 设置对象id
            new_comment.save()

            # 清除缓存
            cache.clear()

            # 处理AJAX请求
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                comments_html = render_to_string('articles/comments_list.html', {'comments': blog.comments.all()})
                return JsonResponse({'comments_html': comments_html})
            
            return HttpResponseRedirect(reverse('articles:blog_detail', args=[blog_id])) #重定向到该博客详情页
    else:
        form = CommentForm()
    
    # 获取评论
    comments = blog.comments.all()

    context = {
        "blog": blog,
        "comments": comments,
        "form": form,
    }

    return render(request, "articles/blog_detail.html", context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # 检查用户是否有权限删除评论
    if request.user == comment.user:
        # 获取评论所属的博客ID
        blog_id = comment.object_id
        comment.delete()
        return HttpResponseRedirect(reverse('articles:blog_detail', args=[blog_id]))
    else:
        # 如果用户无权删除，重定向到博客详情页
        return HttpResponseRedirect(reverse('articles:blog_detail', args=[comment.object_id]))


class BlogDetailView(DetailView):  #detailview是django提供的一个通用视图类，用于显示模型的详细信息
    model = Article  #指定这个视图要用的模型
    template_name = 'blog_detail.html'  #指定渲染模板的名称


class BlogCreateView(LoginRequiredMixin,CreateView):  #createview 和detailview相同，都是通用视图，用于创建新的模型实例
    #loginrequiredmixin是一个mixin
    template_name = 'articles/blog_form.html'  
    success_url = '/blog_display/'
    model = Article
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


def send_blog_creation_email(user_email, blog_title):
    subject = f"your blog '{blog_title}' has been created"
    message = f"Hello, \n\nyour blog titled '{blog_title}' has been successfully created on our platform. Thank you"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
