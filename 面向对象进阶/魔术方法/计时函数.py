import time
from datetime import datetime
from functools import wraps, update_wrapper


class Timeit:
    """This is Timeit class"""
    def __init__(self, fn):
        self.fn = fn
        # self.__doc__ = fn.__doc__  # 设置实例的属性
        # self.__name__ = fn.__name__
        # update_wrapper(self, fn)
        wraps(fn)(self)

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.now() - self.start).total_seconds()
        print("{} took {}s in class".format(self.fn.__name__, delta))

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        ret = self.fn(*args, **kwargs)
        delta = (datetime.now() - start).total_seconds()
        print("{} took {}s in class".format(self.fn.__name__, delta))
        return ret


# def timeit(fn):
#
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.now() - start).total_seconds()
#         print("{} took {}s in dec".format(fn.__name__, delta))
#         return ret
#     return wrapper
#
#
# @timeit
# def add(x, y):
#     """this is add function"""
#     time.sleep(2)
#     return x + y


# add(4, 5)


@Timeit  # add = Timeit(add)实例化，add为Timeit 的实例
def add(x, y):
    """this is a function"""
    time.sleep(1)
    return x + y


add(4, 5)  # add took 1.014002s in class

# with Timeit(add) as t:  # ——> t = Timeit(add)
#     # add(4, 5)
#     t(5, 6)  # 实例调用
#
print(add.__doc__)  # this is add function
print(add.__name__)  # add
