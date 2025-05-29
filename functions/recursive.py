# RECURSION IN PYTHON

# Recursion is when a function calls itself to solve a smaller version of a problem.

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive call

print("5! =", factorial(5))

# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6) =", fibonacci(6))

# BE CAREFUL:
# - Always define a base case to avoid infinite recursion
# - Recursive functions can be inefficient for large inputs

# MEMO:
# - Use recursion for problems that can be divided into similar sub-problems
# - Watch out for the maximum recursion depth limit in Python
