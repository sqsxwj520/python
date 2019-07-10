class Animal:
    __COUNT = 100  # 私有属性，python解释器会自动给你改名为_Animal__COUNT
    HEIGHT = 0

    def __init__(self, age, weight, height):
        self.__COUNT += 1  # self._Animal__COUNT = self._Animal__COUNT + 1
        self.age = age
        self.__weight = weight  # self._Animal__weight = weight
        self.HEIGHT = height

    def eat(self):
        print('{} eat'.format(self.__class__.__name__))

    def __get_weight(self):  # _Animal__get_weight
        print(self.__weight)  # _Animal__weight

    @classmethod
    def show_count1(cls):
        print(cls)
        print(cls.__dict__)
        print(cls.__COUNT)  # cls_Animal__COUNT;子类的没有的就继承父类的

    @classmethod
    def __show_count2(cls):  # cls_Animal__show_count2
        print(cls.__COUNT)   # cls_Animal__COUNT

    def show_count3(self):
        print(self.__COUNT)  # self._Animal__COUNT


class Cat(Animal):
    NAME = 'cat'
    __COUNT = 200  # _cat__COUNT


c = Cat(3, 5, 15)
# c.eat()  # Cat eat
# print(c.HEIGHT)  # 15
# print(c.__COUNT)  # 访问不了，私有属性
# print(c.__get_weight())  # 访问不了，私有方法，c._Animal__get_weight()
# c._Animal__get_weight()  # 5
c.show_count1()  # 100
# c._Animal__show_count2()  # 100
c.show_count3()  # 101
# print(c._Cat__COUNT)  # 200
# print(c._Animal__COUNT)  # 101
print(Animal.__dict__)
