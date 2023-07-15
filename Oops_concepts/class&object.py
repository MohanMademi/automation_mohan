class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# Creating objects of the Car class
car1 = Car("Toyota", "Blue")
car2 = Car("Honda", "Red")

# Accessing object attributes
print(car1.brand)  # Output: Toyota
print(car2.color)  # Output: Red

# Calling object methods
car1.drive()  # Output: The Blue Toyota is driving.
