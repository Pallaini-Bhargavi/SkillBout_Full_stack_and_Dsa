class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getname(self):
        print(self.name)

    def getprice(self):
        print(self.price)

p1 = Product('Prod1',234)
p2 = Product('Prod2',931)
p1.getname()
p1.getprice()
p2.getname()
p2.getprice()