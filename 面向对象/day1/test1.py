

def prefix(str1):
    m = len(str1)
    pi = [0 for _ in range(m)]
    pi[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and str1[k] != str1[q]:
            k = pi[k - 1]
            if str1[k] == str1[q]:
                k = k + 1
                pi[q] = k
    return pi


def match(t, p):
    n = len(t)
    m = len(p)
    pi = prefix(p)
    q = 0
    for i in range(0, n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
            if p[q] == t[i]:
                q = q + 1
            if q == m:
                print("matched in %d.\n" % (i - m + 1))
    print("not matched!\n")
