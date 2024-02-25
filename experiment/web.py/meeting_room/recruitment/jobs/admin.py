from typing import Any
from django.contrib import admin, messages
from jobs.models import Job, Resume
from meetings.models import Candidate
from datetime import datetime

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date','modified_date')
    
    def save_model(self, request, obj, form, change):  #self: 表示方法所属的类的实例，即 JobAdmin 实例。
        obj.creator = request.user                     #request: 是一个包含有关当前请求的信息的对象，其中包括请求的用户等。
        super().save_model(request,obj,form,change)    #obj: 是当前正在保存的模型实例。
                                                       #form: 是用于保存模型数据的表单。 
                                                       #change: 是一个标志，表示当前是创建新记录还是更新现有记录。

def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        #把resume对象中的所有属性拷贝到 candidate 对象中；
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + ',' + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人： %s已经成功进入面试流程' % (candidate_names) )
enter_interview_process.short_description = u'进入面试流程'

from django.utils.html import format_html

class ResumeAdmin(admin.ModelAdmin):
    actions = [enter_interview_process]

    def image_tag(self, obj):
        if obj.picture:
            if obj.picture:
                return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
            return ""
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school','master_school', 'major',
                    'image_tag','created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            'applicant', ('username', 'city',),( 'phone','email',),
            ( 'apply_position', 'born_address'),('gender', 'picture', 'attachment',),
            ('bachelor_school', 'master_school'), ('major', 'degree',), ('created_date', 'modified_date'),
            'candidate_introduction', 'work_experience', 'project_experience',
        )}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job,JobAdmin)
admin.site.register(Resume,ResumeAdmin)