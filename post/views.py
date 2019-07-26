from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from django.views import View
from user.views import authenticate
from utils import json_ify
import datetime
from .models import Post, Content
# from user.models import User
import simplejson
import logging
from django.db import transaction
from utils import d
import math
# from django.db.models import Q


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def validate(dic: dict, name: str, default, validate_func):

    try:
        r = int(dic.get(name, default))
        ret = validate_func(r, default)
    except Exception as e:
        logging.error(e)
        ret = default
    return ret


class PostView(View):  # 不需要装饰器决定方法了

    def get(self, request: HttpRequest):  # 获取全体文章走这里
        print('get ~~~~~~~~~~~')

        page = validate(request.GET, 'page', 1, lambda x, y: x if x > 0 else y)
        print(page)

        # try:  # 页码
        #     page = int(request.GET.get('page', 2))
        #     page = page if page > 0 else 1
        # except Exception as e:
        #     logging.error(e)
        #     page = 1
        #
        # try:  # 每页条数（每页最多能写多少行）
        #     # 注意，这个数据不要轻易让浏览器端改变，如果允许改变，一定要控制范围
        #     size = int(request.GET.get('size', 2))
        #     size = size if 0 < size < 101 else 20
        # except Exception as e:
        #     logging.error(e)
        #     size = 20

        size = validate(request.GET, 'size', 20, lambda x, y: x if 0 < x < 101 else y)

        try:  # 每页条目数
            start = (page - 1) * size

            posts = Post.objects.order_by('-pk')  # 根据主键降序排列
            total = posts.count()

            posts = posts[start: start + size]
            print(posts.query, '77777777777777777')
            # SELECT `post`.`id`, `post`.`title`, `post`.`postdate`, `post`.`author_id`
            # FROM `post` ORDER BY `post`.`id` DESC LIMIT 2 OFFSET 2 7777777777

            return JsonResponse({
                'posts': [
                    json_ify(post, allow=['id', 'title'])
                    for post in posts
                ],  # 列表解析式
                'pagination': {
                    'page': page,
                    'size': size,
                    'total': total,
                    'pages': math.ceil(total / size)
                }
            }, status=200)

        except Exception as e:
            logging.error(e)
            return JsonResponse(d['400'], status=400)

    @authenticate
    def post(self, request: HttpRequest):  # 提交文章数据走这里
        print('post +++++++++++')

        post = Post()
        content = Content()
        try:
            payload = simplejson.loads(request.body)
            print(payload, '~~~~~~~~~~~++++++++++++')
            post.title = payload['title']
            text = payload['content']
            # post.author = User(id=request.user.id)  # 这是一个对象，包含user的id、name、email、password
            post.author = request.user  # 一个对象，推荐使用这种写法
            post.postdate = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=8)))  # 数据库存放的是UTC（世界统一时间），与北京时间差8小时

            # post.save()  # post已经save后（注意save会自动提交），如果出现异常，那么异常后的代码是执行不了的，（content是没法save的）
            # raise Exception()  # 抛出异常
            # 该怎么解决呢？利用事务的原子性；另外还要注意，post必须要小save了，content才能save，两者顺序不能换

            with transaction.atomic():  # 原子操作
                post.save()  # save完后，post表的id就有了

                content.post = post  # 考虑此处为什么是post，而不是post.id ==》此处的写法是Content定义时，就是一对一引用Post
                content.content = text

                # print(content.post, '^^^^^^^^^^^^')  # 注意这两句是不能打印的，直接报错'str' object is not callable
                # print(content.content, '###########')

                content.save()

            return JsonResponse({
                'post': json_ify(post, allow=['id', 'title'])
            }, status=201)  # 增加成功，状态码用201，不要随便修改
        except Exception as e:
            logging.error(e)
            return JsonResponse({'error': '用户输入错误'}, status=400)


# 更新、修改
@authenticate
def put(request: HttpRequest):
    print('put ~~~~~~~~~~~~~~~~~~~')

    # post = Post()
    # content = Content()

    try:
        payload = simplejson.loads(request.body)
        _id = payload["id"]
        post = Post.objects.get(pk=_id, author_id=request.user.id)
        content = Content.objects.get(pk=_id)

        print(payload, '6666666666')

        title = payload['title']

        post.title = title
        content.content = payload['content']
        post.postdate = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8)))

        with transaction.atomic():
            post.save()
            content.save()

        return JsonResponse({
            'post': {
                'author': post.author.name,
                'author_id': post.author_id,
                'title': post.title,
                'postdate': post.postdate,
                'content': post.content.content
            }
        }, status=201)

    except Exception as e:
        logging.error(e)
        return JsonResponse(d['400'], status=400)


@authenticate
def delete(request: HttpRequest):
    print('delete ~~~~~~~~~~~~~~')
    print(request)

    try:
        payload = simplejson.loads(request.body)

        _id = payload['id']

        post = Post.objects.get(pk=_id)
        content = Content.objects.get(pk=_id)

        # content.content = payload['content']
        post.postdate = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8)))

        author_id = post.author_id

        if author_id != request.user.id:
            return JsonResponse(d['400'], status=400)

        post.delete = True
        content.delete = True

        with transaction.atomic():
            post.save()
            content.save()

        return HttpResponse(status=204)
        # return JsonResponse({
        #     'post': {
        #         'id': post.id,
        #         'author': post.author.name,
        #         'author_id': post.author_id,
        #         'postdate': post.postdate,
        #         'content': post.content.content
        #     }
        #
        # }, status=204)

    except Exception as e:
        logging.error(e)
        return JsonResponse(d['400'], status=400)


@require_GET
def get_post(request: HttpRequest, _id):  # 详情页，查看一篇文章，与文章相关的所有信息都应该返回
    print(request)
    # print(_id, type(_id))  # 类型是字符串
    try:
        _id = int(_id)
        post = Post.objects.get(pk=_id)  # only one
        print(post, '101010100101010100')
        return JsonResponse({
            'post':
                {
                    'id': post.id,
                    'title': post.title,
                    'postdate': int(post.postdate.timestamp()),
                    'author': post.author.name,
                    'author_id': post.author_id,  # post.author.id
                    'content': post.content.content  # 后面的content.content就是上面的text
                }
        })
    except Exception as e:
        logging.error(e)
        return JsonResponse(d['404'], status=404)
