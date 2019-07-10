
"""随机整数生成类"""
import random


class RandomGen:
    def __init__(self, start=1, stop=100, count=10):
        self.start = start
        self.stop = stop
        self.count = count
        self._gen = self._generate()  # 调用__init__时，说明实例已经存在，只是没有设置出厂配置；为实例动态增加属性

    # def generate(self):
    #
    #     return [random.randint(self.start, self.stop) for _ in range(self.count)]

    def _generate(self):

        while True:
            yield random.randint(self.start, self.stop)

    def genarate(self):
        # a = self.test()  # 此句可以提到上面的__init__方法中
        return [next(self._gen) for _ in range(self.count)]  # 此处的self.count是实例的属性


r = RandomGen()
# print(RandomGen().generate())  # 不同的实例，生成不同的数
print(r.genarate())


class RandomGene:  # 工具函数，没有实例什么事

    @classmethod
    def generate(cls, start=1, stop=100, count=10):

        return [random.randint(start, stop) for _ in range(count)]


print(RandomGen().genarate())
