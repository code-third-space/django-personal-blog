from django.contrib.syndication.views import Feed
from .models import Article # 假设你的文章模型为 Blog，如有不同请调整

class LatestArticlesFeed(Feed):
    title = "最新博客文章"
    link = "/rss/"
    description = "本站最新发布的博客文章"

    def items(self):
        return Article.objects.order_by('-created_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100] if item.content else ""

    def item_link(self, item):
        return f"/blog_detail/{item.id}/" 