class SingleNode:
    def __init__(self, data, pre=None, sub=None):
        self.data = data
        self.pre = pre
        self.sub = sub

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def __len__(self):
        return len(self.items)

    def add(self, data):
        node = SingleNode(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.sub = node
            node.pre = self.tail
        self.tail = node
        self.items.append(self.tail)
        return self

    def __add__(self, other):
        self.add(other)
        return self

    def __call__(self, index):
        return self[index]

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def insert(self, index, data):
        if index < 0:
            raise IndexError('Wrong index')
        for i, node in enumerate(self):
            if i == index:
                current = node
                break
        else:  # 没有break，说明没找到，索引超界了，尾部追加
            self.add(data)
            return

        node = SingleNode(data)
        pre_node = current.pre
        # sub_node = current
        if pre_node is None:  # 头部
            self.head = node
        else:
            pre_node.sub = node
            node.pre = pre_node
        node.sub = current
        current.pre = node

    def pop(self):
        if self.tail is None:
            raise Exception('链表为空')

        node = self.tail
        data = node
        pre_node = node.pre

        if pre_node is None:  # 只有一个节点
            self.head = None
            self.tail = None
        else:  # 删除最后一个节点
            pre_node.sub = None
            self.tail = pre_node
        return data

    def remove(self, index):
        if self.tail is None:
            raise Exception('链表为空')
        if index < 0:
            raise IndexError('Wrong index')

        for i, node in enumerate(self):
            if i == index:  # 找到了
                current = node
                break
        else:  # 没有break，说明没找到
            raise IndexError('找不到')

        pre_node = current.pre
        sub_node = current.sub

        if pre_node is None and sub_node is None:  # 只有一个节点
            self.head = None
            self.tail = None

        elif pre_node is None:  # 要删除的节点在头部
            self.head = sub_node
            sub_node.pre = None

        elif sub_node is None:  # 要删除的节点在尾部
            self.tail = pre_node
            pre_node.sub = None

        else:
            pre_node.sub = sub_node
            sub_node.pre = pre_node

    def __iter__(self):
        yield from self.items


dll = DoubleLinkedList()
dll.add(1)
dll.add(3).add(5).add(7).add(9) + 11
for x in dll:
    print(x)
print('~~~~~~~~~~~~~~~~~~~')
dll.insert(0, 100)
dll.insert(3, 200)
dll.insert(1000, 300)
for y in dll:
    print(y)
print(dll.pop())
print('~~~~~~~~~~~~~~~~~')
dll.remove(0)
# dll.remove(3)
# dll.remove(7)
for z in dll:
    print(z)
print('~~~~~~~~~~~~~~~~')
dll[0] = 1000
print(dll[0])
