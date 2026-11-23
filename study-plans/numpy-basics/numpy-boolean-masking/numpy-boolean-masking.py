import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    data = np.asarray(data,dtype=np.float64)
    mask = data > threshold
    row_any = mask.any(axis=1, keepdims= True)
    row_all = mask.all(axis =1, keepdims= True)
    return np.stack([mask.astype(np.float64),data*row_any,data*row_all])
    
    
    