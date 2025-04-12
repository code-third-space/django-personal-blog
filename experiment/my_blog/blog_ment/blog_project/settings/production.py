from .base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "47.109.32.142", "www.pepopen.cn", "localhost"]

# CSRF 的配置
CSRF_TRUSTED_ORIGINS = ['https://47.109.32.142','https://www.pepopen.cn','https://127.0.0.1','https://localhost']
# 设置 CSRF cookie 安全选项
CSRF_COOKIE_SECURE = True  # 仅在 HTTPS 上发送 CSRF cookie

# HTTPS 的配置
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True # 自动将 HTTP 请求重定向到 HTTPS