# ids706_individual_project1

# Breast Cancer Dataset Analysis with Pandas
---

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
  - [Exploring the Notebook](#exploring-the-notebook)
- [Descriptive Statistics of the Breast Cancer Dataset](#descriptive-statistics-of-the-breast-cancer-dataset)
  - [Overview of the Dataset](#overview-of-the-dataset)
  - [Statistical Summaries](#statistical-summaries)
- [Files Description](#files-description)
- [Testing](#testing)
- [Makefile Commands](#makefile-commands)
- [Continuous Integration](#continuous-integration)
- [License](#license)

---

## Introduction

This project performs descriptive statistics on the breast cancer dataset using pandas. The project demonstrates efficient data processing, shared code usage, testing with `pytest` and `nbval`, and continuous integration using GitLab CI/CD.

---

## Project Structure

```
project/
├── README.md
├── Makefile
├── requirements.txt
├── lib.py
├── script.py
├── test_lib.py
├── test_script.py
├── notebook.ipynb
└── .gitlab-ci.yml
```

---

## Installation Instructions

### **Prerequisites**

- Python 3.7 or higher
- `pip` package manager

### **Steps**

1. **Clone the Repository**

   ```bash
   git clone https://gitlab.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Install Dependencies**

   ```bash
   make install
   ```

   This command installs all the required packages listed in `requirements.txt`.

---

## Usage

### **Running the Script**

The script `script.py` performs the analysis and outputs the results to the console.

```bash
python script.py
```

**Expected Output:**

```
Descriptive Statistics for 'mean radius':
Mean: 14.127291739894563
Median: 13.37
Standard Deviation: 3.524049388059983
```

### **Exploring the Notebook**

The Jupyter Notebook `notebook.ipynb` provides an interactive exploration of the dataset, including data loading, descriptive statistics, and optional visualizations.

To open the notebook:

```bash
jupyter notebook notebook.ipynb
```

---

## Descriptive Statistics of the Breast Cancer Dataset

### **Overview of the Dataset**

The breast cancer dataset is a classic and very easy multi-class classification dataset. It contains 569 samples of malignant and benign tumor cells, with 30 features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

- **Features:** Mean, standard error, and "worst" or largest (mean of the three largest values) of ten real-valued features computed for each cell nucleus.
- **Target:** Binary classification (malignant = 0, benign = 1).

### **Statistical Summaries**

#### **1. General Statistics**

Using Polars' `describe()` method, we obtain the following statistics for each feature:

| Statistic          | Value                      |
|--------------------|----------------------------|
| **Number of Rows** | 569                        |
| **Number of Columns** | 31 (30 features + target) |

#### **2. Feature-wise Descriptive Statistics**

Below are the descriptive statistics for selected features:

##### **Mean Radius**

- **Mean:** 14.127
- **Median:** 13.370
- **Standard Deviation:** 3.524

##### **Mean Texture**

- **Mean:** 19.289
- **Median:** 18.840
- **Standard Deviation:** 4.301

##### **Mean Perimeter**

- **Mean:** 91.969
- **Median:** 86.240
- **Standard Deviation:** 24.299

#### **3. Target Variable Distribution**

- **Malignant (0):** 212 samples
- **Benign (1):** 357 samples

#### **4. Full Statistical Summary**

Below is a statistical summary for all numerical features:

| Feature                   | Mean     | Median   | Std Dev  | Min      | Max      |
|---------------------------|----------|----------|----------|----------|----------|
| mean radius               | 14.127   | 13.370   | 3.524    | 6.981    | 28.110   |
| mean texture              | 19.289   | 18.840   | 4.301    | 9.710    | 39.280   |
| mean perimeter            | 91.969   | 86.240   | 24.299   | 43.790   | 188.500  |
| mean area                 | 654.889  | 551.100  | 351.914  | 143.500  | 2501.000 |
| mean smoothness           | 0.096    | 0.095    | 0.014    | 0.053    | 0.163    |
| ...                       | ...      | ...      | ...      | ...      | ...      |
| **Total Samples**         | **569**  |          |          |          |          |

*(Note: For brevity, only a few features are listed. The full summary includes all features.)*

---

## Files Description

- **`README.md`**: This file. Provides an overview of the project, instructions, and detailed descriptions.
- **`Makefile`**: Contains commands for installation, testing, linting, and formatting.
- **`requirements.txt`**: Lists all the required Python packages with pinned versions.
- **`lib.py`**: Contains shared functions for data loading and calculations.
- **`script.py`**: A script that performs the analysis using functions from `lib.py`.
- **`test_lib.py`**: Contains tests for the functions in `lib.py`.
- **`test_script.py`**: Contains tests for `script.py`.
- **`notebook.ipynb`**: Jupyter Notebook demonstrating the analysis with detailed explanations.
- **`.gitlab-ci.yml`**: Configuration file for GitLab CI/CD pipeline.

---

## Testing

### **Run All Tests**

To run all tests, including the notebook tests:

```bash
make test
```

This command executes:

- `pytest --nbval notebook.ipynb`
- `pytest test_script.py`
- `pytest test_lib.py`

### **Test Coverage**

The tests cover:

- **Data Loading:** Ensures the dataset is loaded correctly.
- **Calculations:** Validates mean, median, and standard deviation calculations.
- **Script Output:** Checks that `script.py` produces the expected output.

---

## Makefile Commands

The `Makefile` simplifies common tasks:

- **Install Dependencies:**

  ```bash
  make install
  ```

- **Format Code with Black:**

  ```bash
  make format
  ```

- **Lint Code with Ruff:**

  ```bash
  make lint
  ```

- **Run Tests:**

  ```bash
  make test
  ```

---

## Continuous Integration

The project uses GitLab CI/CD for continuous integration. The pipeline performs the following stages:

1. **Install:** Installs dependencies using `make install`.
2. **Lint:** Checks code style and potential errors using `make lint`.
3. **Format:** Formats code using `make format`.
4. **Test:** Runs all tests using `make test`.

### **Pipeline Status Badges**

- **Pipeline Status:**

  [![pipeline status](https://gitlab.com/yourusername/yourproject/badges/main/pipeline.svg)](https://gitlab.com/yourusername/yourproject/-/pipelines)

- **Coverage Report:**

  [![coverage report](https://gitlab.com/yourusername/yourproject/badges/main/coverage.svg)](https://gitlab.com/yourusername/yourproject/-/commits/main)

Replace `yourusername` and `yourproject` with your actual GitLab username and project name.

---

## License

This project is licensed under the MIT License.

---

## Detailed Steps and Explanations

### **1. Data Loading**

- **Function:** `load_breast_cancer_data()` in `lib.py`
- **Description:** Loads the breast cancer dataset from scikit-learn and converts it into a Polars DataFrame.
- **Usage:**

  ```python
  df = load_breast_cancer_data()
  ```

### **2. Data Processing**

- **Polars DataFrame Creation:**
  
  - Data and feature names are used to create the DataFrame.
  - The target variable is added as a new column.

- **Advantages of Polars:**

  - High performance for data manipulation.
  - Efficient handling of large datasets.

### **3. Descriptive Statistics Calculations**

- **Functions in `lib.py`:**
  
  - `calculate_mean(df, column_name)`
  - `calculate_median(df, column_name)`
  - `calculate_std(df, column_name)`

- **Usage:**

  ```python
  mean_value = calculate_mean(df, 'mean radius')
  median_value = calculate_median(df, 'mean radius')
  std_value = calculate_std(df, 'mean radius')
  ```

### **4. Script Execution**

- **Script:** `script.py`
- **Purpose:** Performs the analysis and prints results.
- **Execution Flow:**

  1. Loads data using `load_breast_cancer_data()`.
  2. Specifies the column to analyze (`'mean radius'`).
  3. Calculates mean, median, and standard deviation.
  4. Prints the results.

### **5. Jupyter Notebook Exploration**

- **Notebook:** `notebook.ipynb`
- **Contents:**

  - Data loading and initial exploration.
  - Descriptive statistics using Polars.
  - Visualizations (optional).

- **Features:**

  - Interactive cells to explore data.
  - Use of shared functions from `lib.py`.
  - Detailed explanations and markdown cells.

### **6. Testing**

- **Tests for `lib.py`:**

  - Validates data loading and correctness of calculations.
  - Ensures functions handle data correctly.

- **Tests for `script.py`:**

  - Captures console output.
  - Asserts that the output matches expected results.

### **7. Linting and Formatting**

- **Linting with Ruff:**

  - Checks for code style issues and potential errors.
  - Ensures code adheres to PEP 8 standards.

- **Formatting with Black:**

  - Formats code for consistency.
  - Improves readability.

### **8. Continuous Integration**

- **Configuration:** `.gitlab-ci.yml`
- **Stages:**

  - **Install:** Sets up the environment.
  - **Lint:** Runs `make lint`.
  - **Format:** Runs `make format`.
  - **Test:** Runs `make test`.

- **Benefits:**

  - Automated checks on every push.
  - Early detection of issues.
  - Maintains code quality.

---

## Conclusion

This project demonstrates the use of Polars for efficient data analysis on the breast cancer dataset. By structuring the project with shared code, thorough testing, and continuous integration, we ensure reliability and maintainability. The detailed steps and explanations provided aim to make it easy for others to understand and replicate the analysis.

---

## Contact Information

For any questions or suggestions, please feel free to contact:

- **Name:** Your Name
- **Email:** your.email@example.com
- **GitLab:** [yourusername](https://gitlab.com/yourusername)

---

*Note: Replace placeholder text like `yourusername`, `yourproject`, and contact information with your actual details.*