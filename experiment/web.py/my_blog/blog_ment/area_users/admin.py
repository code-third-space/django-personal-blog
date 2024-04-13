from django.contrib import admin
from .models import Area_User
from django.utils.html import format_html

# Register your models here.

class Area_Admin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.picture:
            if obj.picture:
                return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
            return ""
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    list_display = ('userid','username', 'city','email','gener','image_tag')

    fieldsets = (
        (None, {'fields': (
           'userid',('username', 'city','phone'),('email','gener','user_remark'),
           ('picture','back_ground')
        )}),
    )

    def save_model(self, request, obj, form, change):  
        obj.creator = request.user                     
        super().save_model(request,obj,form,change) 


admin.site.register(Area_User, Area_Admin)