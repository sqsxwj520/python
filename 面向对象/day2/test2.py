
# 堆排序
import math


def _print_tree(array: list, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length))
    index = 1  # 注意不是0

    for i in range(int(depth) - 1, -1, -1):
        pre = 2 ** i - 1
        print(' ' * pre * unit_width, end='')  # 前导空格,end为空字符串，因为前面打完空格，接着还要打印数字
        step = 2 ** (depth - i - 1)
        values = array[index: index + step]
        interval = ' ' * (2 * pre + 1) * unit_width

        print(interval.join(map(lambda x: '{:^{}}'.format(x, unit_width), values)))
        index += step


origin = [0, 40, 90, 80, 50, 30, 20, 60, 10]
size = len(origin) - 1
print(origin)
_print_tree(origin)
print('~' * 30)


def heap_adjust(n, i, array: list):
    # i = n // 2
    while n >= 2 * i:  # 有左孩子节点
        max_child_index = 2 * i  # 假设左孩子节点的值最大
        right_child_index = max_child_index + 1
        if right_child_index <= n and array[right_child_index] > array[max_child_index]:
            # 右孩子节点存在，并且其值大于左孩子节点的值
            max_child_index = right_child_index

        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index  # 注意索引要变
        else:  # 如果没有交换
            return

    return array


# h = heap_adjust(size, 1, origin)  # 分析一个节点，如果代码正确，则扩展
# print(h)
# _print_tree(h)


def heap(n, array: list):  # 构建大顶堆
    start = n // 2
    for i in range(start, 0, -1):
        heap_adjust(n, i, array)
        # _print_tree(array)

    return array


heap(size, origin)
# print(origin)
# print('~' * 30)


def sort(n, array: list):
    while n > 1:
        # _print_tree(array)
        array[n], array[1] = array[1], array[n]  # n为最后一个值
        # _print_tree(array)
        n -= 1
        heap_adjust(n, 1, array)
        # _print_tree(array)
        # print('+' * 40)
    return array


sort(size, origin)
print(origin)
