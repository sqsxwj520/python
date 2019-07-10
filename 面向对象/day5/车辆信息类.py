"""车辆信息"""


class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


class InfoMgr:

    def __init__(self):

        self.__info = []

    def add_info(self, car: Car):

        self.__info.append(car)
        return self

    def get_all(self):

        return [(x.mark, x.color, x.speed) for x in self.__info]  # 屏蔽敏感信息


car1 = Car('Audi', 'red', 40, 200)
car2 = Car('Redflag', 'black', 60, 200)

info = InfoMgr()
print(info.add_info(car1).add_info(car2).get_all())
