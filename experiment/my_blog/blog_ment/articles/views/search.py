from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Q
from django.core.paginator import Paginator
from ..models import Article


def search(request):
    titleName = []
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q'].strip()
        if not q:
            errors.append("请输入搜索关键词。")
        elif len(q) > 50:
            errors.append("搜索关键词不能超过50个字符。")
        else:
            # 搜索标题和内容，保持原有的变量名
            titleName = Article.objects.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            ).select_related('author').order_by('-created_at')
            
            # 为每个搜索结果添加分类和城市信息
            for blog in titleName:
                blog.type_name = blog.get_blog_type_display()
                blog.city_name = blog.get_city_display()
            
            # 添加分页
            paginator = Paginator(titleName, 9)  # 每页显示9篇文章
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            content = {
                'titleName': page_obj,
            }
            return render(request, "articles/search.html", content)
    return render(request, "articles/search.html", {'errors': errors}) 