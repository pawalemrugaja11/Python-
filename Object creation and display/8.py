class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)

l1 = Laptop("Dell", "8GB")
l1.display()
