from django.shortcuts import render
from jobs.models import Job, Resume
from jobs.models import Cities, JobTypes
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
# Create your views here.

import logging

logger = logging.getLogger(__name__)

def register(request):
    context = {
        
    }
    return render(request, 'jobs/base.html', context)

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]
    context = {"job_list":job_list}

    return render(request, 'jobs/joblist.html', context)

def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        logger.info('job info fetched from database jobid:%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'jobs/job.html',{'job':job})

class ResumeDetailView(DetailView):
    #简历详情页
    model = Resume
    templates_name = 'resume_detail.html'


class ResumeCreateView(LoginRequiredMixin, CreateView):
    #简历职位页面
    template_name = 'jobs/resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = [
        'username', 'city', 'phone', 
        'email', 'apply_position', 'gender', 'picture', 'attachment',
        'bachelor_school', 'master_school', 'major', 'degree',
        'candidate_introduction', 'work_experience', 'project_experience',
    ]
    #从URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial
    
    #简历跟当前用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 