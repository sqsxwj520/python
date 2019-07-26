# from django.shortcuts import render
#
# # Create your views here.
from django.http import HttpRequest, JsonResponse, HttpResponse
import simplejson
import logging
from .models import User
# from django.db.models import Q
from django.conf import settings
import jwt
import datetime
import bcrypt
from django.views.decorators.http import require_http_methods, require_POST  # , require_GET
from utils import json_ify
from django.contrib.sessions.backends.db import SessionStore  # 持久的session
# from ..blog import settings  # 不能这么导入，直接报错 from django.conf import settings
# from django.core.mail import send_mail
from .tasks import send_email


AUTH_HEADER = "HTTP_JWT"  # 浏览器端是jwt，服务器端被修改为全大写的HTTP_JWT

AUTH_EXPIRE = 8 * 60 * 60  # 8小时过期

print(settings.SECRET_KEY)  # bytes

FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def gen_token(user_id):
    # 时间戳用来判断是否过期，以便重发token或重新登录
    return jwt.encode({
        'user_id': user_id,
        'exp': int(datetime.datetime.now().timestamp()) + AUTH_EXPIRE  # 一定要支持过期,exp这个名字不要改

    }, settings.SECRET_KEY).decode()  # 算法取默认的SHA256,结果要字符串


# class BlogAuthMiddleware(object):
#     """自定义认证中间件"""
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # 初始化执行一次
#
#     def __call__(self, request):
#         # 视图函数之前执行
#         # 认证
#         print(type(request), '+++++++++++++++++')
#         print(request.GET)
#         print(request.POST)
#         print(request.body)  # json数据
#         print('-'*30)
#         response = self.get_response(request)
#
#         # 视图函数之后执行
#         return response
# # 要在setting的MIDDLEWARE中注册


def authenticate(view_func):
    """此装饰器的作用是用户认证和验证过期"""

    def wrapper(*args):
        *s, request = args  # args为元组，如果元组只有一个元素，request会先拿；如果元组有多个元素，request会拿最后一个
        session: SessionStore = request.session
        print(session.items(), '~~~~~~~~~~~')
        payload = session  # 这么做只是不想修改下面的代码了

        # print(s, '&&&&&&&&&&&')
        # print(request, '$$$$$$$$$$$$$$$$$$$')
        # <WSGIRequest: GET '/users/test'> $$$$$$$$$$$$$$$$$$$

        # 认证，越早越好
        # print('-----------')
        # jwt_header = request.META.get(AUTH_HEADER, '')
        # print(jwt_header, '*********')  # 生产环境中，所有测试代码用logging.debug,所有输出使用logging.info
        #
        # if not jwt_header:
        #     print('00000000000000000000')
        #     return HttpResponse(status=401)
        # print(jwt_header, '*********')
        #
        # # 解码
        # try:
        #     payload = jwt.decode(jwt_header, settings.SECRET_KEY, algorithms=['HS256'],
        #                          options={'verify_signature': True})
        #     print(payload)
        # except Exception as e:  # 解码同时验证过期，有任何异常，都不能通过认证
        #     logging.error(e)
        #     print('1111111111111111')
        #     return HttpResponse(status=401)

        print('-' * 30)

        # 查询数据库,虽然前面的验证通过，但是此用户可能已经被禁用，一定要查
        user_id = payload.get('user_id', 0)
        if user_id == 0:
            print('222222222222222222222')
            return HttpResponse(status=401)

        try:
            user = User.objects.get(pk=user_id)
            request.user = user  # 动态增加属性
        except Exception as e:
            logging.error(e)
            return HttpResponse(status=401)

        res = view_func(*args)  # 注意这里的*args是参数解构
        return res

    return wrapper


# 用户注册
@require_POST
def reg(request: HttpRequest):
    # print(request.GET)
    # print(request.POST)
    # print(request.content_type)
    # print(request.body)
    # print(simplejson.loads(request.body))

    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        # 先查询email是否已经存在
        u = User.objects.filter(email=email).first()  # objects为默认的管理器
        if u:
            return JsonResponse({'error': "用户名已存在"}, status=400)
        name = payload['name']
        password = payload['password'].encode()
        print(email, name, password)

        # 写入数据库
        user = User()
        user.email = email
        user.name = name
        user.password = bcrypt.hashpw(password, bcrypt.gensalt()).decode()

        print(user)  # 因为没有提交到数据库，所以数据库中并没有此条记录，所以其id为None

        # try:
        #     user.save()  # save会自动事务提交，当然提交失败，会自动回滚；此处不需要处理异常了，因为如果此处出现异常，会直接执行下文的except
        #
        # except:
        #     logging.info(e)
        #     raise

        user.save()  # 自动提交
        print(user)

        return JsonResponse({'a': 1000}, status=201)  # 如果正常，返回json数据
    except Exception as e:
        logging.info(e)
        # return HttpResponseBadRequest()  # 这里返回实例，这不是异常类,不能raise，python中非异常类的子类是不能raise的
        return JsonResponse({'error': "用户名已存在"}, status=400)


