''' @File :asgi.py @Author:张宇 @Date :2020/9/30 17:52 @Desc : '''
import os
import django
from channels.routing import get_default_application
from pathlib import Path
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()
application = get_default_application()