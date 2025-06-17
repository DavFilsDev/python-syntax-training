# backtracking.py
# -----------------------------------------------------
# 🔄 Problem: N-Queens
#
# Place N queens on an N×N chessboard so that no two
# queens threaten each other (row, column, diagonal).
# Return all distinct solutions, each solution is a list
# of strings showing board configuration.
#
# Approach: classic backtracking with column & diagonal checks.
# Time complexity: exponential, but acceptable for small N (≤10).
# -----------------------------------------------------

def solve_n_queens(n):
    """
    :param n: int – size of the board (n×n) and number of queens
    :return:  List[List[str]] – all board configurations
    """
    solutions = []
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            # convert board rows to strings
            solutions.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            # place queen
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board[r][c] = "Q"

            backtrack(r + 1)

            # remove queen (backtrack)
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return solutions

# Example usage
if __name__ == "__main__":
    n = 4
    sols = solve_n_queens(n)
    print(f"{len(sols)} solutions for {n}-Queens:")
    for sol in sols:
        for row in sol:
            print(row)
        print()
