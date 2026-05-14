import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    return {"head":df.iloc[:n].to_dict("list"),
           "tail":df.iloc[-n:].to_dict("list")
           }