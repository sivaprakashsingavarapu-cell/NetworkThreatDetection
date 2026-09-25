import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# --------------------------------------------------
# 1. Dataset path
# --------------------------------------------------

file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "network_threat_dataset.parquet"
    )
)


# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

data = pd.read_parquet(file_path)

print("=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Shape:", data.shape)
print()


# --------------------------------------------------
# 3. Separate features and target
# --------------------------------------------------

X = data.drop("Label", axis=1)

y = data["Label"]


print("Number of features:", X.shape[1])
print("Number of records:", X.shape[0])
print()


# --------------------------------------------------
# 4. Encode target labels
# --------------------------------------------------

encoder = LabelEncoder()

y = encoder.fit_transform(y)


print("=" * 60)
print("LABEL ENCODING COMPLETED")
print("=" * 60)

print("Number of classes:", len(encoder.classes_))
print()


# --------------------------------------------------
# 5. Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("=" * 60)
print("TRAIN-TEST SPLIT")
print("=" * 60)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
print()


# --------------------------------------------------
# 6. Create Random Forest model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


print("=" * 60)
print("TRAINING RANDOM FOREST")
print("=" * 60)

print("Training started...")

model.fit(X_train, y_train)

print("Training completed!")
print()


# --------------------------------------------------
# 7. Make predictions
# --------------------------------------------------

print("=" * 60)
print("MAKING PREDICTIONS")
print("=" * 60)

y_pred = model.predict(X_test)

print("Predictions completed!")
print()


# --------------------------------------------------
# 8. Calculate accuracy
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("=" * 60)
print("MODEL RESULT")
print("=" * 60)

print("Accuracy:", accuracy)

print("Accuracy percentage:", accuracy * 100)

print()

print("Day 5 model training completed!")