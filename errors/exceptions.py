# EXCEPTION HANDLING IN PYTHON

# Basic try-except block to catch errors
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ You can't divide by zero!")

# Catching multiple types of exceptions
try:
    num = int("abc")
except (ValueError, TypeError):
    print("❌ Invalid conversion or type!")

# Using else with try-except
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("❌ Please enter a number.")
else:
    print(f"✅ You are {age} years old.")

# Using finally to always execute code
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("❌ File not found.")
finally:
    print("✅ This block always runs (cleanup, close file, etc.)")

# Raising custom exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("❌ Age can't be negative.")
    print("✅ Age is valid.")

try:
    validate_age(-5)
except ValueError as ve:
    print(ve)

# MEMO:
# - Use try-except to catch runtime errors.
# - Use else for code that runs if no exception is raised.
# - Use finally to run cleanup code always.
# - You can raise your own exceptions with `raise`.
