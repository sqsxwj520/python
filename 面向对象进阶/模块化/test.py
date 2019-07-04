class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x + self.y


print('test')
if __name__ == '__main__':
    a = A(4, 5)
    print(a.show())
