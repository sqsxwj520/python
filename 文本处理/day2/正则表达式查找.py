import re

s = """bottle\nbag\nbig\napple"""

r = re.findall('b', s)  # 结果为列表，内容为字符串
print(1, type(r), r)

r = re.findall('b\w', s)
print(2, type(r), r)

for x in r:
    print(type(x), x)

r = re.finditer('b\w', s)  # 结果为迭代器
print(3, type(r), r)  # 类型为match对象

for x in r:
    print(type(x), x, x.start(), x.end(), s[x.start(): x.end()])

r = re.finditer('^b\w', s)  # 结果为迭代器
print(4, type(r), r)  # 类型为match对象

for x in r:
    print(type(x), x, x.start(), x.end(), s[x.start(): x.end()])

r = re.finditer('^b\w', s, re.S | re.M)  # 结果为迭代器
print(5, type(r), r)  # 类型为match对象

for x in r:
    print(type(x), x, x.start(), x.end(), s[x.start(): x.end()])
