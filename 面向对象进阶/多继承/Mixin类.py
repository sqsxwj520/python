
class Document:

    def __init__(self, content):
        self.content = content


class Word(Document):
    pass


class Pdf(Document):
    pass


class PrintableMixin:
    def print(self):
        print(self.content, '{}'.format(self.__class__.__name__))


class PrintableWord(PrintableMixin, Word):  # Mixin类写在最前面
    pass


def printable(cls):  # 用装饰器增强一个类，把功能给类附加上去，哪个类需要它，就装饰它

    def _reg(self):
        print(self.content, '{}'.format(self.__class__.__name__))  # format里面的self不能少，否则会出错
    cls.print = _reg

    return cls  # 利用装饰器给类动态增加方法


@printable
class PrintablePdf(Word):
    pass


class SuperPrintableMixin(PrintableMixin):
    def print(self):
        print('~~' * 20)
        super().print()
        print('~~' * 20)


class SuperPrintablePdf(SuperPrintableMixin, Pdf):
    pass


print(SuperPrintablePdf.__dict__)
print(SuperPrintablePdf.mro())
# [<class '__main__.SuperPrintablePdf'>, <class '__main__.SuperPrintableMixin'>, <class '__main__.PrintableMixin'>,
# <class '__main__.Pdf'>, <class '__main__.Document'>, <class 'object'>]
spp = SuperPrintablePdf('super print pdf')
spp.print()
pw = PrintableWord('test pw string')
print(PrintablePdf.__dict__)  # 装饰器会增加类的print方法。在其字典中可以看到
# {'__module__': '__main__', '__doc__': None, 'print': <function printable.<locals>._reg at 0x0000000002840048>}
print(PrintablePdf.mro())
# [<class '__main__.PrintablePdf'>, <class '__main__.Word'>, <class '__main__.Document'>, <class 'object'>]

print(pw.__class__.__dict__)
# {'__module__': '__main__', '__doc__': None}
print(pw.__class__.mro())  # 结果为列表
# [<class '__main__.PrintableWord'>, <class '__main__.PrintableMixin'>,
# <class '__main__.Word'>, <class '__main__.Document'>, <class 'object'>]
pw.print()  # test pw string PrintableWord
