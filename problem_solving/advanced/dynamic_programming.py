# dynamic_programming.py
# -----------------------------------------------------
# 🧮 Problem: 0/1 Knapsack
#
# Given a list of items, each with a weight and a value,
# determine the maximum total value you can carry in a knapsack
# of capacity W without breaking any item (0/1 choice).
#
# Approach: classic dynamic programming with a 2D table.
# Time complexity: O(n * W)
# -----------------------------------------------------

def knapsack(weights, values, W):
    """
    :param weights: List[int] – weights of items
    :param values:  List[int] – values of items
    :param W:       int       – max capacity of knapsack
    :return:        int       – max total value
    """
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]
        for w in range(W + 1):
            if wt <= w:
                # choose max of including or excluding current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt] + val)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    capacity = 5
    print("Max value:", knapsack(weights, values, capacity))
    # Expected: 7 (items of weight 2 and 3)
