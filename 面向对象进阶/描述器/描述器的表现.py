# class A:  # 数据描述器的访问优先级要高于实例__dict__的访问；非数据描述器的访问，优先级要低于实例字典的访问
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A init')
#
#     def __get__(self, instance, owner):  # instance为owner的实例
#         print('get~~~~~~~~', self, instance, owner)
#         # print(self.__dict__)
#         return self
#
#     def __set__(self, instance, value):  # 可以禁止修改实例的属性
#         print('set~~~~~~~~~~~', value, instance)
#         # self.data = value  # 保存在A的实例里了
#
#         # setattr(instance, 'x', value)  # 无限递归
#         # instance.data = value
#         # instance.__dict__['x'] = value
#         if instance:
#             raise Exception('不许改')
#
#     def __set_name__(self, owner, name):  # python3.6新增的
#         print(owner, name)
#         self.name = name
#
#
# class B:  # 属主
#     x = A()  # 类属性可以，描述器和属主类的类属性有关;解释器执行到这一句时，会调用__set_name__方法
#     z = 5
#
#     def __init__(self):
#         # self.y = A()  # 实例属性不会，描述器与属主类的实例属性无关
#         self.x = 'b.x'  # 动态增加属性
#         print('B init')
#
#
# print('~~~~~~~~~~~~~~~')
# b = B()
# print(b.x)  # <__main__.A object at 0x0000000000789630>
# print(b.__dict__)  # {'x': 'b.x'}
# print('~~~~~~~~~~~~~~~~~~~~~~')
# b.x = 500  # 会调用描述器的__set__方法
# print(b.x)  # <__main__.A object at 0x00000000027C9668>
# print(b.__dict__)  # {'x': 500}
# print("++++++++++++++++")
# B.x = 600  # 如果类的类属性x是描述器，那么不要使用这样的赋值语句
# print(b.x)  # 500
# print(B.x)  # 600
#
# print('~~~~~~~~~~~~~~~')
# b = B()
# b.x = 100
# print(b.x)
#
#
# print('~~~~~~~~~~~~~~~~~')
# print(B.x)  # 会调用A实例的__get__方法;instance为None，B.x或B().x才会调用描述器
# print(B.x.a1)  # instance为None;注意是B.x调用了描述器
# print('++++++++++++++++++')
# b = B()
# print(b.x)  # instance为<__main__.B object at 0x0000000001E89668>
# print(b.x.a1)
from functools import partial


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
