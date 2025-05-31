# SORTING ALGORITHMS IN PYTHON

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
nums = [5, 2, 9, 1, 5, 6]
print("🔢 Sorted with bubble sort:", bubble_sort(nums.copy()))

# Built-in Python sort
nums.sort()
print("⚡ Built-in sort:", nums)

# MEMO:
# - Bubble sort: simple but inefficient (O(n²))
# - Prefer Python's built-in `.sort()` or `sorted()` for real-world use
