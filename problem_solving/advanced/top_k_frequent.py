# 🔢 Problem: Top K Frequent Elements
# 📘 Concept: Heap (Priority Queue), Hash Map
# 🎯 Goal: Return the k most frequent elements from a list

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    :param nums: List[int] - input numbers
    :param k: int - number of most frequent elements to return
    :return: List[int] - k elements with the highest frequencies
    """
    # Count the frequency of each element
    freq_map = Counter(nums)

    # Use a heap to extract the k largest frequency elements
    # heapq.nlargest returns the k keys with the highest freq_map values
    return [item for item, count in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# ✅ Example
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent(nums, k))
    # Expected: [1, 2]
