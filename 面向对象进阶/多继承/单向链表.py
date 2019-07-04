class SingleNode:
    def __init__(self, content, _next=None):
        self.content = content
        self.next = _next

    def __repr__(self):

        return '<SingleNode {}>'.format(self.content)


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, content):
        node = SingleNode(content)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return self

    def iter_nodes(self):
        current = self.head
        while current:
            yield current
            current = current.next


l1 = SingleLinkedList()
l1.add(5)
l1.add(4)
l1.add('abc')
print(l1.head, l1.tail)
print(type(l1.head))

for item in l1.iter_nodes():
    print(item)
