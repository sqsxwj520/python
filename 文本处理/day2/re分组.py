import re

s = """bottle\nbag\nbig\napple"""

for i, c in enumerate(s, 1):
    print((i - 1, c), end='\n' if i % 10 == 0 else ' ')

# match只能从头开始匹配
r = re.match('(b)(\w+)', s)  # match对象，出一个结果;默认模式
print(type(r), r)
print(r.groups())  # 结果为元组
print(r.group(1), r.group(2))
print(r.group())  # match的结果
print(r.group(0))

r = re.match('(?P<header>b)(?P<body>\w+)', s)  # 命名分组
print(type(r), r)
print(r.groups())  # 结果为元组
print(r.group(1), r.group(2))
print(r.group())  # match的结果
print(r.group(0))
print(r.groupdict()['header'])

sl = re.finditer('(?P<header>b)(?P<body>\w+)', s)  # 命名分组
print(type(r), r)
for r in sl:
    print(r.groups())  # 结果为元组
    print(r.group(1), r.group(2))
    print(r.group())  # match的结果
    print(r.group(0))
    print(r.groupdict()['header'])
    print('~' * 30)

pattern = r'(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)'
regex = re.compile(pattern)

r = regex.finditer(s)
print(r)
for x in r:
    print(x.groups())
    print(x.groupdict())  # 字典
