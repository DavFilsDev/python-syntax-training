from collections import deque

# Kata: Knight's Shortest Path
# Given two different positions on a chess board,
# find the least number of moves it would take a knight to get from one to the other.
# The positions are passed as two arguments in algebraic notation, e.g., "a3", "b5".
# The knight can only make valid chess moves and is not allowed to move off the 8x8 board.

def knight(p1, p2):
    # Convert a position like "a3" to (x, y) coordinates (0-indexed)
    def to_coords(pos):
        file = ord(pos[0]) - ord('a')  # 'a'-'h' becomes 0-7
        rank = int(pos[1]) - 1         # '1'-'8' becomes 0-7
        return (file, rank)

    start = to_coords(p1)
    target = to_coords(p2)

    # If the starting and target positions are the same, no moves needed
    if start == target:
        return 0

    # All 8 possible knight moves (L-shaped moves)
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    # Initialize visited matrix and queue for BFS
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, move count)
    visited[start[0]][start[1]] = True

    # Perform BFS to find the shortest path
    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is within the board and not yet visited
            if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
                if (nx, ny) == target:
                    return moves + 1  # Found the shortest path
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    # This should not be reached with valid inputs
    return -1
