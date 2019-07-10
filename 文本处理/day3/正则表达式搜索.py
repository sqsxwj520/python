import re

s = """bottle\nbag\nbig\napple"""

for i, c in enumerate(s, 1):
    print((i - 1, c), end='\n' if i % 10 == 0 else ' ')

r = re.match('b', s)
print(1, type(r), r)

r = re.match('a', s)
print(2, r)

r = re.match('^a', s, re.M)  # 仍然从头开始找，多行模式并没有用
print(3, r)

r = re.match('^a', s, re.S)
print(4, r)

# 先编译，然后使用正则表达式对象
regex = re.compile('a')
r = regex.match(s)
print(5, r)

r = regex.match(s, 15)  # 编译后，可以设置match查找的起始位置
print(6, r)

r = re.search('a', s)  # 扫描找到匹配的第一个位置
print(7, r)

regex = re.compile('b')
r = regex.search(s, 1)
print(8, r)

regex = re.compile('^b', re.M)  # 不管是否是多行模式，找到一个就返回
r = regex.search(s)
print(9, r)

r = regex.search(s, 7)
print(10, r)
# 10 <_sre.SRE_Match object; span=(7, 8), match='b'> span是前包后不包，match是匹配的结果

r = re.fullmatch('bag', s)
print(11, r)

regex = re.compile('bag')
r = regex.fullmatch(s)
print(12, r)

r = regex.fullmatch(s, 7)
print(13, r)

r = regex.fullmatch(s, 7, 10)  # 要完全匹配，多了少了都不行，[7, 10)对应'bag'
print(14, r)

r = re.findall('b', s)
print(15, r)

regex = re.compile('^b\w')  # 默认模式下，不论有多少换行符，都视为一行
r = regex.findall(s)
print(16, r)

regex = re.compile('^b\w', re.M)
r = regex.findall(s)
print(17, r)

r = regex.findall(s, 7)
print(18, r)

r = regex.findall(s, 7, 10)
print(19, r)

regex = re.compile('^b\w', re.S)
r = regex.findall(s)
print(20, r)

regex = re.compile('^b', re.M)
res = regex.finditer(s)
print(type(res))
r = next(res)
print(type(r), r)
print(r.start(), r.end(), s[r.start(): r.end()])
print(type(res))
r = next(res)
print(type(r), r)
print(r.start(), r.end(), s[r.start(): r.end()])
