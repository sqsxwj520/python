"""求两个字符串的最长公共子串"""
s1 = "abcdefcdfgh"
s2 = "abcdfcdgh"


def _find_it(str1, str2):
    count = 0

    if len(str1) > len(str2):
        str1, str2 = str2, str1  # str1最短

    length = len(str1)
    for step in range(length, 0, -1):  # step为假定公共子串长度
        for start in range(length - step + 1):

            sub = str1[start: start + step]
            count += 1

            i = str2.find(sub)
            if i >= 0:
                print('count={}, step={}'.format(count, step))
                return sub
    return ''  # 没有公共子串


print(_find_it(s1, s2))


def find_it_(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    matrix = [[0] * len1 for _ in range(len2)]
    _max = 0
    index = 0

    for i, x in enumerate(str2):
        for j, y in enumerate(str1):
            if x == y:
                if i == 0 or j == 0:
                    matrix[i][j] = 1  # 考虑到边界的问题
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > _max:
                    _max = matrix[i][j]
                    index = j
    # print(_max, index)
    # print(str1[index - _max + 1: index + 1])
    return str1[index - _max + 1: index + 1]


print(find_it_('xyabcdabcd', 'abcd'))
