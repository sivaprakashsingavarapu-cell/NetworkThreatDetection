import pandas as pd
import os
import joblib
from sklearn.metrics import accuracy_score


# ============================================================
# PATHS
# ============================================================

base_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
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

dataset_path = os.path.join(
    base_path,
    "dataset",
    "network_threat_dataset.parquet"
)


# ============================================================
# LOAD MODEL
# ============================================================

print("=" * 60)
print("LOADING MODEL")
print("=" * 60)

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)
top_features = joblib.load(features_path)

print("Model loaded successfully!")
print("Features:", len(top_features))


# ============================================================
# LOAD DATASET
# ============================================================

data = pd.read_parquet(dataset_path)

print("\n" + "=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Dataset shape:", data.shape)


# ============================================================
# SELECT 100 RECORDS
# ============================================================

test_data = data.iloc[:100]

X_test = test_data[top_features]

actual_labels = test_data["Label"]


# ============================================================
# MAKE PREDICTIONS
# ============================================================

predictions = model.predict(X_test)

predicted_labels = encoder.inverse_transform(predictions)


# ============================================================
# CALCULATE ACCURACY
# ============================================================

accuracy = accuracy_score(
    actual_labels,
    predicted_labels
)

correct = sum(
    actual_labels.values == predicted_labels
)

incorrect = len(actual_labels) - correct


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 60)
print("MULTIPLE RECORD TEST")
print("=" * 60)

print("Total records tested:", len(test_data))
print("Correct predictions:", correct)
print("Incorrect predictions:", incorrect)

print("\nAccuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100)


# ============================================================
# SHOW FIRST 10 PREDICTIONS
# ============================================================

print("\n" + "=" * 60)
print("FIRST 10 PREDICTIONS")
print("=" * 60)

for i in range(10):
    print(
        "Record", i + 1,
        "| Actual:", actual_labels.iloc[i],
        "| Predicted:", predicted_labels[i]
    )