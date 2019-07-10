import math


def _print_tree(array: list, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length))  # 注意变化

    index = 1
    # width = 2 ** depth - 1
    for i in range(int(depth) - 1, -1, -1):
        pre = 2 ** i - 1
        print(' ' * pre * unit_width, end='')
        step = 2 ** (depth - i - 1)

        values = array[index: index + step]
        interval = ' ' * (2 * pre + 1) * unit_width
        print(interval.join(map(lambda x: "{:{}}".format(x, unit_width), values)))
        index += step
        # print(values)


origin = [0, 30, 50, 80, 70, 20, 40, 10, 90, 60]
size = len(origin) - 1

_print_tree(origin)


def heap_adjust(n, i, array: list):
    # i = n // 2  # 左孩子一定存在，右孩子存在与否不知道

    while n > 2 * i:
        max_child_index = 2 * i
        right_child_index = max_child_index + 1

        if right_child_index <= n and array[right_child_index] > array[max_child_index]:
            max_child_index = right_child_index

        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:  # 没有交换，没有else子句的话，会死循环
            break  # 不能写成return,否则第五行代码的len(array)会报错，'Nonetype'没有len属性

    return array

#
# h = heap_adjust(size, 1, origin)
# _print_tree(h)


def heap(n, array: list):
    start = n // 2  # 从最后一个有子节点的根节点开始调整
    for i in range(start, 0, -1):  # 注意取不到0
        heap_adjust(n, i, array)
        # _print_tree(array)  # 打印调整的过程
    return array


heap(size, origin)
# print(origin)


def sort(n, array: list):
    while n > 1:  # 最后一个元素不需要再调整了
        # _print_tree(array)
        array[n], array[1] = array[1], array[n]
        # _print_tree(array)

        n -= 1
        # if n == 2 and array[2] > array[1]:  # 待排序的数只剩两个的时候，判断后就不需要再调整了
        #     break
        heap_adjust(n, 1, array)
        # _print_tree(array)
        # print()
    return array


sort(size, origin)
_print_tree(origin)
