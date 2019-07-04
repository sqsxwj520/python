import bisect


def insert_sort(order_list, v):
    ret = order_list[:]
    low = 0
    high = len(ret)  # 注意len(ret) - 1结果就错了，主要是插入的元素比有序的所有元素都大，会出错
    while low < high:
        mid = (low + high) // 2
        if v > ret[mid]:
            low = mid + 1
        else:
            high = mid
        # print(low, mid, high)
    ret.insert(low, v)
    return ret


for i in (8, 18, 6, 2):
    print(insert_sort(list(range(10)), i))


lst = [0, 20, 40, 40, 70, 88, 88, 90]
for i in (0, 40, 198):
    # print(bisect.bisect(lst, i))
    # print(bisect.bisect_right(lst, i))
    # print(bisect.bisect_left(lst, i))
    print(bisect.insort(lst, i))  # 返回值为None


lst2 = [60, 70, 80, 90]
s1 = 'EDCBA'
for score in (60, 80, 75, 55, 95, 65):
    print(bisect.bisect(lst2, score))
    print(score, s1[bisect.bisect(lst2, score)])
