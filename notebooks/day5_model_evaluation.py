import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


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


# --------------------------------------------------
# 4. Encode labels
# --------------------------------------------------

encoder = LabelEncoder()

y = encoder.fit_transform(y)


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


# --------------------------------------------------
# 6. Create Random Forest
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# --------------------------------------------------
# 7. Train model
# --------------------------------------------------

print("=" * 60)
print("TRAINING MODEL")
print("=" * 60)

model.fit(X_train, y_train)

print("Training completed!")
print()


# --------------------------------------------------
# 8. Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 9. Accuracy
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("=" * 60)
print("ACCURACY")
print("=" * 60)

print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100)
print()


# --------------------------------------------------
# 10. Classification report
# --------------------------------------------------

print("=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

report = classification_report(
    y_test,
    y_pred,
    target_names=encoder.classes_,
    zero_division=0
)

print(report)


# --------------------------------------------------
# 11. Confusion matrix
# --------------------------------------------------

print("=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

cm = confusion_matrix(
    y_test,
    y_pred
)

print(cm)

print()
print("Day 5 evaluation completed!")