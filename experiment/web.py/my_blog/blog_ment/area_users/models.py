from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.


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

    class Meta:
        db_table = u'blog_user'
        verbose_name = _("用户")
        verbose_name_plural = _("用户管理")


    def __unicode__(self):
        return self.username
    
    def __str__(self):
        return self.username