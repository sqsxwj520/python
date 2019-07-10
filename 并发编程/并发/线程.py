# from threading import Thread
# # import threading
# import time
#
#
# t = None
#
#
# class MyThread(Thread):
#     def start(self) -> None:  # 返回值是None
#         print("start~~~~~")
#         super().start()  # 跟启动操作系统线程有关
#
#     def run(self):
#         print("run~~~~~~~~")  # 运行函数有关
#         super().run()
#
#
# def worker():
#     time.sleep(1)
#     # print(threading.enumerate())
#     # print(threading.current_thread(), "I'm working")
#     # print("I'm working")
#     global t
#     t = 1000
#     # return t
#
#
# t1 = MyThread(target=worker, name="worker")
# t1.start()  # worker会在当前线程中压栈，没有此句，worker会在主线程中压栈
# time.sleep(2)
# print(t, "~~~~~~~")
# # t.run()
# # t._target = worker
# # t.args = ()
# # t.kwargs = {}
# print("~" * 30)
# # t.start()  # 线程只能启动一次，不论该线程是否结束
# # t.run()
#
# import threading
# import time
#
#
# def show_thread_info():
#     print("current_thread = {}".format(threading.current_thread()))
#     print("main thread = {}".format(threading.main_thread()))
#     print("active_count = {}".format(threading.active_count()))
#
#
# def worker():
#     count = 0
#     show_thread_info()
#     while True:
#         if count > 3:
#             break
#         time.sleep(1)
#         print("I'm working")
#         count += 1
#
#
# t = threading.Thread(target=worker, name='worker')  # 线程对象
# show_thread_info()
# t.start()  # 启动
# print('==End==')
#
# """current_thread = <_MainThread(MainThread, started 1744)>
# main thread = <_MainThread(MainThread, started 1744)>
# active_count = 1
# current_thread = <Thread(worker, started 8888)>
# ==End==
# main thread = <_MainThread(MainThread, started 1744)>
# active_count = 2
# I'm working
# I'm working
# I'm working
# I'm working
#
# """

# import threading
# import logging
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'  # 注意%后不能有空格
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker():
#     for x in range(100):
#         logging.info('{} is running'.format(threading.current_thread().name), end='')
#
#
# for i in range(5):
#     name = 'worker{}'.format(i + 1)
#     t = threading.Thread(target=worker, name=name)
#     t.start()


# import time
# import threading
#
#
# def foo(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# t1 = threading.Thread(target=foo, args=(2,), daemon=True)  # 调换10和20看看效果
# t1.start()
#
# t2 = threading.Thread(target=foo, args=(5,), daemon=False)  # 主线程会等到此线程结束再退出
# t2.start()
# time.sleep(2)  # 会让主线程沉睡2秒
#
# print('Main Thread Exiting')
# """\
# 0
# 0
# 1
# 1
# Main Thread Exiting
# 2
# 3
# 4
# """

# import time
# import threading
#
#
# def foo(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# t1 = threading.Thread(target=foo, args=(10,), daemon=True)
# t1.start()
# t1.join()  # 设置join，取消join对比一下
# print('Main Thread Exiting')

# import time
# import threading
#
#
# def bar():
#     while True:
#         time.sleep(1)
#         print('bar')
#
#
# def foo():
#     print("t1's daemon = {}".format(threading.current_thread().isDaemon()))
#     t2 = threading.Thread(target=bar)  # 默认取t1线程设置的daemon值，即True,但是有join方法,所以t1线程会等待t2线程
#     t2.start()
#     print("t2's daemon = {}".format(t2.isDaemon()))
#     t2.join(2)  # 会死循环，因为t1线程一直要等t2线程，而t2线程函数是死循环，可以设置等待时间
#
#
# t1 = threading.Thread(target=foo, daemon=True)
# t1.start()
# t1.join()  # 主线程会卡在这里
# time.sleep(3)
# print('Main Thread Exiting')
#
# """\
# t1's daemon = True
# t2's daemon = True
# bar
# bar
# bar
# bar
# bar
# Main Thread Exiting
# """

# import threading
# import time
#
#
# # 局部变量实现
# def worker():
#     x = 0
#     for i in range(100):
#         time.sleep(0.0001)
#         x += 1
#     print(threading.current_thread(), x)
#
#
# for _ in range(10):
#     threading.Thread(target=worker).start()


# import threading
# import time
# # 全局对象
#
#
# global_data = threading.local()
#
#
# def worker():
#     global_data.x = 0
#     for i in range(100):
#         time.sleep(0.0001)
#         global_data.x += 1
#     print(threading.current_thread(), global_data.x)
#
#
# for _ in range(5):
#     threading.Thread(target=worker).start()
#
# """\
# <Thread(Thread-5, started 4904)> 100
# <Thread(Thread-1, started 8232)> 100
# <Thread(Thread-2, started 8564)> 100
# <Thread(Thread-3, started 8360)> 100
# <Thread(Thread-4, started 5360)> 100
# """

import threading


X = 'abc'
ctx = threading.local()
ctx.x = 123
print(ctx, type(ctx), ctx.x)


def worker():
    print(X)
    print(ctx)
    print(ctx.x)
    print('working')


worker()  # 普通函数调用，注意此时是在主线程中
print()
threading.Thread(target=worker).start()
# 开启一个新的线程,此时线程函数worker中的ctx.x就会报错，因为此线程看不到主线程中ctx.x的值
# AttributeError: '_thread._local' object has no attribute 'x'

import threading
import logging
import time


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    logging.info('in worker')
    time.sleep(2)  # 2秒之后当前线程接结束，主线程也结束了


count = 0
t = threading.Timer(4, worker)
t.setName('timer')
# t.cancel()
t.start()
t.cancel()  # 会取消执行线程函数
while count < 3:
    print(threading.enumerate())
    time.sleep(1)
    count += 1
