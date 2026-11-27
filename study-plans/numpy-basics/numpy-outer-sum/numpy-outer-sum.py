import numpy as np

def outer_sum(a: list, b: list) -> np.ndarray:
    """
    Returns an (m, n) float64 array of pairwise sums.
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    return a[:,np.newaxis] + b[np.newaxis,:]
    
    