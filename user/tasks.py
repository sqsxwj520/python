from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from blog.celery import app
from django.conf import settings
import datetime


@app.task(name='send_email')
def send_email():
    send_mail(
        'Active mail',  # 主题
        'Here is the message.',  # 信息
        settings.EMAIL_HOST_USER,  # 发件人的邮箱
        ['17826854776@163.com', ],   # 接收的人的邮箱
        fail_silently=False,
        html_message="<h1>测试激活链接{:%Y%m%d-%H:%M:%S}<br /><a href='{}'\
        target='_blank'>金州勇士</a></h1>".format(datetime.datetime.now(), 'http://www.magedu.com')  # 正文
    )


print('~~~~~~~~~~~~~~~~~~~')
