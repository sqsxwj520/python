import time


class A:  # 定义了进入和退出方法的对象叫上下文管理对象
    def __init__(self):
        print('1, init ~~~~~~~~~~~')
        time.sleep(1)
        print('2, init over')

    def __enter__(self):  # 返回值会给a； 进入和退出的方法必须同时存在,它们都是实例的，不是类的
        print('3, enter ~~~~~~~~~~~~')

    def __exit__(self, exc_type, exc_val, exc_tb):  # 默认的返回值为None
        print('6, exit ~~~~~~~~~~~~~')
        print(exc_type)  # <class 'ZeroDivisionError'>
        print(exc_val)  # division by zero
        print(exc_tb)  # <traceback object at 0x000000000221EC48>
        return 'abc'  # 有返回值时，会压制异常


with A() as a:
    print('4, enter with ~~~~~~~~~')
    # import sys
    # sys.exit(100)
    # 1 / 0  # 有异常时，又没有捕获并处理异常，异常下的语句不会再执行
    # 注意即便异常没有处理，__exit__方法下的语句还是要执行
    time.sleep(1)
    print('5, exit with ~~~~~~~~~~')   # 注意执行顺序 ，标注的序号就是执行色顺序


b = A()
with b as c:  # ——> c = b.__enter__()即c为b调用__enter__方法的返回值
    print(1, b)
    print(2, c)  # None ——> __enter__方法的默认返回值为None
    print(b is c)  # False
    print(b == c)  # False
    print(id(b), id(c))
