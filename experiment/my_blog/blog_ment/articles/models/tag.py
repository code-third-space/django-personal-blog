from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Tag(models.Model):
    """文章标签模型"""
    name = models.CharField(max_length=50, unique=True, verbose_name=_("标签名称"))
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name=_("URL别名"))
    description = models.TextField(max_length=200, blank=True, verbose_name=_("标签描述"))
    color = models.CharField(max_length=7, default="#007bff", verbose_name=_("标签颜色"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))
    
    class Meta:
        verbose_name = _("标签")
        verbose_name_plural = _("标签")
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """获取标签的绝对URL"""
        from django.urls import reverse
        return reverse('articles:tag_detail', kwargs={'slug': self.slug})
    
    @property
    def article_count(self):
        """获取使用该标签的文章数量"""
        return self.articles.count() 