# import a  # 注意目录没有__file__属性
#
#
# print(dir(a))
# print(type(a))
# print(a)
# print(a.__path__)
# print(a.x)


# import m  # 注意只加载m，不会递归加载
# from m import m1
# import m.m1
# import m.m2.m21
# import m
# from m.m2 import m22  # 此时m2不在当前名词空间中
# import sys
#
#
# print(dir())  # 加载了m和m1，当前名词空间中只有m
# # print(m.m1)
#
# print(list(filter(lambda x: x.startswith('m'), sys.modules.keys())))
# print(m.abc)
# print(m.m2.y)
# print(m.m2.__dict__.keys())
# print(m.m2.m22)

#
# from a.b import c

# import m
# from m.m2 import m22
# print(dir())
# # print(m.m1)
# print(m22.m1)


# print(__name__)
#
# __all__ = ['X', '_Y']
#
# X = 5
# _Y = 20
# __Z = 300
#
# __my__ = 500
#
#
# def _a():
#     pass
#
#
# class __A:
#     pass
#
#
# print(dir())


class A:
    def show_me(self):
        print('I am A')


print(hash('abc'))
