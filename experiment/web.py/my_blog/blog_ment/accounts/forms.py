from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    自定义用户创建表单
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'city', 'gener', 'user_remark', 'picture', 'back_ground', 'user_type', 'social_links', 'blog_count' )

class CustomUserChangeForm(UserChangeForm):
    """
    自定义用户修改表单
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'city', 'gener', 'user_remark', 'picture', 'back_ground', 'user_type','social_links', 'blog_count' )
        exclude = ('password',)  # 排除密码字段，因为密码通常不应该在修改表单中显示
