from functools import partial, wraps, update_wrapper
import inspect


# 方法一 直接在init方法中写检查函数
class Person:
    def __init__(self, name: str, age: int):
        params = ((name, str), (age, int))
        if not self.check_data(params):
            raise TypeError('类型错误')
        self.name = name
        self.age = age

    @staticmethod
    def check_data(params):
        for p, typ in params:
            if not isinstance(p, typ):
                return False
        return True


# p1 = Person('tom', '20')  # TypeError: 类型错误


def type_check(cls):
    """通过装饰器对类方法的参数进行类型检查"""
    @wraps(cls)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(cls)
        params = sig.parameters  # OrderedDict
        # print(params)
        # values = list(params.values())
        # keys = list(params.keys())
        # for i, p in enumerate(args):
        #     if values[i].annotation != inspect._empty and  not isinstance(p, values[i].annotation):
        #         raise TypeError('Wrong param={} {}'.format(keys[i], p))

        for p, (k, v) in zip(args, params.items()):
            if v.annotation is not v.empty and not isinstance(p, v.annotation):
                raise TypeError('Wrong param= {} {}'.format(k, p))

        for k, v in kwargs.items():
            if params[k].annotation is not v.empty:  # inspect._empty
                if not isinstance(v, params[k].annotation):
                    raise TypeError('Wrong param={} {}'.format(k, v))

        return cls(*args, **kwargs)

    return wrapper


@type_check
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p1 = Person('tony', 20)
# p2 = Person('jacky', '18')  # 直接报错


class TypeCheck:  # 描述器
    def __init__(self, name, typ):
        self.name = name
        self.type = typ

    def __get__(self, instance, owner):
        # print('get~~~~~~~~~~~~~~')
        if instance:
            return instance.__dict__[self.name]
        else:
            raise Exception  # 或者return self，总之不正常

    def __set__(self, instance, value):
        # print('set~~~~~~~~~~~~~')
        if instance:
            if not isinstance(value, self.type):
                raise TypeError(self.name, '+++++++++++')
            else:
                instance.__dict__[self.name] = value  # 存回到属主类的实例字典中,默默的检查，不出错的话，像什么都没有发生一样

    # def __set_name__(self, owner, name):  # python3.6新增的方法
    #     print(name)
    #     self.name = name


class TypeInject:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwarg):
        sig = inspect.signature(self.cls)
        params = sig.parameters
        # print(params)  # OrderedDict([('name', <Parameter "name:str">), ('age', <Parameter "age:int">)])
        for name, param in params.items():
            # print(name, param.annotation)
            if param.annotation != param.empty:  # inspect._empty
                setattr(self.cls, name, TypeCheck(name, param.annotation))

        return self.cls(*args, **kwarg)


@TypeInject  # Person = TypeInject(Person)
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p5 = Person('Green', 28)
p5.age = 30
print(p5.__dict__)


# def type_check(cls):
#     sig = inspect.signature(cls)
#     params = sig.parameters
#     # print(params)  # 有序字典
#     for name, param in params.items():
#         if param.annotation is not param.empty:
#             setattr(cls, name, TypeCheck(name, param.annotation))
#     return cls


# 注意动态给类增加属性（方法）时，__set_name__方法并没有调用，即此方法无效
# @type_check  # Person = type_check(Person)
# class Person:
#     # name = TypeCheck(str)  # 硬编码，不优雅
#     # age = TypeCheck(int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name  # 会调用TypeCheck实例的__set__方法（描述器）
#         self.age = age
#
#
# p3 = Person('curry', 31)
# p4 = Person('durant', 29)  # 直接抛出异常
# print(p3.__dict__)  # {'name': 'curry', 'age': 31}
# print(p4.__dict__)  # {'name': 'durant', 'age': 29}
# print(Person.__dict__)
