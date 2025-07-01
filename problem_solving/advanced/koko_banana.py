# 🍌 Problem: Koko Eating Bananas
# 📘 Concept: Binary Search on Answer Space
# 🎯 Goal: Find minimum speed k such that total hours <= h

import math

def min_eating_speed(piles, h):
    """
    :param piles: List[int] - number of bananas in each pile
    :param h: int - maximum hours to eat all bananas
    :return: int - minimum integer speed k
    """
    left, right = 1, max(piles)
    res = right

    while left <= right:
        k = (left + right) // 2
        hours_needed = sum(math.ceil(p / k) for p in piles)

        if hours_needed <= h:
            res = k
            right = k - 1  # Try smaller speed
        else:
            left = k + 1  # Increase speed

    return res

# ✅ Example
if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print("Minimum speed to finish:", min_eating_speed(piles, h))
    # Expected: 4
