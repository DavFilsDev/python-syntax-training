# FILE INPUT/OUTPUT IN PYTHON

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Python makes file I/O easy!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("📄 File Content:\n", content)

# Appending to a file
with open("example.txt", "a") as f:
    f.write("\nNew line added!")

# Reading line by line
with open("example.txt", "r") as f:
    print("📄 Reading line by line:")
    for line in f:
        print("➡️", line.strip())

# MEMO:
# - Use `with open(...)` to automatically close files.
# - Modes:
#   - "r" = read
#   - "w" = write (overwrites)
#   - "a" = append
#   - "rb"/"wb" = binary
# - `f.read()`: reads all content
# - `f.readline()`: reads one line
# - `f.readlines()`: returns list of lines
