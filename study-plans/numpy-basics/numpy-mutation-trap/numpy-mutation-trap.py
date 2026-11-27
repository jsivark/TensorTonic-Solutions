import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    x = np.asarray(data,dtype=np.float64)
    row = x[row_idx]
    clipped = np.clip(row,lo,hi)
    return np.vstack([row,clipped])
