# 🧭 Problem: Unique Paths III
# 📘 Concept: Backtracking with State Tracking
# 🎯 Goal: Find all unique paths visiting all empty cells exactly once from start to end.

def unique_paths_iii(grid):
    rows, cols = len(grid), len(grid[0])
    empty = 0
    start_x = start_y = 0

    # Count empty cells and locate the start
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                empty += 1
            elif grid[i][j] == 1:
                start_x, start_y = i, j

    # Helper function for backtracking
    def dfs(x, y, remain):
        if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == -1:
            return 0

        if grid[x][y] == 2:
            return remain == -1  # End reached and all empty cells visited

        # Mark as visited
        temp = grid[x][y]
        grid[x][y] = -1

        # Explore 4 directions
        paths = dfs(x + 1, y, remain - 1) + \
                dfs(x - 1, y, remain - 1) + \
                dfs(x, y + 1, remain - 1) + \
                dfs(x, y - 1, remain - 1)

        # Backtrack
        grid[x][y] = temp

        return paths

    return dfs(start_x, start_y, empty)

# ✅ Example
if __name__ == "__main__":
    grid = [[1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]]
    print(unique_paths_iii(grid))  # Output: 2
