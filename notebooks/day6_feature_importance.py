import pandas as pd
import os

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
# SEPARATE FEATURES AND LABEL
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
# TRAIN RANDOM FOREST
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

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)


# ============================================================
# DISPLAY TOP 20 FEATURES
# ============================================================

print("\n" + "=" * 60)
print("TOP 20 IMPORTANT FEATURES")
print("=" * 60)

print(feature_importance.head(20).to_string(index=False))