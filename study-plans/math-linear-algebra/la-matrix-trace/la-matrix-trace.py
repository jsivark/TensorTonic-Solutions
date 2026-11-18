import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    m = len(A)
    n = len(A[0])
    trace=0
    for i in range(m):
      for j in range(n):
        if i==j:
          trace += A[i][j]
    return float(trace)
          