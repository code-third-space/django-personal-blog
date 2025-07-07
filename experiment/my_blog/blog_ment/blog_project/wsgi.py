"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

#将项目路径添加到 sys.path
sys.path.append("/var/www/mY_blog/experiment/web.py/my_blog/blog_ment")

# 2. 找到并加载 .env 文件
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

#设置Django的设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings.production')

application = get_wsgi_application()