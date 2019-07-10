
class Meta(type):
    # 现在的new方法跟以前不同了

    def __new__(mcs, name, bases, attr: dict):
        print(mcs)
        print(name)
        print(bases)
        print(attr)
        attr['id'] = 300  # 会改变类A中自己定义的id
        print()
        return super().__new__(mcs, name + '123', bases, attr)  # 什么都可以改变


print("~~~~~~~~~~~~~~~~~~")


# 元类是创造类的类
class A(metaclass=Meta):  # 修改了元类，并没有改变继承列表
    # A的名字可以被元类改变，不仅如此，A的所有属性都可以被元类修改
    id = 2000

    def __init__(self):
        print('A.init~~~~~~~~')


"""
~~~~~~~~~~~~~~~~~~
<class '__main__.Meta'>
('A', (), {'__module__': '__main__', '__qualname__': 'A'})
{}

"""

print(type(A))  # <class '__main__.Meta'>
print(A.__bases__)  # (<class 'object'>,),没有return语句，直接报错Nonetype
print(A.__dict__)

print('++++++++++++++')


class B(A):
    # B的属性也会受元类的影响，元类也可以改变B类的属性
    pass


print(type(B), B.__bases__)  # 继承时，元类与父类A一样
# <class '__main__.Meta'> (<class '__main__.A'>,)
print(B.__dict__)
# {'__module__': '__main__', 'id': 300, '__doc__': None}
print(B.__name__)  # B123