@require_POST  # 只允许post请求的方式登录
def login(request: HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        print(payload, '+++++++++++')
        email = payload['email']
        password = payload['password'].encode()
        print(password, '%%%%%%%%%%', type(password))

        user = User.objects.get(email=email)  # 只有一条

        print(user.password, '~~~~~~~~~', type(password))
        if bcrypt.checkpw(password, user.password.encode()):
            # # 验证成功
            # token = gen_token(user.id)
            # res = JsonResponse({
            #     # 'use_id': user.id,
            #     # 'email': email,
            #     # 'name': user.name,
            #     'user': json_ify(user, exclude=('password', )),
            #     'token': token
            # })
            # # res.set_cookie('jwt', token)
            # return res
            session: SessionStore = request.session
            print(type(session), session)
            print(session.keys())
            session.set_expiry(300)  # 会话过期，单位秒
            session['user_id'] = user.id
            # 对于频繁需要使用的数据，使用字符串拼出来，省得还要从数据库中查询
            session['user_info'] = "{} {} {}".format(user.id, user.name, user.email)
            res = JsonResponse({
                'user': json_ify(user, exclude=['password']),
                'user_info': session['user_info']
            })

            return res
        else:
            return JsonResponse({'error': "用户名或密码错误"}, status=400)
    except Exception as e:
        logging.error(e)
        # 失败返回错误信息和400，所有其他错误一律用户名密码错误；有时候错误信息不宜太详细
        return JsonResponse({'error': "用户名或密码错误"}, status=400)


@require_POST
# @authenticate
def logout(request: HttpRequest):
    session = request.session
    print(session.items())
    # print(session.session.key)
    if session.get('user_id'):
        info = "{} 登出成功.".format(session['user_id'])
        del request.session['user_id']  # 不会清除数据库中的记录
        request.session.flush()  # 清空当前session，删除表（django_session）对应的记录
        return HttpResponse(info, status=200)
    else:
        return HttpResponse('登出失败', status=400)


def test_send_email(request: HttpRequest):
    print(request)
    try:
        # 用户注册了，注册信息保存了，然后发邮件给他，里面写激活邮件已发出，请等待5分钟查收
        # send_mail()，这样写就没有用到celery
        send_email.delay()
        return HttpResponse('激活邮件已发出，请等待5分钟查收', status=204)
    except Exception as e:
        logging.error(e)
        return JsonResponse({"error": "邮件发送失败"}, status=400)

    # cls = type(instance)
    #
    # fields = cls._meta.fields
    # # print(cls)
    # # print(fields)
    # for f in fields:
    #     print(f, f.name)
    #     if f.name in exclude:
    #         continue
    #     print(getattr(instance, f.name))

#
# @require_http_methods(['POST', 'GET'])  # 允许GET、POST方法
# # @authenticate  # 在需要的视图函数上加此装饰器，建议此装饰器写在下面
# def test(request: HttpRequest):
#     session = request.session
#     print(session.items())
#     print(session.session.key)
#
#     if session.get('user_id'):
#         # print(request)
#         print('view function +++++++++++++++++++')
#         print(request.user, '~~~~~~~~')
#         print('===================================')
#
#         return JsonResponse({'test': 'ok~~~~~~~~~'})
#     else:
#         return HttpResponse('未认证', status=401)

    # user = User(id=1, name='sun', email='17826854776@163.com')
    # json_ify(user, exclude=['email'])
    #
    # return JsonResponse({'test': 'ok'})

    # User.objects.filter(email='sd')
    # email = '17826854776@163.com'
    # qs = User.objects.filter(email='17826854776@163.com').all()
    # print([x for x in qs])
    # print([x for x in qs])
    # qs = User.objects.all()
    # print(qs.all()[1:])
    # print(qs.values())  # values返回一个对象字典的列表，列表中的元素是字典，字典内是字段和值的键值对
    # print(qs.filter(pk=1).values())  # pk就是主键的意思，在这里等价于id
    # print(qs.exclude(id=1).values())  # exclude意思是除了什么之外
    # print(qs.exclude(id=2).order_by('-id'))  # id前的减号意味着降序排列
    #
    # email = '17826854776@163.com'
    # print(qs.get(email=email))  # 只能返回一个结果
    # print(qs.filter(id=1).get())
    #
    # print(qs.filter(email__contains="sqs.com"))
    # print(qs.filter(id__in=[1, 3]))
    # print(qs.filter(id__gt=1))  # 过滤id大于1的，注意不包括等于
    # print(qs.filter(id__gte=1))  # id >= 1
    # print(qs.filter(email__startswith='chang'))
    #
    # # Q对象 & | ~
    # print(qs.filter(pk__lt=5).filter(pk__gt=2))  # 与
    # print(qs.filter(Q(pk__lt=5) & Q(pk__gt=2)))
    # print(qs.filter(Q(pk__lt=5) | Q(pk__gt=2)))
    # print(qs.filter(~Q(pk__lt=5)))  # pk >= 5
    # print(qs.exists())  # 老师课件上没有加s


# def send_email():  # SMTP（简单邮件发送协议）
#     send_mail(
#         'Active mail',  # 主题
#         'Here is the message.',  # 信息
#         "magetest@magedu.com",  # 发件人的邮箱
#         ['17826854776@163.com', ],   # 接收的人的邮箱
#         fail_silently=False,
#         html_message="<h1>测试激活链接<a href='http://www.magedu.com' target='_blank'>magedu.com</a></h1>"  # 正文
#     )
#
#     print('*' * 30)


@require_http_methods(['POST', 'GET'])
def test(request: HttpRequest):
    print(request)
    try:
        send_email()

    except Exception as e:
        logging.error(e)
        return JsonResponse({'error': "邮件发送失败"}, status=500)

    return HttpResponse(status=204)
