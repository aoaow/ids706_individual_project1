from lib import load_breast_cancer_data, calculate_mean

def test_load_breast_cancer_data():
    df = load_breast_cancer_data()
    assert df.shape[0] == 569  # The dataset has 569 samples
    assert 'mean radius' in df.columns

def test_calculate_mean():
    df = load_breast_cancer_data()
    mean_radius = calculate_mean(df, 'mean radius')
    assert round(mean_radius, 2) == 14.13  # Known mean from the dataset
