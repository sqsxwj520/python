class Person:
    age = 20

    def __init__(self, name):  # 初始化——出场配置，对生成的实例进行属性配置；__init__方法不能有返回值
        self.name = name  # self为当前实例，self.name为当前实例的name属性
        print(self, id(self))

    def show_age(self):
        return self.age


t = Person('tom')  # 括号里的参数必须与__init__相同，self不用给
j = Person('Jerry')  # 实例化，注意两个实例是完全不同的；右边先实例化，再初始化

print(t.name, t.age)  # 实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是类所有实例共享的属性和方法
print(j.name, j.age)
Person.age = 40
print(j.age)  # 注意j.age值的变化
print(t.age)

print(Person.__class__, type(Person))  # 两者是等价的
print(Person.__name__)  # 结果为字符串

print(Person.__class__.__name__, type(Person).__name__)  # 结果为字符串

print(Person.__dict__)  # 所有的类属性全在字典中，__init__也是类属性，也在字典中

t1 = Person('tom')
print(t1.__class__, type(t1))  # 返回的是类型，不是字符串

print(t1.__class__.__class__.__name__)  # 返回值为字符串'type'

print(t1.__dict__)  # 实例的属性，所以其字典中只有name属性{'name': 'tom'}

t2 = Person('Jerry')
print(t2.__dict__)  # 字典中只有name属性{'name': 'Jerry'}
