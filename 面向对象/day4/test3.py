class Person:
    age = 3
    height = 190

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom = Person('tom')
jerry = Person('jerry', 20)
Person.age = 30

print(1, Person.age, tom.age, jerry.age)

print(2, Person.height, tom.height, jerry.height)
jerry.height = 187
print(3, Person.height, tom.height, jerry.height)

tom.height += 10
print(4, Person.height, tom.height, jerry.height)

Person.weight = 80
print(5, Person.weight, tom.weight, jerry.weight)  # 实例自己没有，直接找字典要，字典没有直接抛出异常

# print(6, tom.__dict__['weight'])  # 会抛出异常，因为实例字典中没有weight属性
print(7, tom.weight)  # 不会出错，因为tom.weight是属性访问，自己没有此属性的话，会找类要，类没有才会抛出异常
