"""温度转换"""


class Temperature:

    # def __init__(self, t, unit='c'):  # 事先计算好三种温度；还有一种思路就是需要的时候再计算
    #     if unit == 'c':
    #         self.c = t
    #         self.f = self.c2f(t)
    #         self.k = self.c2k(t)
    #     elif unit == 'k':
    #         self.c = self.k2c(t)
    #         self.f = self.k2f(t)
    #         self.k = t
    #     elif unit == 'f':
    #         self.c = self.f2c(t)
    #         self.f = t
    #         self.k = self.f2k(t)
    #     else:
    #         pass
    def __init__(self, t, unit='c'):  # 第二种思路，需要的时候再计算
        self.__c = None
        self.__f = None
        self.__k = None
        if unit == 'c':
            self.__c = t
        elif unit == 'k':
            self.__k = t
            self.__c = self.k2c(t)
        elif unit == 'f':
            self.__f = t
            self.__c = self.f2c(t)

    @property
    def c(self):
        return self.__c

    @property
    def f(self):
        if self.__f is None:
            self.__f = self.c2f(self.__c)  # 此处的self.__c可以换成self.c
            return self.__f

    @property
    def k(self):
        if self.__k is None:
            self.__k = self.c2k(self.__c)
        return self.__k

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


t1 = Temperature(100, 'k')
print(t1.c, t1.f, t1.k)

t2 = Temperature(100, 'c')
print(t2.c, t2.f, t2.k)

t3 = Temperature(100, 'f')
print(t3.c, t3.f, t3.k)
