# 10进制数转二进制、八进制数的函数
def _bin(x, m=2):

    l1 = []
    while x > m:
        x, y = divmod(x, m)

        l1.append(y)
    l1.append(x)
    for i in l1[::-1]:
        print(i, sep='', end='')


_bin(115, m=16)


def f(n, m=2):  # m为占位符，n大于9小于100是，占位符改为3即可

    half = n // 2
    if n & 1:
        [print('{:{}}'.format(n, m) * n if i == half else \
	           '{}{:{}}'.format(' ' * m * (n // 2), n, m)) for i in range(n)]
    else:
        [print('{:{}}'.format(n, m) * n if j == half or j == half -1 else \
               '{}{:{}}{:{}}'.format(' ' * m * (n//2 - 1), n, m, n, m)) for j in range(n)]


f(100, m=4)
