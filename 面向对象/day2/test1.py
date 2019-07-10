import math


# 居中打印
def print_tree(array: list, unit_width=2):  # 应对两位数的问题
    length = len(array)
    depth = math.ceil(math.log2(length + 1))
    index = 0
    width = 2 ** depth - 1  # 按照满二叉树来想，最后一行的宽度，可以保证不重叠
    for i in range(int(depth)):
        for j in range(2 ** i):  # 每行打印几个数字
            print('{:^{}}'.format(array[index], width * unit_width), end=' ' * unit_width)
            index += 1

            if index >= length:
                break
        width //= 2  # 每打印一层，宽度折半
        print()


print_tree(list(range(15)))


# 栅格打印
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


# _print_tree([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])  # 0不算在内
_print_tree(list(range(30)))
