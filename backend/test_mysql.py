import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sivaram@12",
    database="network_threat_detection"
)

if connection.is_connected():
    print("MySQL connection successful!")

connection.close()