import pandas as pd
import os
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# ============================================================
# LOAD DATASET
# ============================================================

file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "network_threat_dataset.parquet"
    )
)

data = pd.read_parquet(file_path)

print("=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Shape:", data.shape)


# ============================================================
# FEATURES AND LABEL
# ============================================================

X = data.drop("Label", axis=1)
y = data["Label"]


# ============================================================
# ENCODE LABELS
# ============================================================

encoder = LabelEncoder()
y = encoder.fit_transform(y)


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# TRAIN MODEL
# ============================================================

print("\n" + "=" * 60)
print("TRAINING MODEL")
print("=" * 60)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Training completed!")


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

top_features = importance.head(20)["Feature"].tolist()


# ============================================================
# TRAIN MODEL USING TOP 20 FEATURES
# ============================================================

print("\n" + "=" * 60)
print("TRAINING FINAL MODEL")
print("=" * 60)

X_train_top20 = X_train[top_features]

final_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

final_model.fit(X_train_top20, y_train)

print("Final model trained!")
print("Features used:", len(top_features))


# ============================================================
# CREATE MODEL DIRECTORY
# ============================================================

model_directory = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "model"
    )
)

os.makedirs(model_directory, exist_ok=True)


# ============================================================
# SAVE MODEL
# ============================================================

model_path = os.path.join(
    model_directory,
    "network_threat_model.pkl"
)

joblib.dump(final_model, model_path)


# ============================================================
# SAVE LABEL ENCODER
# ============================================================

encoder_path = os.path.join(
    model_directory,
    "label_encoder.pkl"
)

joblib.dump(encoder, encoder_path)


# ============================================================
# SAVE FEATURE LIST
# ============================================================

features_path = os.path.join(
    model_directory,
    "top_features.pkl"
)

joblib.dump(top_features, features_path)


# ============================================================
# RESULT
# ============================================================

print("\n" + "=" * 60)
print("MODEL SAVED SUCCESSFULLY")
print("=" * 60)

print("Model:", model_path)
print("Encoder:", encoder_path)
print("Features:", features_path)