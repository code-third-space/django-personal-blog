from .base import *
import os

# 本地开发环境配置
DEBUG = True

# 本地数据库配置（可以通过环境变量覆盖）
os.environ.setdefault('DB_ENGINE', 'mysql.connector.django')
os.environ.setdefault('DB_NAME', 'djangodbl')
os.environ.setdefault('DB_USER', 'djangouser')
os.environ.setdefault('DB_PASSWORD', 'django')
os.environ.setdefault('DB_HOST', 'localhost')
os.environ.setdefault('DB_PORT', '3306')

# 本地开发允许的主机
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# 本地开发不需要 HTTPS
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
