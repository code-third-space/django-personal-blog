from django.contrib import admin
from .models import Candidate, JobsJob, JobsResume

# Register your models here.

admin.site.register(Candidate)
admin.site.register(JobsJob)
admin.site.register(JobsResume)