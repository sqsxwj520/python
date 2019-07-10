
class Color:
    BLACK = 0
    BLUE = 1
    RED = 2
    WHITE = 3
    GREEN = 4


class Item:
    def __init__(self, mark, color, price, **kwargs):
        self.mark = mark
        self.color = color
        self.price = price
        self._spec = kwargs

    def __repr__(self):

        return '{} {}'.format(self.mark, self.price)


class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)
        return self

    def get_all(self):
        return self.items


cart = Cart()
item1 = Item('HuaWei', Color.BLUE, 3500, memory='4G')
cart.add_item(item1)
item2 = Item('RedFlag', Color.WHITE, 200000, year=2019)
cart.add_item(item2)
print(cart.get_all())
