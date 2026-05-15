import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    flitered_data = df[df[column] > threshold]
    return {
        "filtered_data" : flitered_data.to_dict("list"),
        "count" : len(flitered_data)
    }