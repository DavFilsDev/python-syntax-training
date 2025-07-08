# 🤖 Problem: Unique Paths in a Grid
# 📘 Concept: Dynamic Programming (2D DP table)
# 🎯 Goal: Find how many unique paths from top-left to bottom-right in a grid.

def unique_paths(m, n):
    """
    :param m: int - number of rows
    :param n: int - number of columns
    :return: int - number of unique paths
    """
    # Initialize DP grid with 1 in the first row and first column
    dp = [[1] * n for _ in range(m)]

    # Fill the DP grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

# ✅ Example
if __name__ == "__main__":
    print(unique_paths(3, 7))  # Output: 28
    print(unique_paths(3, 2))  # Output: 3
