# DICTIONARIES IN PYTHON

# A dictionary stores data in key-value pairs.

student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Updating value
student["age"] = 22

# Removing a key
del student["major"]
print("After deletion:", student)

# Looping through dictionary
for key, value in student.items():
    print(f"{key} → {value}")

# MEMO:
# - Keys must be unique and immutable
# - Very useful for structured data
