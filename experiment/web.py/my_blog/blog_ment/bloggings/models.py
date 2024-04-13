from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.


BlogTypes = [
    [0, "技术类"],
    [1, "实事类"],
    [2, "财经类"],
    [3, "阅读类"],
    [4, "风景类"],
    [5, "商品类"],
]

Countries = [
    [0, "中国"],
    [1, "美国"],
    [2, "俄罗斯"],
]

Cities = [
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
]

class Me_blog(models.Model):
    blog_title = models.CharField(max_length=56, blank=False, verbose_name=_("标题"))
    blog_type = models.SmallIntegerField(blank=False, choices=BlogTypes, verbose_name=_("博客类型"))
    blog_countries = models.SmallIntegerField(blank=False, choices=Countries, verbose_name=_("所在国"))
    blog_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name=_("所在城市"))
    creator = models.ForeignKey(User, verbose_name=_("创作者"), null=True, on_delete=models.PROTECT)
    created_date = models.DateTimeField(verbose_name=_("创建日期"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("修改时间"), default=datetime.now)
    blog_detail = models.TextField(max_length=4096, verbose_name=_("正文"))
    picture = models.ImageField(upload_to='picture', blank=True, verbose_name=_("图片"))

    class Meta:
        verbose_name = _("博客")
        verbose_name_plural = _("博客展示")