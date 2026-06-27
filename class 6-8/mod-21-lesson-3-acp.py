# Parent class
class Vehicle:

    def __init__(self, fare):
        self.fare = fare


# Child class
class Bus(Vehicle):

    def total_fare(self):
        maintenance = self.fare * 0.10
        total = self.fare + maintenance
        return total


# Take fare as input
fare = float(input("Enter the bus fare: "))

# Create object
bus = Bus(fare)

# Display total fare
print("Total Fare =", bus.total_fare())