import asyncio


@asyncio.coroutine
def sleep():
    # count = 0
    # for i in range(3):
    #     yield count
    #     count += 1
    for i in range(3):
        yield from asyncio.sleep(1)  # 相当于沉睡1秒
        print('+++++++++++')
    return 'my return value = {}'.format(1000)


print(asyncio.iscoroutinefunction(sleep))  # True
print(asyncio.iscoroutine(sleep()))  # True,注意sleep的括号不能丢，不然结果为False


def cb(fut):
    print('future = {} ~~~'.format(fut))


loop = asyncio.get_event_loop()
print(type(loop))

# Future =>Task  # Task是Future的子类
# future = asyncio.ensure_future(sleep())  # 确保得到一个future对象，对协程对象进行封装
#
# print(1, future)
# loop.run_until_complete(future)  # 一定会带你执行下ensure_future
# print(2, future)
#
# print(future.result())

# task = asyncio.ensure_future(sleep())
# task = asyncio.create_task(sleep())  # python3.7版本以上才能使用
task = loop.create_task(sleep())

task.add_done_callback(cb)

print(3, task)
loop.run_until_complete(task)  # 只能放一个future对象,以后会有很多任务，部分任务执行完了，会调用回调函数
print(4, task)

print(task.result(), '~~~~~~~')

loop.close()
