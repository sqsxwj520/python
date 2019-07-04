import time
import datetime
from functools import wraps, update_wrapper


class Timeit:
    """ I am Timeit class"""
    def __init__(self, fn):
        self.fn = fn
        # self.__doc__ = fn.__doc__
        # self.__name__ = fn.__name__
        # update_wrapper(self, fn)  # fn为被包装函数，self为Timeit的实例
        wraps(fn)(self)

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        # print('took {}s in class Timeit'.format(delta))
        print('{} took {}s in class Timeit'.format(self.fn.__name__, delta))

    def __call__(self, *args, **kwargs):
        # return self.fn(*args, **kwargs)
        start = datetime.datetime.now()
        ret = self.fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s in dec'.format(fn.__name__, delta))
        return ret


def logger(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s in dec'.format(fn.__name__, delta))
        return ret
    return wrapper


@logger  # 对单个函数计时
def add(x, y):
    """ this is add function"""
    time.sleep(5)
    return x + y

#
# add(3, 4)
# print(add.__doc__)


with Timeit(add) as timeit_instance:  # 上写文管理做得是总计时
    add(4, 5)
    timeit_instance(4, 5)

Timeit(add)(5, 6)


@Timeit
def add(x, y):
    """this is add function"""
    time.sleep(2)
    return x + y


@Timeit  # 类也可以作为装饰器 sub = Timeit(sub)——>实例化  sub是Timeit的实例
def sub(x, y):
    """this is sub function"""
    time.sleep(2)
    return x - y


print(sub.__doc__)
print(sub.__name__)
print(add.__doc__)
print(add.__name__)
