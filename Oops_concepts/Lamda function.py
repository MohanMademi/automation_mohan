lambda arguments: expression


# adding two numbers using lamda function

add = lambda x, y: x + y
result = add(5, 10)
print(result)  # Output: 15


# doubling a nuber using lamda functions

double = lambda x: x * 2
result = double(6)
print(result)  # Output: 12


# Finding a squqre of number using lamda functiomn

square = lambda x: x ** 2
result = square(4)
print(result)  # Output: 16


# Using a lambda function as a key for sorting a list of tuples:

data = [(2, 'Alice'), (1, 'Bob'), (3, 'Eve')]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(2, 'Alice'), (1, 'Bob'), (3, 'Eve')]


# Using lambda functions in map and filter:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared)       # Output: [1, 4, 9, 16, 25]
print(even_numbers)  # Output: [2, 4]
