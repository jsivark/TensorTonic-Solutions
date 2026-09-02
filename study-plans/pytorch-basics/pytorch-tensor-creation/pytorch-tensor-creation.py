import torch

def create_tensor(method, shape, value=0.0):
  
    """
    Returns: list
    """
    shape_tuple = tuple(shape)
    if method == "zeros":
      return torch.zeros(shape_tuple).tolist()
    if method == "ones":
      return torch.ones(shape_tuple).tolist()
    elif method == "full":
      return torch.full(tuple(shape), value).tolist()
    
    
  