class Product:

    counter = 1

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.id = Product.counter
        Product.counter += 1
