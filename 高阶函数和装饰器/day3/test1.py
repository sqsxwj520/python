
import datetime
import time
import inspect
from functools import wraps


def cache(fn):

    local_cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):

        sig = inspect.signature(fn)
        params = sig.parameters  # OrderedDict
        # print(sig)
        # print(params)
        params_dict = {}

        for v, k in zip(args, params.keys()):
            params_dict[k] = v

        for k, v in kwargs.items():
            params_dict[k] = v

        for k, v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default

        key = tuple(sorted(params_dict.items()))

        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]
    return wrapper


def logger(fn):

    # 带参装饰器
    # 等价于 wrapper = update_wrapper(fn)(wrapper)
    @wraps(fn)
    def wrapper(*args, **kwargs):  # 此处的*args是可变位置参数
        """
        my name is wrapper
        """
        print('begin to work')
        start = datetime.datetime.now()
        print('add function: {} | {}'.format(args, kwargs))
        ret = fn(*args, **kwargs)  # 此处的*args是参数解构
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {:.2f}s.'.format(fn.__name__, delta))

        return ret
    return wrapper


@logger
@cache
def add(x, z, y=5)-> int:
    time.sleep(2)
    return x + y + z


print(add(4, 6))
print(add(4, z=6))
print(add(4, y=5, z=6))
print(add(x=4, y=5, z=6))
