
def heap_adjust(array: list, i, n):
    while 2 * i + 1 <= n:
        left_child_index = 2 * i + 1
        if left_child_index + 1 <= n and array[left_child_index] < array[left_child_index + 1]:
            left_child_index += 1
        if array[left_child_index] > array[i]:
            array[left_child_index], array[i] = array[i], array[left_child_index]
            i = left_child_index
        else:
            break
    return array


def heap_sort(array, n):
    start = n // 2 - 1
    for i in range(start, -1, -1):
        heap_adjust(array, i, n)
    while n > 0:
        array[0], array[n - 1] = array[n - 1], array[0]
        n -= 1
        heap_adjust(array, 0, n - 1)
    return array


origin = [80, 90, 20, 10, 40, 30, 60, 50, 70]
length = len(origin)

print(heap_sort(origin, length))
