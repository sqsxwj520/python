# # import os.path  # 注意os模块和path模块都加载了，但是dir()中只能拿到os
# import os  # import后只能写模块名
# import os.path
# import os.path as osp  # 取别名,注意是os.path的别名，不是os的别名
#
# print(dir())
# # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# # '__package__', '__spec__', 'os']
# # print(sorted(locals().keys()))
# # print(sorted(globals().keys()))
#
# print(os)
# print(os.path)
# print(osp)
# print(os.path.exists('c:/tt'))  # 虽然没有导入path模块但是解释器替你做了，所以此语句可以执行
# print(osp.exists('c:/text.txt'))
#
#

#
# def a():
#     import pathlib
#     print(dir())  # ['pathlib'] 受作用域的影响
#
#
# a()
# print('~~~~~~~~~~')
# print(dir())
# # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# # '__package__', '__spec__', 'a']
#
# from os import stat  # from后必须是模块,可以逗号分隔
# from os.path import exists
# from pathlib import Path
# from pathlib import *
# from functools import _make_key
# # from os import path as osp
# from functools import wraps as wr, update_wrapper
#
# # from module import * | module | class | function | ...
# print(dir())
#
# from os.path import exists  # 注意from后的模块并不导入，只是加载
# import os.path
#
# print(exists)
#
# print(os.path.exists)
# print(os.path.__dict__['exists'])
# print(getattr(os.path, 'exists'))
# # <function exists at 0x0000000001DE31E0>
#
# from pathlib import Path
# import pathlib as pl
#
# print(id(Path), Path)
# # 42604072 <class 'pathlib.Path'>
# print(id(pl.Path), pl.Path)
# # 42604072 <class 'pathlib.Path'>
# p1 = Path()
# p2 = pl.Path()  # 注意p1和p2肯定不一样
# print(Path is pl.Path)  # True
# import pathlib
# import sys
#
#
# print(*sys.path, sep='\n')
# print(pathlib.Path.__doc__)
# print(sys.path)

# import sys
# import os.path
#
#
# print(sys.modules)

import test


if __name__ == '__main__':
    print('in __main__')
else:
    print('in import module')
