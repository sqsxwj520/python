from django.conf.urls import url
from .views import PostView, get_post, put, delete
# from user.views import authenticate


urlpatterns = [
    # 路径/posts/
    # View类调用as_view之后类等价一个视图函数，可以被装饰
    # 装饰器函数新的函数

    # url(r'^$', authenticate(PostView.as_view())),  # 如果所有视图函数都需要认证，可以使用此种方法
    url(r'^$', PostView.as_view()),
    url(r'^(\d+)$', get_post),
    url(r'^put$', put),
    url(r'^delete$', delete)
    ]
