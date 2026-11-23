import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    x = np.asarray(data, dtype=np.float64)
    mask = x > threshold

    out = np.empty((3,) + x.shape)                               # one allocation
    out[0] = mask                                                # bool → 1.0/0.0 automatically
    np.multiply(x, mask.any(axis=1, keepdims=True), out=out[1])
    np.multiply(x, mask.all(axis=1, keepdims=True), out=out[2])
    return out
    
    
    