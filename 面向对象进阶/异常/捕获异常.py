# # 自定义的异常
#
#
# class MyException(Exception):
#     pass
#
#
# try:
#     raise MyException()  # MyException也是可以的
# except MyException:
#     print('catch the exception')

#
# class MyException(Exception):
#     pass
#
#
# try:
#     # a = 1 / 0  # 异常捕获规则：捕获从上到下依次比较，如果匹配，则执行匹配的except语句块
#     # raise MyException()
#     open('a.txt')
# except MyException:
#     print('catch the MyException')
# except ZeroDivisionError:  # 如果一个except语句捕获，其他except语句就不会再次捕获了
#     print('1/0')
# except Exception:
#     print('Exception')  # 如果没有任何一个except语句捕获这个异常，则该异常向外抛出


# class MyException(Exception):
#     def __init__(self, code, message):
#         self.code = code
#         self.message = message
#
#
# try:
#     # raise MyException  # raise后跟类名是无参数构造实例，因此需要两个参数
#     raise MyException(200, '0k')
#
# except MyException as e:
#     print('MyException = {} {}'.format(e.code, e.message))
#     # MyException = 200 0k
#
# except Exception as e:
#     print('Exception = {}'.format(e))
#     # Exception = __init__() missing 2 required positional arguments: 'code' and 'message'

# f = None
#
# try:
#     f = open('test.txt')  # 相对路径下，没有test.txt文件
# except FileNotFoundError as e:
#     print('{} {} {}'.format(e.__class__, e.errno, e.strerror))
#     # <class 'FileNotFoundError'> 2 No such file or directory
# finally:
#     print('清理工作')
#     # f.close()  # NameError: name 'f' is not defined.解决的办法是在外部定义f
#     # # AttributeError: 'NoneType' object has no attribute 'close',因为f根本就不存在，可以做如下修改
#     # if f:
#     #     f.close()
#     # 也可以在finally中再次捕捉异常
#     try:
#         f.close()
#     except AttributeError as e:
#         print(e)
#         # 'NoneType' object has no attribute 'close'


# def foo1():
#     return 1 / 0
#
#
# def foo2():
#     print('foo2 start')
#     foo1()
#     print('foo2 stop')
#
#
# foo2()


# # 线程中测试异常
# import threading
# import time
#
#
# def foo1():
#     return 1 / 0
#
#
# def foo2():
#     time.sleep(3)
#     print('foo2 start')
#     foo1()
#     print('foo2 stop')
#
#
# t = threading.Thread(target=foo2)
# t.start()
# while True:
#     time.sleep(1)
#     print('Everything OK')
#     print(threading.enumerate())  # 打印当前所有线程

# def foo():
#
#     try:
#         1 / 0
#     except KeyError as e:
#         print(e)
#     finally:
#         print('inner fin')
#         return  # 异常被压制
#
#
# try:
#     foo()
# except ArithmeticError:
#     print('outer catch')
# finally:
#     print('outer fin')


# def parse_int(s):
#     try:
#         return int(s)
#     except:
#         return 0
#
#
# print(parse_int('s'))


try:
    ret = 1 * 0
except ArithmeticError as e:
    print(e)
else:
    print('OK')
finally:
    print('fine')
