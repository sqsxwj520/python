import functools
import inspect
# from functools import reduce


# print(reduce(lambda x, y: x + y, range(5), 10))
# #最后的10为初始值，如果没有初始值，就把range(5)里的第一个元素作为初始值
# #10为初始值给x，0给y，然后把x + y的结果即10给x，1给y，以此类推
#
# print(reduce(lambda x, y: x * y, range(1, 5), 10))
#
# nums = [1, 3, 5, 7, 9]
# print(sum(nums))
# print(reduce(lambda x, y: x + y, nums))


# def add(x, y: int = 6) -> int:
#     return x + y
#
#
# # new_func = functools.partial(add, 4) # 等价于 def new__func(y)
# # print(new_func(5))
# # #print(new_func(x=5, y=5)) #会出错，因为x已经固定为4了，现在又把5给了x，所以会报错
#
# _newfunc = functools.partial(add, y=5)  # def _newfunc(x),此时的y不在是普通的位置参数了，而变成了keyword-only参数
#
# print(_newfunc)  # 返回一个函数
# print(_newfunc(6))
# print(_newfunc(6, y=4))  # 此处的y会覆盖partial中的缺省值
# print(_newfunc(y=10, x=4))
#
# print(inspect.signature(_newfunc))


# partial方法举例

def add(x, y, *args) -> int:
    print(args)
    return x + y


new_add = functools.partial(add, 1, 2, 3, 4)

print(new_add(5))
print(new_add(5, 6))
# print(new_add(7, 8, y=9, x=10)) #会报错，x，y的值给多了
print(new_add())

print(inspect.signature(new_add))


# # 偏函数的本质
# def partial(func, *args, **keywords):
#     def new_func(*fargs, **fkeywords):  # 包装函数
#         new_keywords = keywords.copy()  # {'x': 4}
#         new_keywords.update(fkeywords)  # {'x':4}
#         return func(*(args + fargs), **new_keywords)  # 5,x=4,7
#
#     new_func.func = func  # 保留原函数
#     new_func.args = args  # 保留原函数的可变位置参数
#     new_func.keywords = keywords  # 保留原函数的可变关键字参数
#     return new_func
#
#
# def add(x, y):
#     return x + y
#
#
# foo = partial(add, 4)
# print(foo(5))
#
#
# def add(x, y, z):
#     return x + y + z
#
#
# newfun = functools.partial(add, y=4)  # def newfun(y, z)
#
# print(newfun(5, 6))  # 会报错，y的给多了，z没有值
# print(inspect.signature(newfun))
