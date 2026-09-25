import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "dataset",
    "Benign-Monday-no-metadata.parquet"
)

file_path = os.path.abspath(file_path)

print("Looking for file:")
print(file_path)

data = pd.read_parquet(file_path)

print("Dataset loaded successfully!")
print(data.head())
print("Shape:", data.shape)
print("Columns:")
print(data.columns)