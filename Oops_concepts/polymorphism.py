# POLYMORPHISM EXAMPLE:
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

# Polymorphism in action
animals = [Dog(),Cat()]
for animal in animals:
    animal.speak()




# METHOD OVERIDING:
#

class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.make_sound())  # Output: "Generic animal sound"
print(dog.make_sound())     # Output: "Woof!"
print(cat.make_sound())  # Output: "Meow!"
print("-----------------------------------")


# METHOD OVER RIDING EXAMPLE 2:

class A:
    def display(self):
        print("this is class A")

class B(A):
    def display(self):
        print("this is class B")
        super().display()

obj=B()
obj.display()
print("--------------------------------------------")


# METHOD OVERLOADIUNG:


# same class
# same fuction and method names
# different parameters
class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=1):
        return a+b+c
class Matics(Math):
    def multiply(self,a,b):
        return a * b

    def multiply(self,a,b,c=2):
        return a * b * c

obj=Matics()
print(obj.multiply(2, 3, 4))
print("------------------------------------------------")
print(obj.add(2, 3, 7))