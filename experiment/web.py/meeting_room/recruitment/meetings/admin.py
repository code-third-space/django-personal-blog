from django.contrib import admin, messages
from django.http import HttpResponse
from django.db.models import Q
from django.utils.safestring import mark_safe

from meetings.models import Candidate
from meetings import candidate_fieldset as cf
from .tasks import send_dingtalk_message
from jobs.models import Resume

# Register your models here.
import logging
import csv
from datetime import datetime

logger = logging.getLogger(__name__)

#定义可导出的字段
exportable_fields = ('username','city','phone','bachelor_school','master_school','degree',
                     'first_result','first_interviewer_user','second_result','second_interviewer_user',
                     'hr_result','hr_score','hr_remark','hr_interviewer_user',)

#通知一面面试官面试
def notify_interviewer(modeladmin, request, queryset):
     candidates = ""
     interviewers = ""
     for obj in queryset:
         candidates = obj.username + ";" + candidates
         if obj.first_interviewer_user and obj.first_interviewer_user.username:
            interviewers = obj.first_interviewer_user.username + ";" + interviewers
     send_dingtalk_message.delay("候选人 %s 进入面试环节，亲爱的面试官，请做好面试准备: %s" % (candidates, interviewers))
     messages.add_message(request, messages.INFO, '已经成功通知面试')

notify_interviewer.short_description = u"通知一面面试官"

#自定义动作函数
def export_model_as_csv(ModelAdmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=recruitment-candidates-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d:%H-%M-%S'),
    )
    #创建CSV写入器
    writer = csv.writer(response)
    #写入CSV表头
    # writer.writerow(
    #     [ queryset.model._meta.get_field(f).verbose_name.title() for f in field_list ]
    # )
    header_row = [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    writer.writerow(header_row)
    
    #便利查询集 并将数据写入CSV文件
    for obj in queryset:
        csv_line_value = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_value.append(field_value)
        writer.writerow(csv_line_value)

    logger.info("%s exported %s candidate records" % (request.user, len(queryset)))

    return response

export_model_as_csv.short_description = u'导出为CSV文件'
export_model_as_csv.allowed_permissions = ('export',)

#候选人管理类

class CadnidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date',)

    actions = [export_model_as_csv, notify_interviewer]

    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, 'export'))

    list_display = (
        "username", "city", "bachelor_school", "get_resume",
        "first_score", "first_result", "first_interviewer_user",
        "second_result", "second_interviewer_user",
        "hr_score", "hr_result",
        "last_editor",
    )

    #筛选字段
    list_filter = ('city','first_result','second_result','hr_result',
                   'first_interviewer_user','second_interviewer_user','hr_interviewer_user')

    #查询字段
    search_fields = ('username','phone','email','bachelor_school',)

    #排序字段
    ordering = ('hr_result','second_result','first_result')

    #默认可编辑字段
    default_list_editable = ('first_interviewer_user','second_interviewer_user',)

    def get_resume(self, obj):
        if not obj.phone:
            return ""
        resumes = Resume.objects.filter(phone=obj.phone)
        if resumes and len(resumes) > 0:
            return mark_safe(u'<a href="/resume/%s" target="_blank">%s</a>' % (resumes[0].id, "查看简历"))
        return ""
    
    get_resume.short_description = u'查看简历'
    

    #获取可编辑字段
    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)
        
        if request.user.is_superuser or 'hr' in group_names:
            return self.default_list_editable
        return()
    
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CadnidateAdmin, self).get_changelist_instance(request)
    #获取当前用户组
    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names or []
    
    #对于非管理员，非HR，获取自己是一面面试官或者二棉面试官的候选人集合
    def get_queryset(self, request):
        qs = super(CadnidateAdmin, self).get_queryset(request)
        
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'hr' in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user) 
        )
    #获取只读字段
    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names:
            logger.info("interviewer is in user's group for %s" % request.user.username)
            return ('first_interviewer_user', 'second_interviewer_user',)
        return()
    #获取字段集合
    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names and obj.first_interviewer_user  == request.user:
            return cf.default_fieldsets_first
        elif 'interviewer' in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        return cf.fieldsets

admin.site.register(Candidate, CadnidateAdmin)