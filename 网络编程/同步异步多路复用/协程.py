import asyncio


async def a():  # async def 中不能出现yield，必须和await配合使用
    for i in range(3):
        print('a.x', i)
        # await wait()
        await asyncio.sleep(0.1)
    return 'a() return 1000'


async def b():  # 不能再出现yield
    for i in 'abc':
        print('b.x', i)
        # await wait()  # await后往往是阻塞的函数，相当于yield from wait()
        await asyncio.sleep(0.1)
    return 'b() return 2000'


loop = asyncio.get_event_loop()


def cb(fut):
    print(fut.result())


ts = []
for x in (a(), b()):
    t = asyncio.ensure_future(x)
    t.add_done_callback(cb)
    ts.append(t)


task1 = loop.create_task(a())
task2 = loop.create_task(b())

# 相当于遍历元组中的元素
ret = loop.run_until_complete(asyncio.wait(ts))
print(ret)  # 结果为二元组，第一个是set，里面有2个task对象

for p in ret[0]:
    print(p.result())
