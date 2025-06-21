import sys

# Read dimensions
l = int(input())  # width of one character (e.g., 4)
h = int(input())  # height of one character (e.g., 5)
t = input().upper()  # text to convert (e.g., "E")

# Read ASCII art rows
ascii_art = []
for _ in range(h):
    row = input().strip()  # Read one full row of the ASCII art
    ascii_art.append(row)

# Process each row of the output
for row in ascii_art:
    output_line = []
    for char in t:
        # Determine position in alphabet (A=0, B=1, ..., Z=25, ?=26)
        if 'A' <= char <= 'Z':
            pos = ord(char) - ord('A')
        else:
            pos = 26  # ? for unknown characters
        
        # Calculate slice indices
        start = pos * l
        end = start + l
        
        # Extract the character's slice from this row
        char_slice = row[start:end]
        output_line.append(char_slice)
    
    # Print the combined line
    print(''.join(output_line))