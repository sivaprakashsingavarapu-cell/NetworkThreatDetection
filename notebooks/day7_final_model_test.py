import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# PATHS
# ============================================================

base_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

dataset_path = os.path.join(
    base_path,
    "dataset",
    "network_threat_dataset.parquet"
)

model_path = os.path.join(
    base_path,
    "model",
    "network_threat_model.pkl"
)

encoder_path = os.path.join(
    base_path,
    "model",
    "label_encoder.pkl"
)

features_path = os.path.join(
    base_path,
    "model",
    "top_features.pkl"
)


# ============================================================
# LOAD SAVED FILES
# ============================================================

print("=" * 60)
print("LOADING SAVED MODEL")
print("=" * 60)

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)
top_features = joblib.load(features_path)

print("Model loaded successfully!")
print("Label encoder loaded successfully!")
print("Top features loaded successfully!")
print("Number of features:", len(top_features))


# ============================================================
# LOAD DATASET
# ============================================================

data = pd.read_parquet(dataset_path)

print("\n" + "=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Shape:", data.shape)


# ============================================================
# SEPARATE FEATURES AND LABEL
# ============================================================

X = data.drop("Label", axis=1)
y = data["Label"]


# ============================================================
# ENCODE LABELS
# ============================================================

y = encoder.transform(y)


# ============================================================
# CREATE SAME TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# SELECT TOP 20 FEATURES
# ============================================================

X_test_top20 = X_test[top_features]


# ============================================================
# PREDICT
# ============================================================

print("\n" + "=" * 60)
print("TESTING SAVED MODEL")
print("=" * 60)

predictions = model.predict(X_test_top20)

print("Prediction completed!")


# ============================================================
# ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n" + "=" * 60)
print("FINAL MODEL ACCURACY")
print("=" * 60)

print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_,
        zero_division=0
    )
)