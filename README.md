# AI-Powered Network Threat Detection and Monitoring System

An AI-powered network security system that detects and classifies different types of network threats using Machine Learning. The system provides a web-based dashboard for real-time prediction, prediction history, and threat statistics.

## Features

- Network traffic threat classification using Machine Learning
- Random Forest classification model
- Classification of 15 traffic categories
- Top 20 important network features used for prediction
- Flask REST API for predictions
- MySQL database for storing prediction history
- Web-based monitoring dashboard
- Threat statistics and threat rate
- System health monitoring
- Prediction history
- Clear prediction history
- Automatic dashboard refresh

## Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Joblib

### Backend

- Flask
- Flask-CORS
- REST API

### Database

- MySQL

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- VS Code

## Machine Learning Model

The project uses a Random Forest Classifier to classify network traffic into different categories.

The original dataset contains 77 network traffic features.

Feature importance analysis was performed and the top 20 features were selected for the final model.

The final model achieved approximately:

**97.41% accuracy on the held-out test set.**

> Note: The dataset uses a stratified train/test split. Some attack classes have very few samples, so per-class performance varies.

## Detected Traffic Categories

The model can classify traffic into 15 categories:

- Benign
- Bot
- DDoS
- DoS GoldenEye
- DoS Hulk
- DoS Slowhttptest
- DoS slowloris
- FTP-Patator
- Heartbleed
- Infiltration
- PortScan
- SSH-Patator
- Web Attack - Brute Force
- Web Attack - SQL Injection
- Web Attack - XSS

## Project Structure

```text
NetworkThreatDetection/
│
├── backend/
│   ├── app.py
│   ├── test_api.py
│   ├── test_mysql.py
│   └── test_real_record.py
│
├── dataset/
│   └── Dataset files
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── model/
│   ├── network_threat_model.pkl
│   ├── label_encoder.pkl
│   └── top_features.pkl
│
├── notebooks/
│   └── Machine learning and dataset analysis scripts
│
├── .gitignore
├── requirements.txt
└── README.md

System Architecture

Network Traffic Data
        |
        v
Data Preprocessing
        |
        v
Feature Selection
        |
        v
Random Forest Model
        |
        v
Flask REST API
        |
        +------------------+
        |                  |
        v                  v
     MySQL             Web Dashboard
        |                  |
        +--------+---------+
                 |
                 v
        Prediction Monitoring

        How It Works
Network traffic features are provided to the system.
The Flask API receives the prediction request.
The required top 20 features are extracted.
The trained Random Forest model predicts the traffic category.
The predicted category is returned through the API.
The prediction is stored in MySQL.
The dashboard displays the prediction and updated statistics.

Installation

Clone the repository:

git clone https://github.com/sivaprakashsingavarapu-cell/NetworkThreatDetection.git

Move into the project directory:

cd NetworkThreatDetection

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file in the project root:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD
MYSQL_DATABASE=network_threat_detection

The .env file is excluded from Git using .gitignore.

Database Setup

Create the MySQL database:

CREATE DATABASE network_threat_detection;

Create the predictions table:

USE network_threat_detection;

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prediction VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Run the Application

Start the Flask backend:

python backend/app.py

The API will run at:

http://127.0.0.1:5000

Open the frontend:

frontend/index.html
API Endpoints
Endpoint	Method	Purpose
/predict	POST	Predict network traffic
/predictions	GET	Get prediction history
/stats	GET	Get dashboard statistics
/health	GET	Check system status
/clear-history	DELETE	Clear prediction history
Example Prediction Response
{
    "prediction": "Benign"
}

For malicious traffic:

{
    "prediction": "Web Attack - XSS"
}
Dashboard

The web dashboard provides:

Prediction interface
Benign/threat result display
Prediction history
Total predictions
Benign traffic count
Threat count
Threat rate
System status
Automatic refresh
Future Improvements
Real-time packet capture
Live network traffic monitoring
Deep learning based detection
Email/SMS threat alerts
User authentication
Advanced visualization
Cloud deployment
Containerization using Docker
Author

Siva Prakash

B.Tech Computer Science Engineering

GitHub: https://github.com/sivaprakashsingavarapu-cell