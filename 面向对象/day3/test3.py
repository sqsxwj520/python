class MyClass:  # class开头，类命必须采用大驼峰格式，
    """A example of class"""  # 文档字符串
    x = 'abc'  # 类属性

    def foo(self):  # 类属性，也是类方法
        print('foo method')


print(MyClass.__doc__)
print(MyClass.x)  # 访问属性
print(MyClass.foo)  # 访问方法，foo后不能再带括号了
print(MyClass.__name__)  # 结果为字符串

"""类对象：类的定义执行后会生成一个类对象
类的属性：类定义中的变量和类中定义的方法都是类的属性
类变量：上例中x是类MyClass的变量"""

# 实例化
a = MyClass()
print(a)
