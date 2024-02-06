from django.shortcuts import render, redirect
from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    blogs = Blog.objects.all()
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()
    if blog.owner != request.user:
        raise Http404

    context = {'blog': blog, 'posts':posts}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

""" @login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blogs')
        
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context) """

@login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner= request.user
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
    
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)