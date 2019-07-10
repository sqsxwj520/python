"""
实现一个cache装饰器，实现可过期被清除的功能
简化设计，函数的形参定义不包含可变位置参数、可变关键词参数和keyword-only参数
可以不考虑缓存大小，也不用考虑缓存满了之后的换出问题
"""

from functools import wraps
import inspect
import time
import datetime


def logger(fn):

    # 带参装饰器
    # 等价于 wrapper = update_wrapper(fn)(wrapper)
    @wraps(fn)
    def wrapper(*args, **kwargs):  # 此处的*args是可变位置参数
        """
        my name is wrapper
        """
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)   # 此处的*args是参数解构
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {:.2f}s.'.format(fn.__name__, delta))
        return ret
    return wrapper


def cache(duration=5):
    def _cache(fn):

        local_cache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):

            expire_keys = []  # 满了之后，用的时候，再去清除，如果数据规模大的话，清除时会比较耗时
            now = datetime.datetime.now().timestamp()
            for k, (_, timestamp) in local_cache.items():
                if now - timestamp > duration:  # 两者的差值可能是负数，以后写代码要注意
                    expire_keys.append(k)
            for k in expire_keys:
                local_cache.pop(k)  # 注意字典不能在遍历的时候删除

            sig = inspect.signature(fn)
            params = sig.parameters
            print(params)

            target = {}
            #
            # for k, v in zip(params.keys(),args):
            #     target[k] = v
            # target.update(zip(params.keys(), args))

            # #解决关键字
            # # for k, v in kwargs:
            # #     target[k] = v
            # target.update(kwargs)
            target.update(zip(params.keys(), args), **kwargs)

            # 解决缺省值

            # for k, v in params.items():
            #     if k not in target.keys():
            #         target[k] = v.default  # 如果没有缺省值呢
            target.update(((k, v.default) for k, v in params.items() if k not in target.keys()))
            # 方法二
            # for k in (params.keys() - target.keys()):
            #     target[k] = params[k].default
            # target.update(((k, params[k].default) for k in (params.keys() - target.keys())))

            key = tuple(sorted(target.items()))

            if key not in local_cache.keys():
                local_cache[key] = (fn(**target), datetime.datetime.now().timestamp())  # fn(*args, **kwargs)

            return local_cache[key]
        return wrapper
    return _cache


@logger
@cache()
def add(x=4, y=5):

    time.sleep(2)
    return x + y


print(add())
print(add(y=5))
print(add(y=5, x=4))
print('~~~~~~~~~~~~~~~~')
time.sleep(6)
print(add(y=5, x=4))
print(add(4, 5))
