# BASIC FUNCTION DEFINITIONS IN PYTHON

# A function is a block of reusable code that performs a specific task.
# You define a function using the 'def' keyword.

# Simple function with no parameter
def greet():
    print("Hello! Welcome to Python functions.")

greet()  # Call the function

# Function with parameters
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)

# Default parameter values
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello()  # Uses default value

# Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old.")

introduce(age=25, name="John")

# Variable scope
x = 10  # global variable

def show_scope():
    x = 5  # local variable
    print("Inside function:", x)

show_scope()
print("Outside function:", x)

# MEMO:
# - Functions are defined with def
# - Use return to give back a value
# - Variables inside functions are local by default
