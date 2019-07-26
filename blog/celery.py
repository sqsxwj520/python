from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')  # 必须修改模块名

app = Celery()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# 增加以下配置内容
# app的配置
app.conf.broker_url = 'redis://192.168.171.128/0'  # 0号库执行任务队列

app.conf.broker_transport_options = {'visibility_timeout': 43200}  # 过期时间为12小时 12 * 3600
app.conf.result_backend = 'redis://192.168.171.128:6379/1'  # 1号库执行结果

app.conf.update(enable_utc=True, tiemzone='Asia/Shanghai')
