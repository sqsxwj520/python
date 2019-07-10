
class Person:

    def __init__(self):
        self.name = 'tom'
        self.__age = 20

    def get_age(self):
        return self.__age  # 可以写成lambda表达式

    def set_age(self, age):  # 不能改写为lambda表达式，lambda表达式不能有等号
        self.__age = age

    age = property(get_age, set_age)  # property是类


t = Person()
print(t.get_age())
t.set_age(30)
print(t.age)
t.age = 300
print(t.age)
