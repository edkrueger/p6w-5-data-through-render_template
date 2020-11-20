from flask import Flask, jsonify, render_template
import csv
import os
import json

app = Flask(__name__)

def load_data():
    # in real life, this would be readind from a database
    with open("owid-covid-2020-11-19-usa.csv") as file:
        dict_reader = csv.DictReader(file)
        return json.dumps(list(dict_reader))

@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)