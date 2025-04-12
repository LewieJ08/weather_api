from flask import Flask, request, jsonify
from flask_limiter import Limiter
from weather import fetch_data
from cache import cache, fetch
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

@app.route("/", methods = ["GET"])

def index():
    location = request.args.get("location")
    if not location:
        return jsonify({"Unexpected error": "Location empty"})
    
    api_key = os.getenv("API_KEY")
    redis_url = os.getenv("REDIS_URL")

    data = fetch(location, redis_url)
    
    if data != None:
        data = json.loads(data)
        return jsonify(data)
    
    else:
        data = fetch_data(location, api_key)
        cache_data = json.dumps(data)
        cache(location, cache_data, redis_url)
  
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)