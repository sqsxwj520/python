
class Document:  # 抽象类——>不是用来实例化的;虽然可以实例化，但是不推荐
    def __init__(self, content):
        self.content = content

#
# def printable(cls):
#
#     def _print(self):
#         print(self.content, '~~ in {}'.format(self.__class__.__name__))  # 注意format中的self不能少，否则会出错，因为不在类内
#     cls.print = _print
#     return cls


def printable(cls):  # 利用装饰器给类增加一个方法
    def reg(self):
        print(self.content)
    cls.print = reg  # 类的属性
    return cls


def fn(name: str):  # 利用装饰器给类增加一个变量
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper


@fn('abc')
class Person:
    pass


print(Person.__dict__)


@printable   # Word = printable(Word)  ——>return Word
class Word(Document):
    pass


w = Word('test word string')
w.print()
