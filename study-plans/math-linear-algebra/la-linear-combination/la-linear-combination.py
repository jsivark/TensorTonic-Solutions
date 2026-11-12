import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    result = np.array(coefficients) @ np.array(vectors)
    return np.asarray(result, dtype = np.float64)
  