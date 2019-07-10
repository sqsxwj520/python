# def add_name(name: str):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper


# @add_name('xyz')  # Person = add_name(Person)
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age  # 双下划线说明此属性是私有属性

    def grow_up(self, i=1):

        if 0 < i < 150:
            self.__age += 1  # 私有的就是实例自己的，不公开让别人访问

    def show_age(self):
        return self.__age  # 私有属性会改变该属性的访问名称，改为_类名__age；注意解释器只有在类中才会帮助你改名称


t = Person('tom')
t.grow_up(200)
print('~' * 30)
# t.age = 300
print(1, t.show_age())
t.__age = 20  # 赋值即重新定义；类外部使用的双下划线，解释器不会帮助您修改名称
# print(2, t.__age)
print(Person.__dict__)
print(t.__dict__)
print(3, t.show_age())
t._Person__age = 30
print(4, t.show_age())
