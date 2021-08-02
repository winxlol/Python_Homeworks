class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return self.__pi * self.diameter

    def calculate_area(self):
        return self.__pi * pow(self.radius, 2)

    def calculate_area_of_sector(self, angle):
        return (angle/360) * self.calculate_area()


angle = int(input())
calculation_circle = Circle(angle)

print(f"{calculation_circle.calculate_circumference():.2f}")
print(f"{calculation_circle.calculate_area():.2f}")
print(f"{calculation_circle.calculate_area_of_sector(angle):.2f}")
