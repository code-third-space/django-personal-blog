from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    自定义用户创建表单：仅展示 username, email, password1, password2
    并在保存时为模型中其它必填字段赋默认值。
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # 只要用户名和邮箱

    def save(self, commit=True):
        # 先拿到未入库的实例
        user = super().save(commit=False)
        # 以下字段在模型中是必填的，这里统一赋默认值
        user.city          = ''          # 或者 '未知'
        user.phone         = ''          # 或者 '000-0000-0000'
        user.gener         = ''
        user.user_remark   = ''
        user.picture       = None        # ImageField 留空
        user.back_ground   = None
        user.user_type     = 'normal'    # 默认用户类型
        user.social_links  = {}          # JSONField 赋空 dict
        user.blog_count    = 0

        if commit:
            user.save()
        return user

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
