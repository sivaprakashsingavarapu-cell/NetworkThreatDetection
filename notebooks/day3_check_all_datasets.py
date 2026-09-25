import pandas as pd
import os

# Dataset folder path
dataset_folder = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset"
    )
)

# Get all parquet files
files = [file for file in os.listdir(dataset_folder) if file.endswith(".parquet")]

print("Dataset folder:")
print(dataset_folder)
print()

print("Number of Parquet files:", len(files))
print()

# Check every dataset
for file in files:

    file_path = os.path.join(dataset_folder, file)

    print("=" * 60)
    print("File:", file)

    # Read only Label column first
    data = pd.read_parquet(file_path, columns=["Label"])

    print("Number of rows:", len(data))

    print("Labels:")
    print(data["Label"].unique())

    print("Label counts:")
    print(data["Label"].value_counts())

    print()