# import tracemalloc
#
#
# tracemalloc.start()
# # d = [dict(zip('xy', (4, 5)))for i in range(1000000)]  # 237M
# # t = [tuple(zip('xy', (4, 5)))for j in range(1000000)]  # 191M
# # snapshot = tracemalloc.take_snapshot()  # 快照
# # # stats = snapshot.statistics('lineno')
# # stats = snapshot.statistics('filename')
# # for s in stats:
# #     print(s)
#
#
# class A:
#     __slots__ = 'y', 'x'  # 阻止了实例字典的创建,无法阻止类属性的修改,没有继承
#     # __slots__ = 'x y'.split()
#
#     def __init__(self):
#         self.x = 5
#         self.y = 6
#
#
# print(A.__dict__)
# # print(A().__dict__)
# # print(A().x, A().y)
# a = A()
# # a.z = 100  # 会报错，__slots__阻止你对实例属性的修改
# A.t = 2000
# print(A.__dict__)
# # a.y = 200
# # print(a.y)  # AttributeError: y
# d = [A() for i in range(1000000)]
# s = tracemalloc.take_snapshot()
# for x in s.statistics('filename'):
#     print(x)  # 61.7M,有__slots__方法
#     # 无__slots__方法时，占用空间为169M


# print(type(NotImplementedError))  # <class 'type'> NotImplementedError为异常类
# print(type(None))  # <class 'NoneType'>
# print(type(NotImplemented))  # <class 'NotImplementedType'>未实现单值


class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "<A {}>".FORAMT(self.x)

    def __add__(self, other):
        print('add~~~~~~')
        if hasattr(other, 'x'):
            return self.x + other.x
        else:
            try:
                x = int(other)
            except:
                x = 0
            return self.x + x

    def __iadd__(self, other):
        print('iadd~~~~~~~')

        return A(self + other)  # 运算符重载，解释器看到+会调用__add__方法

    def __radd__(self, other):
        print('radd~~~~~~~')

        return self + other
#
#
# a1 = A(4)
# a2 = A(5)
# # print(a1 + a2)  # 9 int——> a1.__add__(a2)
# # print(a2 + a1)
# print(a1 + 1)  # 会报错 a1.__add__(1),而1没有x属性
# print(1 + a1)  # 会报错 1.__add__(a1)  int.__add__(1, a1)
# print(a1 + A(10))  # a1.__add__(A(10))


class B:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        # return 123
        if type(self) != type(other):
            return NotImplemented
        return 123


b1 = B(6)
print(a1 + b1)  # add~~~~~~ 10, a1.__add__(b1)
print(b1 + a1)  # radd~~~~~~~10, a1.__radd__(b1);b1没有add方法,或者有这个方法，但是返回值为NotImplemented，就会调用后面的反向方法
