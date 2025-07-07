# 🔤 Problem: Decode Ways (LeetCode 91)
# 📘 Concept: Recursion + Memoization / Dynamic Programming
# 🎯 Goal: Find number of ways to decode a digit string into letters

def num_decodings(s):
    """
    :param s: str - string of digits
    :return: int - number of ways to decode the string
    """
    memo = {}

    def dfs(index):
        if index in memo:
            return memo[index]

        if index == len(s):
            return 1  # fully decoded

        if s[index] == '0':
            return 0  # can't decode a leading zero

        # Take one digit
        ways = dfs(index + 1)

        # Take two digits if it's between 10 and 26
        if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
            ways += dfs(index + 2)

        memo[index] = ways
        return ways

    return dfs(0)

# ✅ Example
if __name__ == "__main__":
    print(num_decodings("12"))  # Output: 2
    print(num_decodings("226"))  # Output: 3
    print(num_decodings("06"))   # Output: 0
