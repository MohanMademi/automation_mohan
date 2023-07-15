class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Dog barks.")

animal = Animal("Generic Animal")
animal.speak()  # Output: Animal speaks.

dog = Dog("Buddy")
dog.speak()  # Output: Dog barks.
