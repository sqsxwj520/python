"""单词统计进阶
在上一题基础之上，要求用户可以排除一些单词的统计，例如a、the、an等不应该出现的在具有实际意义
的统计之中，应当忽略。要求全部代码使用函数封装，并调用完成。

"""
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


stopwords = {'the', 'a', 'an'}  # 停用词


def wordcount(filename, encoding='utf-8'):
    d = {}
    with open(filename, encoding=encoding) as f:
        for line in f:
            # print(line)
            # words = line.split()
            # for word in map(lambda x: x.lower(), words):
            # for word in map(str.lower, _make_key(line)):  # str.lower 等价于 lambda x: str.lower(x) 此时的str是类
            #     if word not in stopwords:
            for word in filter(lambda x: x.lower() not in stopwords, _make_key(line)):
                    d[word] = d.get(word, 0) + 1
    # print(d)
    return d


def top(filename, n=10, encoding='utf-8'):
    # return sorted(wordcount(filename, encoding=encoding).items(), key=lambda x: x[1], reverse=True)[:n]
    # 相当于把二元组的第二个元素拿出来，进行排序
    yield from sorted(wordcount(filename, encoding=encoding).items(), key=lambda x: x[1], reverse=True)[:n]


print(*top('C:\\Users\\Administrator\\Desktop\\sample.txt'), sep='\n')
