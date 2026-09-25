import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

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

# Separate features and target
X = data.drop("Label", axis=1)
y = data["Label"]

# Create LabelEncoder
encoder = LabelEncoder()

# Convert text labels to numbers
y_encoded = encoder.fit_transform(y)

print("=" * 60)
print("LABEL ENCODING")
print("=" * 60)

print("Original labels:")
print(encoder.classes_)
print()

print("Encoded numbers:")
print(y_encoded[:20])
print()

print("Label mapping:")
for number, label in enumerate(encoder.classes_):
    print(number, "->", label)

print()

print("Number of classes:", len(encoder.classes_))