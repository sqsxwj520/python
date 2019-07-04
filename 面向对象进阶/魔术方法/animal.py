class Animal:
    x = 123

    def __init__(self, name):
        self.name = name
        self.age = 20
        self.weight = 20


y = 200
print('animal Module\'s names = {}'.format(dir()))  # 模块的属性
# animal Module's names = ['Animal', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'y']


class Person:

    def show(self):
        a = 100
        t = int(a)
        print(1, dir())  # 结果为列表 1 ['a', 'self', 't']
        print(2, locals())  # 结果为字典 2 {'t': 100, 'a': 100, 'self': <__main__.Person object at 0x0000000001E496A0>}
        print(3, locals().keys())


def test(a=50, b=100):
    c = 180
    print(4, dir())  # 4 ['a', 'b', 'c']
    print(5, locals())  # 5 {'c': 180, 'b': 100, 'a': 50}


Person().show()
test()
print(6, dir())  # 6,7,8三者的结果一样
print(7, sorted(locals().keys()))  # globals和locals返回时字典
print(8, sorted(globals().keys()))
# 8 ['Animal', 'Person', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
#  '__name__', '__package__', '__spec__', 'test', 'y']
