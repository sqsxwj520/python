
def __init__(self):
    self.x = 1000


def show(self):
    print(self.x)


XClass = type('X', (object, ), {'a': 100, 'b': 'abc',
                                '__init__': __init__,
                                'show': show})  # 类
print(XClass)
# <class '__main__.X'>
print(XClass.__name__)  # X
print(XClass.__dict__)
# (<class 'object'>,)
print(XClass.__bases__)
print(XClass.mro())
# [<class '__main__.X'>, <class 'object'>]
print(XClass().x)  # 1000

print(XClass().show())  # None

print(type(XClass))  # <class 'type'>
