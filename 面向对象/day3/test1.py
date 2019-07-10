
class Person:  # 类的命名方式为大驼峰
    tall = 178
    age = 34

    def __init__(self, name, age):  # 初始化——出厂配置，对生成的实例进行属性配置
        self.name = name  # 当前实例的name属性
        self.age = age  # self指当前实例；__init__方法不能有返回值

    def show_age(self):  # self必须为第一形参
        print(self.age, self.name)

    @classmethod  # 类方法装饰的方法，第一参数是类本身，不在是self了，还可以有其他参数
    def clsmtd(cls):
        print(cls)

    @staticmethod  # 静态方法装饰的方法，可以没有任何参数
    def stmtd():
        print('static')


t = Person('tom', 20)  # 实例化；实例没有__name__属性
j = Person('Jack', 45)  # 实例之间没有关系

j.show_age()  # python语法会将j作为实例，所以括号里不需要参数了
print(Person.show_age)  # 后面不能再加括号，否则直接抛出异常
print(t.tall)  # 实例可以访问类属性
print(j.tall)  # 实例优先使用自己的属性，自己没有的属性，使用类的，类没有直接抛出AttibuteError
print(Person.tall)
j.tall = 196  # 可以为实例也动态增加实例的属性
Person.tall = 188
print(Person.__dict__)  # 类的字典存放的是类的属性
print(t.__dict__)  # 实例的字典存放的是实例的属性；__dict__[变量名]为字典访问方式，'实例.变量名'访问方式为属性访问
Person.weight = 180  # 可以动态的为类增加一个类属性
Person.clsmtd()  # 不用添加参数
