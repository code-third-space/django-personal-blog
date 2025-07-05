from django.contrib import admin
from django import forms
from .models import Article
from .models import get_subcategories

# Register your models here.

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        blog_type = None
        if self.instance and self.instance.blog_type is not None:
            blog_type = self.instance.blog_type
        subcats = get_subcategories(blog_type) if blog_type is not None else []
        self.fields['subcategory'].widget = forms.Select(
            choices=[('', '---------')] + [(i, name) for i, name in subcats]
        )

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    search_fields = ('title',)
    list_filter = ('author', 'blog_type', 'city', 'country')
    list_display = ('title', 'get_blog_type_display', 'get_subcategory_display', 'author', 'created_at')
    list_display_links = ('title',)
    
    # 在列表中显示分类名称
    def get_blog_type_display(self, obj):
        return obj.get_blog_type_display()
    get_blog_type_display.short_description = '一级分类'

    def get_subcategory_display(self, obj):
        if obj.subcategory is not None and obj.blog_type is not None:
            subcategories = get_subcategories(obj.blog_type)
            for id, name in subcategories:
                if id == obj.subcategory:
                    return name
        return '-'
    get_subcategory_display.short_description = '二级分类'

    def save_model(self, request, obj, form, change):
        if obj.author is None:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    # 自定义表单字段
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'author')
        }),
        ('分类信息', {
            'fields': ('blog_type', 'subcategory'),
            'description': '先选择一级分类，保存后再选择对应的二级分类'
        }),
        ('位置信息', {
            'fields': ('country', 'city')
        }),
        ('内容', {
            'fields': ('content', 'content_middle', 'content_bottom', 'featured_image')
        })
    )

admin.site.register(Article, ArticleAdmin)