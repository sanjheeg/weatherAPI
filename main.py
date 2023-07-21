from flask import Flask, render_template
import pandas as pd

# class creates website object instances
app = Flask(__name__)

# the @ is a decorator, it connects the route method with the function (home in this case)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
#print(stations)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def station(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    date_form = str(date[:4]) + "-" + str(date[4:6]) + "-" + str(date[6:])
    temperature = df.loc[df["    DATE"] == date_form]["   TG"].squeeze() /10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)


