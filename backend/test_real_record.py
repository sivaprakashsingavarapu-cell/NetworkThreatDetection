import requests
import pandas as pd

# Load dataset
data = pd.read_parquet(
    "dataset/network_threat_dataset.parquet"
)

# Load the 20 features
top_features = [
    "Init Fwd Win Bytes",
    "Bwd Packet Length Mean",
    "Bwd Packet Length Std",
    "Fwd IAT Mean",
    "Flow IAT Max",
    "Flow IAT Mean",
    "Bwd Packets/s",
    "Avg Bwd Segment Size",
    "Bwd Header Length",
    "Fwd Packet Length Max",
    "Fwd IAT Max",
    "Init Bwd Win Bytes",
    "Packet Length Variance",
    "Fwd IAT Min",
    "Fwd IAT Total",
    "Flow Packets/s",
    "PSH Flag Count",
    "Fwd Header Length",
    "Bwd Packets Length Total",
    "Bwd Packet Length Max"
]

# Take one real record
record = data.iloc[0]

# Actual label
actual_label = record["Label"]

# Prepare data for API
input_data = {}

for feature in top_features:
    input_data[feature] = record[feature].item()

# Send request
url = "http://127.0.0.1:5000/predict"

response = requests.post(
    url,
    json=input_data
)

print("Status Code:", response.status_code)
print("Actual Label:", actual_label)
print("Predicted Label:", response.json()["prediction"])