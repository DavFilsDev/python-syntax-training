# ✍️ Problem: Edit Distance (Minimum number of insertions, deletions, or replacements)
# 📘 Concept: Dynamic Programming (2D table)
# 🎯 Goal: Convert word1 to word2 using the fewest operations

def edit_distance(word1, word2):
    """
    :param word1: str - original word
    :param word2: str - target word
    :return: int - minimum edit distance
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = min operations to convert word1[0:i] to word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill base cases
    for i in range(m + 1):
        dp[i][0] = i  # i deletions
    for j in range(n + 1):
        dp[0][j] = j  # j insertions

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )

    return dp[m][n]

# ✅ Example
if __name__ == "__main__":
    print(edit_distance("horse", "ros"))   # Expected: 3
    print(edit_distance("intention", "execution"))  # Expected: 5
