# pthon实现单链表
class Node:
    def __init__(self, item, _next=None):
        self.item = item
        self.next = _next

    def __repr__(self):
        return repr(self.item)


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.head is None:  # 链表为空
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return self

    def __add__(self, item):
        return self.append(item)

    def iter_nodes(self):
        current = self.head
        while current:
            yield current
            current = current.next


sll = SingleLinkedList()
sll.append(1).append(3).append(5) + 7
for x in sll.iter_nodes():
    print(x)
   
 # 单链表容器化
 class SingleNode:

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __repr__(self):
        return repr(self.data)


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def __len__(self):
        return len(self.items)

    def __call__(self, index):
        return self[index]

    def add(self, data):
        node = SingleNode(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node  # 当前节点
        self.tail = node
        self.items.append(self.tail)
        return self

    def __add__(self, other):
        self.add(other)
        return self

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        yield from self.items

    def __repr__(self):
        return repr(self.items)


sll = SingleLinkedList()
sll.add(1)
sll.add(3)
sll.add(5).add('abc')
sll.add(7) + 9
print(len(sll))
for i in range(len(sll)):
    print(sll(i))
print(sll.head, sll.tail)
for x in sll:
    print(x)
sll[0] = 1000
print(sll[0])
