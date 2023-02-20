my_list = [1, 2, 3, 4, 5]

print(my_list) #Output: [1, 2, 3, 4, 5]

#Accessing elements in a list
print(my_list[0]) # Output: 1
print(my_list[-1]) # Output: 5

# Modifying elements in a list 
my_list[0] = 10
print(my_list) # Output: [10, 2, 3, 4, 5]

# Slicing a list
print(my_list[1:3]) # Output: [2, 3]
print(my_list[2:]) # Output: [3, 4, 5]

# Appending an element to a list
my_list.append(6)
print(my_list) # Output: [1, 2, 3, 4, 5, 6]

# Inserting an element into a list
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
print(my_list) # Output: [1, 2, 10, 3, 4, 5]

# Removing an element from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list) # Output: [1, 2, 4, 5]

# Sorting a list
my_list = [5, 3, 1, 4, 2]
my_list.sort()
print(my_list) # Output: [1, 2, 3, 4, 5]

# Reversing a list:
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # Output: [5, 4, 3, 2, 1]

# Create another list
my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]

my_list.extend(my_list2)
print('List after extend():', my_list)

