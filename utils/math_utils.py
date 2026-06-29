"""Math utilities for linear algebra operations."""

import numpy as np
from typing import Union

Vector = np.ndarray
Matrix = np.ndarray


def create_vector(*components: float) -> Vector:
    """Create a vector from components."""
    return np.array(components, dtype=float)


def create_matrix(rows: list[list[float]]) -> Matrix:
    """Create a matrix from nested lists."""
    return np.array(rows, dtype=float)


def vector_add(v1: Vector, v2: Vector) -> Vector:
    """Add two vectors."""
    return v1 + v2


def vector_subtract(v1: Vector, v2: Vector) -> Vector:
    """Subtract two vectors."""
    return v1 - v2


def scalar_multiply(scalar: float, vector: Vector) -> Vector:
    """Multiply vector by scalar."""
    return scalar * vector


def dot_product(v1: Vector, v2: Vector) -> float:
    """Calculate dot product of two vectors."""
    return np.dot(v1, v2)


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """Calculate cross product of two 3D vectors."""
    return np.cross(v1, v2)


def vector_magnitude(vector: Vector) -> float:
    """Calculate magnitude (length) of vector."""
    return np.linalg.norm(vector)


def vector_normalize(vector: Vector) -> Vector:
    """Normalize vector to unit length."""
    mag = vector_magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot normalize zero vector")
    return vector / mag


def matrix_add(m1: Matrix, m2: Matrix) -> Matrix:
    """Add two matrices."""
    return m1 + m2


def matrix_subtract(m1: Matrix, m2: Matrix) -> Matrix:
    """Subtract two matrices."""
    return m1 - m2


def matrix_multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """Multiply two matrices."""
    return np.matmul(m1, m2)


def scalar_matrix_multiply(scalar: float, matrix: Matrix) -> Matrix:
    """Multiply matrix by scalar."""
    return scalar * matrix


def matrix_transpose(matrix: Matrix) -> Matrix:
    """Transpose a matrix."""
    return matrix.T


def matrix_determinant(matrix: Matrix) -> float:
    """Calculate determinant of matrix."""
    return np.linalg.det(matrix)


def matrix_inverse(matrix: Matrix) -> Matrix:
    """Calculate inverse of matrix."""
    return np.linalg.inv(matrix)


def matrix_trace(matrix: Matrix) -> float:
    """Calculate trace of matrix."""
    return np.trace(matrix)


def eigenvalues_eigenvectors(matrix: Matrix) -> tuple[np.ndarray, Matrix]:
    """Calculate eigenvalues and eigenvectors."""
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def solve_linear_system(A: Matrix, b: Vector) -> Vector:
    """Solve system Ax = b."""
    return np.linalg.solve(A, b)


def gaussian_elimination(A: Matrix, b: Vector) -> tuple[Matrix, Vector]:
    """Perform Gaussian elimination (returns augmented matrix steps)."""
    n = len(b)
    # Create augmented matrix
    Ab = np.column_stack([A.copy(), b.copy()])

    steps = []

    for col in range(n):
        # Find pivot
        max_row = np.argmax(np.abs(Ab[col:, col])) + col

        # Swap rows if needed
        if max_row != col:
            Ab[[col, max_row]] = Ab[[max_row, col]]
            steps.append(f"R{col+1} ↔ R{max_row+1}")

        # Make pivot 1
        pivot = Ab[col, col]
        if pivot != 0:
            Ab[col] = Ab[col] / pivot
            steps.append(f"R{col+1} → R{col+1} / {pivot:.2f}")

        # Eliminate below
        for row in range(col + 1, n):
            factor = Ab[row, col]
            Ab[row] = Ab[row] - factor * Ab[col]
            steps.append(f"R{row+1} → R{row+1} - ({factor:.2f}) × R{col+1}")

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i+1:n] * x[i+1:n])

    return x, steps


def rank(matrix: Matrix) -> int:
    """Calculate rank of matrix."""
    return np.linalg.matrix_rank(matrix)


def is_invertible(matrix: Matrix) -> bool:
    """Check if matrix is invertible."""
    try:
        np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False
