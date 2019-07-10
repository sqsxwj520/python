# class Person:
#     def __init__(self):
#         self,name = 'tom'
#     def normal_function():
#         print('normal')
#
#     def method(self):
#         print('method')
#
#
# Person.normal_function()
# # Person().normal_function()  # 直接抛出异常，因为实例调用，会将Person()注入给后者，而后者不需要任何参数
# Person.method(1)  # 可以的，因为可以把1给self,增加__init__后，就会出错，因为1没有name属性


class Person:
    def __init__(self, name):
        self.name = name

    def method(self):
        print('method', self.name)

    @classmethod  # 类方法，此装饰器装饰的方法，第一参数不在是self了
    # 装饰器的作用是，你是类直接将类注入到方法中，你是实例，直接将实例的类注入到方法中
    def clsmtd(cls):
        print(cls)

    @staticmethod  # 静态方法，此装饰器装饰的方法，可以没有任何参数
    def stmtd():
        print('static')


Person.clsmtd(), Person('tom').clsmtd()

Person.stmtd(), Person('tom').stmtd()  # @staticmethod会阻止实例注入其装饰的方法中
print(Person.__dict__)
