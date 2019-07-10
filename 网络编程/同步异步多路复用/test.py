import asyncio


@asyncio.coroutine
def a():
    for i in range(3):
        print('a.x', i)
        yield
    return 'a() return 1000'


@asyncio.coroutine
def b():
    for i in 'abcdefg':
        print('b.x', i)
        yield
    return 'b() return 2000'


# x = a()
# y = b()
# print(asyncio.iscoroutinefunction(a))
# print(asyncio.iscoroutine(x))
#
# for j in range(3):  # 循环，生成器函数
#     next(x)
#     next(y)

loop = asyncio.get_event_loop()  # 大循环


def cb(fut):
    print(fut.result())


ts = []
for x in (a(), b()):
    t = asyncio.ensure_future(x)
    t.add_done_callback(cb)
    ts.append(t)


task1 = loop.create_task(a())
task2 = loop.create_task(b())

# wait 迭代所有的coroutine对象，将他们封装成一个future对象
# loop.run_until_complete(asyncio.wait((task1, task2)))
ret = loop.run_until_complete(asyncio.wait(ts))   # 相当于遍历元组中的元素
print(ret)  # 结果为二元组，第一个是set，里面有2个task对象

for p in ret[0]:
    print(p.result())
