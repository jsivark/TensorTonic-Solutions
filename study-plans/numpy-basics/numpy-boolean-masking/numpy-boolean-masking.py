import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    mask, any_l, all_l = [], [], []
    for row in data:
        m = [1.0 if v > threshold else 0.0 for v in row]
        zeros = [0.0] * len(row)
        mask.append(m)
        any_l.append(row if 1.0 in m else zeros)
        all_l.append(row if 0.0 not in m else zeros)
    return np.array([mask, any_l, all_l], dtype=np.float64)
    
    
    