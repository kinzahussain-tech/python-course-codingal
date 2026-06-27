# Class BMW
class BMW:

    def speed(self):
        print("BMW Speed: 250 km/h")

    def fuel(self):
        print("BMW uses Petrol")


# Class Ferrari
class Ferrari:

    def speed(self):
        print("Ferrari Speed: 340 km/h")

    def fuel(self):
        print("Ferrari uses Petrol")


# Function demonstrating polymorphism
def car_info(car):
    car.speed()
    car.fuel()
    print()


# Create objects
bmw = BMW()
ferrari = Ferrari()

# Call the same function with different objects
car_info(bmw)
car_info(ferrari)