import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)

    rows_before = len(df)
    df = df.drop_duplicates(keep="first")
    rows_after = len(df)
    cleaned_data = df.to_dict(orient="list")

    return [rows_before,rows_after,cleaned_data]
    