# from urllib.request import urlopen, Request
# from http.client import HTTPResponse
#
#
#
# url = 'http://www.bing.com'
#
#
# request = Request(url)
# request.add_header('User-agent', "Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/68.0")
# # 伪装成了浏览器
#
# response: HTTPResponse = urlopen(request)
# print(response, type(response).mro())
#
# with response:
#     print(1, response.status)
#     print(2, response.headers)  # 响应头
#     print(3, response.info())  # 响应头
#     print(4, response.geturl())
#     print(5, response.read().decode())
#
# print(response.closed)

from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote


base_url = 'http://www.magedu.com'

res = urlencode(
    {
        # 'id': 5,
        # 'name': '刘亦菲',
        'wd': "马哥教育"
    }
)
# 一般来说，url不需要编码，只需将查询字符串进行编码
print(res)
print(unquote(res))

headers = {
    'User-agent': "User-agent': Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/68.0"
}
request = Request("{}?{}".format(base_url, res), headers=headers)

response = urlopen(request)

with response:
    with open('c:/a.html') as f:
        f.write(response.read())
