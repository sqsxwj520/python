import random


class RandomNumber:

    def __init__(self, n, m, p):
        self.n = n
        self.m = m
        self.p = p

    def generate(self):
        # for i in range(self.n):
        #     print(random.randint(self.m, self.p))
        return [random.randint(self.m, self.p) for _ in range(self.n)]


t1 = RandomNumber(10, 0, 20)
print(t1.generate())


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y


t2 = RandomNumber(20, 0, 10)
# print(t2.generate())
points = [Coordinate(random.choice(t2.generate()),
                     random.choice(t2.generate())) for i in range(20)]
# print(points)
for q in points:
    print('({}, {})'.format(q.x, q.y))


class Car:

    def __init__(self, mark,  color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed

    def get_desc(self):
        information = str(self.mark) + ' ' + str(self.color) + ' ' + \
                      str(self.price) + ' ' + str(self.speed)
        return information


class CarInfo:

    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def get_all_info(self):
        return self.cars


car_info = CarInfo()
car1 = Car('audi', 'black', '350000￥', '100km/h')
print(car1.get_desc())
car2 = Car('宝马', 'white', '450000￥', '90km/h')
print(car2.get_desc())
car_info.add_car(car1)
car_info.add_car(car2)
# print(car_info.get_all_info())
# print(car_info.__dict__)
for i in car_info.get_all_info():
    print(i.get_desc())


class TempConverte:

    def __init__(self, t, f, k):
        self.t = t
        self.f = f
        self.k = k

    def temcov(self):
        f = 9 * self.t / 5 + 32
        return f

    def temcov2(self):
        t = 5 * (self.f - 32) / 9
        return t

    def temcov3(self):
        k = self.t + 273.15
        return k

    def temcov4(self):
        t = self.k - 273.15
        return t


temp = TempConverte(30, 86, 303.15)
print(temp.temcov())
print(temp.temcov2())
print(temp.temcov3())
print(temp.temcov4())


class Products:
    def __init__(self, **kwargs):
        self.goods = kwargs

    def get_desc(self):
        information = self.goods
        return information


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product: Products):
        self.products.append(product)

    def get_all_product(self):

        return self.products


mycart = ShoppingCart()
good1 = Products(mark='Nike', color='balck', size='42', price='1800￥')
good2 = Products(mark='Nike', color='white', size='42', price='1800￥')
mycart.add_product(good1)
mycart.add_product(good2)
mycart.get_all_product()
for j in mycart.get_all_product():
    print(j.get_desc())
