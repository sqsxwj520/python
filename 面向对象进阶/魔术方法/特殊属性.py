# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# x = 100
#
# print(dir())  # x 也在内
# print(__name__)


class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)
        return self

    def __add__(self, other):
        self.add(other)
        return self

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        # return iter(self.items)
        yield from self.items  # 从列表中一个一个的产出元素

    def __repr__(self):
        return "<Cart {} {}>".format(__class__.__name__, self.items)


c1 = Cart()
c1.add(1)
c1.add(2)
c1.add(3).add(4)
print(len(c1))
print(c1)
print(c1[0])
c1[2] = 200
print(c1[2])
print(c1 + 3 + 5)
for x in c1:
    print(x)
