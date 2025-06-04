# unique_characters.py
# This script checks whether all characters in a string are unique.
# Example:
# "hello" => False (because of two 'l')
# "world" => True

def has_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# Example usage
if __name__ == "__main__":
    test_strings = ["hello", "world", "python", "noon"]
    for word in test_strings:
        result = has_unique_characters(word)
        print(f"'{word}' has all unique characters? {result}")
