class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        area = self.length * self.breadth
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", area)

r1 = Rectangle(10, 5)
r1.display()
