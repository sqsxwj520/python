# import threading
# import time
#
#
# def show_threading_info():
#     print(1, threading.current_thread())
#     print(2, threading.main_thread())
#     print(3, threading.enumerate())
#     print()
#
#
# def worker(n, m):
#     show_threading_info()
#     for i in range(n):
#         print("I'm working")
#         time.sleep(m)
#         if i == 3:
#             # 1/0  # 会一直往外抛，最后抛给函数当前所在的线程
#             break
#     print('finish')
#
#
# # t = threading.Thread(target=worker, name='worker', args=(5, 1))
# # t = threading.Thread(target=worker, name='worker', args=(5,), kwargs={'m': 1, 'n': 5})
#
# def a():
#     t = threading.Thread(target=worker, name='worker', args=(), kwargs={'m': 1, 'n': 5})
#
#     t.start()  # 线程结束的两种方式：线程函数内语句执行完毕；线程函数抛出未处理异常
# # 只要主线程不崩溃，返回的状态码就是0，跟子线程抛出未处理异常没有关系。
#
#
# show_threading_info()
# time.sleep(2)
# # print(t.ident)  # 线程id
# while True:
#     time.sleep(1)
#     print(threading.enumerate(), '~~~~~~')
#     # if threading.active_count() == 1:
#     #     print('Bye')
#     #     break
#     print('alive~~' if threading.active_count() > 1 else 'dead~~')
#     if threading.active_count() == 1:
#         a()
# # print('++++++end++++++++++')


# class Dispather:
#     cmds = {}
#
#     def reg(self, cmd, fn):
#         self.cmds[cmd] = fn
#
#     def run(self):
#         while True:
#             cmd = input(">>>")
#             if cmd.strip() == "quit":
#                 break
#             self.cmds.get(cmd, lambda: print('unknown cmd'))()
#
#     # def default(self):
#     #     print("unknown cmd")
