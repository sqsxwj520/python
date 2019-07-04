
class Node:
    __slots__ = ('item', 'pre', 'next')

    def __init__(self, item, pre=None, sub=None):
        self.item = item
        self.pre = pre
        self.next = sub

    def __repr__(self):
        return "{}<——{}——>{}".format(self.pre.item if self.pre else None,
                                     self.item,
                                     self.next.item if self.next else None)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            # self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            # self.tail = node
        self.tail = node
        self._size += 1
        return self

    def insert(self, index, value):
        # if index < 0:
        #     raise IndexError('Wrong index')
        # for i, node in enumerate(self.iter_nodes()):
        #     if i == index:
        #         current = node
        #         break
        # else:
        #     self.append(value)
        #     return
        if index >= len(self):  # 尾部追加
            self.append(value)
            return
        if index < -len(self):  # 索引超左边界，直接在头部插入
            index = 0
        current = self[index]
        new_node = Node(value)
        pre = current.pre
        if pre is None:
            self.head = new_node
        else:
            pre.next = new_node
            new_node.pre = pre
        new_node.next = current
        current.pre = new_node
        self._size += 1

    def pop(self):
        if self.tail is None:
            raise Exception('链表为空')
        node = self.tail
        value = node.item
        pre = node.pre
        if pre is None:
            self.head = None
            self.tail = None
        else:
            self.tail = pre
            pre.next = None
        self._size -= 1
        return value

    def remove(self, index):
        # if index < 0:
        #     raise IndexError('Wrong index')
        # if self.tail is None:
        #     raise Exception('空链表')
        # for i, node in enumerate(self.iter_nodes()):
        #     if i == index:
        #         current = node
        #         break
        # else:
        #     raise IndexError('Wrong index')
        current = self[index]
        pre = current.pre
        _next = current.next
        if pre is None and _next is None:
            self.head = None
            self.tail = None
        elif pre is None:
            self.head = _next
            _next.pre = None
        elif _next is None:
            self.tail = pre
            pre.next = None
        else:
            pre.next = _next
            _next.pre = pre
        self._size -= 1

    def iter_nodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next

    def __len__(self):
        return self._size

    def __add__(self, other):
        return self.append(other)

    # def __iter__(self):
    #     # yield from self.iter_nodes()
    #     return self.iter_nodes()

    __iter__ = iter_nodes

    def __reversed__(self):
        # yield from self.iter_nodes(True)
        return self.iter_nodes(True)

    def __getitem__(self, index):
        if index >= len(self) or index < -len(self):
            raise IndexError('Wrong index')
        reverse = True if index < 0 else False
        start = 1 if index < 0 else 0
        for i, node in enumerate(self.iter_nodes(reverse), start):
            if i == abs(index):
                return node

    def __setitem__(self, index, value):
        self[index].item = value

    def __contains__(self, item):
        current = self.head
        while current:
            if item == current.item:
                return True
            current = current.next
        else:
            return False


dll = DoubleLinkedList()
dll.append(1).append(3).append(5).append(7).append('abc') + 9
dll.insert(0, 'start')
dll.insert(100, 'end')
dll.insert(2, 200)
for x in dll:
    print(x)
print('~~~~~~~~~~~~~~~~~~~~~~~')
dll.remove(0)
dll.remove(6)
for y in dll:
    print(y)
print(dll.pop())
dll[0] = 'start'
print(dll[0])
print(dll[-1])
print(dll[-2])
print('abc' in dll)
