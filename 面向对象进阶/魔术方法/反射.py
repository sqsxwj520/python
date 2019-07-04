
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # def show(self):
#     #     print(self.x, self.y)
#
#     def __repr__(self):
#         return "<Point {} {}>".format(self.x, self.y)
#
#     __str__ = __repr__
#
#
# p1 = Point(4, 5)
# print(p1.x, p1.y)
# p1.x = 20
# print(p1.__dict__)
# p1.z = 100
# p1.__dict__['x'] = 200
# print(p1.__dict__)
#
# print(dir(p1))
# print(sorted(p1.__dir__()))
#
#
# p2 = Point(4, 5)
# print(p2.x)
# print(getattr(p2, 'y', 2000))  # 2000为缺省值
# # print(getattr(p2, 'z'))
# if not hasattr(p2, 'z'):
#     print(getattr(p2, 'z', 3000))  # 3000为缺省值
#
# setattr(p2, 'z', 3000)
# print(p2.__dict__)  # {'x': 4, 'y': 5, 'z': 3000}
# # print(getattr(p2, '__dict__'))
#
#
# setattr(Point, 'XYZ', 1000)   # 给类动态增加属性
# print(Point.__dict__)
#
# if not hasattr(Point, 'show'):
#     # 为类动态的增加方法
#     setattr(Point, 'show', lambda self: print(self.x, self.y))
#
# p3 = Point(4, 5)
# p3.show()
# Point.show(p3)
#
# p4 = Point(5, 6)
# if not hasattr(p4, 'showy'):
#     setattr(p4, 'showy', lambda self: print(self.y))  # 给实例动态的增加方法,但是没有绑定，就是要手动注入实例，不推荐这么增加方法
#     # TypeError: <lambda>() missing 1 required positional argument: 'self'
#     # setattr(p4, 'showy', lambda: print(123))
# p4.showy(p4)  # 6
# # p4.showy()  # 123
# print(p4.show)  # <bound method <lambda> of <__main__.Point object at 0x0000000002209748>>;即会将第一参数绑定为实例
# print(p4.showy)  # <function <lambda> at 0x0000000002260BF8>
#
# p5 = Point(10, 10)
# p6 = Point(4, 5)
#
# setattr(Point, '__add__', lambda self, other: self.__class__(self.x + other.x, self.y + other.y))
# print(p5 + p6)  # <Point 14 15>
#
#
# # 命令分发器
# class Dispatcher:
#     def __init__(self):
#         pass
#
#     def reg(self, name, fn):
#         setattr(self, name, fn)
#
#     def run(self):
#         while True:
#             cmd = input('>>>').strip()
#             if cmd == "quit":
#                 break
#             getattr(self, cmd, lambda: print('Unknown cmd {}'.format(cmd)))()  # lambda函数为缺省值
#
#
# def foo2(x, y):
#     return x + y
#
#
# dis = Dispatcher()
# dis.reg('ls', lambda: print('ls'))
# dis.reg('foo1', lambda: print('foo1 function'))
# dis.reg('foo2', foo2)
# dis.run()


class Base:
    n = 0


class Point(Base):
    z = 6
    d = {'tt': '20000'}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # setattr(self, 'x', x)
        # setattr(self, 'y', y)
        # self.__dict__['x'] = x
        # self.__dict__['y'] = y

    def show(self):
        print(self.x, self.y)

    # def __getattribute__(self, item):  # 默认的返回值为None
    #     # print(type(item))
    #     # print(item)
    #     # return 1
    #     # return super().__getattribute__(item)
    #     # return object.__getattribute__(self, item)
    #     raise AttributeError('tt')

    def __getattr__(self, item):
        print(item, '~~~~~~~~~~~~')
        # print(type(item))  # item是字符串
        # return "missing {}".format(item)
        # return self.d[item]
        return __class__.d[item]  # 注意不能写成self.d[item]，否则会无限递归

    # def __setattr__(self, key, value):
    #     print('setattr {}={}'.format(key, value))
    #     if key not in self.__dict__.keys():
    #         self.d[key] = value
    #     else:
    #         self.__dict__[key] = value  # 操作实例字典，将属性赋值放在字典中
    #     # super().__setattr__(key, value)  # 调用父类object的__setattr__方法
    #     # self.key = value  # 无限递归
    #     # setattr(self, key, value)  # 无限递归

    def __delattr__(self, item):
        print('del attribute {}'.format(item))


# p3 = Point(4, 5)
# # print(p3.__dict__)  # {'x': 4, 'y': 5}
# # print(p3.x)   # 实例访问的第一道关是__getattribute__方法
# print(p3.tt)  # 20000


p2 = Point(4, 5)
del p2.x
del p2.z
print(p2.x)
# print(p2.__dict__)  # {'x': 4, 'y': 5}
# print(p2.x, p2.y)
# p2.tt = 2000
# print(p2.tt)  # tt ~~~~~~~~~~~~ 2000


# p1 = Point(4, 5)
# print(p1.x)
# print(p1.z)
# print(p1.n)
# print(p1.t)  # 实例没有t属性
# p1.x = 50  # setattr x=50;实例通过点号设置属性，就会调用__setattr__()
# print(p1.x)  # missing x
# print(p1.__dict__)  # {}
# p1.__dict__['x'] = 60
# print(p1.__dict__)  # {'x': 60}
# print(p1.x)
