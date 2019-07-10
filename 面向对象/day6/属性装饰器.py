class Person:

    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    @property  # 属性装饰器，该装饰器装饰方法，下文中都必须用该方法
    def age(self):  # 给你看，不希望你修改
        print('getter')
        return self.__age

    @age.setter  # 此装饰器必须是age开头，且装饰的方法只能是age，可以修改私有属性
    def age(self, age):
        self.__age = age
        print('setter')

    @age.deleter
    def age(self):
        print('del')
        # del self.__age  # 一般不需要删除


tom = Person('Tom')
print(tom.age)
tom.age = 20  # 不管你是私有属性还是保护属性，用户只想通过普通属性修改和访问————属性装饰器
print(tom.age)
