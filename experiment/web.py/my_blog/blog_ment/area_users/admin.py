from django.contrib import admin
from django import forms
from .models import Area_User
from django.utils.html import format_html

# Register your models here.
class Area_UserForm(forms.ModelForm):
    class Meta:
        model = Area_User
        fields = '__all__'

class Area_Admin(admin.ModelAdmin):
    form = Area_UserForm

    def image_tag(self, obj):
        if obj.picture:
            if obj.picture:
                return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
            return ""
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    list_display = ('userid','username', 'city','email','gener','image_tag')

    readonly_fields = ('userid',)

    fieldsets = (
        (None, {'fields': (
        ('userid',),('username', 'city','phone'),('email','gener','user_remark'),
        ('picture','back_ground')
        )}),
    )

    def save_model(self, request, obj, form, change):  
        obj.creator = request.user                     
        super().save_model(request,obj,form,change) 


admin.site.register(Area_User, Area_Admin)