from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

# LDAP_AUTH_CONNECTION_USERNAME = None

# LDAP_AUTH_CONNECTION_PASSWORD = None

SECRET_KEY = 'django-insecure-8!ljr^j%1#=19*)405lw$f6mk$l)!sdo6*&24556349u1)-9ed'

DEBUG = True

INSTALLED_APPS = [
    'jobs',
    'meetings',
    'django_python3_ldap',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")