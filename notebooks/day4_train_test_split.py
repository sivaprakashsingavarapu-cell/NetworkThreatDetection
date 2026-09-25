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
y = encoder.fit_transform(y)

print("=" * 60)
print("BEFORE TRAIN-TEST SPLIT")
print("=" * 60)

print("X shape:", X.shape)
print("y shape:", y.shape)
print()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("=" * 60)
print("AFTER TRAIN-TEST SPLIT")
print("=" * 60)

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)

print()

print("Training labels:", y_train.shape)
print("Testing labels:", y_test.shape)

print()

print("Train-Test split completed successfully!")