from flask import Flask, render_template, request
from vc_api import fetch_data

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def index():

    if request.method == "POST":
        location = request.form["location"]

        data = fetch_data(location)

        return render_template("index.html", data = data)
    
    return render_template("index.html", data = None)

if __name__ == "__main__":
    app.run(debug=True)