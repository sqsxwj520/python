"""单词统计
有一个文件，对其进行单词统计，不 区分大小写，并显示单词重复最多的10个单词
"""
from collections import defaultdict
filename = 'C:\\Users\\Administrator\\Desktop\\sample.txt'


def make_key(s: str):
    ret = []
    chars = set(r"""~!@#/\()[]{}+-*`.,'" """)
    for c in s:
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    # print(ret)
    return ''.join(ret).split()


# d = {}
d = defaultdict(lambda: 0)  # 恒定返回0;缺省字典需要从模块collections中导入
with open(filename, encoding='utf-8') as f:
    for line in f:
        # print(line)
        # words = line.split()
        # for word in map(lambda x: x.lower(), words):
        for word in make_key(line):
            # d[word] = d.get(word, 0) + 1
            d[word] += 1
# print(d)
print(sorted(d.items(), key=lambda x: x[1], reverse=True))  # 相当于把二元组的第二个元素拿出来，进行排序

# print(list(filter(lambda key: key.lower().find('path') > -1, d.keys())))
