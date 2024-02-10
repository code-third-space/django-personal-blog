from django.contrib import admin
from jobs.models import Job  
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date','modified_date')
    
    def save_model(self, request, obj, form, change):  #self: 表示方法所属的类的实例，即 JobAdmin 实例。
        obj.creator = request.user                     #request: 是一个包含有关当前请求的信息的对象，其中包括请求的用户等。
        super().save_model(request,obj,form,change)    #obj: 是当前正在保存的模型实例。
                                                       #form: 是用于保存模型数据的表单。 
                                                       #change: 是一个标志，表示当前是创建新记录还是更新现有记录。
admin.site.register(Job,JobAdmin)
