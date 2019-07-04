import math


def print_tree(array: list, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length + 1))
    index = 0
    width = 2 ** depth - 1
    for i in range(int(depth)):
        for j in range(2 ** i):
            print('{:^{}}'.format(array[index], width * unit_width), end=' ' * unit_width)
            index += 1
            if index >= length:
                break
        width //= 2
        print()
    return array


origin = [10, 90, 50, 70, 20, 40, 30, 60, 80]
size = len(origin)
print_tree(origin)


def heap_adjust(n, i, array: list):
    while 2 * i + 1 <= n:
        max_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        if right_child_index <= n and array[max_child_index] < array[right_child_index]:
            max_child_index = right_child_index
        if array[max_child_index] > array[i]:
            array[max_child_index], array[i] = array[i], array[max_child_index]
            i = max_child_index
        else:
            break
    return array


# h = heap_adjust(size, 0, origin)
# print(h)
# print_tree(h)


def heap(n, array: list):
    start = n // 2 - 1
    for i in range(start, -1, -1):
        heap_adjust(n, i, array)  # 就地修改的
        # print_tree(array)
    return array


heap(size, origin)
# print_tree(heap(size, origin))
# print(origin)


def sort(n, array: list):
    while n > 0:
        array[0], array[n - 1] = array[n - 1], array[0]
        n -= 1
        # print_tree(array)
        if n == 1 and array[1] > array[0]:  # 最后两个数不需要再调整了
            break
        heap_adjust(n - 1, 0, array)
        # print_tree(array)
    return array


sort(size, origin)
print_tree(origin)
print(origin)


# def big_endian(arr, start, end):
#     root = start
#     while end >= root * 2 + 1:
#         child = root * 2 + 1  # 左孩子
#         # if child > end:  # 孩子比最后一个节点还大 也就意味着最后一个叶子节点了 就得跳出去一次循环已经调整完毕
#         #     break
#         if child + 1 <= end and arr[child] < arr[child + 1]:  # 为了始终让其跟子元素的较大值比较 如果右边大就左换右，左边大的话就默认
#             child += 1
#         if arr[root] < arr[child]:  # 父节点小于子节点直接换位置 同时坐标也得换这样下次循环可以准确判断是否为最底层是不是调整完毕
#             arr[root], arr[child] = arr[child], arr[root]
#             root = child
#         else:  # 父子节点顺序正常 直接过
#             break
#
#
# def heap_sort(arr):
#     # 无序区大根堆排序
#     first = len(arr) // 2 - 1
#     for start in range(first, -1, -1):  # 从下到上，从右到左对每个节点进调整 循环得到非叶子节点
#         big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
#     for end in range(len(arr) - 1, 0, -1):
#         arr[0], arr[end] = arr[end], arr[0]  # 顶部尾部互换位置
#         big_endian(arr, 0, end - 1)  # 重新调整子节点的顺序  从顶开始调整
#     return arr
#
#
# def main():
#     l1 = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
#     print(heap_sort(l1))  # 原地排序
#
#
# if __name__ == "__main__":
#     main()
