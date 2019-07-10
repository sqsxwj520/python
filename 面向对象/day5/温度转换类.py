"""温度转换"""


class Temperature:

    def __init__(self, t, unit='c'):  # 事先计算好三种温度；还有一种思路就是需要的时候再计算
        if unit == 'c':
            self.c = t
            self.f = self.c2f(t)
            self.k = self.c2k(t)
        elif unit == 'k':
            self.c = self.k2c(t)
            self.f = self.k2f(t)
            self.k = t
        elif unit == 'f':
            self.c = self.f2c(t)
            self.f = t
            self.k = self.f2k(t)
        else:
            pass

    @classmethod  # 提供工具函数，转换温度
    def c2f(cls, c):
        return 9 * c / 5 + 32

    @classmethod
    def f2c(cls, f):
        return (f - 32) * 5 / 9

    @classmethod
    def c2k(cls, c):
        return c - 273.15

    @classmethod
    def k2c(cls, k):
        return k + 273.15

    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))

    @classmethod
    def k2f(cls, k):
        return cls.c2f(cls.k2c(k))


t1 = Temperature(40, 'c')
print(t1.f)
print(t1.k)
print(t1.c)
print('~' * 40)

t1 = Temperature(40, 'k')
print(t1.f)
print(t1.k)
print(t1.c)
print('~' * 40)

t1 = Temperature(40, 'f')
print(t1.f)
print(t1.k)
print(t1.c)
