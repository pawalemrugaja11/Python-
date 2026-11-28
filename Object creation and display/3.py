class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

c1 = Car("BMW", "Black")
c1.display()
