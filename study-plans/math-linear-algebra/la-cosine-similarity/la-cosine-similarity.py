import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a_arr = np.asarray(a, dtype=np.float64)
    b_arr = np.asarray(b, dtype=np.float64)
    numerator = np.dot(a_arr,b_arr)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    norm_prod = np.dot(a_norm,b_norm)
    dot_prod = np.dot(a_arr,b_arr)
    if norm_prod == 0:
      return 0.0
    return float(dot_prod/norm_prod)