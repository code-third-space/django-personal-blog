from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Q, Case, When, IntegerField
from django.core.paginator import Paginator
from django.utils.html import format_html
import logging

logger = logging.getLogger(__name__)

# 分页配置常量
SEARCH_RESULTS_PER_PAGE = 9
# 搜索配置常量
MAX_SEARCH_QUERY_LENGTH = 50

def search(request):
    titleName = []
    errors = []
    search_query = ''
    
    if 'q' in request.GET and request.GET['q']:
        search_query = request.GET['q'].strip()
        if not search_query:
            errors.append("请输入搜索关键词。")
        elif len(search_query) > MAX_SEARCH_QUERY_LENGTH:
            errors.append("搜索关键词不能超过50个字符。")
        else:
            try:
                # 记录搜索历史 (如果用户已登录)
                if request.user.is_authenticated:
                    try:
                        from accounts.models import SearchHistory
                        SearchHistory.objects.create(
                            user=request.user,
                            query=search_query,
                            ip_address=request.META.get('REMOTE_ADDR')
                        )
                    except Exception as e:
                        logger.warning(f"搜索历史记录失败: {e}")
                
                # 暂时禁用缓存进行调试
                # cache_key = f"search_results_{search_query}_{request.GET.get('page', 1)}"
                # cached_results = cache.get(cache_key)
                
                # if cached_results:
                #     titleName = cached_results
                #     logger.info(f"搜索缓存命中: {search_query}")
                # else:
                #     # 改进的搜索逻辑 - 按相关性排序
                titleName = perform_search(search_query)
                
                # 缓存结果
                # cache.set(cache_key, titleName, 300)  # 5分钟
                logger.info(f"搜索执行: {search_query}, 结果数: {len(titleName)}")
                
                # 更新搜索历史的结果数量
                if request.user.is_authenticated:
                    try:
                        from accounts.models import SearchHistory
                        SearchHistory.objects.filter(
                            user=request.user,
                            query=search_query
                        ).update(results_count=len(titleName))
                    except Exception as e:
                        logger.warning(f"更新搜索历史失败: {e}")
                
                # 添加分页
                paginator = Paginator(titleName, SEARCH_RESULTS_PER_PAGE)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                
                context = {
                    'titleName': page_obj,
                    'search_query': search_query,
                    'total_results': len(titleName) if titleName else 0,
                }
                return render(request, "articles/search.html", context)
                
            except Exception as e:
                logger.error(f"搜索错误: {e}")
                errors.append("搜索过程中出现错误，请稍后重试。")
    
    return render(request, "articles/search.html", {
        'errors': errors,
        'search_query': search_query
    })

def perform_search(query):
    """
    执行搜索并按相关性排序
    """
    from ..models import Article
    
    # 拆分搜索关键词
    keywords = query.split()
    
    # 构建搜索条件 - 使用 icontains 确保不区分大小写
    search_conditions = Q()
    
    for keyword in keywords:
        search_conditions |= (
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword)
        )
    
    # 基础查询
    try:
        articles = Article.objects.filter(search_conditions).select_related('author')
        
        # 调试信息
        logger.info(f"搜索条件: {search_conditions}")
        logger.info(f"查询结果数量: {articles.count()}")
        
        # 按相关性排序 - 标题匹配优先级更高
        articles = articles.annotate(
            relevance_score=Case(
                # 标题完全匹配 (不区分大小写)
                When(title__iexact=query, then=100),
                # 标题包含完整查询
                When(title__icontains=query, then=80),
                # 标题包含关键词
                When(title__icontains=keywords[0] if keywords else '', then=60),
                # 内容包含完整查询
                When(content__icontains=query, then=40),
                # 内容包含关键词
                When(content__icontains=keywords[0] if keywords else '', then=20),
                default=10,
                output_field=IntegerField()
            )
        ).order_by('-relevance_score', '-created_at')
        
        # 为每个搜索结果添加显示信息
        results = []
        for article in articles:
            article.type_name = article.get_blog_type_display()
            article.city_name = article.get_city_display()
            article.highlighted_title = highlight_search_terms(article.title, query)
            article.highlighted_content = highlight_search_terms(
                article.content[:100] if article.content else '', query
            )
            results.append(article)
        
        return results
        
    except Exception as e:
        logger.error(f"搜索查询错误: {e}")
        return []

def highlight_search_terms(text, query):
    """
    高亮搜索关键词
    """
    if not text or not query:
        return text
    
    try:
        keywords = query.split()
        highlighted_text = text
        
        for keyword in keywords:
            if keyword.lower() in highlighted_text.lower():
                # 使用不区分大小写的替换
                import re
                pattern = re.compile(re.escape(keyword), re.IGNORECASE)
                highlighted_text = pattern.sub(
                    f'<mark class="search-highlight">{keyword}</mark>',
                    highlighted_text
                )
        
        return format_html(highlighted_text)
    except Exception as e:
        logger.error(f"高亮处理错误: {e}")
        return text 