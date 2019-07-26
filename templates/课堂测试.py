dic = {'page': 10, 'size': 200}


def fn(d: dict, name: str, default, _max=None):
    try:
        r = int(d.get(name))
        if _max:
            ret = r if r > 0 else default
        else:
            ret = r if 0 < r < 101 else default
        # ret = (r if r > 0 else default) if _max else (r if r > 0 and r < 101 else default)

    except Exception as e:
        print(e)
        ret = default
    return ret


print(fn(dic, 'page', 1))
print(fn(dic, 'size', 20))
