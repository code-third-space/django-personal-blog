from .base import *

ALLOWED_HOSTS = ["recruit.ihopeit.com",'127.0.0.1']

LDAP_AUTH_CONNECTION_USERNAME = None

LDAP_AUTH_CONNECTION_PASSWORD = None

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