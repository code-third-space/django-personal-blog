from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from comments.models import Comment
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from .constants import get_subcategories


class Article(models.Model):
    """博客文章模型（更专业的命名替代原Me_blog）"""
    title = models.CharField(max_length=56, blank=False, verbose_name=_("标题"))
    blog_type = models.SmallIntegerField(blank=False, choices=[
        [0, "Python"],
        [1, "Web"],
        [2, "Backend"],
        [3, "Database"],
        [4, "Algo"],
        [5, "Tools"],
    ], verbose_name=_("主分类"))
    subcategory = models.SmallIntegerField(blank=True, null=True, verbose_name=_("二级分类"))
    country = models.SmallIntegerField(blank=False, choices=[
        [0, "中国"],
        [1, "美国"],
        [2, "俄罗斯"],
    ], verbose_name=_("所在国家"))
    city = models.SmallIntegerField(blank=False, choices=[
        [0, "北京"],
        [1, "上海"],
        [2, "深圳"],
        [3, "杭州"],
        [4, "成都"],
        [5, "长沙"],
        [6, "南京"],
        [7, "重庆"],
        [8, "贵州"],
        [9, "武汉"],
        [10, "纽约"],
        [11, "华盛顿"],
        [12, "洛杉矶"],
        [13, "加州"],
        [14, "德克萨斯州"],
        [15, "莫斯科"],
    ], verbose_name=_("所在城市"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("作者"), null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name=_("创建时间"), default=datetime.now)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), default=datetime.now)
    content = models.TextField(max_length=10240, blank=True, null=True, verbose_name=_("正文"))
    content_middle = models.TextField(max_length=1024, blank=True, null=True, verbose_name=_("正文中部"))
    content_bottom = models.TextField(max_length=1024, blank=True, null=True, verbose_name=_("正文下部"))
    featured_image = models.ImageField(upload_to='blog_images', blank=True, verbose_name=_("特色图片"))
    comments = GenericRelation(Comment)
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("浏览次数"))
    
    class Meta:
        verbose_name = _("文章")
        verbose_name_plural = _("文章")
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_subcategory_display(self):
        """获取二级分类的显示名称"""
        if self.blog_type is not None and self.subcategory is not None:
            subcategories = get_subcategories(self.blog_type)
            for id, name in subcategories:
                if id == self.subcategory:
                    return name
        return ""
