my_list = [1, 2, 3, 4, 5]  # List with initial values
empty_list = []  # Empty list

print(my_list[0])  # Accessing the first element
print(my_list[2])  # Accessing the third element
print(my_list[-1])  # Accessing the last element using negative indexing


my_list[0] = 10  # Modifying the value of the first element
print(my_list)  # Output: [10, 2, 3, 4, 5]


my_list.append(6)  # Adding an element at the end
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

my_list.insert(2, 7)  # Inserting an element at a specific index
print(my_list)  # Output: [10, 2, 7, 3, 4, 5, 6]

my_list.remove(3)  # Removing an element by value
print(my_list)  # Output: [10, 2, 7, 4, 5, 6]

my_list.pop(4)  # Removing an element by index
print(my_list)  # Output: [10, 2, 7, 4, 6]


for element in my_list:
    print(element)


squared_list = [x**2 for x in my_list]  # Creating a new list with squared values
print(squared_list)

even_list = [x for x in my_list if x % 2 == 0]  # Creating a new list with even numbers
print(even_list)

#
slice_list = my_list[1:4]  # Slicing a list to get elements from index 1 to 3
print(slice_list)

my_list.sort()  # Sorting the list in ascending order
print(my_list)

my_list.reverse()  # Reversing the order of elements in the list
print(my_list)

length = len(my_list)  # Finding the length of the list
print(length)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Accessing an element in a 2D list


my_list = [1, 2, 3, 4, 5]
print(sum(my_list))  # Calculating the sum of all elements
print(max(my_list))  # Finding the maximum element
print(min(my_list))  # Finding the minimum element
