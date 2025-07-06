from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

UserTypes = [
    ('normal', '普通用户'),
    ('admin', '管理员')
]

class CustomUser(AbstractUser):
    """
    自定义用户模型 扩展django的AbstractUser
    """
    city = models.CharField(max_length=135, verbose_name=_("所在城市"))
    phone = models.CharField(max_length=135, verbose_name=_("手机号码"))
    # 可以移除 email 字段，因为 User 模型已经有 email
    gener = models.CharField(max_length=135, blank=True, verbose_name=_("性别"))
    user_remark = models.CharField(max_length=135, blank=True, verbose_name=_("备注"))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_("头像"))
    back_ground = models.ImageField(upload_to='background/', blank=True, verbose_name=_("背景"))
    user_type = models.CharField(max_length=56, choices=UserTypes, default='normal', verbose_name=_("用户类型"))
    social_links = models.JSONField(blank=True, null=True, verbose_name=_("社交媒体链接"))
    blog_count = models.PositiveIntegerField(default=0, verbose_name=_("博客数量"))
    
    class Meta:
        verbose_name = _("用户")
        verbose_name_plural = _("用户管理")
    
    def __str__(self):
        return self.username


class UserActivity(models.Model):
    """用户活动模型 - 记录阅读历史、点赞等"""
    ACTIVITY_TYPES = [
        ('view', _('浏览')),
        ('like', _('点赞')),
        ('share', _('分享')),
        ('bookmark', _('收藏')),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("用户"))
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, verbose_name=_("文章"))
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES, verbose_name=_("活动类型"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("活动时间"))
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("IP地址"))
    user_agent = models.TextField(blank=True, verbose_name=_("用户代理"))
    
    class Meta:
        verbose_name = _("用户活动")
        verbose_name_plural = _("用户活动")
        ordering = ['-created_at']
        unique_together = ['user', 'article', 'activity_type']
        indexes = [
            models.Index(fields=['user', 'activity_type']),
            models.Index(fields=['article', 'activity_type']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.get_activity_type_display()} - {self.article.title}"


class ArticleBookmark(models.Model):
    """文章收藏模型"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("用户"))
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, verbose_name=_("文章"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("收藏时间"))
    notes = models.TextField(blank=True, verbose_name=_("备注"))
    
    class Meta:
        verbose_name = _("文章收藏")
        verbose_name_plural = _("文章收藏")
        unique_together = ['user', 'article']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} 收藏了 {self.article.title}"


class SearchHistory(models.Model):
    """搜索历史模型"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("用户"))
    query = models.CharField(max_length=200, verbose_name=_("搜索关键词"))
    results_count = models.PositiveIntegerField(default=0, verbose_name=_("结果数量"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("搜索时间"))
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("IP地址"))
    
    class Meta:
        verbose_name = _("搜索历史")
        verbose_name_plural = _("搜索历史")
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['query']),
        ]
    
    def __str__(self):
        return f"{self.user.username} 搜索了 '{self.query}'"


class UserProfile(models.Model):
    """用户资料扩展模型"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("用户"))
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name=_("头像"))
    bio = models.TextField(max_length=500, blank=True, verbose_name=_("个人简介"))
    website = models.URLField(blank=True, verbose_name=_("个人网站"))
    location = models.CharField(max_length=100, blank=True, verbose_name=_("所在地"))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("生日"))
    
    # 偏好设置
    email_notifications = models.BooleanField(default=True, verbose_name=_("邮件通知"))
    theme_preference = models.CharField(
        max_length=20, 
        choices=[('light', _('浅色')), ('dark', _('深色'))],
        default='light',
        verbose_name=_("主题偏好")
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("更新时间"))
    
    class Meta:
        verbose_name = _("用户资料")
        verbose_name_plural = _("用户资料")
    
    def __str__(self):
        return f"{self.user.username} 的资料"
    
    @property
    def full_name(self):
        """获取用户全名"""
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username