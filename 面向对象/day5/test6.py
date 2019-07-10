
# 类的继承(inheritance)


class Animal:  # 如果类定义时，没有基类列表，等同于继承自object;在python3中，一切类都继承自object类
    def __init__(self, name):
        self.name = name

    def shout(self):
        print('{} shouts'.format(type(self).__name__))


class Cat(Animal):  # 生成子类的过程也叫派生；继承说的是类与类的关系，不是实例
    pass


class Dog(Animal):
    pass


a = Animal('Monster')
a.shout()
c = Cat('cat')
c.shout()  # 继承父类Animal
print(c.name)
d = Dog('dog')
print(d.name)
print(Dog.__bases__)  # 结果是元组

print(Animal.__bases__)
print(Animal.__subclasses__())
print(Cat.__mro__)  # 方法解析顺序；结果为元组，注意元组中全是类
print(Cat.mro())  # 结果为列表
# 实例找属性，优先找自己字典中的属性，没有的话，从类的字典中查找，仍然没有的话，从父类中找
