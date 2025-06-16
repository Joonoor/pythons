class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sayName(self):
        print(self.name)

    def sayPrice(self):
        print(self.price)

    def sayProduct(self):
        print(self.name, end='')
        print(self.price, end='')
