import torch

def tensor_op(x, y, op):
    """
    Returns the resulting tensor converted to a Python list.
    """
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)

    op = op.lower()

    if op == "add":
        result = torch.add(x, y)
    elif op == "multiply":
        result = torch.mul(x, y)
    elif op == "matmul":
        result = torch.matmul(x, y)
    elif op == "power":
        result = torch.pow(x, y)
    elif op == "max":
        result = torch.maximum(x, y)

    return result.tolist()