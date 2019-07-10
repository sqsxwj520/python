# origin = [30, 20, 80, 40, 50, 10, 60, 70, 90]
import math


# 居中打印
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
                return
        width //= 2
        print()


print_tree(list(range(15)))


# 栅格打印
def _print_tree(array: list, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length))  # 注意变化

    index = 0
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


# _print_tree([0, 10, 20, 30, 40, 50, 60])
_print_tree(list(range(1, 30)))
