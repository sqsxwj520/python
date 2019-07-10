# class Animal:
#     x = 100
#
#     def shout(self):
#         print('Animal shouts')
#
#
# class Cat(Animal):
#
#     def shout(self):  # 覆盖了父类的shout方法；override
#         print('Mia')
#
#
# class Dog(Animal):
#     def shout(self):
#         # print('wang')  # 直接用自己的
#         # Dog.__base__.shout(self)  # 调用父类的shout方法
#         #  __class__.__base__.shout(self)  # 不推荐这么写
#
#         print(super())  # <super: <class 'Dog'>, <Dog object>>
#         super().shout()  # shout()中不能再添加self了，否则直接抛出异常
#         # super(__class__, self).shout()  # 不推荐这么写，上述的写法更简洁
#         print(super().x)
#
#
# c = Cat()
# c.shout()
#
# d = Dog()
# d.shout()


class A:
    def __init__(self, a=5):
        print('init in A')
        self.a = a

    def show_a(self):
        print(self.a)


class B(A):
    def __init__(self, b=6, c=8):  # 子类会覆盖父类中__init__属性；此种覆盖可能有风险
        # A.__init__(self, b)
        # super().__init__(b)  # 注意__init__方法中不能再添加self了，因为super()会自动注入实例
        print('init in B')
        self.b = b
        self.c = c
        super().__init__(b)  # 此句最好有，具体的位置由你决定（这是一个好习惯）


b1 = B()
print(b1.__dict__)
# b1.show_a()  # 会出错，因为实例b1的字典中没有a属性
