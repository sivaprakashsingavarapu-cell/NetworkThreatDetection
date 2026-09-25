from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import joblib
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

CORS(app)
# Project path
base_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

# Model files
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

# Load ML files
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)
top_features = joblib.load(features_path)

print("Model loaded successfully!")
print("Features loaded:", len(top_features))


# MySQL connection function
def get_db_connection():

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    return connection


# Home API
@app.route("/")
def home():

    return jsonify({
        "message": "Network Threat Detection API is running!",
        "model": "Random Forest",
        "features": len(top_features)
    })


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # Convert input to DataFrame
    input_data = pd.DataFrame([data])

    # Select required features
    input_data = input_data[top_features]

    # Make prediction
    prediction = model.predict(input_data)

    # Convert encoded number to attack name
    predicted_label = encoder.inverse_transform(prediction)[0]

    # Connect to MySQL
    connection = get_db_connection()

    cursor = connection.cursor()

    # Save prediction
    query = """
        INSERT INTO predictions (prediction)
        VALUES (%s)
    """

    cursor.execute(query, (predicted_label,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "prediction": predicted_label,
        "database": "Prediction saved successfully"
    })

@app.route("/predictions", methods=["GET"])
def get_predictions():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT id, prediction, created_at
        FROM predictions
        ORDER BY id DESC
        LIMIT 10
    """

    cursor.execute(query)

    predictions = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(predictions)


@app.route("/stats", methods=["GET"])
def get_stats():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Total predictions
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM predictions
    """)
    total = cursor.fetchone()["total"]

    # Benign predictions
    cursor.execute("""
        SELECT COUNT(*) AS benign
        FROM predictions
        WHERE prediction = 'Benign'
    """)
    benign = cursor.fetchone()["benign"]

    # Threat predictions
    threats = total - benign

    cursor.close()
    connection.close()

    return jsonify({
        "total": total,
        "benign": benign,
        "threats": threats
    })

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "online"
    })

@app.route("/clear-history", methods=["DELETE"])
def clear_history():

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM predictions")

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Prediction history cleared successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)