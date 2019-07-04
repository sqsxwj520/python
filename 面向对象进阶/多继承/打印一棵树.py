# 打印一颗树
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


print_tree(list(range(15)))


def _print_tree(array: list, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length))

    index = 1
    for i in range(int(depth) - 1, -1, -1):
        pre = (2 ** i - 1)
        print(pre * ' ' * unit_width, end='')  # end必须是空字符串，因为前面空格打印完，紧接着就是打印数字
        step = 2 ** (depth - i - 1)
        values = array[index: index + step]
        interval = ' ' * (2 * pre + 1) * unit_width
        print(interval.join(map(lambda x: '{:{}}'.format(x, unit_width), values)))
        # 注意values也需要设置数值的宽度

        index += step
    return array


# _print_tree([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])  # 0不算，只是占位
_print_tree(list(range(20)))
