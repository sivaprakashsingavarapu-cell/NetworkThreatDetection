import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Init Fwd Win Bytes": 0,
    "Bwd Packet Length Mean": 0,
    "Bwd Packet Length Std": 0,
    "Fwd IAT Mean": 0,
    "Flow IAT Max": 0,
    "Flow IAT Mean": 0,
    "Bwd Packets/s": 0,
    "Avg Bwd Segment Size": 0,
    "Bwd Header Length": 0,
    "Fwd Packet Length Max": 0,
    "Fwd IAT Max": 0,
    "Init Bwd Win Bytes": 0,
    "Packet Length Variance": 0,
    "Fwd IAT Min": 0,
    "Fwd IAT Total": 0,
    "Flow Packets/s": 0,
    "PSH Flag Count": 0,
    "Fwd Header Length": 0,
    "Bwd Packets Length Total": 0,
    "Bwd Packet Length Max": 0
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())