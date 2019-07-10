import logging
# from logging import Logger
import sys


FORMAT = "[%(name)s] %(thread)8d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y/%m/%d %H:%M:%S", stream=sys.stdout)  # 定制级别,控制输出
# datefmt格式化时间字符串的,注意设置的是root

# logging.debug('test')  # 括号里的是message
# logging.info('I am {} {}'.format(20, 'years old.'))
# logging.warning('I am %d %s', 20, 'years old.')
# l1 = Logger('l1')
# l2 = Logger('l2')
# print(l1 == l2)
# print(l1 is l2)
#
# root = logging.getLogger()
# l3 = logging.getLogger()
# l4 = logging.getLogger()
# print(l3 is l4)  # True
# print(type(l3))
# print(l3 is root)  # True
# print(l4 is Logger.root)  # True
#
#
# l5 = logging.getLogger('l1')
# l6 = logging.getLogger('l1')
# print(l5 is l6)
# print(l5 is l1)  # False
# print()
# root = logging.getLogger()
# print(root.name, type(root), root.parent)  # root没有父
# c = logging.getLogger(__name__)
# print(c.name, type(c), c.parent is root)  # __main__ <class 'logging.Logger'> True
#
# c1 = logging.getLogger(__name__ + '.child')
#
# print(c1.name, type(c1), c1.parent is c)
# # __main__.child <class 'logging.Logger'> True

# root = logging.getLogger()
# root.level = 30  # level可以动态的改变
# root.warning('test info')
# root = logging.getLogger()
# print(root.handlers)  # [<StreamHandler <stderr> (NOTSET)>]
#
# h = logging.FileHandler('c:/测试/test.log')
# root.addHandler(h)
# print(root.handlers)
#
# h = logging.FileHandler('c:/测试/test2.log')
# root.addHandler(h)
# print(root.handlers)
#
# logging.info('test info')  # 思考此语句为什么没有在控制台输出？

# root = logging.getLogger()
# print(root.handlers)
# root.addHandler(logging.StreamHandler(sys.stdout))
# # root.handlers = []
#
# log1 = logging.getLogger('hello')
# print('in log1', log1.handlers)
# log1.info('test info in log1')

log3 = logging.getLogger('log1')
log3.propagate = False

# 2019/06/12 09:49:40 log1     7368 log1 test info string
# logging.getLogger().info('root test info')
# # 2019/06/12 09:49:40 root     7368 root test info
h = logging.StreamHandler(sys.stdout)
log3.addHandler(h)

f = logging.Formatter('log3 fmt:[%(name)s] %(message)s')
h.setFormatter(f)
# print(log3.handlers[0].formatter._fmt)
# h.setLevel(logging.WARNING)

# log3.info('log3 test info string')
_filter = logging.Filter('log3')
print(_filter, _filter.name, _filter.nlen)  # filter.nlen为name的长度
h.addFilter(_filter)

log4 = logging.getLogger('log3.log4')
log4.info('log4 test info string')

# log5 = logging.getLogger('log5')
# log5.info('log5 test info')
