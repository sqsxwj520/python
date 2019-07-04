
class Document:  # 抽象基类
    """抽象基类中可以定义多个抽象方法，可以全都不实现，只是约束子类的规范,子类中进行覆盖"""

    def __init__(self, content):
        self.content = content

    def print(self):  # 抽象方法 ——> 抛出异常的方法（只定义不实现的方法）
        # 在python中如果采用这种方式定义的抽象方法，子类可以不实现，直到子类使用该方法时才报错
        raise NotADirectoryError('不用实现')


def printable(cls):  # 用装饰器增强一个类，把功能给类附加上去，哪个类需要它，就装饰它

    def _reg(self):
        print(self.content, '{}'.format(self.__class__.__name__))  # format里面的self不能少，否则会出错
    cls.print = _reg

    return cls  # 利用装饰器给类动态增加方法


def fn(name: str):  # 利用装饰器给类动态增加变量

    def wrapper(cls):
        cls.NAME = name
        return cls

    return wrapper


@printable
class Word(Document):  # 先继承后装饰
    pass

    # def print(self):  # 覆盖父类的方法
    #     print(self.content, '~~~ in word')


@fn('xyz')
class Pdf(Document):

    def print(self):
        print(self.content, '~~~ in pdf')


w = Word('test word string')
w.print()

p = Pdf('test pdf string')
p.print()
print(p.NAME)
