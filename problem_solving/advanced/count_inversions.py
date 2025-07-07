# 🔄 Problem: Count Inversions in an Array
# 📘 Concept: Divide and Conquer (Merge Sort variation)
# 🎯 Goal: Count number of (i, j) pairs where i < j and nums[i] > nums[j]

def count_inversions(arr):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, inv_left = merge_sort(nums[:mid])
        right, inv_right = merge_sort(nums[mid:])

        merged = []
        i = j = inversions = 0

        # Merge step with inversion counting
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i  # All remaining left elements > right[j]
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        total_inversions = inv_left + inv_right + inversions
        return merged, total_inversions

    _, count = merge_sort(arr)
    return count

# ✅ Example
if __name__ == "__main__":
    print(count_inversions([2, 4, 1, 3, 5]))  # Expected: 3
    print(count_inversions([5, 4, 3, 2, 1]))  # Expected: 10
