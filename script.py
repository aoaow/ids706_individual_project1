from lib import load_breast_cancer_data, calculate_mean, calculate_median, calculate_std

def main():
    # Load the data
    df = load_breast_cancer_data()
    
    # Specify the column to analyze
    column = 'mean radius'
    
    # Perform calculations
    mean_value = calculate_mean(df, column)
    median_value = calculate_median(df, column)
    std_value = calculate_std(df, column)
    
    # Output the results
    print(f"Descriptive Statistics for '{column}':")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_value}")

if __name__ == "__main__":
    main()

