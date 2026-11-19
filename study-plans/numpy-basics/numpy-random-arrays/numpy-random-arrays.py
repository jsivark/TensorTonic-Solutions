import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    rng = np.random.default_rng(seed)
    size = tuple(shape)
    if kind == "normal":
      result = rng.standard_normal(size)
    elif kind == "uniform":
      result = rng.random(size)

    return result.astype(np.float64)