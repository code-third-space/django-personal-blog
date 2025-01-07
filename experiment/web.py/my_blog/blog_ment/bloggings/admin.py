from django.contrib import admin
from django import forms
from django.http import HttpResponse
from datetime import datetime

from .models import Me_blog, Cities, BlogTypes, Countries

import csv
# Register your models here.

exporttable_fields = ('blog_title','blog_type','creator', 'created_date', 'modified_date')

def export_model_as_csv(ModelAdmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    field_list = exporttable_fields
    response['Content-Disposition'] = 'attachment; filename=blog-title-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d:%H-%M-%S'),
    )

    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in exporttable_fields]
    )
    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    return response
export_model_as_csv.short_description = u'导出数据'

class Me_blogAdminForm(forms.ModelForm):
    class Meta:
        model = Me_blog
        exclude = ('creator', 'created_date', 'modified_date')


class Me_blogAdmin(admin.ModelAdmin):
    form = Me_blogAdminForm

    actions = (export_model_as_csv,)

    search_fields = ('blog_title',)

    # ordering = ('modified_date',)

    # fieldsets = (
    #     (None, {
    #         'fields': ('blog_title','blog_type','blog_detail_one','blog_detail_two','blog_detail_three'),
    #     }),
    # )

    list_filter = ('creator','blog_type')
    list_display = ('blog_title','blog_type','creator', 'created_date', 'modified_date')
    list_display_links = ('blog_title',)

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Me_blog, Me_blogAdmin)