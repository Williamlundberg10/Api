from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Route to add data
@app.route("/add", methods=["POST"])
def add_data():
    new_data = request.json
    if not new_data:
        return jsonify({"error": "No data provided"}), 400
    
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    
    data.append(new_data)
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    
    return jsonify({"message": "Data added successfully", "data": new_data})

# Route to get all data
@app.route("/data", methods=["GET"])
def get_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

# Basic homepage
@app.route("/")
def home():
    return "<h1>Welcome to the Data API</h1><p>Use /add to POST data and /data to GET data.</p>"

if __name__ == "__main__":
    app.run(debug=True)
