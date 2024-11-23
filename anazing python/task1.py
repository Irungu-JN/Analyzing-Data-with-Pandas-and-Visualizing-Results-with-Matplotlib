# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}.")

    def browse(self):
        print(f"Browsing on the {self.brand} {self.model}.")

# Child class inheriting from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life  # Unique to Smartwatch

    def track_steps(self):
        print(f"Tracking steps on {self.brand} {self.model}.")

# Create objects
phone = Smartphone("Apple", "iPhone 15", 1200)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 400, "24 hours")

# Use methods
phone.call("123-456-7890")
phone.browse()

watch.call("987-654-3210")  # Inherits call() from Smartphone
watch.track_steps()
