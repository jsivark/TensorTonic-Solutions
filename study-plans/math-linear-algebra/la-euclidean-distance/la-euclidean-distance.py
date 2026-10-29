import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    y_arr = np.asarray(y, dtype=np.float64)
    return float(np.sqrt(np.sum((x_arr - y_arr)**2)))
  
    
      
     