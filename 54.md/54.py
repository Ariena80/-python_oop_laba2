class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_ratio(self):
        return self.get_square() / self.get_perimeter()


rectangle = Rectangle(5, 3)
print("Square:", rectangle.get_square())
print("Perimeter:", rectangle.get_perimeter())
print("Ratio:", rectangle.get_ratio())