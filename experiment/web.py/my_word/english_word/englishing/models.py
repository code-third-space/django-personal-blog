from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy

# Create your models here.

class English_Word(models.Model):
    word_english = models.CharField(max_length=56,blank=False,verbose_name=_("单词英文"))
    word_chinese = models.CharField(max_length=56,blank=False,verbose_name=_("单词中文"))
    word_definition = models.CharField(max_length=256,blank=False,verbose_name=_("单词释义"))
    word_root = models.CharField(max_length=56,blank=False,verbose_name=_("单词词根"))