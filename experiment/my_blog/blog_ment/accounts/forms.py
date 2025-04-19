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


class ProfileForm(forms.ModelForm):
    """
    用户个人资料编辑表单
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_remark', 'picture', 'phone')
        labels = {
            'user_remark': '个人简介',
            'picture': '头像',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
