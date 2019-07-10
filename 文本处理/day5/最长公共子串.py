s1 = "bccdfgh"
s2 = "abccdecdfg"


def get_string(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    record = [[0 for m in range(length2 + 1)] for q in range(length1 + 1)]  # 多一位，为了防止超界
    # print(record)
    max_string = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(length1):
        for j in range(length2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > max_string:
                    # 获取最大匹配长度
                    max_string = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - max_string:p], max_string


print(get_string(s1, s2))
