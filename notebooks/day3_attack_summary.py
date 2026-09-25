import pandas as pd
import os

# Dataset folder
dataset_folder = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset"
    )
)

# Find all parquet files
files = [
    file for file in os.listdir(dataset_folder)
    if file.endswith(".parquet")
]

all_labels = []

# Read labels from every dataset
for file in files:

    file_path = os.path.join(dataset_folder, file)

    data = pd.read_parquet(
        file_path,
        columns=["Label"]
    )

    all_labels.append(data["Label"])

# Combine all labels
labels = pd.concat(all_labels, ignore_index=True)

print("=" * 60)
print("COMPLETE DATASET LABEL SUMMARY")
print("=" * 60)

print()

print("Total number of records:", len(labels))

print()

print("All labels:")
print(labels.unique())

print()

print("Count of each label:")
print(labels.value_counts())

print()

print("Total number of unique labels:")
print(labels.nunique())