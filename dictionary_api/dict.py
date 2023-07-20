from flask import Flask, render_template
import pandas as pd

# class creates website object instances
app = Flask(__name__)

# the @ is a decorator, it connects the route method with the function (home in this case)
@app.route("/")
def dict_home():
    return render_template("dict_home.html")

@app.route("/api/v1/<word>")
def result(word):
    definition = word.upper()
    res_dict = {"word": word, "definition": definition}
    return res_dict

app.run(debug=True, port=5001)
