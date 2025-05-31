# SEARCH ALGORITHMS IN PYTHON

# Linear Search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Binary Search (list must be sorted)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [1, 3, 5, 7, 9]
print("🔍 Linear search (5):", linear_search(nums, 5))
print("🔍 Binary search (7):", binary_search(nums, 7))

# MEMO:
# - Linear search: works for unsorted lists (O(n))
# - Binary search: fast (O(log n)), but needs sorted list
