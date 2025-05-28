# CONDITIONAL STATEMENTS IN PYTHON

age = int(input("Enter your age: "))

# Standard if/elif/else structure
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Example of boolean condition
is_student = True
if is_student:
    print("Welcome, student!")

# ---------------------------------------
# TERNARY OPERATOR (Conditional expression)
# ---------------------------------------
# Syntax: value_if_true if condition else value_if_false

# Let's use a ternary to check driving eligibility
driving_status = "Can drive" if age >= 18 else "Cannot drive"
print(driving_status)

# Another example with a number
number = int(input("Enter a number: "))
parity = "Even" if number % 2 == 0 else "Odd"
print(f"The number is {parity}.")

# REMEMBER:
# - Ternary is useful for short, simple conditions
# - Avoid nesting ternary expressions — use if/else instead
