import re

s = """bottle\nbag\nbig\napple"""

for i, c in enumerate(s, 1):
    print((i - 1, c), end='\n' if i % 10 == 0 else ' ')

r = re.sub('b\w', 'magedu', s, 1)  # 1表示替换的次数
print(type(r), r)

r = re.sub('(b\w)', r'magedu--------\1', s)  # 1表示替换的次数
print(type(r), r)

t = """
os.path.abspath(path)
normpath(join(os.getcwd(), RE-path)).
"""
# print(t.split())
# print(re.split(r'[\s().,]+', t))

print(re.split(r'\W+', t))

print(re.split(r'[^a-zA-Z0-9-_]+', t))
