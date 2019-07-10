#
# def add(x, y):
#     return x + y
#
# r:list = add([4], [5]) # python3.6才有的语法 变量注解
# r.append(6)
# print(r)
# add(4, 5)
# add('hello', 'world')
# add(4, 'hello') # 会出错

#
# def add(x: int, y:str=6) -> int: # 参数注解是python3.5 的语法,对于x而言，如果没有写参数注解，就是说x可以是任意类型
#     return x + y
#
# print(add.__annotations__) #annotations 不会显示缺省值;annotations是字典
# #
# # print(add(4, 5))#由于字典是无序的，所以在annotations中具体x是4还是5不确定的
# #
# # print(add(4))


import inspect
from inspect import Parameter

# sig = inspect.signature(add)
# params = sig.parameters
# print(params)
# print(sig.return_annotation)

def check(fn):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters #Orderdict
        #print(sig.return_annotation)
        # values = list(params.values())
        # keys = list(params.keys())
        # for i, x in enumerate(args):
        #     if not isinstance(x, values[i].annotation):
        #         raise TypeError('Wrong param={} {}'.format(keys[i], x))
        flag = True
        for x, (k, v) in zip(args, params.items()):
            if v.annotation != inspect._empty and not isinstance(x, v.annotation):
                #raise TypeError('Wrong param={} {}'.format(k, x))
                #写日志记录
                flag = False
                break


        for k, v in kwargs.items():
            if params[k].annotation != params[k].empty and not isinstance(v, params[k].annotation):
                #raise TypeError('Wrong param={} {}'.format(k, v))
                flag = False
                break
        #
        # for k, v in params.items():
        #     v:Parameter = v
        #     print(v.name)
        #     print(v.default)
        #     print(v.kind)
        #     print()
        if not flag:
            pass
            return
        else:
            ret = fn(*args, **kwargs)
            return ret

    return wrapper


# print(check(add)(4, 5))
# print(check(add)(4, y=5))

@check
def add(x, y:int) -> int:
    return x + y


print(check(add)(4, 6))

print(check(add)(4, y=6))

