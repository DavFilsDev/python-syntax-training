# TUPLES IN PYTHON

# A tuple is an ordered, immutable collection of items.

coordinates = (10, 20)
print("Tuple:", coordinates)

# Accessing elements
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Tuple unpacking
x, y = coordinates
print("Unpacked X and Y:", x, y)

# Single-element tuple
single = (5,)
print("Single-element tuple:", single)

# MEMO:
# - Tuples are immutable → values cannot be changed
# - Useful for fixed-size data (e.g., coordinates)
