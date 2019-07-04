# class A:
#     X = 1
#     # __slots__ = 'x', 'y'
#     # __slots__ = ('x', 'y')
#     __slots__ = ['x', 'y']
#
#     def __init__(self):
#         self.x = 5
#         self.y = 6
#
#     def show(self):
#         print(self.x, self.y)
#
#
# a = A()
# a.show()
# print('A', A.__dict__)
# print(a.__slots__)  # ('x', 'y')
# # a.new = 10  # AttributeError
# A.new = 10  # 可以动态的增加类色属性
# print(A.__dict__)

print(type(NotImplementedError))  # <class 'type'> NotImplementedError为异常类
# <class 'type'>
print(type(None))  # <class 'NoneType'>
print(type(NotImplemented))  # <class 'NotImplementedType'>未实现单值
# <class 'NotImplementedType'>
