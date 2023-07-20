from flask import Flask, render_template
import pandas as pd

# class creates website object instances
app = Flask(__name__)

# the @ is a decorator, it connects the route method with the function (home in this case)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    return render_template("about.html")

app.run(debug=True)


