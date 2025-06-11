# longest_substring.py
# This script finds the length of the longest substring without repeating characters.
# The problem tests understanding of string traversal and use of data structures like hash maps or sets.

def length_of_longest_substring(s):
    char_index_map = {}  # Stores the last index of each character seen
    start = max_length = 0

    for i, char in enumerate(s):
        # If char is found in map and its index is inside the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move start to one position right of the last occurrence
            start = char_index_map[char] + 1
        # Update or add the current character's index
        char_index_map[char] = i
        # Calculate max length of substring seen so far
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage
if __name__ == "__main__":
    test_str = "abcabcbb"
    print(f"Input: '{test_str}'")
    print("Length of the longest substring without repeating characters:", length_of_longest_substring(test_str))
