from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'phone', 'city', 'gener', 'user_remark', 'picture', 'back_ground', 'user_type','social_links', 'blog_count', 'is_staff',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'city', 'gener', 'user_remark', 'picture', 'back_ground', 'user_type','social_links', 'blog_count',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'city', 'gener', 'user_remark', 'picture', 'back_ground', 'user_type','social_links', 'blog_count',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)