"""异常捕获

"""
import sys


def foo():
    print('before')
    try:  # try会捕获语句块内的所有异常
        sys.exit(100)
        # raise NotImplementedError()
        # print(1 / 0)  # 待捕获异常的代码块
    except SystemExit:  # 指定捕获异常类型
        print('sys exit')
    print('after')


foo()


class A:
    pass


try:
    # 1 / 0
    # raise A()
    # raise 'abc'  # 注意'abc'不是继承BaseExceptIon类的实例
    raise Exception('错误')  # Exception()是Exception（内建）类的实例

# except ZeroDivisionError as e:
#     print(e)  # division by zero
except Exception as e:
    print('exc ~~~~~~~~~~~~', e)  # exc ~~~~~~~~~~~~ 错误
    print(type(e))  # <class 'Exception'>,e为Exception的实例


try:
    f = open('tesssssss')
except FileNotFoundError as e:
    print(e.filename, e.strerror, e.errno)
except Exception as e:
    print('exc ~~~~~~', e)

finally:
    try:
        f.close()
    except Exception as e:
        print(e)
