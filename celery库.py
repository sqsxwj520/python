# from celery import Celery
#
#
# # app = Celery('my_task')  # my_task为名字
# app = Celery()
# print(type(app), app)
# # <class 'celery.app.base.Celery'> <Celery my_task at 0x21f0a58>
#
#
# @app.task(name='sun')
# def add(x, y):
#     return x + y
#
#
# # print(add.name)  # my_task.add
# print(add.name)  # sun
# print(add)
#
# print(app.tasks)
# print(app.conf)
# print(*list(app.conf.items()), sep='\n')


from django.core.mail import send_mail


def email():  # SMTP（简单邮件发送协议）
    send_mail(
        'Active mail',  # 主题
        'Here is the message.',  # 信息
        'from@example.com',  # 发件人的邮箱
        ['to@example.com'],   # 接收的人的邮箱
        fail_silently=False,
        html_message=""  # 正文
    )
