import re

s = """bottle\nbag\nbig\napple"""

for i, c in enumerate(s, 1):
    print((i - 1, c), end='\n' if i % 10 == 0 else ' ')

# match只能从头开始匹配
r = re.match('b', s)  # match对象，出一个结果;默认模式
print(type(r), r, 1)
r = re.match('a', s)  # match对象，没有结果
print(type(r), r)

r = re.match('^b', s)  # match对象，出一个结果
print(type(r), r, 3)

r = re.match('^a', s, re.M)  # match对象，没有结果; 仍然从头开始找，多行模式并没有用
print(4, type(r), r)

regex = re.compile('^a', re.M)
r = regex.match(s)
print(r)  # 结果为None

r = regex.match(s, 8)
print(r)  # 结果为None

regex = re.compile('a', re.M)
r = regex.match(s, 8)
print(r)

regex = re.compile('a', re.M)
r = regex.match(s, 15)
print(r)

regex = re.compile('^a', re.M)  # 先编译后，match可以指定从某个位置开始匹配
r = regex.match(s, 15)
print(r)

r = re.search('b', s)
print(type(r), r)

r = re.search('a', s)
print(type(r), r)

r = re.fullmatch('.+', s)  # 将整个字符串全部匹配，结果为None
print(type(r), r)

r = re.fullmatch('.+', s, re.S)
print(type(r), r)

regex = re.compile('.+', re.M)  # 先编译后，match可以指定从某个位置开始匹配
r = regex.fullmatch(s)  # None
print(r, 20)

regex = re.compile('.+', re.M)  # 先编译后，match可以指定从某个位置开始匹配
r = regex.fullmatch(s, 15)  # apple
print(r)

regex = re.compile('.+', re.M)  # 先编译后，match可以指定从某个位置开始匹配
r = regex.fullmatch(s, 15, 19)  # 结果appl,注意不包括19对应的字符
print(r)
