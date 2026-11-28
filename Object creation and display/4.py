class Mobile:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Mobile:", self.name)
        print("Price:", self.price)

m1 = Mobile("Samsung", 20000)
m1.display()
