from functools import partial


class Property:
    def __init__(self, fn):
        self._fn = None
        self.__fn = None
        self.fn = fn

    def setter(self, fn):
        self._fn = fn
        return self

    def deleter(self, fn):
        self.__fn = fn

    def __get__(self, instance, owner):
        # print('get~~~~~~~~', instance, owner)
        if instance:
            return self.fn(instance)
        else:
            return Exception

    def __set__(self, instance, value):
        # print('set~~~~~~~~~', instance, value)
        self._fn(instance, value)

    def __delete__(self, instance):
        self.__fn(instance)


class A:
    def __init__(self, x):
        self.__x = x

    @Property  # data = Property(data)
    def data(self):
        return self.__x

    @data.setter  # data = data.setter(data)
    def data(self, value):
        self.__x = value

    @data.deleter  # data = data.deleter(data)
    def data(self):
        # del self__data
        print('del')


a = A(1)
print(a.data)
a.data = 100
print(a.data)
del a.data


class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return partial(self.fn, owner)  # 固定owner即属主类


class D:
    @StaticMethod  # stmd = StaticMethod(stmd) 非数据描述器
    def stmd(x, y):
        print('static method', x, y)

    @ClassMethod  # foo = ClassMethod(foo)
    def foo(cls, x, y):
        print(cls.__name__, x, y)


d = D()
d.stmd(4, 5)  # static method 4 5

d2 = D()
d2.foo(5, 6)  # D 5 6
