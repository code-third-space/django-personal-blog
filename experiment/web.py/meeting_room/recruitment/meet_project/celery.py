from __future__ import absolute_import, unicode_literals

import os
import django

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
django.setup()

app = Celery('meet_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_connection_retry_on_startup = True

@app.task(bind=True)
def debug_task(self):
    print("Resquest: {0!r}".format(self.request))


from .tasks import add
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'meet_project.tasks.add',
        'schedule': 10.0,
        'args':(16, 4,)
    },
}


from celery.schedules import crontab

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s("hello"), name='hello every 10')

    sender.add_periodic_task(30.0, test.s('World'), expires = 10)

    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


# import json
# from django_celery_beat.models import PeriodicTask, IntervalSchedule

# schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS,)

# task = PeriodicTask.objects.create(interval=schedule, name='say welcome ', task='meet_project.tasks.test', args=json.dumps(['welcome']),)


@app.task
def test(arg):
    print(arg)