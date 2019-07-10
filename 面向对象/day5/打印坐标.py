import random


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


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # 打印字符串，具体是什么内容，由你来定
        return "<Point {}:{}>".format(self.x, self.y)


r = RandomGen()
points = [Point(x, y) for x, y in zip(r.generate(), r.generate())]

for p in points:
    print(p)
