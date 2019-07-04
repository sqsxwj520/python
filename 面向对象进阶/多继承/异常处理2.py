# class A:
#     pass
#
#
# try:
#     # 1 / 0
#     # raise A()
#     # raise 'abc'  # 注意'abc'不是继承BaseExceptIon类的实例
#     raise Exception('错误')  # Exception()是Exception（内建）类的实例
#
# # except ZeroDivisionError as e:
# #     print(e)  # division by zero
# except Exception as e:
#     print('exc ~~~~~~~~~~~~', e)  # exc ~~~~~~~~~~~~ 错误
#     print(type(e))  # <class 'Exception'>,e为Exception的实例


# def foo():
#     print('before')
#
#     def bar():
#         print(1 / 0)
#
#     bar()
#
#     print('after')
#
#
# foo()
#
#
# def _bar():
#     print('before')
#     raise Exception('my exception')
#     print('after')
#
#
# _bar()

# try:
#     print('begin')
#     c = 1 / 0
#     print('end')
#
# except ArithmeticError:
#     print('catch the exception')
# print('outer')
#
# """
# begin
# catch the exception
# outer
# """


# class A:
#     pass
#
#
# try:
#     # 1 / 0
#     # raise 1
#     # raise 'abc'
#     raise {}
#     # raise A
#     # raise A()
# except:
#     print('catch the exception')


import sys


# print('before')
# sys.exit(1)
# print('SysExit')
# print('outer')  # 是否执行 ——>不会执行

try:
    sys.exit(100)
except SystemExit:
    print('SysExit')  # 会执行
print('outer')  # 也会执行
