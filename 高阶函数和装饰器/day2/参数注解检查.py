import inspect


def check(fn):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters  # Ordereddict
        print(params)
        # values = list(params.values())
        # keys = list(params.keys())
        # for i, p in enumerate(args):
        #     if values[i].annotation != inspect._empty and  not isinstance(p, values[i].annotation):
        #         raise TypeError('Wrong param={} {}'.format(keys[i], p))

        for p, (k, v) in zip(args, params.items()):
            if v.annotation is not inspect._empty and not isinstance(p, v.annotation):
                raise TypeError('Wrong param={} {}'.format(k, p))

        for k, v in kwargs.items():
            if params[k].annotation is not inspect._empty:
                if not isinstance(v, params[k].annotation):
                    raise TypeError('Wrong param={} {}'.format(k, v))

        return fn(*args, **kwargs)

    return wrapper


@check
def add(x, y: int = 7) -> int:  # add = check(add)
    return x + y


print(add(4, 5))
print(add(4, y=6))
print(add(y=6, x=9))
