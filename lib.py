import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_breast_cancer_data():
    """
    Loads the breast cancer dataset and returns a Polars DataFrame.
    """
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target

    return df

def calculate_mean(df, column_name):
    """
    Calculates the mean of a specified column in the DataFrame.
    """
    return df[column_name].mean()

def calculate_median(df, column_name):
    """
    Calculates the median of a specified column in the DataFrame.
    """
    return df[column_name].median()

def calculate_std(df, column_name):
    """
    Calculates the standard deviation of a specified column in the DataFrame.
    """
    return df[column_name].std()
