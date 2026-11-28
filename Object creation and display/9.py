class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display(self):
        area = 3.14 * self.radius * self.radius
        print("Radius:", self.radius)
        print("Area:", area)

c1 = Circle(5)
c1.display()
