import inspect
from functools import update_wrapper, wraps, reduce, partial

# print(reduce(lambda x, y: x + y, range(5), 10)) #10为初始值给x，0先给y，然后把x + y的结果即10给x，1给y，以此类推
#
# print(reduce(lambda x, y: x * y, range(1, 5), 10)) #10为初始值给x，1先给y，然后把x * y的结果即10给x，2给y，以此类推

def add(x, y):
    return x + y
newfunc = partial(add, 4) # def newfunc(y)
print(newfunc) # 返回一个函数
print(newfunc(5))
print(inspect.signature(newfunc))
#print(newfunc(x=5)) # 会出错


def add(x, y, z):
    return x + y  +z

# newfunc = partial(add, 4) # def newfunc(y, z)
# print(newfunc(4, z=6))

newfunc = partial(add, y=4) # def newfunc(x, z)
print(newfunc(4, y=5, z=6)) # 此处的y会覆盖partial函数中y的缺省值


#偏函数的本质
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords): # 包装函数
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func # 保留原函数
    newfunc.args = args # 保留原函数的位置参数
    newfunc.keywords = keywords # 保留原函数的关键字参数参数
    return newfunc




def add(x, y, *args, z, **kwargs):
    return x + y + z

newfunc2 = partial(add, 4) # def newfunc2(y)
newfunc2(y=6)
print(newfunc2(y=6))

