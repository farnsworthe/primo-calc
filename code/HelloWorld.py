from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":

        abyss = request.form.get("abyss")
        print(abyss)
        days = request.form.get("numdays")
        print(days)
        #return redirect(request.url)
    return render_template("results.html")

""" @app.route("/", methods=["GET", "POST"])
def data():
    if request.method == "POST":

        abyss = request.form.get("abyss")
        print(abyss)
        return redirect(request.url)

    return render_template("index.html") """

if __name__ == '__main__':
    app.run(debug=True)