from . import d  # 有相对导入的模块不能作为主模块了
from .. import e

# d = 1000
print(d.__file__)
print(e.__file__)
