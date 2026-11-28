class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

p1 = Product("Laptop", 45000, 2)
p1.display()
