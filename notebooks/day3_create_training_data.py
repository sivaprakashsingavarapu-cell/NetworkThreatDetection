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

# Output folder
output_folder = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset"
    )
)

files = [
    file for file in os.listdir(dataset_folder)
    if file.endswith(".parquet")
]

# Number of records to take from each label
SAMPLES_PER_LABEL = 2000

all_data = []

print("Creating balanced training dataset...")
print()

for file in files:

    file_path = os.path.join(dataset_folder, file)

    print("Reading:", file)

    data = pd.read_parquet(file_path)

    # Process each label separately
    for label in data["Label"].unique():

        label_data = data[data["Label"] == label]

        # Take maximum 2000 records
        sample_size = min(SAMPLES_PER_LABEL, len(label_data))

        sampled_data = label_data.sample(
            n=sample_size,
            random_state=42
        )

        all_data.append(sampled_data)

        print(
            label,
            "->",
            sample_size,
            "records"
        )

# Combine everything
final_data = pd.concat(
    all_data,
    ignore_index=True
)

# Shuffle dataset
final_data = final_data.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save
output_path = os.path.join(
    output_folder,
    "network_threat_dataset.parquet"
)

final_data.to_parquet(
    output_path,
    index=False
)

print()
print("=" * 60)
print("DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print("Shape:", final_data.shape)

print()
print("Label counts:")
print(final_data["Label"].value_counts())

print()
print("Saved to:")
print(output_path)