from .base import *
import os

# 生产环境配置
DEBUG = False

# 生产环境数据库配置（必须通过环境变量设置）
# 这些环境变量需要在服务器上设置
DB_ENGINE = os.getenv('DB_ENGINE', 'mysql.connector.django')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')

# 验证必要的环境变量
if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise ValueError("生产环境必须设置 DB_NAME, DB_USER, DB_PASSWORD 环境变量")

# 更新数据库配置
DATABASES['default'].update({
    'ENGINE': DB_ENGINE,
    'NAME': DB_NAME,
    'USER': DB_USER,
    'PASSWORD': DB_PASSWORD,
    'HOST': DB_HOST,
    'PORT': DB_PORT,
})

# 生产环境允许的主机
ALLOWED_HOSTS = [
    "127.0.0.1", 
    "47.109.32.142", 
    "www.pepopen.cn", 
    "localhost"
]

# CSRF 的配置
CSRF_TRUSTED_ORIGINS = [
    'https://47.109.32.142',
    'https://www.pepopen.cn',
    'https://127.0.0.1',
    'https://localhost'
]

# 设置 CSRF cookie 安全选项
CSRF_COOKIE_SECURE = True  # 仅在 HTTPS 上发送 CSRF cookie

# HTTPS 的配置
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True  # 自动将 HTTP 请求重定向到 HTTPS

# 生产环境安全设置
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'