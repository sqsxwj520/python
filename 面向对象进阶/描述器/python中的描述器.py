class A:
    @classmethod
    def foo(cls):  # 非数据描述符——> foo = classmethod(foo)
        pass

    @staticmethod
    def bar():  # 非数据描述符
        pass

    @property
    def z(self):  # 数据描述符
        return 5

    def get_foo(self):  # 非数据描述符
        return self.foo

    def __init__(self):  # 非数据描述符
        self.foo = 100
        self.bar = 200
        # self.z = 300  # 不能覆盖，会报错，因为z为数据描述符


a = A()
print(a.__dict__)  # {'foo': 100, 'bar': 200}
print(A.__dict__)
