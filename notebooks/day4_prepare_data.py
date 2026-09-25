import pandas as pd
import os

# Dataset path
file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "network_threat_dataset.parquet"
    )
)

# Load dataset
data = pd.read_parquet(file_path)

print("=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Shape:", data.shape)
print()

# Display first 5 rows
print("First 5 rows:")
print(data.head())
print()

# Separate features and target
X = data.drop("Label", axis=1)
y = data["Label"]

print("=" * 60)
print("FEATURES AND TARGET")
print("=" * 60)

print("Number of features:", X.shape[1])
print("Number of records:", X.shape[0])
print()

print("Target column:")
print(y.name)
print()

print("Feature columns:")
print(X.columns.tolist())
print()

# Check data types
print("=" * 60)
print("DATA TYPES")
print("=" * 60)

print(X.dtypes)
print()

# Check missing values
print("=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = X.isnull().sum()

print("Total missing values:", missing_values.sum())
print()

# Check infinite values
print("=" * 60)
print("INFINITE VALUES")
print("=" * 60)

infinite_values = X.select_dtypes(include="number").isin(
    [float("inf"), float("-inf")]
).sum().sum()

print("Total infinite values:", infinite_values)
print()

# Target distribution
print("=" * 60)
print("TARGET DISTRIBUTION")
print("=" * 60)

print(y.value_counts())
print()

print("Day 4 data preparation completed!")