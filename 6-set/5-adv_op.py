# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Compute the symmetric difference between the two sets
symmetric_difference = set1.symmetric_difference(set2)

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)

# Check if set2 is a superset of set1
is_superset = set2.issuperset(set1)


# Print the results
print(f"Symmetric difference: {symmetric_difference}")
print(f"Is set1 a subset of set2? {is_subset}")
print(f"Is set2 a superset of set1? {is_superset}")
