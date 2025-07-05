from django.shortcuts import render
from django.core.cache import cache
from ..models import Article


def search(request):
    titleName = []
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            titleName = Article.objects.filter(title__icontains=q
                ).values('id', 'title', 'content', 'created_at')
            content = {
                'titleName': titleName,
            }
            cache.clear()
            return render(request, "articles/search.html", content)
        cache.clear()
    return render(request, "articles/search.html", {'errors': errors}) 