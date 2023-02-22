# A list of strings
my_list = ['apple', 'banana', 'cherry', 'date']

print(my_list)

#Accessing elements in a list
print(my_list[0]) # Output: 'banana'
print(my_list[-2]) # Output: 'cherry'

# Modifying elements in a list 
my_list[1] = 'orange'
print(my_list) # Output: ['apple', 'orange', 'cherry', 'date']

# Slicing a list
print(my_list[1:3]) # Output: ['orange', 'cherry']
print(my_list[1:]) # Output: ['orange','cherry', 'date']

# Appending an element to a list
my_list.append('banana')
print(my_list) # Output: ['apple', 'orange', 'cherry', 'date', 'banana']
