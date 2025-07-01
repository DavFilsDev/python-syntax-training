# 🏃 Problem: Jump Game II
# 📘 Concept: Greedy (jump farthest within the current window)
# 🎯 Goal: Reach the last index in the minimum number of jumps

def jump(nums):
    """
    :param nums: List[int] - max jump length from each index
    :return: int - minimum number of jumps to reach the end
    """
    jumps = 0
    farthest = 0
    current_end = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        # Time to jump to next range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

# ✅ Example
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print("Minimum jumps to reach the end:", jump(nums))
    # Expected: 2
