import pandas as pd
import os

# Dataset path
file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "Benign-Monday-no-metadata.parquet"
    )
)

# Load dataset
data = pd.read_parquet(file_path)

print("Dataset loaded successfully!")
print()

# 1. Dataset size
print("Number of rows and columns:")
print(data.shape)
print()

# 2. Column names
print("Column names:")
print(data.columns.tolist())
print()

# 3. Labels
print("Labels:")
print(data["Label"].unique())
print()

# 4. Number of records for each label
print("Label counts:")
print(data["Label"].value_counts())
print()

# 5. Missing values
print("Missing values:")
print(data.isnull().sum())
print()

# 6. Duplicate rows
print("Number of duplicate rows:")
print(data.duplicated().sum())
print()

# 7. Data types
print("Data types:")
print(data.dtypes)