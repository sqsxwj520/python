from django.conf.urls import url
from .views import reg, test, login, logout, test_send_email


urlpatterns = [
    # 下面三个有一个即可
    url(r'^$', reg),
    url(r'^test$', test),
    url(r'^logout$', logout),
    url(r'^login$', login),
    url(r'^mail$', test_send_email),
    ]
