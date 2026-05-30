from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

@app.route("/api")
def api():
    data = load_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
