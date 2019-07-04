import math
import pickle
import json
import msgpack


class Shape:

    def area(self):
        raise NotImplementedError('不用实现')


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        # print(s)
        return s


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        s = self.x * self.y
        # print(s)
        return s


class SerializableMixin:
    def dumps(self, typ=json):
        if typ == 'json':
            ret = json.dumps(self.__dict__)
        elif typ == 'msgpack':
            ret = msgpack.dumps(self.__dict__)
        else:
            ret = pickle.dumps(self.__dict__)
        return ret


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        s = math.pi * self.r * self.r
        # print(s)
        return s


class SerializableCircleMixin(SerializableMixin, Circle):
    pass


scm = SerializableCircleMixin(4)
print(scm.area)
print(scm.dumps())
print(scm.__dict__)

t = Triangle(3, 4, 5)  # 改进版的思路：对于同一个实例，不需要重复计算
print(t.area())
r1 = Rectangle(5, 6)
print(r1.area())
c1 = Circle(4)
print(c1.area())
