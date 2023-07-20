from flask import Flask, render_template

# class creates website object instances
app = Flask("Website")


# the @ is a decorator, it connects the route method with the function (home in this case)
@app.route("/home")
def home():
    return render_template("tutorial.html")


app.run(debug=True)


