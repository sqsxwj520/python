# from contextlib import contextmanager
#
#
# @contextmanager  # 上下文管理的装饰器
# def a():
#     print('enter~~~~~~')  # 进入代码
#     try:
#         yield 123
#     except ZeroDivisionError:
#         pass
#     finally:  # 退出的代码放在finally语句中
#         print('exit~~~~~~~~')  # 退出代码
#
#
# with a() as f:  # f = a().__enter__()
#     print('f = ', f)  # f =  123
#     print(1 / 0)
#     print('with over~~~~')
#
#
# print('+++++++++++++++')
#
#
# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __len__(self):
#         return len(self.items)
#
#     def __iter__(self):
#         yield from self.items
#
#     def __getitem__(self, index):
#         if index < 0:
#             raise IndexError('Wrong index')
#         if index < len(self.items):
#             return self.items[index]
#         for i in range(len(self.items), index + 1):
#             self.items.append(self.items[i - 1] + self.items[i - 2])
#         return self.items[index]
#
#     def __call__(self, index):
#         return self[index]
#
#     def __repr__(self):
#         return "<{} {}>".format(self.__class__.__name__, self.items)
#
#
# f = Fib()
# print(f(5))
# for x in f:
#     print(x)
# print(len(f))
# print(f[6])


import contextlib
import time
import datetime


@contextlib.contextmanager
def add(x, y):  # 为生成器函数增加了上下文管理
    start = datetime.datetime.now()
    try:
        time.sleep(2)
        yield x + y
    finally:
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)


with add(4, 5) as f:  # f = x + y
    print(f)
