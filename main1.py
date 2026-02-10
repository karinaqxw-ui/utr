class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        s = 0
        for i in self.items:
            s += i.price
        print(s)


p1 = Product("Хліб", 30)
c = Cart()
c.add(p1)
c.total()
