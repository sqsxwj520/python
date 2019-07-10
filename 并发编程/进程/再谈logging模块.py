import logging
# from logging import Logger
import sys


FORMAT = "%(asctime)s [%(name)s] %(thread)8d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y/%m/%d %H:%M:%S",
                    filename='c:/root.log')
# 定制级别,控制输出，datefmt格式化时间字符串的,注意设置的是root


root = logging.getLogger()

# h = logging.FileHandler('c:/root.log')
# root.addHandler(h)
# print(root.handlers)

"""
h = logging.FileHandler('c:/root2.log')
root.addHandler(h)
print(root.handlers)
"""
root.addHandler(logging.StreamHandler(sys.stdout))  # 默认只有message
# # logging.info('test info')  # 在对应的文件里，默认只有message信息
# log1 = logging.getLogger('hello')
# print('in log1', log1.handlers)
# # 注意log1的handlers为空，之所以能输出，是因为从root那里传播过来的
# log1.info('test info in log1')
print(root.handlers)
root.handlers[1].level = 30
print(root.handlers)

logging.info('test info')
# 能否输出，首先要跟当前logger对象的有效水平进行比较，过了之后再跟当前logger的handlers设置的有效级别进行比较
