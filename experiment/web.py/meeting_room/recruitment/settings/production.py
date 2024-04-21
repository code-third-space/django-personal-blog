import os
from .base import *

ALLOWED_HOSTS = ['127.0.0.1', "host.docker.internal", "*"]

SECRET_KEY = 'django-insecure-8!ljr^j%1#=19*)405lw$f6mk$l)!sdo6*&24556349u1)-9ed'

DEBUG=False

INSTALLED_APPS += (
    # 'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1',
]