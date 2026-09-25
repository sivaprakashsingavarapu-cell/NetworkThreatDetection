import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


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
# TRAIN FULL MODEL
# ============================================================

print("\n" + "=" * 60)
print("TRAINING MODEL WITH ALL FEATURES")
print("=" * 60)

full_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

full_model.fit(X_train, y_train)

full_predictions = full_model.predict(X_test)

full_accuracy = accuracy_score(
    y_test,
    full_predictions
)

print("Features used:", X.shape[1])
print("Full model accuracy:", full_accuracy)
print("Full model accuracy percentage:", full_accuracy * 100)


# ============================================================
# GET TOP 20 FEATURES
# ============================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": full_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

top_features = importance.head(20)["Feature"].tolist()


# ============================================================
# CREATE REDUCED DATASET
# ============================================================

X_train_reduced = X_train[top_features]
X_test_reduced = X_test[top_features]


print("\n" + "=" * 60)
print("TRAINING MODEL WITH TOP 20 FEATURES")
print("=" * 60)

reduced_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

reduced_model.fit(
    X_train_reduced,
    y_train
)

reduced_predictions = reduced_model.predict(
    X_test_reduced
)

reduced_accuracy = accuracy_score(
    y_test,
    reduced_predictions
)

print("Features used:", len(top_features))
print("Reduced model accuracy:", reduced_accuracy)
print(
    "Reduced model accuracy percentage:",
    reduced_accuracy * 100
)


# ============================================================
# COMPARISON
# ============================================================

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print("All 77 features:", full_accuracy * 100, "%")
print("Top 20 features:", reduced_accuracy * 100, "%")