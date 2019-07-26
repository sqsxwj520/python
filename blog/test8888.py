# from django.template import loader


# def index(request: HttpRequest):
#     """视图函数：请求进来返回响应"""
#     template = loader.get_template('index.html')  # 加载器模块搜索模板并加载它
#     print(template.origin)  # 显示模板路径
#     context = {'content': 'www.magedu.com'}  # 数据字典
#     return HttpResponse(template.render(context, request))
from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    """视图函数：请求进来返回响应"""
    return render(request, 'index.html', {'content': 'www.magedu.com'})
