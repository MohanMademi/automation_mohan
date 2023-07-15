class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute

    def display_salary(self):
        print(f"The salary of {self.name} is {self._salary}.")

employee = Employee("John", 5000)
print(employee.name)  # Output: John
print(employee._salary)  # Output: 5000 (can be accessed but considered conventionally protected)
employee.display_salary()  # Output: The salary of John is 5000.
