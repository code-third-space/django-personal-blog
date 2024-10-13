from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.

UserTypes = [
    ('normal', '普通用户'),
    ('admin', '管理员')
]

class Area_User(models.Model):
    userid = models.AutoField(primary_key=True, verbose_name=_("用户ID"))
    creator = models.ForeignKey(User, verbose_name=_("创作者"), null=True, on_delete=models.PROTECT)
    username = models.CharField(max_length=135, verbose_name=_("用户名"))
    city = models.CharField(max_length=135, verbose_name=_("所在城市"))
    phone = models.CharField(max_length=135, verbose_name=_("手机号码"))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_("邮箱"))
    gener = models.CharField(max_length=135, blank=True, verbose_name=_("性别"))
    user_remark = models.CharField(max_length=135, blank=True, verbose_name=_("备注"))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_("头像"))
    back_ground = models.ImageField(upload_to='background/', blank=True, verbose_name=_("背景"))
    user_type = models.CharField(max_length=56, choices=UserTypes, default='normal', verbose_name=_("用户类型"))
    social_links = models.JSONField(blank=True, null=True, verbose_name=_("社交媒体链接"))
    blog_count = models.PositiveIntegerField(default=0, verbose_name=_("博客数量"))

    class Meta:
        db_table = u'blog_user'
        verbose_name = _("用户")
        verbose_name_plural = _("用户管理")

        permissions = [
            ('notify', "notify interviewer for blogusers"),
        ]


    def __unicode__(self):
        return self.username
    
    def __str__(self):
        return self.username