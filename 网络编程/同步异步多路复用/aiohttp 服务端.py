
# https://aiohttp.readthedocs.io/en/stable/, aiohttp是小型的网页设计库，比flask、Djiango要小巧
from aiohttp import web


routes = web.RouteTableDef()  # 改为装饰器
# https://aiohttp.readthedocs.io/en/stable/web_quickstart.html#run-a-simple-web-server

"""
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
"""


@routes.get('/')
async def handle(request):
    # name = request.match_info.get('name', "Anonymous")
    # text = "Hello, " + name
    text = "<html><body><h1>{}<h1></body></html>".format('你好，中国!')
    print(request)
    return web.Response(body=text, status=201, content_type='text/html', charset='utf-8')
    # 201是成功的把数据加入到了数据库,content_type默认是纯文本格式，现在设置为html


@routes.get(r'/{id:\d+}')  # r的意思是把后面当做原始字符串，不转义，\d+是正则表达式
async def id_handle(request: web.Request):
    print(request.match_info.get('id', '0000'))  # 获取不到，用默认值0000
    text = 'path={}, qs={}'.format(request.path, request.query_string)  # qs为查询条件（查询字符串）
    return web.Response(body=text, status=200)  # 默认的状态码可以省略

app = web.Application()

# app.add_routes([web.get('/', handle),  # 路径映射
#                 # web.get('/{name}', handle),
#                 web.get('/{id}', id_handle)])  # {id}为字典，利用正则表达式匹配

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, host='127.0.0.1', port=9988)

"""

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)
"""
