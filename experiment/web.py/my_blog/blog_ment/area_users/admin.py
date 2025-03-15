from django.contrib import admin, messages
from django import forms
from django.http import HttpResponse
from .models import Area_User
from django.utils.html import format_html
from .dingtalk import send
from .tasks import send_dingtalk_message

import csv
from datetime import datetime

# Register your models here.
exportable_fields = ('user', 'city', 'gener', 'phone', 'user_remark')

def export_model_as_csv(ModelAdmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=blog_project-blogusers-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d:%H-%M-%S')
    )

    writer = csv.writer(response)
    header_row = [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    writer.writerow(header_row)

    for obj in queryset:
        csv_line_value = []
        for field in field_list:
            fields_object = queryset.model._meta.get_field(field)
            field_value = fields_object.value_from_object(obj)
            csv_line_value.append(field_value)
        writer.writerow(csv_line_value)

    return response 
export_model_as_csv.short_description = u'导出为CSV文件'
export_model_as_csv.allowed_permissions = ('export',)

class Area_UserForm(forms.ModelForm):
    class Meta:
        model = Area_User
        fields = '__all__'


def notify_bloguser(ModelAdmin, request, queryset):
    blogusers = ""
    interviewers = ""
    for obj in queryset:
        blogusers = obj.user.username+";"+blogusers
        if obj.user.username:
            interviewers = obj.user.username+";"+interviewers
    send_dingtalk_message.delay("用户 %s 注册通过 %s" % (blogusers, interviewers))

notify_bloguser.short_description = u"注册通知"

class Area_Admin(admin.ModelAdmin):
    form = Area_UserForm
    actions = [export_model_as_csv, notify_bloguser]

    def image_tag(self, obj):
        if obj.picture:
            if obj.picture:
                return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
            return ""
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    list_display = ('user_id','user_name', 'city','user_email','gener','image_tag')

    search_fields = ('user__name', 'user_remark',)
    list_filter = ('city',)
    ordering = ('user',)
    readonly_fields = ('user',)
    list_per_page = 3
    save_on_top = True

    def has_export_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False  

    fieldsets = (
        (None, {'fields': (
        ('user',),('city','phone'),('gener','user_remark'),
        ('picture','back_ground')
        )}),
    )

    def save_model(self, request, obj, form, change):  
        super().save_model(request,obj,form,change)

    def user_id(self, obj):
        return obj.user.id
    user_id.short_description = "用户ID"

    def user_name(self, obj):
        return obj.user.username
    user_name.short_description = "用户名"

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "邮箱"


admin.site.register(Area_User, Area_Admin)