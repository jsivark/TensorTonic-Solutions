import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df  = pd.DataFrame(data)
    dtypes_before = df.dtypes.astype(str).to_dict()
    df[column] = df[column].astype(target_type)
    dftypes_after = df.dtypes.astype(str).to_dict()
    return [dtypes_before,dftypes_after]