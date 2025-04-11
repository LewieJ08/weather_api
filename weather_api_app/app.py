from flask import Flask, request, jsonify
from vc_api import fetch_data
from cache import cache
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/", methods = ["GET"])

def index():
    location = request.args.get("location")
    api_key = os.getenv("API_KEY")

    data = fetch_data(location, api_key)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)