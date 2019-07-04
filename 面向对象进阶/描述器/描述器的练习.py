from functools import partial, wraps, update_wrapper

import inspect


# class StaticMethod:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(instance, owner)
#         return self.fn


# class ClassMethod:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         newfunc = partial(self.fn, owner)  # 固定owner
#         # update_wrapper(newfunc, self.fn)
#         wraps(self.fn)(newfunc)
#         return newfunc
#
#
# class A:
#     @StaticMethod  # smtd = StaticMethod(stmd)  # 实例化
#     def smtd(x, y):
#         """================
#         """
#         print("static method~~~", x, y)
#
#     @ClassMethod  # foo = ClassMethod(foo)
#     def foo(cls, x, y):
#         """++++++++++++++++"""
#         print(cls.__name__, x, y)
#
#
# a = A()  # A的实例
# a.smtd(4, 5)
# a.foo(10, 11)


class TypeCheck:
    def __init__(self, name, typ):
        self.name = name
        self.type = typ

    def __get__(self, instance, owner):  # instance为owner的实例
        # print('get~~~~~~~~', self, instance, owner)
        if instance:
            return instance.__dict__[self.name]  # 存回到属主的实例字典中
        else:
            raise Exception  # return self

    def __set__(self, instance, value):
        # print('set~~~~~~~~~~~', value, instance)
        if instance:
            if isinstance(value, self.type):
                instance.__dict__[self.name] = value  # 存回到属主的实例字典中,默默的检查，像什么都没有发生一样
            else:
                raise TypeError(self.name + "=======")  # 只有参数类型有错时，才会报错

    # def __set_name__(self, owner, name):  # python3.6新增的
    #     # print(owner, name)
    #     self.name = name


def data_inject(cls):  # 类属性注入
    sig = inspect.signature(cls)
    params = sig.parameters
    # print(params)  # OrderedDict([('name', <Parameter "name:str">), ('age', <Parameter "age:int">)])
    for name, param in params.items():
        # print(name, param.name, param.kind, param.default, param.annotation)
        if param.annotation != param.empty:  # inspect._empty
            setattr(cls, name, TypeCheck(name, param.annotation))
    return cls


@data_inject
class Person:
    # name = TypeCheck(str)
    # age = TypeCheck(int)  # 硬编码，不优雅

    def __init__(self, name: str, age: int):
        # params = ((name, str), (age, int))
        # # 做参数检查
        # if not self.check_data(params):
        #     raise TypeError
        self.name = name
        self.age = age

    # def check_data(self, params):
    #     for p, typ in params:
    #          if not isintance(p, typ):
    #             print(p, typ)
    #             raise False
    #     return True


t = Person('tom', 20)
print(t.__dict__)  # {'name': 'tom', 'age': 20}
j = Person('jerry', 18)
print(j.__dict__)  # {'name': 'jerry', 'age': 18}
print(t.name)
print(t.age)
