import re

s = """bottle\nbag\nbig\napple"""

regex = re.compile('b\wg')
result = regex.sub('sun', s)
print(1, result)

result = regex.sub('quan', s, 1)
print(2, result)

regex = re.compile('\s+')
result = regex.subn('\t', s)
print(3, result)  # 结果为被替换后的新字符串及替换次数的元祖

t = """
os.path.abspath(path)
normpath(join(os.getcwd(), RE-path)).
"""
print(t.split())
print(re.split('[.()\s,]+', t))
print(re.split(r'\W+', t))
print(re.split('[^a-zA-Z0-9-_]+', t))

regex = re.compile('(b\w+)')
r = regex.match(s)
print(4, r.groups())  # 结果为元组

r = regex.search(s, 1)  # 从指定位置向后匹配一次
print(5, r.groups())

regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
r = regex.match(s)
print(6, r)
print(7, r.group(1), r.group(2), r.group(3))
print(8, r.group(0).encode())  # 返回整个匹配字符串，即match
print(9, r.group('name2'), r.group('name3'))
print(10, r.groups())  # 返回一个元组
print(11, r.groupdict())  # 返回字典(命名分组)

r = regex.findall(s)
for x in r:
    print(type(x), x)  # x为元组
    print('~' * 30)

regex = re.compile('(?P<head>b\w+)')
r = regex.finditer(s)
for x in r:
    print(type(x), x, x.group(), x.group('head'))  # x为match对象

s = '^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*_).{10,15}$'
