from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.conf import settings  # 添加此导入
#Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_("内容类型"))
    object_id = models.PositiveIntegerField(verbose_name=_("对象ID"))
    content_object = GenericForeignKey('content_type', 'object_id')
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("用户"))
    text = models.TextField(verbose_name=_("评论内容"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("更新时间"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name=_("楼主评论"))
    is_active = models.BooleanField(default=True, verbose_name=_("是否有效"))
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _("评论")
        verbose_name_plural = _("评论管理")
    
    def __str__(self):
        try:
            username = self.user.username if hasattr(self.user, 'username') else "未知用户"
            content_obj = str(self.content_object) if self.content_object else f"对象(ID:{self.object_id})"
            return f'评论来自{username} 于 {content_obj}'
        except Exception:
            return f'评论ID:{self.id if hasattr(self, "id") else "未知"}'