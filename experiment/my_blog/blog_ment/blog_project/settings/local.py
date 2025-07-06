from .base import *
import os

# 本地开发环境配置
DEBUG = True

# 本地开发允许的主机
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# 本地开发不需要 HTTPS
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
