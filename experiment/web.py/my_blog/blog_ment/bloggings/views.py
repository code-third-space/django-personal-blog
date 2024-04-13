from django.shortcuts import render
from django.http import Http404 
from .models import Me_blog
from .models import Cities,Countries,BlogTypes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.

def blog_display(request):
    blog_list = Me_blog.objects.order_by("blog_type")

    for blog in blog_list:
        blog.city_name = Cities[blog.blog_city][1]
        blog.blog_type = BlogTypes[blog.blog_type][1]
    print("Number of blogs:", len(blog_list))    
    context = {"blog_list": blog_list}

    return render(request, 'bloggings/blog_display.html',context)


def detail(request, blog_id):
    try:
        blog=Me_blog.objects.get(pk=blog_id)
        blog.city_name = Cities[blog.blog_city][1]

    except Me_blog.DoesNotExist:
        raise Http404("blog does not exist")
    return render(request, "bloggings/blog_detail.html", {'blog':blog})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('bloggings:name')

class BlogDetailView(DetailView):
    model = Me_blog
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin,CreateView):
    template_name = 'blog_detail.html'
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