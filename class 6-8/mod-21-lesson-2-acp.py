class Circle:

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def area(self):
        return 3.14 * self.radius * self.radius

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * 3.14 * self.radius


# Take radius as input
r = float(input("Enter the radius of the circle: "))

# Create object
c = Circle(r)

# Display results
print("Area of Circle =", c.area())
print("Perimeter of Circle =", c.perimeter())