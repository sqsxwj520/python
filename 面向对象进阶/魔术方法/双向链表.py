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

    def append(self, data):
        node = SingleNode(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.sub = node  # 当前节点
            node.pre = self.tail  # 上一个节点
        self.tail = node
        return self

    def insert(self, index, data):
        if index < 0:
            raise IndexError('Wrong index')
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                current = node
                break
        else:  # 没有break，说明没找到，索引超界了，尾部追加
            self.append(data)
            return

        node = SingleNode(data)
        pre_node = current.pre
        if pre_node is None:  # 当前节点为头部
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
        if index < 0:
            raise IndexError('Wrong index')
        if self.tail is None:
            raise Exception('链表为空')

        for i, node in enumerate(self.iter_nodes()):
            if i == index:  # 找到了
                current = node
                break
        else:  # 没有break，说明没找到,索引超界了
            raise IndexError('Wrong index')

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

    def iter_nodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.sub


dll = DoubleLinkedList()
dll.append(1)
dll.append(3).append(5).append(7).append(9)
for x in dll.iter_nodes():
    print(x)
print('~~~~~~~~~~~~~~~~~~~')
dll.insert(0, 100)
dll.insert(3, 200)
dll.insert(1000, 300)
for y in dll.iter_nodes():
    print(y)
print(dll.pop())
print('~~~~~~~~~~~~~~~~~')
dll.remove(0)
# dll.remove(3)
# dll.remove(7)
for z in dll.iter_nodes():
    print(z)
