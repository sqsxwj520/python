# class Fib:
#     def __init__(self):
#         self.items = [0,  1, 1]
#
#     def __len__(self):
#         return len(self.items)
#
#     def __iter__(self):
#         yield from self.items
#
#     def __getitem__(self, index):
#         if index < 0:
#             raise IndexError('not negative, Wrong index {}'.format(index))
#         if index < len(self):
#             return self.items[index]
#
#         for i in range(len(self.items), index + 1):
#             self.items.append(self.items[i - 1] + self.items[i - 2])
#
#         return self.items[index]
#
#     def __call__(self, index):
#         return self[index]
#
#     def __repr__(self):
#         return '<{} {}>'.foramt(__class__.__name__, self.items)
#
#
# f = Fib()
# print(f(0), f(1), f(2))
# print('~~~~~~~~~~~~~~~~')
# print(f(35))
# print('!!!!!!!!!!!!!!!')
# print(f(5))
# print(f[6])
# for z in f:
#     print(z)

#
# def foo():
#     print(foo.__module__, foo.__name__)
#
#
# foo()  # 等价于 foo.__call__()
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         return "< Point {} {}>".format(self.x, self.y)
#
#
# p = Point(4, 5)
# print(p)
# print(p())  # 类中定义了__call__方法，实例可以像函数一样调用
#
#
# class Adder:
#     def __call__(self, *args):
#         ret = 0
#         for x in args:
#             ret += x
#         self.ret = ret
#         return ret
#
#
# adder = Adder()
# print(adder(4, 5, 6))
# print(adder.ret)


class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        yield from self.items

    def __getitem__(self, index):
        if index < 0:
            raise KeyError('Wrong index')
        if index < len(self.items):
            return self.items[index]

        for i in range(len(self.items), index + 1):
            self.items.append(self.items[i - 2] + self.items[i - 1])
        return self.items[index]

    def __call__(self, index):
        return self[index]

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.items)


f = Fib()
print(f(5))
for x in f:
    print(x)
print(f[6])
print(len(f))
