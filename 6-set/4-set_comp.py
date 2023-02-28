# Create a set of integers
my_set = {1, 2, 3, 4, 5}

# Create a new set that contains only the even numbers from the original set
even_set = {x for x in my_set if x % 2 == 0}

# Print the new set
print(even_set)
