# matrix_determinant.py
# -----------------------------------------------------
# 🧮 Problem: Matrix Determinant (Recursive Laplace Expansion)
#
# Given an N x N square matrix, compute its determinant.
# 
# Rules:
# - 1x1 matrix → return the single value
# - 2x2 matrix → use formula: a*d - b*c
# - NxN matrix → apply Laplace expansion (recursive minor reduction)
# 
# For a matrix M = [[a, b], [c, d]]:
#   det(M) = a*d - b*c
# 
# For 3x3 or more:
#   det(M) = a * det(minor_a) - b * det(minor_b) + ...
#            (alternate signs for each element in the first row)
# 
# This function is not optimized for huge matrices (O(n!)), but works well for small/intermediate N.
# -----------------------------------------------------

def determinant(matrix):
    """
    Recursively calculates the determinant of a square matrix.
    
    :param matrix: list[list[int]] - N x N matrix
    :return: int - determinant value
    """
    # Base case: 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if len(matrix) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return a * d - b * c

    # Recursive case: Laplace expansion on the first row
    det = 0
    for col_index, element in enumerate(matrix[0]):
        # Build the minor by excluding current row (0) and current column (col_index)
        minor = [
            [row[c] for c in range(len(matrix)) if c != col_index]
            for row in matrix[1:]
        ]

        # Alternate sign: + - + - ...
        sign = (-1) ** col_index
        det += sign * element * determinant(minor)

    return det

# Example test
if __name__ == "__main__":
    m1 = [[1]]
    m2 = [[1, 2], [3, 4]]
    m3 = [[6, 1, 1],
          [4, -2, 5],
          [2, 8, 7]]

    print("Determinant of m1 (1x1):", determinant(m1))  # Expected: 1
    print("Determinant of m2 (2x2):", determinant(m2))  # Expected: -2
    print("Determinant of m3 (3x3):", determinant(m3))  # Expected: -306
