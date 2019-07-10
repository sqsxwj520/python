
"""私有方法的本质：双下划线的方法，是私有方法，解释器会改名，改名策略和私有变量相同，_类名__方法名
方法变量都在类的__dict__中可以找到
"""

# 补丁：可以通过修改或替换类的成员，使用调用的方式没有改变，但是类提供的功能可能已经改变了

#
# class Person:
#     def get_score(self):
#         return {'English': 59, 'Math': 57, 'Chinese': 68}


# 一般好的设计是，把实例的某些属性保护起来，不让外部直接访问，外部使用getter读取属性和setter设置属性


class Person:

    def __init__(self):
        self.name = 'tom'
        self.__age = 20

    age = property(lambda self: self.__age)  # property是类, 该方法是getter


t = Person()
print(t.age)
# t.age = 300  # 此方法没有setter，只有getter
