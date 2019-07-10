# from os import path  # python3.4之前使用这种方式
from pathlib import Path  # python3.4建议使用这种方式

# p = path.join('/etc', 'sysconfig', 'network')
# print(type(p), p)  # p的类型是字符串
# print(path.exists(p))
#
# print(path.split(p))  # 类型是元组;分割的结果为路径和基名
# print(path.split('c:/test/a/b.txt'))  # ('c:/test/a', 'b.txt')，最后一部分为basename基名
# print(path.dirname('c:/test/a/b.tar.gz'))  # linux中对于路径中的冒号，会将其认为是合法的文件名称
# print(path.abspath('.'))  # 当前目录的绝对路径
# print(path.abspath(''))  # 同样是当前目录的绝对路径
# print(__file__)  # 当前路径下的当前文件
#
# p1 = '/a/b/c/d/e/f/g.tar.gz'  # 打印p1的所有父目录
#
# parent = path.dirname(p1)
# print(parent)
# while parent != path.dirname(parent):
#     parent = path.dirname(parent)
#     print(parent)

p2 = Path()  # 创建了一个路径对象
print(p2)  # 结果为点.，默认为当前路径
print(p2.absolute())

print(Path())  # 三种方式都是当前路径
# print(Path('.'))
# print(Path(''))

p3 = Path('/etc', 'sysconfig', 'network')
print(p3)

p4 = Path('a/b', 'c', 'd/e')
print(p4)

p5 = Path(p3, p4)
print(p5)

print(p5 / 'f' / 'g/h' / '123.zip')

# 总结：Path / str, str / Path, Path / Path 三种方式拼接结果都是路径对象

p1 = Path('/a/b/c/d/e/f/g.tar.gz')
# for x in p1.parents:  # 打印p1的所有父目录
#     print(x)  # 一定要注意，x的类型是路径对象，不是字符串
print(p1.name, p1.stem, p1.suffix)  # g.tar.gz g.tar .gz
print(p1.suffixes)  # ['.tar', '.gz']返回多个扩展名列表

print(p1.with_name('magedu.xz'))  # 替换目录最后一个部分，并返回一个新的路径\a\b\c\d\e\f\magedu.xz
print(p1.with_suffix('.png'))  # 有扩展名则替换，无则补充扩展名\a\b\c\d\e\f\g.tar.png

print(Path().cwd())  # 当前工作路径
print(Path.home())  # C:\Users\Administrator当前家目录，

print(p1.is_dir())
print(p1.is_file())  # False，因为文件根本就不存在
print(p1.is_socket())
print(p1.exists())  # 结果为False

p9 = p1.cwd() / 'test.txt'
print(p9.exists())
print(p9.is_dir())
print(p9.is_file())  # 结果为True
print(p9.is_socket())
