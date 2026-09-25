import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

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

# Separate features and target
X = data.drop("Label", axis=1)
y = data["Label"]

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("=" * 60)
print("TRAINING DATA CLASS DISTRIBUTION")
print("=" * 60)

train_counts = pd.Series(y_train).value_counts().sort_index()

for number, count in train_counts.items():
    print(
        number,
        "->",
        encoder.classes_[number],
        ":",
        count
    )

print()

print("=" * 60)
print("TESTING DATA CLASS DISTRIBUTION")
print("=" * 60)

test_counts = pd.Series(y_test).value_counts().sort_index()

for number, count in test_counts.items():
    print(
        number,
        "->",
        encoder.classes_[number],
        ":",
        count
    )

print()

print("=" * 60)
print("CLASS CHECK")
print("=" * 60)

print("Number of classes in training:", len(train_counts))
print("Number of classes in testing:", len(test_counts))

print()

if len(train_counts) == len(encoder.classes_) and len(test_counts) == len(encoder.classes_):
    print("All 15 classes are present in both datasets.")
else:
    print("Some classes are missing.")

print()
print("Day 4 class distribution check completed!")