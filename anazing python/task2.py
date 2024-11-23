# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗.")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️.")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤.")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
