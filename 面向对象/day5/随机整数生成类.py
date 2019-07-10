import random


# class RandomGen:
#     def __init__(self, start=1, end=100, count=10):
#         self.start = start
#         self.end = end
#         self.count = count
#
#     def generate(self):
#         return [random.randint(self.start, self.end) for _ in range(self.count)]
#
#
# num = RandomGen()
# print(num.generate())

#
# class RandomGen:  # 工具类，定义一个工具函数，就是一批一批的生成数；以后可以定义很多工具函数
#     @classmethod
#     def generate(cls, start=1, end=100, count=10):
#         return [random.randint(start, end) for _ in range(count)]
#
#
# num = RandomGen()
# print(num.generate())
#
# class RandomGen:
#     def __init__(self, start=1, end=100, count=10):  # __init__没有返回值，怎么得到实例的呢？
#         # 调用__init__的时候，实例就已经存在了，不是通过__init__返回实例的
#         self.start = start
#         self.end = end
#         self.__count = count
#         self._gen = self._generate()  # 结果是生成器对象
#
#     @property
#     def count(self):
#         return self.__count
#
#     @count.setter
#     def count(self, count):
#         self.__count = count
#
#     def _generate(self):
#         while True:  # 无限的产生数据
#             yield random.randint(self.start, self.end)  # 一个一个的产生数据
#
#     def generate(self, count=10):
#         c = count if 10 < count < 100 else self.count  # 也可以直接改为self.__count
#         # a = self.test()
#         return [next(self._gen) for _ in range(c)]  # 对一个生成器对象拨动了self.count下
#
#
# r = RandomGen()  # 实例化分两步，第一步先实例化，然后再是初始化，初始化时，实例就已经存在了
# print(r.generate())
# r.count = 5
# print(r.generate())


class RandomGen:
    def __init__(self, start=1, end=100, count=10):  # __init__没有返回值，怎么得到实例的呢？
        # 调用__init__的时候，实例就已经存在了，不是通过__init__返回实例的
        self.start = start
        self.end = end
        self.__count = count
        self._gen = self._generate()  # 结果是生成器对象

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def _generate(self):
        while True:  # 无限的产生数据
            # 一批一批的产生数据
            yield [random.randint(self.start, self.end) for _ in range(self.count)]

    def generate(self, count=10):
        if count > 0:
            self.__count = count

        return next(self._gen)  # 对一个生成器对象拨动了self.count下


r = RandomGen()  # 实例化分两步，第一步先实例化，然后再是初始化，初始化时，实例就已经存在了
print(r.generate())
# r.count = 5
print(r.generate(3))
