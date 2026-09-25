import pandas as pd
import os
import joblib


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
print("Feature list loaded successfully!")

print("\nNumber of features:", len(top_features))


# ============================================================
# LOAD DATASET
# ============================================================

data = pd.read_parquet(dataset_path)

print("\n" + "=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Dataset shape:", data.shape)


# ============================================================
# SELECT ONE RECORD
# ============================================================

sample = data.iloc[[0]]

print("\n" + "=" * 60)
print("TEST RECORD")
print("=" * 60)

print("Actual label:", sample["Label"].values[0])


# ============================================================
# SELECT TOP 20 FEATURES
# ============================================================

X_sample = sample[top_features]


# ============================================================
# MAKE PREDICTION
# ============================================================

prediction = model.predict(X_sample)


# ============================================================
# CONVERT NUMBER TO LABEL
# ============================================================

predicted_label = encoder.inverse_transform(prediction)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)

print("Actual threat:", sample["Label"].values[0])
print("Predicted threat:", predicted_label[0])


# ============================================================
# CHECK RESULT
# ============================================================

if sample["Label"].values[0] == predicted_label[0]:
    print("Prediction: CORRECT")
else:
    print("Prediction: INCORRECT")