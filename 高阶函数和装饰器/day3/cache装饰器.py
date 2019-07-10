
"""
简化设计，函数的形参定义不包含可变位置参数、可变关键词参数和keyword-only参数
可以不考虑缓存大小，也不用考虑缓存满了之后的换出问题
"""

import time
import datetime
import inspect
from functools import wraps


def cache(duration):
    def _cache(fn):

        local_cache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):

            # 清理过期的key
            overtime_keys = []
            for k, (_, timestamp) in local_cache.items():

                now = datetime.datetime.now().timestamp()
                if now - timestamp > duration:
                    overtime_keys.append(k)
                for k in overtime_keys:
                    local_cache.pop(k)

            sig = inspect.signature(fn)
            params = sig.parameters  # OrderedDict

            # print(sig)
            # print(params)
            params_dict = {}

            for v, k in zip(args, params.keys()):
                params_dict[k] = v

            for k, v in kwargs.items():
                params_dict[k] = v

            # 缺省值的处理
            for k, v in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = v.default

            key = tuple(sorted(params_dict.items()))

            if key not in local_cache.keys():
                local_cache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())

            return local_cache[key]
        return wrapper
    return _cache


@cache(5)
def add(x, z, y=5):

    time.sleep(2)

    return x + y + z


result = list()
result.append(add(4, 6))
result.append(add(4, z=6))
result.append(add(4, y=5, z=6))
result.append(add(y=5, z=6, x=4))
result.append(add(4, 6, 5))
result.append(add(4, 7))
for i in result:
    print(i)
