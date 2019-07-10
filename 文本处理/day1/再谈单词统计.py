
filename = 'C:\\Users\\Administrator\\Desktop\\sample.txt'


def _make_key(s: str):
    # ret = []
    start = 0
    length = len(s)
    chars = set("""~!"'@#/\%$()[]{}+-*`., \r\n""")
    for i, c in enumerate(s):
        if c in chars:
            if start == i:
                start = i + 1
                continue  # 连续的直接跳过
            # ret.append(s[start: i])  # ab'cde'f便于理解; a((path))
            yield s[start: i]
            start = i + 1
    else:
        if start < length:
            # ret.append(s[start:])
            yield s[start:]
    # print(ret)
    # return ret


print(1, _make_key('((ab.))'))

d = {}
with open(filename, encoding='utf-8') as f:
    for line in f:
        # print(line)
        # words = line.split()
        # for word in map(lambda x: x.lower(), words):
        for word in map(str.lower, _make_key(line)):  # str.lower 等价于 lambda x: str.lower(x) 此时的str是类
            d[word] = d.get(word, 0) + 1
# print(d)
print(sorted(d.items(), key=lambda x: x[1], reverse=True))  # 相当于把二元组的第二个元素拿出来，进行排序

# print(list(filter(lambda key: key.lower().find('path') > -1, d.keys())))
