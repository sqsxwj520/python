# class Base:
#     n = 10
#
#
# class Point(Base):
#     z = 6
#     d = {}
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         setattr(self, 'y', y)
#         # self.__dict__['x'] = x
#         # self.__dict__['y'] = y
#         self.d['tttt'] = 20000
#
#     # def show(self):
#     #     print(self.x, self.y, self.z)
#
#     def __getattribute__(self, item):
#         print(item)
#
#     def __getattr__(self, item):  # 注意此方法是实例的
#         # print(item, '~~~~~~~~~~~~')
#         # print(type(item))  # <class 'str'>
#         # value = 1000
#         # self.__dict__[item] = value
#         # return value
#         return self.d[item]
#
#     def __setattr__(self, key, value):
#         print(key, value, '=====')
#         self.__dict__[key] = value
#
#         # if key not in self.__dict__.keys():
#         #     self.d[key] = value
#         # else:
#         #     self.__dict_[key] = value
#         # super().__setattr__(key, value)
#         # self.__dict__[key] = value
#         # setattr(self, key, value)  # 无限递归
#         # self.key  =value  # 无限递归
#
#     # def __delattr__(self, item):
#     #     print('del attribute {}'.format(item))
#
#
# # p1 = Point(4, 5)
# # print(p1.x, p1.y)
# # print(p1.z)
# # print(p1.n)
# # print(p1.__dict__)
# # print(p1.xxxxx)  # 找不到属性的时候，__getattr__方法会拦截错误
# # # xxxxx ~~~~~~~~~~~~
# # print('~' * 30)
# # print(p1.ttt)  # 1000
# # print(p1.__dict__)  # {'x': 4, 'y': 5, 'xxxxx': 1000, 'ttt': 1000}
#
# # p2 = Point(6, 7)
# # print(p2.x, '+++++++++++')
# # print(p2.y, "___________")
# # print(p2.__dict__)  # {'x': 6, 'y': 7}
#
# # p3 = Point(8, 9)
# # del p3.x
# # del Point.z
# # del p3.z
#
# p4 = Point(9, 10)
# print(p4.__dict__)  # {'x': 9, 'y': 10}
# print(p4.x, p4.y)
# p4.tttt = 2000
# print(p4.__class__.__dict__)
# # {'__module__': '__main__', 'z': 6, 'd': {'x': 9, 'tttt': 2000},
# # '__init__': <function Point.__init__ at 0x00000000021D3F28>, 'show': <function Point.s
# print(p4.tttt)


class Point:
    Z = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):  # 该方法会阻止通过实例来删除属性
        print('Can not del {}'.format(item))


p = Point(12, 2)
del p.x  # Can not del x
del p.Z  # Can not del Z
p.z = 17
del p.z  # Can not del z
print(Point.__dict__)
print(p.__dict__)  # {'x': 12, 'y': 2, 'z': 17}
del Point.Z
print(Point.__dict__)  # 类的字典中Z属性被删除了
