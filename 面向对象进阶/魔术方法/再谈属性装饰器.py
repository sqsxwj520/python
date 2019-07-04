class Property:
    def __init__(self, fget, fset=None):
        self.fset = fset  # 这是实例的属性保存一个函数没有绑定
        self.__fn = None
        self.fget = fget  # 没有绑定，给实例动态增加方法，该方法为函数，没有绑定效果

    def setter(self, fn):
        self.fset = fn
        return self

    def deleter(self, fn):
        self.__fn = fn

    def __get__(self, instance, owner):
        # print('get~~~~~~~~', instance, owner)
        if instance:
            return self.fget(instance)  # 因为没有绑定效果，所以不会把self注入——> x(self)
        else:
            return Exception  # 没有使用实例访问

    def __set__(self, instance, value):
        print('set~~~~~~~~~', instance, value)
        if self.fset is None:
            raise AttributeError("can't set attribute")

        self.fset(instance, value)

    def __delete__(self, instance):
        self.__fn(instance)


class A:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @Property  # data = Property(data)
    def data(self):
        return self.__x

    @Property
    def y(self):
        return self.__y

    @data.setter  # data = data.setter(data) ——> 是Property的实例
    def data(self, value):
        self.__x = value

    @data.deleter  # data = data.deleter(data) ——> 是Property的实例,同一个
    def data(self):
        # del self__data
        print('del')


a = A(1, 3)
print(a.data)
print(a.y)
# a.y = 9999
a.data = 100
print(a.data)
print(a.y)
del a.data
