from flask import Flask
from flask import request
from flask import render_template
import joblib

app = Flask(__name__)

# @ is a function decorator
# must run the app.route first before running any function below


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS")
        pred = model.predict([[rates]])
        print(pred)
        return (render_template("index.html", result='1'))
    else:
        return (render_template("index.html", result='2'))
    