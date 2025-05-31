# SETS IN PYTHON

# A set is an unordered collection of unique elements.

unique_numbers = {1, 2, 3, 4, 5}
print("Original set:", unique_numbers)

# Adding elements
unique_numbers.add(6)
print("After add:", unique_numbers)

# Removing elements
unique_numbers.discard(3)
print("After discard:", unique_numbers)

# Set operations
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}

print("Union:", evens.union(odds))
print("Intersection:", evens.intersection(unique_numbers))
print("Difference:", evens.difference(unique_numbers))

# MEMO:
# - Sets do not allow duplicates
# - Great for membership tests and set algebra
