import polars as pl
from sklearn.datasets import load_breast_cancer

def load_breast_cancer_data():
    """
    Loads the breast cancer dataset and returns a Polars DataFrame.
    """
    data = load_breast_cancer()
    df = pl.DataFrame(data.data, columns=data.feature_names)
    df = df.with_columns([
        pl.Series(name='target', values=data.target)
    ])
    return df

def calculate_mean(df, column_name):
    """
    Calculates the mean of a specified column in the DataFrame.
    """
    return df.select(pl.col(column_name).mean()).item()

def calculate_median(df, column_name):
    """
    Calculates the median of a specified column in the DataFrame.
    """
    return df.select(pl.col(column_name).median()).item()

def calculate_std(df, column_name):
    """
    Calculates the standard deviation of a specified column in the DataFrame.
    """
    return df.select(pl.col(column_name).std()).item()

