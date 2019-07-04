class Node:
    def __init__(self, item, pre=None, _next=None):
        self.item = item
        self.pre = pre
        self.next = _next  # 节点对象

    def __repr__(self):
        return "{}<—{}—>{}".format(self.pre.item if self.pre else None,
                                   self.item,
                                   self.next.item if self.next else None)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.pre = self.tail
        self.tail = node
        return self

    def insert(self, index, value):
        if index < 0:
            raise IndexError('Wrong index')
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                current = node
                break
        else:  # 只要没有break，一定执行else语句
            self.append(value)  # 没找到，尾部追加，注意执行此语句时，插入已经结束，所以要return,也可以return self(链式编程）
            return
        new_node = Node(value)
        pre_node = current.pre
        if pre_node is None:  # 当前节点在头部，即在开头插入 index == 0 i == 0
            self.head = new_node
        else:
            pre_node.next = new_node
            new_node.pre = pre_node
        new_node.next = current
        current.pre = new_node

    def pop(self):
        if self.tail is None:
            raise Exception('链表为空')
        node = self.tail
        value = node.item
        pre_node = node.pre
        if pre_node is None:  # 只有一个元素 self.head.next is None
            self.head = None
            self.tail = None
        else:
            pre_node.next = None
            self.tail = pre_node
        return value  # 只是弹出值(你插入的一个值，我就弹出一个值）

    def remove(self, index):
        if index < 0:
            raise IndexError('Wrong index')
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                current = node
                break
        else:
            raise IndexError('Wrong index')
        pre_node = current.pre
        next_node = current.next

        if pre_node is None and next_node is None:  # 只有一个节点 self.head == self.tail(类没有定义__eq__方法)相当于is
            self.head = None
            self.tail = None
        elif pre_node is None:  # 从头部删除
            self.head = next_node
            next_node.pre = None
        elif next_node is None:  # 从尾部删除
            self.tail = pre_node
            pre_node.next = None
        else:
            pre_node.next = next_node
            next_node.pre = pre_node

        del current  # current引用计数减1

    def iter_nodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next


dll = DoubleLinkedList()
dll.append(1).append(3).append(5)
for x in dll.iter_nodes():
    print(x)
print('~~~~~~~~~~~~~')
dll.insert(0, 100)
dll.insert(10, 1000)
dll.insert(3, 300)
for y in dll.iter_nodes():
    print(y)
print(dll.pop())
print(dll.pop())
print('~~~~~~~~~~~~')
dll.remove(0)
dll.remove(1)
for z in dll.iter_nodes():
    print(z)
