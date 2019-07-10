class Person:
    def __init__(self, name, age):  # 初始化——出场配置，对生成的实例进行属性配置；__init__方法不能有返回值
        self.name = name  # self为当前实例，self.name为当前实例的name属性
        self.age = age

    def showage(self):
        print(self.age, self.name)


t = Person('tom', 20)  # 括号里的参数必须与__init__相同，self不用给
j = Person('Jerry', 18)  # 实例化，注意两个实例是完全不同的；右边先实例化，再初始化

print(t.name, t.age)  # 实例的属性
print(j.name, j.age)

t.showage()  # python语法看到实例调用，会隐含的将t实例注入到showage中
# print(Person.showage())  # 会抛出异常，showage中缺少参数
print(Person.showage)
print(Person.showage(t))
print(j.showage)  # 绑定，将j和self绑在一起

j.age += 1
j.showage()
