
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
