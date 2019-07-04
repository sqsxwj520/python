class SingleNode:
    def __init__(self, data, pre=None, _next=None):
        self.data = data
        self.pre = pre
        self.next = _next

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
            self.tail.next = node
            node.pre = self.tail
        self.tail = node
        return self

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Wrong index")
        if self.tail is None:
            raise Exception('链表为空')
        # current = None
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                current = node
                break
        else:  # 没有break，说明index大于链表的长度，尾部追加
            self.append(data)
            return  # 没有此句的话,41行会报AttributeError: 'NoneType' object has no attribute 'pre'，因为current为None
            # 有了此句current = None就可以没有了

        node = SingleNode(data)
        pre_node = current.pre
        if pre_node is None:  # 说明当前为链表的头部
            self.head = node
        else:
            pre_node.next = node
            node.pre = pre_node
        node.next = current
        current.pre = node

    def pop(self):  # 尾部删除
        if self.tail is None:
            raise Exception('链表为空')
        node = self.tail
        data = node.data
        pre_node = node.pre
        if pre_node is None:  # 只有一个节点
            self.head = None
            self.tail = None
        else:
            self.tail = pre_node
            pre_node.next = None
        return data

    def remove(self, index):
        if index < 0:
            raise IndexError('Wrong index')
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                current = node
                break
        else:  # 索引超界了
            raise IndexError('Wrong index')

        pre_node = current.pre
        next_node = current.next

        if pre_node is None and next_node is None:
            self.head = None
            self.tail = None
        elif pre_node is None:
            self.head = next_node
            next_node.pre = None
        elif next_node is None:
            self.tail = pre_node
            pre_node.next = None
        else:
            pre_node.next = next_node
            next_node.pre = pre_node

    def iter_nodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next


dll = DoubleLinkedList()
dll.append(1).append(3).append(5).append(7).append(9)
dll.insert(0, 100)
dll.insert(10, 300)
dll.insert(2, 200)
for x in dll.iter_nodes():
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~~")
print(dll.pop())
print(dll.pop())
for y in dll.iter_nodes():
    print(y)
print('~~~~~~~~~~~~~~~~~')
# t = (dll.remove(0), dll.remove(1), dll.remove(3))
# dll.remove(0)
# dll.remove(1)

for z in dll.iter_nodes():
    print(z)
