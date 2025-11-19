import os
import sys

# مسیر پروژه‌ت رو عوض کن با اسم فولدر settingsت (مثل prj)
path = '/usr/src/app'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # prj رو با اسم فولدرت عوض کن (مثل mysite.settings)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()