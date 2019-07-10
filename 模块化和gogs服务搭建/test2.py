# import test
#
# from test import A, _B, __C, __my__
from test import *  # 最前面带下划线的是无法导入的
# from pathlib import *
import test


print(dir())
print(test._Y)
