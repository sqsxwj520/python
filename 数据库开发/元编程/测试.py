
class Meta(type):
    # 现在的new方法跟以前不同了

    def __new__(mcs, name, bases, attr: dict):
        print(mcs)
        print(name)
        print(bases)
        print(attr)
        attr['id'] = 300  # 会改变类A中自己定义的id
        print()
        return super().__new__(mcs, name, bases, attr)  # 什么都可以改变


print("~~~~~~~~~~~~~~~~~~")


# 元类是创造类的类
class A(metaclass=Meta):  # 修改了元类，并没有改变继承列表
    # A的名字可以被元类改变，不仅如此，A的所有属性都可以被元类修改
    id = 2000

    def __init__(self):
        print('A.init~~~~~~~~')


class B(A):
    # B的属性也会受元类的影响，元类也可以改变B类的属性
    pass


C = Meta('C', (), {})
print(type(C), C.__bases__)
print(type(A), A.__bases__)
print(type(B), B.__bases__)  # 继承时，元类与父类A一样

"""
<class '__main__.Meta'> (<class 'object'>,)
<class '__main__.Meta'> (<class 'object'>,)
<class '__main__.Meta'> (<class '__main__.A'>,)
"""
print('+++++++++++++++++')


class D:
    pass


E = type('E', (), {})

print(type(D), D.__bases__)
print(type(E), E.__bases__)
# <class 'type'> (<class 'object'>,)
# <class 'type'> (<class 'object'>,)
print('====================')


class F(Meta):  # 注意是继承，F现在也是元类,元类实例化就是在构造新的类
    pass


print(type(F), F.__bases__)
# <class 'type'> (<class '__main__.Meta'>,)
