# class A:
#     # @staticmethod
#     def __new__(cls, *args, **kwargs):  # 静态方法
#         cls.test = 'abc'  # 给类增加属性，但是不好，每次实例化都要创建一次
#         # return 'abc'
#         print(cls)
#         print(args)  # ('tom',)
#         # args = ('jerry', )  # 不会改变a.name的值
#         print(kwargs)  # {'name': 'tom'}
#         ret = super().__new__(cls)
#         # ret.age = 100  # 不建议在这里，可以放在__init__方法中
#         return ret  # 调用父类的方法；返回实例
#
#     def __init__(self, name):  # 将__new__方法返回的实例注入到self
#         self.name = name
#
#
# # a = A('tom')
# a = A(name='tom')
# print(a)  # None
# print(a.name)
# print(A.__dict__)
# print(a.age)

#
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return 'str: {} {}'.format(self.name, self.age)
#
#     def __repr__(self):
#         return 'repr: {} {}'.format(self.name, self.age)
#
#     def __bytes__(self):
#         return 'bytes: {} {}'.format(self.name, self.age).encode()
#
#
# a = Person(name='tom')
# print(a)  # <__main__.Person object at 0x00000000027F0FD0>
# # str: tom 18
# print(str(a))  # <__main__.Person object at 0x00000000027F0FD0>
# print(str(a).encode())  # b'str: tom 18'
#
# print(bytes(a))  # b'bytes: tom 18'
# print(repr(a))  # repr: tom 18
#
# print([a])  # [repr: tom 18]  print(str([])) 列表中又调用repr
# print((a, ))  # (repr: tom 18,)
# print('{}'.format(a))  # str: tom 18
# # 没有str方法，会找repr方法，但是没有repr方法，直接找基类的

#
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return 1
#
#     def __eq__(self, other):
#         return self.age == other.age  # 这样写的话，p1 == p2 ——>True
#
#     def __repr__(self):
#         return '<Person {} {}>'.format(self.name, self.age)
#
#
# print(hash(1), hash(2), hash(5000000))  # 整数的hash算法是取模，除数是62位的整数
# print(hash('abc'))
# print(hash(('abc', )))
# print(hash(Person))
# print(hash(Person('tom')))
# p1 = Person('tom')
# p2 = Person('jerry')
# print(hash(p1), hash(p2))
# print({123, 123})  # {123}去重了
# print({p1, p2})  # {<Person tom 18>, <Person jerry 18>}
# # 没有去重，是因为p1和p2的内容不同（虽然他们的hash值相同）;去重两个条件内容相同，hash值相同
# print('~~~~~~~~~~', p1 == p2)  # 会调用__eq__方法
# print({(123, ), (123, )})  # {(123,)} 去重了

# print(hash(list()))

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return '<Point {},{}>'.format(self.x, self.y)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# p1 = Point(12, 14)
# p2 = Point(34, 65)
# p3 = Point(12, 14)
# print(p1)  # <Point 12,14>
# print(p2)
# print(hash(p1))
# print(hash(p2))
# print(p1 == p2)  # False
# print(p1 == p3)  # True


# class A:
#     pass
#
#
# print(bool(A))  # True
# print(bool(A()))  # True
# print(bool([]))  # False
#
#
# class B:
#     def __bool__(self):
#         print('in bool')
#         # return 1
#         # return bool(self)  # 无限递归
#         return bool(1)
#
#
# print(bool(B))  # True
# # print(bool(B()))  # 会出错
# if B():
#     print('b~~~~~~~~~~~~')
#
#
# class C:
#     def __len__(self):
#         return 1  # 必须大于0
#
#
# print(bool(C))
# print(bool(C()))


# class A:
#     def __init__(self, age):
#         self.age = age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __isub__(self, other):
#         # return A(self.age - other.age)  #新实例
#         # self.age -= other.age
#         # return self  # 31691272 <__main__.A object at 0x0000000001E39208>\
#         # 31691272 <__main__.A object at 0x0000000001E39208>就地修改
#         return A(self - other)  # 新实例
#
#
# a1 = A(20)
# a2 = A(12)
# print(id(a1), a1)  # 32150024 <__main__.A object at 0x0000000001EA9208>
# # print(a1 - a2)  # 8数值
# # print(a1.__sub__(a2))  # 8
# # print(a2 - a1, a2.__sub__(a1))  # -8
# a1 -= a2  # a1__isub__(a2)
# print(id(a1), a1)  # 32151032 <__main__.A object at 0x0000000001EA95F8>

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def add(self, other):
#         return self.__class__(self.x + other.x, self.y + other.y)
#     #
#     # def __add__(self, other):
#     #     return self.add(other)
#     __add__ = add
#
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self  # 可以链式
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __repr__(self):
#         return '<Point {},{}>'.format(self.x, self.y)
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1 + p2)  # <Point 4,6>
# p1 += p2
# print(id(p1), p1)  # 32150416 <Point 4,6>
# print(p1 + p2 + p2)  # <Point 10,14>


# from functools import total_ordering
#
#
# @total_ordering
# class A:
#     def __init__(self, values):
#         self.values = values
#
#     def __eq__(self, other):
#         return self.values == other.values
#
#     def __gt__(self, other):
#         return self.values > other.values
#
#
# a = A(10)
# b = A(8)
# print(a == b)
# print(a != b)
# print(a > b, a < b, a >= b, a <= b)


# class A(dict):
#     def __missing__(self, key):  # 默认返回None
#         print(key, 'missing ~~~')
#         value = 1000
#         self.__dict__[key] = value
#         return value
#
#
# a = A()
# print(isinstance(a, dict))  # True
# print(a['tt'])  # None; 1000
# print(a.__dict__)  # {'tt': 1000}


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        return self

    def __add__(self, other):
        self.add(other)
        return self

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        # print(index)
        return self.items[index]  # self[index]会无限递归

    def __setitem__(self, index, value):  # 一般不需要返回值
        self.items[index] = value
        # self[index] = value  # 不能这么写，会无限递归

    def __repr__(self):
        return '<Cart {} {}>'.format(__class__.__name__, self.items)

    def __iter__(self):
        # return iter(self.items)
        # for i in self.items:
        #     yield i
        yield from self.items


c1 = Cart()
c1.add(1)
c1.add(2)
c1.add(1).add(2)
print(c1)
c1 + 4 + 5
print(c1)
print(len(c1))
print(c1[0])
c1[1] = 100
print(c1[1])
for z in c1:
    print(z)
