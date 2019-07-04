
import time


class A:  # 定义进入和退出方法的对象叫上下文对象

    def __init__(self):
        print('1, init ~~~~~~~~~~~~~~~')
        time.sleep(1)

    def __enter__(self):  # 进入.__enter__方法和__exit__方法必须同时出现
        print('2, enter~~~~~~~~~')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 退出(实例的方法)

        print(exc_type)  # <class 'ZeroDivisionError'>
        print(exc_val)  # division by zero
        print(exc_tb)  # <traceback object at 0x0000000001EAEBC8>
        print('5, exit~~~~~~~~~')
        return 'abc'  # 会压制异常；return返回值等效为True，则压制异常，否则异常向外抛出

# with操作的对象，必须支持上下文管理，即必须要有enter方法和exit方法
# 没有as子句并不影响上下文管理
# with语句不会开辟新的作用域

# f = open('可调用对象.py')
# with f as f1:
#     print(f is f1)  # True
#     print(id(f), id(f1))  # 5705376 5705376
#     print(f == f1)  # True
#     print()

# with open('可调用对象.py') as f2:
#     print(f2.read())  # 结果将可调用对象.py文件的输出结果也读取了


with A() as a:  # 注意调用顺序；with操作的是with后的对象，不是as后的对象
    print('3, enter with ~~~~~~~~~~')
    # 1 / 0
    # import sys
    # sys.exit(100)  # 4不会执行，5会执行；time.sleep(1)也不会执行；会退出当前解释器
    time.sleep(1)
    print('4, exit with ~~~~~~~~~~~~~~')
b = A()
with b as c:  # b = c.__enter__() ——> 等效为 b = c.__enter__方法的返回值为self时)
    print(1, b)
    print(2, c)
    print(b is c)  # True
    print(b == c)  # True
    print(id(b), id(c))  # 32215952 32215952


# d = A()
# with d as e:
#     # 1 / 0
#     pass
