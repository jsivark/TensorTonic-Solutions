import numpy as np

def hadamard_product(A: list, B: list) -> np.ndarray:
    """
    Returns the element-wise product as a float64 array.
    """
    m = len(A)
    n = len(A[0])
    result = np.zeros((m,n), dtype=np.float64)
    for i in range(m):
      for j in range(n):
        result[i][j] += A[i][j]*B[i][j]
    return result