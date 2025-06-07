# LISTS IN PYTHON

# A list is an ordered, mutable collection of elements.

fruits = ["apple", "banana", "cherry", "peachh"]
print("Original list:", fruits)
print(fruits[1:])
print(fruits[1:3])

# Accessing elements
print("First fruit:", fruits[0])

# Modifying elements
fruits[1] = "mango"
print("Modified list:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Inserting at specific position
fruits.insert(1, "grape")
print("After insert:", fruits)

# Removing elements
fruits.remove("cherry")
print("After remove:", fruits)

# Looping through list
for fruit in fruits:
    print("Fruit:", fruit)

# List comprehension
uppercase_fruits = [f.upper() for f in fruits]
print("Uppercase fruits:", uppercase_fruits)

# MEMO:
# - Lists are mutable
# - Use indexing, slicing, and list methods to manipulate
