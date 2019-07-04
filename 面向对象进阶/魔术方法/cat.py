import animal
from animal import Animal


class Cat(Animal):
    x = 'cat'
    y = 'abcd'


class Dog(Animal):
    @staticmethod
    def __dir__():  # 返回可迭代对象的返回值
        return ['dog']  # 必须返回可迭代对象，并且内容都是字符串


print('Current Module\'s names = {}'.format(dir()))
print('Current Module\'s names = {}'.format(dir(animal)))
# animal Module's names = ['Animal', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__']
# Current Module's names = ['Animal', 'Cat', 'Dog', '__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'animal']

print("object's __dict__ = {}".format(sorted(object.__dict__.keys())))
# object's __dict__ = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

print("Animal's dir() = {}".format(dir(Animal)))  # 类Animal的dir()
# Animal's dir() = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'x']
print("Cat's dir() = {}".format(dir(Cat)))  # 类Cat的dir()
# Cat's dir() = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'x', 'y']
print('~~~~~~~~~~~~~~~~')
tom = Cat('tom')
print(sorted(dir(tom)))  # 尽可能多的收集实例tom的属性、Cat类及所有祖先类的类属性
print(sorted(tom.__dir__()))  # 同上
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  'age', 'name', 'weight', 'x', 'y']
print("Dog's dir = {}".format(dir(Dog)))  # Animal类中的x也在其中
dog = Dog('snoppy')
print(dir(dog))  # ['dog']
print(dog.__dict__)  # {'name': 'snoppy', 'age': 20, 'weight': 20}
