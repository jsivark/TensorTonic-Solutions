import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """
    m = len(A)
    n = len(A[0])
    result = np.zeros((n,m),dtype=np.float64)
    for i in range(m):
      for j in range(n):
        result[j][i] = A[i][j]
    return result
        
        