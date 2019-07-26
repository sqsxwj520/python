"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpRequest  # , HttpResponse  # , JsonResponse
# from django.template import loader
from django.shortcuts import render
import datetime


def index(request: HttpRequest):
    """视图函数：请求进来返回响应"""
    # return HttpResponse(b"welcome to Golden State Warriors!")
    # d = {}
    # d['method'] = request.path
    # d['path'] = request.path
    # d['path_info'] = request.path_info
    # d['qs'] = request.GET
    #
    # return JsonResponse(d, status=201)
    # template = loader.get_template('index.html')  # 加载器模板搜索模板并加载它
    # print(template.origin)  # 显示模板路径
    # context = {'content': 'www.magedu.com'}  # 数据字典
    #
    # return HttpResponse(template.render(context, request))

    # abc = "我是内容".encode()
    # res = HttpResponse(b'<html><body>' + abc + b'</body></html>')  # 这样写太麻烦了，早就不用这么写了
    # return res
    # my_dict = {
    #     'a': 1,
    #     'b': 0,
    #     'c': list('abcdefghijklmn'),
    #     'e': list(range(1, 10)),
    #     'd': {'x': 1000, 'y': 200},
    #     'date': datetime.datetime.now()
    # }
    #
    new_dict = {
        'a': 100,
        'b': 0,
        'c': list(range(10, 20)),
        'd': 'abc',
        'date': datetime.datetime.now(),
        'f': list(range(1, 10))
    }

    # content = {
    #     'a': 100,
    #     'b': 0,
    #     'c': list(range(10)),
    #     'd': {'x': 1000, 'y': 200},
    #     'date': datetime.datetime.now()
    # }

    # res = render(request, 'index.html', content)
    # return res

    # context = {'content': 'www.magedu.com', 'my_dict': my_dict}
    context = {'content': 'www.magedu.com', 'new_dict': new_dict}
    return render(request, 'index.html', context)


urlpatterns = [
    # 下面三个有一个即可
    url(r'^admin/', admin.site.urls),  # url在 2.x版本 re_path
    url(r'^$', index),
    url(r'^index$', index),
    url(r'^users/', include('user.urls')),  # 多级路由，查看include的原码
    url(r'^posts/', include('post.urls'))
]
