# ➗ Problem: Single Number II
# 📘 Concept: Bit Manipulation
# 🎯 Goal: Find the unique number when all others appear three times

def single_number(nums):
    """
    :param nums: List[int] - input array where each element appears 3 times except one
    :return: int - the unique element
    """
    ones, twos = 0, 0

    for num in nums:
        # Update ones and twos
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

# ✅ Example
if __name__ == "__main__":
    print(single_number([2, 2, 3, 2]))       # Output: 3
    print(single_number([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
