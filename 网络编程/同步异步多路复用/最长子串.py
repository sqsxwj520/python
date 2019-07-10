
"""
给定一个字符串，找出不含有重复字符的最长子串的长度
"""
s = "abbbac"


def longest_substring(src):
    d = {}
    start = 0
    ans = 0

    for i, c in enumerate(src):
        if c in d:
            start = max(start, d[c] + 1)
        d[c] = i
        ans = max(ans, i - start + 1)
    return ans


print(longest_substring(s))
