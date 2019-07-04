class Document:  # 抽象类——>不是用来实例化的;虽然可以实例化，但是不推荐
    def __init__(self, content):
        self.content = content

    def print(self):  # 抽象方法——>抛出异常的方法；用来约束子类的规范
        # print(self.content)
        raise NotImplementedError('我就不实现')
    # 抽象类中可以定义很多抽象方法（全部都不实现），只是用来约束子类的规范


class Word(Document):  # 子类中必须覆盖父类中的所有抽象方法，子类才能实例化（其他语言），python没有强制要求，但是实例使用该方法时会报错
    def print(self):  # 不会出现递归调用，因为类内定义的方法，名字为类名.方法名
        print(self.content, '~~ in word')  # 此print时内建函数


class Pdf(Document):
    def print(self):
        print(self.content, '~~ in pdf')


w = Word('test word string')
w.print()

p = Pdf('test pdf string')
p.print()

# d = Document('test string')
# d.print()  # 直接抛出异常
