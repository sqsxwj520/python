import inspect


class TypeCheck:
    def __init__(self, name, typ):
        self.name = name
        self.type = typ

    def __get__(self, instance, owner):  # instance为owner的实例
        # print('get~~~~~~~~', self, instance, owner)
        if instance:
            return instance.__dict__[self.name]  # 存回到属主的实例字典中
        else:
            raise Exception
            # return self

    def __set__(self, instance, value):
        # print('set~~~~~~~~~~~', value, instance)
        if instance:
            if isinstance(value, self.type):
                instance.__dict__[self.name] = value  # 存回到属主的实例字典中,默默的检查，像什么都没有发生一样
            else:
                raise TypeError(self.name + "=======")  # 只有参数类型有错时，才会报错


class DataInject:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwarg):
        sig = inspect.signature(self.cls)
        params = sig.parameters
        # print(params)  # OrderedDict([('name', <Parameter "name:str">), ('age', <Parameter "age:int">)])
        for name, param in params.items():
            print(name, param.name, param.kind, param.default, param.annotation)
            if param.annotation != param.empty:  # inspect._empty
                setattr(self.cls, name, TypeCheck(name, param.annotation))

        return self.cls(*args, **kwarg)


# def data_inject(cls):  # 类属性注入
#     sig = inspect.signature(cls)
#     params = sig.parameters
#     # print(params)  # OrderedDict([('name', <Parameter "name:str">), ('age', <Parameter "age:int">)])
#     for name, param in params.items():
#         # print(name, param.name, param.kind, param.default, param.annotation)
#         if param.annotation != param.empty:  # inspect._empty
#             setattr(cls, name, TypeCheck(name, param.annotation))
#     return cls


@DataInject
class Person:  # Person = Data_Inject(Person)

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age


print(Person.__dict__)
t = Person('tom', 20)
print(t.__dict__)  # {'name': 'tom', 'age': 20}
j = Person('jerry', 18)
print(j.__dict__)  # {'name': 'jerry', 'age': 18}
print(t.name)
print(t.age)
