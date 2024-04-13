from django.contrib import admin
from django import forms
from .models import Me_blog, Cities, BlogTypes, Countries
# Register your models here.


class Me_blogAdminForm(forms.ModelForm):
    class Meta:
        model = Me_blog
        exclude = ('creator', 'created_date', 'modified_date')

class Me_blogAdmin(admin.ModelAdmin):
    form = Me_blogAdminForm

    search_fields = ('blog_title',)

    # ordering = ('created_date',)

    list_filter = ('creator',)
    list_display = ('blog_title','creator', 'created_date', 'modified_date')
    list_display_links = ('blog_title',)

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Me_blog, Me_blogAdmin)