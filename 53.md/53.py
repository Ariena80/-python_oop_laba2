class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * self.__radius ** 2

    def get_circumference(self):
        return 2 * 3.14159 * self.__radius

circle = Circle(5)
print("Area:", circle.get_area())
print("Circumference:", circle.get_circumference())