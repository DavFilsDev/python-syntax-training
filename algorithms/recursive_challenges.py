# RECURSION IN PYTHON

# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("🧮 Factorial(5):", factorial(5))

# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("📈 Fibonacci(6):", fibonacci(6))

# MEMO:
# - Recursion: when a function calls itself
# - Be careful: can be slow if not optimized (e.g., memoization)
# - Always define a base case to avoid infinite recursion
