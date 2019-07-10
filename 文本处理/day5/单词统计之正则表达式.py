import re

with open('C:\\Users\\Administrator\\Desktop\\sample.txt', encoding='utf-8') as f:
    s = f.read()
r = re.split(r'\W+', s)
# print(r)
d = dict()
for k in r:
    d[k] = d.get(k, 0) + 1
print(sorted(d.items(), key=lambda item: item[1], reverse=True)[:10])
